import React from "react";
import { FaTrash, FaEdit } from "react-icons/fa";


const Body: React.FC = () => {
    return (
        <div className="flex flex-col p-2">
            <div className="flex space-x-4 mb-6 justify-center p-3">
                <button
                className="bg-slate-200 p-2 rounded-lg w-64"
                >
                    Today
                </button>
                <button
                className="bg-slate-200 p-2 rounded-lg w-64"
                >Pending</button>
                <button
                className="bg-slate-200 p-2 rounded-lg w-64"
                >Overdue</button>
            </div>
            <div className="flex flex-col w-screen items-center">
                <div className="flex justify-between w-3/5 p-1">
                    <h2>Tasks</h2>
                    <button
                    className="bg-yellow-900 rounded-md p-1 px-6 text-white hover:bg-yellow-700"
                    >Add Task</button>
                </div>
                <div className="flex flex-col gap-4 w-3/5">
                    <div className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                        <h2>Task name</h2>
                        <p> WEdnesday Oct 17</p>
                        <div className="flex justify-around items-center gap-5">
                            <FaEdit
                            className="text-blue-500 cursor-pointer hover:text-blue-700"
                            />
                            <FaTrash
                            className="text-red-500 cursor-pointer hover:text-red-700"
                            />
                        </div>
                    </div>
                    <div className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                        <h2>Task name</h2>
                        <p> WEdnesday Oct 17</p>
                        <div className="flex justify-around items-center gap-5">
                            <FaEdit
                            className="text-blue-500 cursor-pointer hover:text-blue-700"
                            />
                            <FaTrash
                            className="text-red-500 cursor-pointer hover:text-red-700"
                            />
                        </div>
                    </div>
                    <div className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                        <h2>Task name</h2>
                        <p> WEdnesday Oct 17</p>
                        <div className="flex justify-around items-center gap-5">
                            <FaEdit
                            className="text-blue-500 cursor-pointer hover:text-blue-700"
                            />
                            <FaTrash
                            className="text-red-500 cursor-pointer hover:text-red-700"
                            />
                        </div>
                    </div>
                    <div className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                        <h2>Task name</h2>
                        <p> WEdnesday Oct 17</p>
                        <div className="flex justify-around items-center gap-5">
                            <FaEdit
                            className="text-blue-500 cursor-pointer hover:text-blue-700"
                            />
                            <FaTrash
                            className="text-red-500 cursor-pointer hover:text-red-700"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Body;