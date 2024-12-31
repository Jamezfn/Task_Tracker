import axios from "axios";


export const loginUser = (email: string, password: string) => {
    console.log(email, password);
    axios.get('/auth/login')
        .then((response) => {
            // const {id, name, email} = response.data;
            console.log(response);
        })
        .catch((error) => {
            console.log(error);
        })
        .finally(() => {
            console.log('Exiting login')
        })
}