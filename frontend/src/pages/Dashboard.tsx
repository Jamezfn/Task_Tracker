import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../store/store";

const Dashboard: React.FC = () => {
    const { name, email } = useSelector((state: RootState) => state.user)
    return (
        <div className="flex flex-col justify-center items-center h-screen w-screen">
            <h2 className="text-xl">This is the dashboard</h2>
            <p>User with name {name} is logged in with email {email}</p>
        </div>
    )
}

export default Dashboard;