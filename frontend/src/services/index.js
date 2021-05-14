const axios = require("axios")

// Conexão com a API
export const api = axios.create({
    baseURL: 'http://localhost:3000/'   
});




