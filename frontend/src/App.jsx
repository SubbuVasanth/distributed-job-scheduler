import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Projects from "./pages/Projects";
import Queues from "./pages/Queues";
import Jobs from "./pages/Jobs";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/projects" element={<Projects />} />

        <Route path="/queues" element={<Queues />} />

        <Route path="/jobs" element={<Jobs />} />

      </Routes>

    </BrowserRouter>

  );

}

export default App;