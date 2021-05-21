CREATE TABLE IF NOT EXISTS Paciente (
  CPF char(11) PRIMARY KEY,
  nome varchar NOT NULL,
  sexo boolean DEFAULT null,
  genero tipoGenero DEFAULT null,
  data_nascimento date DEFAULT null,
  tipo_sangue tipoSangue DEFAULT null,
  endereco varchar DEFAULT null,
  telefone char(11) DEFAULT null,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  dados varchar,
  enfermeiro_id char(11) NOT NULL
);

CREATE TABLE IF NOT EXISTS Funcionario (
  CPF char(11) PRIMARY KEY,
  nome varchar NOT NULL,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  senha varchar(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS Enfermeiro (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS EnfermeiroChefe (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS Administrador (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS Estagiario (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS Medicamento (
  codigo bigserial PRIMARY KEY,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  nome varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS Posologia (
  id bigserial PRIMARY KEY,
  medicamento bigint,
  paciente char(11) NOT NULL,
  quantidade float NOT NULL,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  notas varchar
);

CREATE TABLE IF NOT EXISTS Agendamento (
  id bigserial PRIMARY KEY,
  posologia bigint NOT NULL,
  paciente char(11) NOT NULL,
  enfermeiro bigint DEFAULT NULL,
  estagiario bigint DEFAULT NULL,
  enferchefe bigint NOT NULL,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  horario timestamptz DEFAULT null
);

ALTER TABLE Paciente ADD FOREIGN KEY (enfermeiro_id) REFERENCES Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Enfermeiro ADD FOREIGN KEY (func_id) REFERENCES Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE EnfermeiroChefe ADD FOREIGN KEY (func_id) REFERENCES Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Administrador ADD FOREIGN KEY (func_id) REFERENCES Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Estagiario ADD FOREIGN KEY (func_id) REFERENCES Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Posologia ADD FOREIGN KEY (medicamento) REFERENCES Medicamento (codigo) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Posologia ADD FOREIGN KEY (paciente) REFERENCES Paciente (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE INDEX ON Paciente (CPF);

CREATE INDEX ON Funcionario (CPF);

CREATE INDEX ON Enfermeiro (func_id);

CREATE INDEX ON EnfermeiroChefe (func_id);

CREATE INDEX ON Administrador (func_id);

CREATE INDEX ON Estagiario (func_id);

CREATE INDEX ON Medicamento (codigo);

CREATE INDEX ON Posologia (paciente, medicamento);

CREATE INDEX ON Agendamento (id);

CREATE INDEX ON Agendamento (paciente);

CREATE INDEX ON Agendamento (horario);

COMMENT ON COLUMN Paciente.sexo IS 'Sexo biológico';

COMMENT ON COLUMN Paciente.genero IS 'Gênero com o qual a pessoa se identifica';

COMMENT ON COLUMN Paciente.dados IS 'Informações a respeito do diagnóstico do paciente';

COMMENT ON COLUMN Paciente.enfermeiro_id IS 'Funcionario que cadastrou esse paciente. Restringir no código quais tipos de funionário podem cadastrar pacientes';

COMMENT ON COLUMN Posologia.quantidade IS 'A quantidade diária a ser administrada';