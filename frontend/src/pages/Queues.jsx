import { useEffect,useState } from "react";

import Navbar from "../components/Navbar";

import Sidebar from "../components/Sidebar";

import api from "../api/api";

function Queues(){

const [queues,setQueues]=useState([]);

const [projectId,setProjectId]=useState("");

const [name,setName]=useState("");

const load=()=>{

api.get("/queues")

.then(res=>setQueues(res.data));

}

useEffect(()=>{

load();

},[]);

const createQueue = async (e) => {
    e.preventDefault();
    try {
        await api.post("/queues", {
            project_id: Number(projectId),
            name,
            priority: 1,
            max_concurrency: 5,
            retry_policy_id: 1
        });
        setName("");
        setProjectId("");
        load();
    } catch (error) {
        alert("Failed to create queue: " + (error.response?.data?.detail || error.message));
    }
}

const pauseQueue = async (id) => {
    await api.patch(`/queues/${id}/pause`);
    load();
}

const resumeQueue = async (id) => {
    await api.patch(`/queues/${id}/resume`);
    load();
}

return(

<>

<div className="app-container">
<Sidebar/>
<div className="main-content">
<Navbar/>
<div className="content-wrapper">

<h1><i className="bi bi-hdd-stack-fill"></i> Queues</h1>

<form onSubmit={createQueue} className="glass-panel" style={{ padding: '24px', marginBottom: '32px' }}>
    <div className="row g-3">
        <div className="col-md-3">
            <input
                className="premium-input"
                placeholder="Project ID"
                value={projectId}
                onChange={(e)=>setProjectId(e.target.value)}
                required
            />
        </div>
        <div className="col-md-6">
            <input
                className="premium-input"
                placeholder="Queue Name"
                value={name}
                onChange={(e)=>setName(e.target.value)}
                required
            />
        </div>
        <div className="col-md-3">
            <button className="premium-btn w-100">
                <i className="bi bi-plus-lg"></i> Create
            </button>
        </div>
    </div>
</form>

<div className="glass-panel premium-table-container">
<table className="premium-table">

<thead>

<tr>

<th>ID</th>
<th>Name</th>
<th>Status</th>
<th>Actions</th>
</tr>

</thead>

<tbody>

{

queues.map(q=>(

<tr key={q.id}>

<td>{q.id}</td>
<td>{q.name}</td>
<td>
    {q.is_paused ? 
        <span className="status-badge failed">Paused</span> : 
        <span className="status-badge success">Active</span>
    }
</td>
<td>
    {q.is_paused ? (
        <button 
            className="premium-btn" 
            style={{ padding: '6px 12px', fontSize: '12px', background: 'var(--success)' }}
            onClick={() => resumeQueue(q.id)}
        >
            <i className="bi bi-play-fill"></i> Resume
        </button>
    ) : (
        <button 
            className="premium-btn premium-btn-danger" 
            style={{ padding: '6px 12px', fontSize: '12px' }}
            onClick={() => pauseQueue(q.id)}
        >
            <i className="bi bi-pause-fill"></i> Pause
        </button>
    )}
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

export default Queues;