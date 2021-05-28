// const axios = require('axios').default;
const baseURL = " ";


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
     * Busca um usuário especifico pelo seu id
     */
    static async getUsuarioId(cpf){
        const user = (await axios.get(baseURL+`/lista_usuario/${cpf}`)).data;
        return user;
    }

    /**
     * Cria um novo usuário do sistema
     */
    static async createUsers(cpf,nome,email,senha){

        axios.post(baseURL+'/cadastro_usuario', {
            CPF: `${cpf}`,
            nome: `${nome}`,
            email: `${email}`,
            senha: `${senha}`
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
    static async updateUser(cpf,nome,email,senha){
        axios.put(baseURL+`/edicao_usuario/${id}`, {
            CPF: `${cpf}`,
            nome: `${nome}`,
            email: `${email}`,
            senha: `${senha}`
        }).then((response)=> {
            console.log(response);
            return true;    // Por enquanto retorna um booleano, mas deve retornar alguma resposta
        }).cath((err)=>{
            console.log(err);
        })
    }

    /** 
     * Deleta um usuário do sistema
     */
    static async deleteUser(id){

        axios.delete(baseURL+`/edicao_usuario/${id}`)
    }

}

// AdmService.createUsers();

export {AdmService};

