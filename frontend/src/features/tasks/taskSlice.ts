import { createSlice, PayloadAction } from "@reduxjs/toolkit";


interface taskState {
    title: string;
    description: string;
    status: string;
    startDate: string;
    endDate: string;
}


const initialState: taskState = {
    title: "",
    description: "",
    status: "",
    startDate: "",
    endDate: ""
};


const taskSlice = createSlice({
    name: 'task',
    initialState,
    reducers: {
        setTask: (state, action: PayloadAction<taskState>) => {
            state.title = action.payload.title,
            state.description = action.payload.description,
            state.status = action.payload.status,
            state.startDate = action.payload.startDate,
            state.endDate = action.payload.endDate
        },
        clearTask: (state) => {
            state.title = "",
            state.description = "",
            state.status = "",
            state.startDate = "",
            state.endDate = ""
        }
    }
})

export const { setTask, clearTask } = taskSlice.actions;
export default taskSlice.reducer;