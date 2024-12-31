import { BrowserRouter, Routes, Route} from "react-router-dom";
import Register from "../pages/auth/register";
import Dashboard from "../pages/Dashboard";
import Login from "../pages/auth/login";

const AppRouter = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/auth/register" element={<Register />}/>
                <Route path="/" element={<Dashboard />} />
                <Route path="/auth/login" element={<Login />} />
            </Routes>
        </BrowserRouter>
    )
}

export default AppRouter;