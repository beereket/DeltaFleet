import axios from 'axios';

const api = axios.create({
    baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api/',
});

export default api;