import React, { useEffect, useState} from "react";
import { FaTrash, FaEdit } from "react-icons/fa";
import api from "../api/axios";
import { AxiosResponse } from "axios";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import TaskModel from "./TaskModel";


const Body: React.FC = () => {

    const [todos, setTodos] = useState([]);
    const [activeTab, setActiveTab] = useState("today");
    const [isModelOpen, setIsModalOpen] = useState(false);
    const [editingTask, setEditingTask] = useState(null);
    const [editId, setEditId] = useState("")
    

    const navigate = useNavigate()

    const handleEditClick = (task: any) => {
        setEditingTask(task);
        setIsModalOpen(true);
        setEditId(task.id)
    }
    const fetchTasks = () => {
        api.get('/api/tasks')
            .then((response: AxiosResponse) => {
                const tasks = response.data.tasks;
                const formattedTasks = tasks.map((task: any) => ({
                    ...task,
                    startDate: new Date(task.start_date),
                    endDate: new Date(task.due_date),
                }))
                setTodos(formattedTasks);
            })
            .catch((error: any) => {
                console.log(error.response?.data?.error);
                if (error.response?.data?.error !== "User has no tasks") {
                    navigate('/auth/login');
                }                
            })
    };
    useEffect(() => {
        fetchTasks();
    }, [])


    const handleAddTask = (taskData: any) => {
        api.post('/api/tasks', taskData)
            .then((response: AxiosResponse) => {
                toast.success(response.data.message || 'Task created successfully!', {
                    duration: 3000,
                    position: 'top-center',
                    icon: '🎉',
                    style: {
                        background: '#DCFCE7',
                        color: '#16A34A',
                        border: '1px solid #16A34A'
                    }
                });
                setIsModalOpen(false);
                // refreshing tasks again
                fetchTasks()
                
            })
            .catch(error => {
                toast.error(error.response?.data?.error || 'Failed to create task', {
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
    }

    const handleDeleteTask = (id: string) => {
        api.delete(`api/tasks/${id}`)
        .then((response: AxiosResponse) => {
            toast.success(response.data.message || 'Task created successfully!', {
                duration: 3000,
                position: 'top-center',
                icon: '🎉',
                style: {
                    background: '#DCFCE7',
                    color: '#16A34A',
                    border: '1px solid #16A34A'
                }
            });
            setIsModalOpen(false);
            // refreshing tasks again
            fetchTasks()
            
        })
        .catch(error => {
            toast.error(error.response?.data?.error || 'Failed to create task', {
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
    }

    const handleUpdateTask = (taskData: any) => {
        if (editId) {
            api.put(`/api/tasks/${editId}`, taskData)
            .then((response: AxiosResponse) => {
                toast.success(response.data.message || 'Task updated successfully!', {
                    duration: 3000,
                    position: 'top-center',
                    icon: '🎉',
                    style: {
                        background: '#DCFCE7',
                        color: '#16A34A',
                        border: '1px solid #16A34A'
                    }
                });
                setIsModalOpen(false);
                setEditingTask(null);
                setEditId("");
                fetchTasks();
            })
            .catch(error => {
                toast.error(error.response?.data?.error || 'Failed to update task', {
                    duration: 4000,
                    position: 'top-center',
                    icon: '❌',
                    style: {
                        background: '#FEE2E2',
                        color: '#DC2626',
                        border: '1px solid #DC2626'
                    }
                });
            });
        }
    }

    return (
        <div className="flex flex-col p-2">
            <div className="flex space-x-4 mb-6 justify-center p-3">
                <button
                className={`${activeTab == "today" ? "bg-yellow-900 text-white" : "bg-slate-200 "} p-2 rounded-lg w-64`}
                onClick={() => setActiveTab("today")}
                >
                    Today
                </button>
                <button
                className={`${activeTab == "pending" ? "bg-yellow-900 text-white" : "bg-slate-200"} p-2 rounded-lg w-64`}
                onClick={() => setActiveTab("pending")}
                >Pending</button>
                <button
                className={`${activeTab == "overdue" ? "bg-yellow-900 text-white" : "bg-slate-200"} p-2 rounded-lg w-64`}
                onClick={() => setActiveTab("overdue")}
                >Overdue</button>
            </div>
            <div className="flex flex-col w-screen items-center">
                <div className="flex justify-between w-3/5 p-1">
                    <h2>Tasks</h2>
                    <button
                    className="bg-yellow-900 rounded-md p-1 px-6 text-white hover:bg-yellow-700"
                    onClick={() => setIsModalOpen(true)}
                    >Add Task</button>
                </div>
                <TaskModel
                isOpen={isModelOpen}
                onClose={() => {
                    setIsModalOpen(false);
                    setEditingTask(null);
                }}
                onSubmit={editingTask ? handleUpdateTask : handleAddTask}
                initialTask={editingTask}
                />
                <div className="flex flex-col gap-4 w-3/5">
                    {todos.length > 0 ? (
                        <>
                            {activeTab === "pending" && 
                                todos.filter((todo: {status: string}) => todo.status === "pending").length > 0 ? (
                                todos
                                    .filter((todo: {status: string;}) => todo.status === "pending")
                                    .map((todo: {id: string; title: string; endDate: string; }) => (
                                        <div key={todo.id} className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                                            <h2>{todo.title}</h2>
                                            <p>{new Date(todo.endDate).toLocaleDateString()}</p>
                                            <div className="flex justify-around items-center gap-5">
                                                <FaEdit
                                                className="text-blue-500 cursor-pointer hover:text-blue-700"
                                                onClick={() => handleEditClick(todo)}                                                
                                                />
                                                <FaTrash
                                                className="text-red-500 cursor-pointer hover:text-red-700"
                                                onClick={() => handleDeleteTask(todo.id)}
                                                />
                                            </div>
                                        </div>
                                    ))
                            ) : activeTab === "today" && 
                                todos.filter((todo: {endDate: string;}) => new Date(todo.endDate).toDateString() === new Date().toDateString()).length > 0 ? (
                                todos
                                    .filter((todo: {endDate: string}) => new Date(todo.endDate).toDateString() === new Date().toDateString())
                                    .map((todo: {id: string; title: string; endDate: string}) => (
                                        <div key={todo.id} className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                                            <h2>{todo.title}</h2>
                                            <p>{new Date(todo.endDate).toLocaleDateString()}</p>
                                            <div className="flex justify-around items-center gap-5">
                                                <FaEdit
                                                className="text-blue-500 cursor-pointer hover:text-blue-700"
                                                onClick={() => handleEditClick(todo)}
                                                />
                                                <FaTrash
                                                className="text-red-500 cursor-pointer hover:text-red-700"
                                                onClick={() => handleDeleteTask(todo.id)}
                                                />
                                            </div>
                                        </div>
                                    ))
                            ) : activeTab === "overdue" && 
                                todos.filter((todo: {endDate: string}) => new Date(todo.endDate) < new Date()).length > 0 ? (
                                todos
                                    .filter((todo: {endDate: string}) => new Date(todo.endDate) < new Date())
                                    .map((todo: {id: string; title: string; endDate: string}) => (
                                        <div key={todo.id} className="flex justify-around items-center h-20 shadow shadow-gray-400 rounded w-full">
                                            <h2>{todo.title}</h2>
                                            <p>{new Date(todo.endDate).toLocaleDateString()}</p>
                                            <div className="flex justify-around items-center gap-5">
                                                <FaEdit
                                                className="text-blue-500 cursor-pointer hover:text-blue-700"
                                                onClick={() => handleEditClick(todo)}
                                                />
                                                <FaTrash
                                                className="text-red-500 cursor-pointer hover:text-red-700"
                                                onClick={() => handleDeleteTask(todo.id)}
                                                />
                                            </div>
                                        </div>
                                    ))
                            ) : (
                                <div className="flex flex-col items-center justify-center p-8 text-center">
                                    <div className="bg-gray-50 rounded-lg shadow-sm p-6 w-full">
                                        <h3 className="text-xl text-gray-600 font-medium mb-2">No Tasks Found</h3>
                                        <p className="text-gray-500">No tasks available for {activeTab} tab. Click "Add Task" to create one!</p>
                                    </div>
                                </div>
                            )}
                        </>
                    ) : (
                        <div className="flex flex-col items-center justify-center p-8 text-center">
                            <div className="bg-gray-50 rounded-lg shadow-sm p-6 w-full">
                                <h3 className="text-xl text-gray-600 font-medium mb-2">No Tasks Found</h3>
                                <p className="text-gray-500">Your task list is empty. Click the "Add Task" button to get started!</p>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>    )
}

export default Body;