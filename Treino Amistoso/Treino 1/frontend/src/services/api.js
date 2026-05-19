import axios from "axios";

const createAPI=(baseURL)=> {
    return axios.create({
        baseURL
    });
};

export const API ={
    guest: createAPI("http://localhost:5002")
};