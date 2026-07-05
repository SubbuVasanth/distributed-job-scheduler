import { useNavigate } from "react-router-dom";

function Navbar(){

    const navigate=useNavigate();

    const logout=()=>{
        localStorage.clear();
        navigate("/");
    }

    const email = localStorage.getItem("user_email") || "User";

    return(
        <nav className="top-navbar">
            <div style={{ flex: 1, fontWeight: '500' }}>
                👤 Welcome, {email}
            </div>
            <button
                className="premium-btn premium-btn-danger"
                onClick={logout}
            >
                <i className="bi bi-box-arrow-right"></i> Logout
            </button>
        </nav>
    )
}

export default Navbar;