import React, { useState } from "react";
// import { useDispatch } from "react-redux";
// import { setUser } from "../../features/user/userSlice";
import { useNavigate } from "react-router-dom"
// import { loginUser } from "../../api/login";
import api from "../../api/axios";
import { toast, Toaster } from "react-hot-toast";
import { AxiosResponse } from "axios";

const Register: React.FC = () => {
    // const dispatch = useDispatch();
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setIsLoading(true);

        api.post('/api/register', {
            name,
            email,
            password
        })
            .then((response: AxiosResponse) => {
                const { message } = response.data;
                toast.success(message, {
                    duration: 3000,
                    position: 'top-center',
                    icon: '🎉',
                    style: {
                        background: '#DCFCE7',
                        color: '#16A34A',
                        border: '1px solid #16A34A'
                    }
                })
                setTimeout(() => {
                    navigate('/auth/login');
                }, 3000);
            })
            .catch((err: any) => {
                const errorMessage = err.response?.data?.error || err.message || 'Registration failed. Please try again.';
                toast.error(errorMessage, {
                    duration: 4000,
                    position: 'top-center',
                    icon: '❌',
                    style: {
                        background: '#FEE2E2',
                        color: '#DC2626',
                        border: '1px solid #DC2626'
                    } 
                })            
            })
            .finally(() => {
                setIsLoading(false)
            })

    }
    
    return (
        <div className="flex flex-col items-center justify-center h-screen w-screen">
            <Toaster />
            <div className="flex flex-col items-center justify-center h-1/2 w-1/2 bg-gray-100 shadow shadow-gray-500 rounded-md">
                <h2 className="text-2xl font-bold mb-6">Welcome to Task Tracker</h2>
                <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-80">
                    <label className="flex flex-col">
                        <span className="mb-1">Name</span>
                        <input
                        type="text"
                        name="name"
                        id="name"
                        value={name}
                        placeholder="Name"
                        onChange={(e) => setName(e.target.value)}
                        className="p-2 border rounded focus:outline-none focus:ring-2 focus:ring-orange-600"
                        />
                    </label>
                    <label className="flex flex-col">
                        <span className="mb-1">Email</span>
                        <input
                            type="email"
                            name="email"
                            id="email"
                            value={email}
                            placeholder="Email"
                            onChange={(e) => setEmail(e.target.value)}
                            className="p-2 border rounded focus:outline-none focus:ring-2 focus:ring-orange-600"
                        />
                    </label>
                    <label className="flex flex-col">
                        <span className="mb-1">Password</span>
                        <input
                            type="password"
                            name="password"
                            id="password"
                            value={password}
                            placeholder="Password"
                            onChange={(e) => setPassword(e.target.value)}
                            className="p-2 border rounded focus:outline-none focus:ring-2 focus:ring-orange-600"
                        />                      
                    </label>
                    <button 
                    className="bg-orange-600 text-white border-none p-3 rounded hover:bg-orange-700"
                    type="submit"
                    disabled={isLoading}
                    >
                       {isLoading ? 'Signing in...' : 'Signin'}
                    </button>
                </form>
            </div>            
        </div>
    )
}

export default Register;
