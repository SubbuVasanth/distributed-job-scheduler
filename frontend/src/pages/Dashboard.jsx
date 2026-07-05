import { useEffect, useState } from "react";

import api from "../api/api";

import Sidebar from "../components/Sidebar";

import Navbar from "../components/Navbar";

import StatsCard from "../components/StatsCard";

function Dashboard(){

    const [stats,setStats]=useState({
        queued:0,
        scheduled:0,
        running:0,
        completed:0,
        dead:0,
        queues:0
    });

    useEffect(()=>{

        api.get("/dashboard/stats")

        .then(res=>setStats(res.data))

        .catch(console.error);

    },[]);

    return(

        <>

        <div className="app-container">
            <Sidebar/>
            <div className="main-content">
                <Navbar/>
                <div className="content-wrapper">
                    <h1><i className="bi bi-speedometer2"></i> Dashboard Overview</h1>

                <div className="row g-4">

                    <StatsCard
                        title="Queued Jobs"
                        value={stats.queued}
                        color="warning"
                    />

                    <StatsCard
                        title="Scheduled Jobs"
                        value={stats.scheduled}
                        color="info"
                    />

                    <StatsCard
                        title="Running Jobs"
                        value={stats.running}
                        color="primary"
                    />

                    <StatsCard
                        title="Completed"
                        value={stats.completed}
                        color="success"
                    />

                    <StatsCard
                        title="Dead Jobs"
                        value={stats.dead}
                        color="danger"
                    />

                    <StatsCard
                        title="Total Queues"
                        value={stats.queues}
                        color="secondary"
                    />

                </div>
            </div>
        </div>
        </div>

        </>

    )

}

export default Dashboard;