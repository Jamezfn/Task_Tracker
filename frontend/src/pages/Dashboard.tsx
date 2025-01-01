import React from "react";
// import { useSelector } from "react-redux";
// import { RootState } from "../store/store";
import Header from "../components/Header";
import Body from "../components/Body";

const Dashboard: React.FC = () => {
    return (
        <div className="h-screen w-screen">
            <Header />
            <Body />
        </div>
    )
}

export default Dashboard;