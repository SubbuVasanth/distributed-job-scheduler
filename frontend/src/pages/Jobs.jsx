import {useEffect,useState} from "react";

import Navbar from "../components/Navbar";

import Sidebar from "../components/Sidebar";

import api from "../api/api";

function Jobs(){

const [jobs,setJobs]=useState([]);

const [queueId,setQueueId]=useState("");
const [message,setMessage]=useState("");
const [delaySeconds, setDelaySeconds]=useState("");
const [cronExpression, setCronExpression]=useState("");

const load=()=>{

api.get("/jobs")

.then(res=>setJobs(res.data));

}

useEffect(()=>{

load();

},[]);

const createJob = async (e) => {
    e.preventDefault();
    try {
        let parsedPayload = {};
        try {
            parsedPayload = JSON.parse(message);
        } catch(err) {
            parsedPayload = { message };
        }
        
        await api.post("/jobs", {
            queue_id: Number(queueId),
            payload: parsedPayload,
            delay_seconds: delaySeconds ? Number(delaySeconds) : null,
            cron_expression: cronExpression ? cronExpression : null
        });
        setMessage("");
        setDelaySeconds("");
        setCronExpression("");
        load();
    } catch (error) {
        alert("Failed to create job: " + (error.response?.data?.detail || error.message));
    }
}

const retryJob = async (id) => {
    await api.patch(`/jobs/${id}/retry`);
    load();
}

const viewJob = (job) => {
    alert(JSON.stringify(job, null, 2));
}

return(

<>

<div className="app-container">
<Sidebar/>
<div className="main-content">
<Navbar/>
<div className="content-wrapper">

<h1><i className="bi bi-lightning-charge-fill"></i> Jobs</h1>

<form onSubmit={createJob} className="glass-panel" style={{ padding: '24px', marginBottom: '32px' }}>
    <div className="row g-3">
        <div className="col-md-3">
            <input
                className="premium-input"
                placeholder="Queue ID"
                value={queueId}
                onChange={(e)=>setQueueId(e.target.value)}
                required
            />
        </div>
        <div className="col-md-9">
            <input
                className="premium-input"
                placeholder="Message (JSON payload)"
                value={message}
                onChange={(e)=>setMessage(e.target.value)}
                required
            />
        </div>
    </div>
    <div className="row g-3 mt-1">
        <div className="col-md-3">
            <input
                className="premium-input"
                placeholder="Delay (sec)"
                type="number"
                value={delaySeconds}
                onChange={(e)=>setDelaySeconds(e.target.value)}
            />
        </div>
        <div className="col-md-6">
            <input
                className="premium-input"
                placeholder="Cron Expression (e.g. * * * * *)"
                value={cronExpression}
                onChange={(e)=>setCronExpression(e.target.value)}
            />
        </div>
        <div className="col-md-3">
            <button className="premium-btn w-100">
                <i className="bi bi-plus-lg"></i> Create Job
            </button>
        </div>
    </div>
</form>

<div className="glass-panel premium-table-container">
<table className="premium-table">

<thead>

<tr>

<th>ID</th>
<th>Status</th>
<th>Priority</th>
<th>Actions</th>
</tr>

</thead>

<tbody>

{

jobs.map(job=>(

<tr key={job.id}>

<td>{job.id}</td>
<td>
    <span className={`status-badge ${job.status.toLowerCase()}`}>
        {job.status}
    </span>
</td>
<td>{job.priority}</td>
<td>
    <div style={{ display: 'flex', gap: '8px' }}>
        <button 
            className="premium-btn" 
            style={{ padding: '6px 12px', fontSize: '12px', background: 'var(--text-muted)' }}
            onClick={() => viewJob(job)}
        >
            <i className="bi bi-eye-fill"></i> View
        </button>
        {(job.status === 'DEAD' || job.status === 'FAILED') && (
            <button 
                className="premium-btn" 
                style={{ padding: '6px 12px', fontSize: '12px', background: 'var(--warning)' }}
                onClick={() => retryJob(job.id)}
            >
                <i className="bi bi-arrow-clockwise"></i> Retry
            </button>
        )}
    </div>
</td>
</tr>

))

}

</tbody>

</table>
</div>

</div>
</div>
</div>

</>

)

}

export default Jobs;