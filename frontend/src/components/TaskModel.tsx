import React, { useState, useEffect } from "react";
import toast from "react-hot-toast";

interface TaskModelProps {
    isOpen: boolean;
    onClose: () => void;
    onSubmit: (task: any) => void;
    initialTask:  any;
}

const TaskModel: React.FC<TaskModelProps> = ({ isOpen, onClose, onSubmit, initialTask }) => {
    const formatDate = (dateString: string) => {
        const date = new Date(dateString);
        if (isNaN(date.getTime())) return "";
        return date.toISOString().split("T")[0];
    };

    const [formData, setFormData] = useState({
        title: initialTask?.title || '',
        description: initialTask?.description || '',
        status: initialTask?.status || 'pending',
        start_date: initialTask?.start_date || '',
        due_date: initialTask?.due_date || ''
    });

    useEffect(() => {
        setFormData({
            title: initialTask?.title || '',
            description: initialTask?.description || '',
            status: initialTask?.status || 'pending',
            start_date: initialTask?.start_date ? formatDate(initialTask.start_date) : "",
            due_date: initialTask?.due_date ? formatDate(initialTask.due_date) : "",
        });
    }, [initialTask]);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();

        if (!formData.title || !formData.start_date || !formData.due_date) {
            toast.error('Title, start date and due date are both required', {
                duration: 4000,
                position: 'top-center',
                icon: '❌',
                style: {
                    background: '#FEE2E2',
                    color: '#DC2626',
                    border: '1px solid #DC2626'
                }
            });
            return;
        }

        onSubmit(formData);
    }

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white p-8 rounded-lg w-96">
                <h2 className="text-2xl font-bold mb-4">{initialTask ? "Edit task" : "Add new Task"}</h2>
                <form onSubmit={handleSubmit}>
                    <input
                    type="text"
                    placeholder="Task title"
                    className="w-full p-2 mb-4 border rounded"
                    value={formData.title}
                    onChange={(e) => setFormData({...formData, title: e.target.value})}
                    />
                    <textarea
                    placeholder="Description"
                    className="w-full p-2 mb-4 border rounded"
                    onChange={(e) => setFormData({...formData, description: e.target.value})}
                    value={formData.description}
                    />
                    <select
                    className="w-full p-2 mb-4 border rounded"
                    onChange={(e) => setFormData({...formData, status: e.target.value})}
                    value={formData.status}
                    >
                        <option value="pending">Pending</option>
                        <option value="today">Today</option>
                    </select>
                    <label>
                        <span>Start Date:</span>
                        <input
                        type="date"
                        className="w-full p-2 mb-4 border rounded"
                        value={formData.start_date}
                        onChange={(e) => setFormData({...formData, start_date: e.target.value})}
                        />
                    </label>
                    <label>
                        <span>End Date:</span>
                        <input
                        type="date"
                        className="w-full p-2 mb-4 border rounded"
                        value={formData.due_date}
                        onChange={(e) => setFormData({...formData, due_date: e.target.value})}
                        />
                    </label>
                    <div className="flex justify-end gap-2">
                        <button
                        type="button"
                        onClick={onClose}
                        className="px-4 py-2 bg-gray-200 rounded"
                        >Cancel</button>
                        <button
                        type="submit"
                        className="px-4 py-2 bg-yellow-900 text-white rounded"
                        >{initialTask ? "Edit Task" : "Add Task"}</button>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default TaskModel;