DROP SCHEMA IF EXISTS public CASCADE;

CREATE SCHEMA public;

CREATE TYPE public.tipoSangue AS ENUM (
  'a+',
  'a-',
  'b+',
  'b-',
  'ab+',
  'ab-',
  'o+',
  'o-',
  'null_rh'
);

CREATE TYPE public.tipoGenero AS ENUM (
  'cis',
  'trans',
  'non-b'
);

CREATE TYPE public.tipoFuncionario AS ENUM (
  'ENFERMEIRO',
  'ESTAGIARIO',
  'ADMINISTRADOR',
  'ENFERMEIRO_CHEFE'
);

CREATE TYPE public.tipoSexo AS ENUM (
  'MASCULINO',
  'FEMININO'
);

CREATE TABLE IF NOT EXISTS public.Paciente (
  CPF char(11) PRIMARY KEY,
  nome varchar NOT NULL,
  sexo tipoSexo DEFAULT null,
  genero tipoGenero DEFAULT null,
  data_nascimento date DEFAULT null,
  tipo_sangue tipoSangue DEFAULT null,
  endereco varchar DEFAULT null,
  telefone char(11) DEFAULT null,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  nome_atendente varchar
);

CREATE TABLE IF NOT EXISTS public.dado_paciente (
  id bigserial PRIMARY KEY,
  nome_campo varchar DEFAULT '',
  valor_campo varchar DEFAULT '',
  paciente char(11) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.Log (
  id bigserial PRIMARY KEY,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz
);

CREATE TABLE IF NOT EXISTS public.Log_Linha (
  id bigserial PRIMARY KEY,
  campo varchar DEFAULT '\n',
  log_id bigserial NOT NULL
);

CREATE TABLE IF NOT EXISTS public.Funcionario (
  CPF char(11) PRIMARY KEY,
  nome varchar NOT NULL,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  senha varchar(80) NOT NULL,
  tipo tipoFuncionario DEFAULT null
);

CREATE TABLE IF NOT EXISTS public.Enfermeiro (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS public.Enfermeiro_chefe (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS public.Administrador (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS public.Estagiario (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS public.Medicamento (
  codigo varchar PRIMARY KEY,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  nome varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS public.Posologia (
  id bigserial PRIMARY KEY,
  medicamento varchar,
  paciente char(11) NOT NULL,
  quantidade float NOT NULL,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  notas varchar
);

CREATE TABLE IF NOT EXISTS public.Agendamento (
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

ALTER TABLE public.Enfermeiro ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Enfermeiro_chefe ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Administrador ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Estagiario ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Posologia ADD FOREIGN KEY (medicamento) REFERENCES public.Medicamento (codigo) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Posologia ADD FOREIGN KEY (paciente) REFERENCES public.Paciente (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Log_Linha ADD FOREIGN KEY (log_id) REFERENCES public.Log (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.dado_paciente ADD FOREIGN KEY (paciente) REFERENCES public.Paciente (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE INDEX ON public.Paciente (CPF);

CREATE INDEX ON public.dado_paciente(id);

CREATE INDEX ON public.dado_paciente(paciente);

CREATE INDEX ON public.log (id);

CREATE INDEX ON public.Log_Linha(id);

CREATE INDEX ON public.Log_Linha(log_id);

CREATE INDEX ON public.Funcionario (CPF);

CREATE INDEX ON public.Enfermeiro (func_id);

CREATE INDEX ON public.Enfermeiro_chefe (func_id);

CREATE INDEX ON public.Administrador (func_id);

CREATE INDEX ON public.Estagiario (func_id);

CREATE INDEX ON public.Medicamento (codigo);

CREATE INDEX ON public.Posologia (paciente, medicamento);

CREATE INDEX ON public.Agendamento (id);

CREATE INDEX ON public.Agendamento (paciente);

CREATE INDEX ON public.Agendamento (horario);

CREATE INDEX ON public.Agendamento (horario);

COMMENT ON COLUMN public.Paciente.sexo IS 'Sexo biológico';

COMMENT ON COLUMN public.Paciente.genero IS 'Gênero com o qual a pessoa se identifica';

COMMENT ON COLUMN public.Paciente.nome_atendente IS 'Funcionario que atendeu esse paciente. Restringir no código quais tipos de funionário podem cadastrar pacientes';

COMMENT ON COLUMN public.Posologia.quantidade IS 'A quantidade diária a ser administrada';

INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on,tipo) VALUES ('00000000000','Admin','$2b$12$atVjgAGzJQ65rt2mc3eY6uew3cGwYpmJXJQTjUbZFxkNPbDa07IfG','2021-06-25 17:50:12.534074+00:00',NULL,'ADMINISTRADOR');
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on,tipo) VALUES ('70314381015','Pedro','$2b$12$PSQI5dtRvG6GYWseCtwdReSQJ/c6Y90rJmpdcst6L70irshS8.NKy','2021-06-25 17:52:41.382401+00:00',NULL,'ENFERMEIRO');
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on,tipo) VALUES ('00000000001','Test','$2b$12$fgtQLLR2jejvGdYqaXlgl.LDiUhXjTE8d0Wxt1JMyt8M2K/5ZBK7S','2021-06-25 18:10:34.548183+00:00',NULL,'ENFERMEIRO_CHEFE');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('1','70314381015');
INSERT INTO public.Enfermeiro_chefe(id,func_id) VALUES ('1','00000000001');