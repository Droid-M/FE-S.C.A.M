import pytest
from schemas.administrador import AdministradorCreated
from schemas.estagiaro import EstagiarioCreated
from model.Funcionario import Funcionario
from DAO.EstagiarioDAO import EstagiarioDAO

def test_estagiario():
    estDAO = EstagiarioDAO()
    
    #Removendo essa tupla pra evitar confusões:
    estDAO.DeleteByPK("00000000000")
    estDAO.DeleteByPK("12345678900")
    
    retorno3 = estDAO.DeleteByPK("00000000000")
    assert(retorno3 is None)
    
    #Inserindo
    nome = "Dr Fulano"
    senha = "senhaComplexa123"
    CPF = "00000000000"
    estagiario = EstagiarioCreated(nome = nome, CPF = CPF, senha = senha)
    retorno = estDAO.createBySchema(estagiario)
    assert(retorno is not None)
    assert(type(retorno) == Funcionario)
    dicionarioDados = retorno.typesAcceptables
    assert(dicionarioDados.get("CPF") == estagiario.CPF == CPF)
    assert(dicionarioDados.get("nome") == estagiario.nome == nome)
    assert(dicionarioDados.get("senha") == estagiario.senha == senha)
    retorno1 = estDAO.createBySchema(estagiario)
    assert(retorno1 is None)
    #Buscando
    retorno2 = estDAO.findByPK("00000000000")
    assert(retorno2 is not None)
    assert(type(retorno2) == Funcionario)
    assert(retorno2.typesAcceptables == retorno.typesAcceptables)
    
    #Atualizando a instância com os dados do banco
    retorno2.nome = "Dr Ciclano"
    assert(retorno2.nome == "Dr Ciclano")
    estDAO.refresh(retorno2)
    assert(retorno2.nome != "Dr Ciclano")
    assert(retorno2.nome == "Dr Fulano")
    
    
    #Atualizando o banco com os dados da instância
    retorno2.nome = "Dr Ciclano"
    assert(retorno2.nome == "Dr Ciclano")
    areUpdated = estDAO.update(retorno2)
    assert(areUpdated == True)
    assert(retorno2.nome == "Dr Ciclano")
    novo = Funcionario(nome = "Ninguém", CPF="12345678900", senha = "nao_tenho")
    areUpdated = estDAO.update(novo)
    assert(areUpdated == False)
    
    #Removendo (outra vez kkkkk)
    retorno3 = estDAO.DeleteByPK("00000000000")
    assert(retorno3 is not None)
    assert(type(retorno3) == Funcionario)
    
    retorno3 = estDAO.DeleteByPK("00000000000")
    assert(retorno3 is None)