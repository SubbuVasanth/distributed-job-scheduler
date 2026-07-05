import { Link, useLocation } from "react-router-dom";

function Sidebar(){
    const location = useLocation();
    const currentPath = location.pathname;

    return(
        <aside className="sidebar glass-panel">
            <h3><i className="bi bi-rocket-takeoff"></i> Job Scheduler</h3>
            <Link to="/dashboard" className={currentPath === '/dashboard' ? 'active' : ''}>
                <i className="bi bi-grid-1x2-fill"></i> Dashboard
            </Link>
            <Link to="/projects" className={currentPath === '/projects' ? 'active' : ''}>
                <i className="bi bi-folder-fill"></i> Projects
            </Link>
            <Link to="/queues" className={currentPath === '/queues' ? 'active' : ''}>
                <i className="bi bi-hdd-stack-fill"></i> Queues
            </Link>
            <Link to="/jobs" className={currentPath === '/jobs' ? 'active' : ''}>
                <i className="bi bi-lightning-charge-fill"></i> Jobs
            </Link>
        </aside>
    )
}

export default Sidebar;