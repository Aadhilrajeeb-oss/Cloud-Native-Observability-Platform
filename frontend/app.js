const API = "http://localhost:6060";
const METRICS_API = "http://localhost:6060/metrics";


const PROM_API="http://localhost:9090/api/v1/query";


const AUTH_API="http://localhost:7000";

async function loadUsers(){

let res=await fetch(AUTH_API+"/users");
let users=await res.json();

let list=document.getElementById("userList");

if(!list) return;

list.innerHTML="";

users.forEach(u=>{

let li=document.createElement("li");

li.innerText=u.username+" ("+u.role+")";

list.appendChild(li);

});

}

async function createUser(){

let username=document.getElementById("newUser").value;
let password=document.getElementById("newPass").value;
let role=document.getElementById("newRole").value;

await fetch(AUTH_API+"/users",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
username:username,
password:password,
role:role
})

});

loadUsers();

}

loadUsers();

async function queryProm(query){

let res=await fetch(PROM_API+"?query="+encodeURIComponent(query));

let data=await res.json();

if(!data.data.result.length) return 0;

return data.data.result[0].value[1];

}


async function loadSystemMetrics(){

let cpu=await queryProm("rate(node_cpu_seconds_total[1m])");
let memory=await queryProm("node_memory_MemAvailable_bytes");
let containers=await queryProm("count(container_last_seen)");
let api=await queryProm("rate(task_requests_total[1m])");

document.getElementById("cpuMetric").innerText=cpu;
document.getElementById("memoryMetric").innerText=memory;
document.getElementById("containerMetric").innerText=containers;
document.getElementById("apiMetric").innerText=api;

}

setInterval(loadSystemMetrics,5000);

let chart;

/* ---------- AUTH CHECK ---------- */

if(!localStorage.getItem("token")){
    window.location="login.html"
}

/* ---------- TASK FUNCTIONS ---------- */

async function loadTasks(){

const token = localStorage.getItem("token");

let res = await fetch(API+"/tasks",{
headers:{
"Authorization":"Bearer "+token
}
});

let tasks = await res.json();

let list = document.getElementById("taskList");

if(!list) return;

list.innerHTML="";

tasks.forEach(t=>{
let li=document.createElement("li");
li.innerText=t.title+" - "+t.status;
list.appendChild(li);
});

}

async function addTask(){

let input=document.getElementById("taskInput");

const token = localStorage.getItem("token");

await fetch(API+"/tasks",{
method:"POST",
headers:{
"Content-Type":"application/json",
"Authorization":"Bearer "+token
},
body:JSON.stringify({
title:input.value,
status:"pending"
})
});

input.value="";

loadTasks();
}

/* ---------- METRICS CHART ---------- */

async function loadMetrics(){

let res = await fetch(METRICS_API);
let text = await res.text();

let match = text.match(/task_requests_total\s+(\d+)/);

if(!match) return;

let value = parseInt(match[1]);

updateChart(value);

}

function updateChart(value){

if(!chart){

let ctx = document.getElementById("metricsChart");

if(!ctx) return;

chart = new Chart(ctx,{
type:"line",
data:{
labels:["Requests"],
datasets:[{
label:"API Requests",
data:[value],
borderColor:"cyan"
}]
}
});

}else{

chart.data.labels.push("");
chart.data.datasets[0].data.push(value);
chart.update();

}

}

/* ---------- AUTO LOAD ---------- */

loadTasks();
setInterval(loadMetrics,3000);

function logout(){

localStorage.removeItem("token");

window.location="login.html";

}