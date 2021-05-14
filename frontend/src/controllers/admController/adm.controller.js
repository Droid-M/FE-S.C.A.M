// const axios = require('axios').default;
import axios from 'axios';

const baseURL = "http://localhost:3000"



class AdmController{

    /**
     * Retorna todos os usuários cadastrados no sistema
     */
    static async getUsuarios(){
        const enfermeiroChefe = (await axios.get(baseURL+'/enfermeiroChefe')).data;
        const administrador = (await axios.get(baseURL+'/administrador')).data;
        const enfermeiro = (await axios.get(baseURL+'/enfermeiro')).data;
        const estagiario = (await axios.get(baseURL+'/estagiario')).data;

        const usuarios = [enfermeiroChefe,administrador,enfermeio,estagiario];
        return usuarios
    }

    /**
     * Cria um novo usuário do sistema
     */
    static async createUsers(CPF,nome,senha){

        axios.post('/user', {
            CPF: 'Fred',
            nome: 'Flintstone',
            senha: ''
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });

    }

    /**
     * Atualiza um usuário especifico
     */
    static async updateUser(){

    }

    /** 
     * Deleta um usuário do sistema
     */
    static async deleteUser(){

    }

}

// function getAllUsuarios(){
//     const usuarios = axios.get(baseURL+'/produtos').then(function(response){
//         document.body.addEventListener
//         console.log(response.data);

//     }).catch(function(error){
//         console.log("errou");
//     })

//     document.querySelector("teste").innerHTML=usuarios
//     console.log(getAllUsuarios());
// }




// const axios = require('../services/index')



// // retorna todos os usuários cadastrados

//   function getUsuarios(){
//     const usuarios = axios.get('/produtos')
//         .then(function(response){
//             response.data;
//         }).catch((e)=>{
//             console.log("error")
//         });  

// }

// console.log(getUsuarios())


// function cadastroUsuarios(){

// }
