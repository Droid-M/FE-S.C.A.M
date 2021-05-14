// const axios = require('axios').default;
import axios from 'axios';

const baseURL = "http://localhost:3000"



class AdmService{

    /**
     * Retorna todos os usuários cadastrados no sistema
     */
    static async getUsuarios(){
        const enfermeiroChefe = (await axios.get(baseURL+'/enfermeiroChefe')).data;
        const administrador = (await axios.get(baseURL+'/administrador')).data;
        const enfermeiro = (await axios.get(baseURL+'/enfermeiro')).data;
        const estagiario = (await axios.get(baseURL+'/estagiario')).data;

        const usuarios = [enfermeiroChefe,administrador,enfermeiro,estagiario];

        // const produtos = (await axios.get(baseURL+'/produtos')).data;
        // const categorias = (await axios.get(baseURL+'/categorias')).data;

        // const usuarios = [produtos,categorias];

       // console.log(usuarios)

       return usuarios
    }

    /**
     * Cria um novo usuário do sistema
     */
    static async createUsers(){

        axios.post('/user', {
            CPF: 'Fred',
            nome: 'Flintstone',
            email: '',
            senha: ''
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });

            // axios.post(baseURL+'/produto',{
          //   nome:'Caderno',
          //   descricao: 'Usa para escrever',
          //   preco: 30.0
          // }).then(function(response){
          //   console.log(response.data);
          // }).catch((error)=>{
          //   console.log(error);
          // })

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

AdmService.createUsers();

export {AdmService};

