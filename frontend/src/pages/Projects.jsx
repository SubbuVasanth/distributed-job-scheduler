import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import api from "../api/api";

function Projects() {

    const [projects,setProjects]=useState([]);

    const [name,setName]=useState("");

    const [description,setDescription]=useState("");

    const loadProjects=()=>{

        api.get("/projects")

        .then(res=>setProjects(res.data));

    }

    useEffect(()=>{

        loadProjects();

    },[]);

    const createProject = async (e) => {
        e.preventDefault();
        try {
            await api.post("/projects", {
                name,
                description
            });
            setName("");
            setDescription("");
            loadProjects();
        } catch (error) {
            alert("Failed to create project: " + (error.response?.data?.detail || error.message));
        }
    }

    const deleteProject = async (id) => {
        if(window.confirm("Are you sure you want to delete this project?")) {
            await api.delete(`/projects/${id}`);
            loadProjects();
        }
    }

    return(

    <>

    <div className="app-container">
        <Sidebar/>
        <div className="main-content">
            <Navbar/>
            <div className="content-wrapper">
                <h1><i className="bi bi-folder-fill"></i> Projects</h1>

    <form onSubmit={createProject} className="glass-panel" style={{ padding: '24px', marginBottom: '32px' }}>
        <div className="row g-3">
            <div className="col-md-5">
                <input
                    className="premium-input"
                    placeholder="Project Name"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    required
                />
            </div>
            <div className="col-md-5">
                <input
                    className="premium-input"
                    placeholder="Description"
                    value={description}
                    onChange={(e)=>setDescription(e.target.value)}
                    required
                />
            </div>
            <div className="col-md-2">
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
    <th>Description</th>
    <th>Actions</th>
    </tr>

    </thead>

    <tbody>

    {

    projects.map(project=>(

    <tr key={project.id}>

    <td>{project.id}</td>
    <td>{project.name}</td>
    <td>{project.description}</td>
    <td>
        <button 
            className="premium-btn premium-btn-danger" 
            style={{ padding: '6px 12px', fontSize: '12px' }}
            onClick={() => deleteProject(project.id)}
        >
            <i className="bi bi-trash"></i> Delete
        </button>
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

export default Projects;