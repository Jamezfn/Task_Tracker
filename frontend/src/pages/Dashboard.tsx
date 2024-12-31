import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../store/store";
import Header from "../components/Header";

const Dashboard: React.FC = () => {
    const { name, email } = useSelector((state: RootState) => state.user)
    return (
        <div className="h-screen w-screen">
            <Header />
            <h2 className="text-xl">This is the dashboard</h2>
            <p>User with name {name} is logged in with email {email}</p>
        </div>
    )
}

export default Dashboard;