import pytest
from fescam.model.Posologia import Posologia
from fescam.schemas.posologia import PosologiaCreated
from fescam.DAO.PosologiaDAO import PosologiaDAO
from fescam.DAO.MedicamentoDAO import MedicamentoDAO
from fescam.DAO.PacienteDAO import PacienteDAO

def test_posologia():
    posDAO = PosologiaDAO()
    MedicamentoDAO().createByTuple(codigo = 123456789, nome = "Benegripe") #Criando um medicamento pra evitar futuros problemas
    PacienteDAO().createByTuple(CPF = "69758848600", nome = "Paciente_0 Zombie da Silva")
    
    #removendo posologias com esses dados para evitar futuros erros ->:
    posDAO.deleteByTuple(
        medicamento = 123456789,
        paciente = "69758848600",
        quantidade = 5.95,
        notas = "A administração deve ser feita utilizando mg, tomar cuidado com os efeitos colaterais"
    )
    
    #Inserir informações
    medicamento = 123456789
    paciente = "69758848600"
    quantidade = 5.95
    notas = "A administração deve ser feita utilizando mg, tomar cuidado com os efeitos colaterais"
    posologia = PosologiaCreated(medicamento = medicamento, paciente = paciente, quantidade = quantidade, notas = notas)
    retorno = posDAO.createBySchema(posologia)
    assert(retorno is not None)
    assert(type(retorno) == Posologia)
    dicionarioDados = retorno.typesAcceptables
    assert(dicionarioDados.get("medicamento") == posologia.medicamento == medicamento)
    assert(dicionarioDados.get("paciente") == posologia.paciente == paciente)
    assert(dicionarioDados.get("quantidade") == posologia.quantidade == quantidade)
    assert(dicionarioDados.get("notas") == posologia.notas == notas)

    posologiaBuscada = posDAO.findByTuple(**posologia.dict())[0] #findByTuple retorna uma lista de instâncias e só queremos a primeira
    retorno1 = posDAO.createByTuple(**posologiaBuscada.typesAcceptables)
    assert(retorno1 is None)

    

    