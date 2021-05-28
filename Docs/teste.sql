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

CREATE TABLE IF NOT EXISTS public.Paciente (
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

CREATE TABLE IF NOT EXISTS public.Funcionario (
  CPF char(11) PRIMARY KEY,
  nome varchar NOT NULL,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  senha varchar(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.Enfermeiro (
  id bigserial PRIMARY KEY,
  func_id char(11) UNIQUE
);

CREATE TABLE IF NOT EXISTS public.EnfermeiroChefe (
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
  codigo bigserial PRIMARY KEY,
  created_on timestamptz DEFAULT (now()),
  updated_on timestamptz,
  nome varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS public.Posologia (
  id bigserial PRIMARY KEY,
  medicamento bigint,
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

ALTER TABLE public.Paciente ADD FOREIGN KEY (enfermeiro_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Enfermeiro ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.EnfermeiroChefe ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Administrador ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Estagiario ADD FOREIGN KEY (func_id) REFERENCES public.Funcionario (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Posologia ADD FOREIGN KEY (medicamento) REFERENCES public.Medicamento (codigo) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE public.Posologia ADD FOREIGN KEY (paciente) REFERENCES public.Paciente (CPF) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE INDEX ON public.Paciente (CPF);

CREATE INDEX ON public.Funcionario (CPF);

CREATE INDEX ON public.Enfermeiro (func_id);

CREATE INDEX ON public.EnfermeiroChefe (func_id);

CREATE INDEX ON public.Administrador (func_id);

CREATE INDEX ON public.Estagiario (func_id);

CREATE INDEX ON public.Medicamento (codigo);

CREATE INDEX ON public.Posologia (paciente, medicamento);

CREATE INDEX ON public.Agendamento (id);

CREATE INDEX ON public.Agendamento (paciente);

CREATE INDEX ON public.Agendamento (horario);

COMMENT ON COLUMN public.Paciente.sexo IS 'Sexo biológico';

COMMENT ON COLUMN public.Paciente.genero IS 'Gênero com o qual a pessoa se identifica';

COMMENT ON COLUMN public.Paciente.dados IS 'Informações a respeito do diagnóstico do paciente';

COMMENT ON COLUMN public.Paciente.enfermeiro_id IS 'Funcionario que cadastrou esse paciente. Restringir no código quais tipos de funionário podem cadastrar pacientes';

COMMENT ON COLUMN public.Posologia.quantidade IS 'A quantidade diária a ser administrada';






INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('71375160116','Carlos Eduardo da ConceiÃ§Ã£o','3mNCHI60%@','2021-05-21 03:31:47.708961+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('40181898460','Leonardo Souza','5xR%2OhhuJ','2021-05-21 03:31:47.919488+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('51849909218','Kamilly da Cunha','+5!JqC8J^w','2021-05-21 03:31:48.989623+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('45202282629','Luiz Miguel Pereira','&Vu7IAe3+r','2021-05-21 03:31:49.736218+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('05770720438','Dr. Thiago Cavalcanti','5qCM8fJC!a','2021-05-21 03:31:50.172274+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('28365997206','Augusto Barros','_1#V1eGk00','2021-05-21 03:31:51.286415+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('34984954627','Sr. Fernando Nogueira','5py0p#Fr!A','2021-05-21 03:31:51.842986+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('69839219802','Ana JÃºlia Rezende','6)1GjSfVJ&','2021-05-21 03:31:52.227535+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('84828333995','CauÃ£ Pinto','9shJWMxD^2','2021-05-21 03:31:52.457064+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('79357174178','LavÃ­nia da Rocha','+!9Z#2ezL1','2021-05-21 03:31:52.740600+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('32108412377','Nina Castro','@R2&PQhUwl','2021-05-21 03:31:53.274668+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('21148074068','Mirella Sales','Kl8GXrzB#D','2021-05-21 03:31:53.991259+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('82996495216','Kevin Correia','(+6GfYynd!','2021-05-21 03:31:54.706849+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('85174297656','Carlos Eduardo Porto','&6GGHw+yx6','2021-05-21 03:31:55.071896+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('47015360570','Murilo Moreira','p_iF08CeaT','2021-05-21 03:31:55.366433+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('02573559077','Sr. Miguel Santos','(zonAgNmn2','2021-05-21 03:31:55.711977+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('74957236822','Ana Beatriz da Costa','0JjMIx2z^s','2021-05-21 03:31:56.070023+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('15580080774','JoÃ£o Vitor da Luz','31$CPEzI@9','2021-05-21 03:31:56.309053+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('90948553266','Catarina Duarte','&oBV$fqiX2','2021-05-21 03:31:56.723105+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('74255628406','Luiz Felipe Costa','aO5ExztC8@','2021-05-21 03:31:56.916130+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('09477601436','Heitor Ferreira','u(3YtX227x','2021-05-21 03:31:57.069649+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('08307105705','Sra. Maria VitÃ³ria Teixeira','*0U+^Ujl&3','2021-05-21 03:31:57.236671+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('44201821435','Gabriela Campos','92dGZkEg@n','2021-05-21 03:31:57.495704+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('05583047314','Francisco Pinto','$lNN1qVH42','2021-05-21 03:31:57.760737+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('16721424607','BÃ¡rbara Nogueira','Z+BN8L5eaR','2021-05-21 03:31:58.031772+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('75578836399','Renan Farias','_VhS6MmZ$T','2021-05-21 03:31:58.366314+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('71437446494','Maysa da Cruz','Ob&G2Hn^M&','2021-05-21 03:31:58.650350+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('25964933951','Diogo Correia','1#7sCT^mQU','2021-05-21 03:31:59.083405+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('29990495623','Augusto Moura','@H1Qom0nfb','2021-05-21 03:31:59.526961+00:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('97441463814','Vitor Gabriel Costa','65uUqlDO%A','2021-05-21 03:31:59.840501+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('71375160116','Carlos Eduardo da ConceiÃ§Ã£o','3mNCHI60%@','2021-05-21 03:31:47.708961+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('40181898460','Leonardo Souza','5xR%2OhhuJ','2021-05-21 03:31:47.919488+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('51849909218','Kamilly da Cunha','+5!JqC8J^w','2021-05-21 03:31:48.989623+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('45202282629','Luiz Miguel Pereira','&Vu7IAe3+r','2021-05-21 03:31:49.736218+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('05770720438','Dr. Thiago Cavalcanti','5qCM8fJC!a','2021-05-21 03:31:50.172274+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('28365997206','Augusto Barros','_1#V1eGk00','2021-05-21 03:31:51.286415+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('34984954627','Sr. Fernando Nogueira','5py0p#Fr!A','2021-05-21 03:31:51.842986+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('69839219802','Ana JÃºlia Rezende','6)1GjSfVJ&','2021-05-21 03:31:52.227535+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('84828333995','CauÃ£ Pinto','9shJWMxD^2','2021-05-21 03:31:52.457064+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('79357174178','LavÃ­nia da Rocha','+!9Z#2ezL1','2021-05-21 03:31:52.740600+00:00',NULL);
INSERT INTO public.Enfermeiro(CPF,nome,senha,created_on,updated_on) VALUES ('32108412377','Nina Castro','@R2&PQhUwl','2021-05-21 03:31:53.274668+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('44201821435','Gabriela Campos','92dGZkEg@n','2021-05-21 03:31:57.495704+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('05583047314','Francisco Pinto','$lNN1qVH42','2021-05-21 03:31:57.760737+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('16721424607','BÃ¡rbara Nogueira','Z+BN8L5eaR','2021-05-21 03:31:58.031772+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('75578836399','Renan Farias','_VhS6MmZ$T','2021-05-21 03:31:58.366314+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('71437446494','Maysa da Cruz','Ob&G2Hn^M&','2021-05-21 03:31:58.650350+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('25964933951','Diogo Correia','1#7sCT^mQU','2021-05-21 03:31:59.083405+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('29990495623','Augusto Moura','@H1Qom0nfb','2021-05-21 03:31:59.526961+00:00',NULL);
INSERT INTO public.EnfermeiroChefe(CPF,nome,senha,created_on,updated_on) VALUES ('97441463814','Vitor Gabriel Costa','65uUqlDO%A','2021-05-21 03:31:59.840501+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('21148074068','Mirella Sales','Kl8GXrzB#D','2021-05-21 03:31:53.991259+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('82996495216','Kevin Correia','(+6GfYynd!','2021-05-21 03:31:54.706849+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('85174297656','Carlos Eduardo Porto','&6GGHw+yx6','2021-05-21 03:31:55.071896+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('47015360570','Murilo Moreira','p_iF08CeaT','2021-05-21 03:31:55.366433+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('02573559077','Sr. Miguel Santos','(zonAgNmn2','2021-05-21 03:31:55.711977+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('74957236822','Ana Beatriz da Costa','0JjMIx2z^s','2021-05-21 03:31:56.070023+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('15580080774','JoÃ£o Vitor da Luz','31$CPEzI@9','2021-05-21 03:31:56.309053+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('90948553266','Catarina Duarte','&oBV$fqiX2','2021-05-21 03:31:56.723105+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('74255628406','Luiz Felipe Costa','aO5ExztC8@','2021-05-21 03:31:56.916130+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('09477601436','Heitor Ferreira','u(3YtX227x','2021-05-21 03:31:57.069649+00:00',NULL);
INSERT INTO public.Estagiario(CPF,nome,senha,created_on,updated_on) VALUES ('08307105705','Sra. Maria VitÃ³ria Teixeira','*0U+^Ujl&3','2021-05-21 03:31:57.236671+00:00',NULL);
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('44301834634','Bruno AragÃ£o','True','non-b','1983-03-25','null_rh','Vila Emanuel Peixoto, 448
Penha
76461514 Teixeira / SC','08257559781','2021-05-21 03:32:00.459580+00:00',NULL,'','97441463814');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('18900731843','Daniel Porto','True','non-b','1958-05-04','o-','Setor Eduardo Peixoto
Nova Vista
98373095 Mendes Verde / ES','82633428109','2021-05-21 03:32:00.725614+00:00',NULL,'','40181898460');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('31470298935','JoÃ£o Martins','True','non-b','1987-10-03','a-','Quadra de Lopes, 50
Araguaia
91712846 da Paz / DF','89074166474','2021-05-21 03:32:01.404700+00:00',NULL,'','25964933951');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('40794324231','Yago Nascimento','False','cis','1983-08-26','a+','Lago de Lopes
Pantanal
23337-424 Cardoso / RN','14465283871','2021-05-21 03:32:01.816252+00:00',NULL,'','16721424607');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('57743031673','Maria Clara Ferreira','True','trans','1934-12-28','o+','Lagoa de Santos, 50
Pilar
76196-268 Nascimento / CE','23879968782','2021-05-21 03:32:02.170297+00:00',NULL,'','16721424607');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('13377643987','Gabriel Lima','True','trans','1954-12-10','ab+','Viaduto Emanuella Sales, 80
Vila Nova Gameleira 2Âª SeÃ§Ã£o
64305-143 Oliveira da Prata / PR','15399729749','2021-05-21 03:32:02.648358+00:00',NULL,'','34984954627');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('86056765124','Alice Duarte','False','non-b','1936-07-31','b+','Largo de Moreira
Marilandia
24854-742 Teixeira / SE','93580554293','2021-05-21 03:32:03.071412+00:00',NULL,'','05770720438');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('49475995813','AlÃ­cia Moura','False','non-b','1927-10-25','ab-','Largo Renan Silveira
Oeste
06619031 Pinto de Cunha / MA','66789382551','2021-05-21 03:32:03.391952+00:00',NULL,'','71375160116');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('55614222350','Maria Fernandes','False','non-b','1991-07-08','o+','Fazenda Teixeira, 6
Taquaril
10383661 Caldeira / SC','37982936204','2021-05-21 03:32:03.858011+00:00',NULL,'','05583047314');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('64794045636','Diogo da Rosa','True','cis','1944-08-11','ab-','Travessa de Fernandes, 98
Trevo
53720-932 Lima / BA','01666849964','2021-05-21 03:32:04.334572+00:00',NULL,'','84828333995');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('69269418526','Maria CecÃ­lia Rocha','False','cis','1926-09-02','o+','ColÃ´nia de da Mota, 376
Salgado Filho
18093801 Correia Paulista / SP','24694276520','2021-05-21 03:32:04.593605+00:00',NULL,'','28365997206');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('72257143448','Dr. Noah Moura','False','cis','1923-03-06','null_rh','PÃ¡tio de Farias
Barroca
00974939 Pinto do Sul / ES','76195962809','2021-05-21 03:32:04.856138+00:00',NULL,'','75578836399');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('02484301543','Rodrigo Duarte','True','trans','1928-11-03','ab-','PÃ¡tio da Cruz, 23
SÃ£o Jorge 3Âª SeÃ§Ã£o
10694673 da Luz Grande / AM','35652068553','2021-05-21 03:32:05.093668+00:00',NULL,'','51849909218');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('62419002277','Stella da Cruz','False','non-b','1925-06-08','o+','Feira Freitas, 24
Monsenhor Messias
43921-405 Rocha de Porto / ES','19254320585','2021-05-21 03:32:05.330198+00:00',NULL,'','29990495623');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('92079719817','Sr. Emanuel Ribeiro','True','cis','1946-05-24','b-','Conjunto de Nogueira, 6
Nazare
84866-719 Ramos / GO','35505917646','2021-05-21 03:32:05.549226+00:00',NULL,'','79357174178');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('71706660167','Pedro Henrique Pereira','False','cis','1988-03-27','b-','Conjunto CecÃ­lia Santos, 99
Atila De Paiva
90173834 Rezende / PB','54292352984','2021-05-21 03:32:06.092795+00:00',NULL,'','51849909218');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('65105857070','Lucas Gabriel da Paz','True','trans','1977-03-30','null_rh','PÃ¡tio LÃ­via Silva, 5
Vila ParaÃ­so
79603776 Lopes / RN','16786996057','2021-05-21 03:32:06.988409+00:00',NULL,'','05770720438');
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4978491995','medicamento_143226','2021-05-21 03:32:08.536105+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4789220888','medicamento_960973','2021-05-21 03:32:11.484480+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6318994394','medicamento_872476','2021-05-21 03:32:12.760142+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2438099985','medicamento_995527','2021-05-21 03:32:12.892159+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5884950027','medicamento_590527','2021-05-21 03:32:13.103686+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8806961712','medicamento_178110','2021-05-21 03:32:13.280708+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1742314767','medicamento_31626','2021-05-21 03:32:13.366219+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8050890714','medicamento_113797','2021-05-21 03:32:13.566244+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3774394752','medicamento_216106','2021-05-21 03:32:13.652255+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7094368104','medicamento_413962','2021-05-21 03:32:13.798774+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6533947832','medicamento_605315','2021-05-21 03:32:13.881784+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7964541904','medicamento_131760','2021-05-21 03:32:14.014801+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2522200859','medicamento_206962','2021-05-21 03:32:14.207826+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2285145013','medicamento_541385','2021-05-21 03:32:14.289336+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9184702822','medicamento_427496','2021-05-21 03:32:14.361845+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2215305717','medicamento_856847','2021-05-21 03:32:14.477860+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6499672883','medicamento_774164','2021-05-21 03:32:14.563871+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7283695928','medicamento_609432','2021-05-21 03:32:14.673385+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1443692943','medicamento_402464','2021-05-21 03:32:14.786899+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5307225915','medicamento_139879','2021-05-21 03:32:14.877911+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8786185854','medicamento_862246','2021-05-21 03:32:14.964422+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4813460180','medicamento_889244','2021-05-21 03:32:15.172948+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6415562395','medicamento_677247','2021-05-21 03:32:15.258459+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6337887104','medicamento_527279','2021-05-21 03:32:15.345470+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5368209549','medicamento_263013','2021-05-21 03:32:15.452484+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8116114259','medicamento_125475','2021-05-21 03:32:15.555997+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9884092583','medicamento_316742','2021-05-21 03:32:15.629006+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1827356608','medicamento_761148','2021-05-21 03:32:15.788026+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('735161311','medicamento_912428','2021-05-21 03:32:15.929044+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1350946825','medicamento_476595','2021-05-21 03:32:16.179576+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2258882167','medicamento_306476','2021-05-21 03:32:16.260586+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2558556285','medicamento_216006','2021-05-21 03:32:16.343597+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5460201450','medicamento_909773','2021-05-21 03:32:16.470613+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('828255939','medicamento_945597','2021-05-21 03:32:16.632134+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3648993786','medicamento_344667','2021-05-21 03:32:16.745148+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4976370672','medicamento_713391','2021-05-21 03:32:16.862663+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5800051804','medicamento_743987','2021-05-21 03:32:16.948174+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2932647887','medicamento_714740','2021-05-21 03:32:17.019683+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5625459741','medicamento_418216','2021-05-21 03:32:17.094692+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3007557411','medicamento_429608','2021-05-21 03:32:17.185204+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3802760722','medicamento_634120','2021-05-21 03:32:17.253712+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9550447357','medicamento_682949','2021-05-21 03:32:17.333723+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3057128783','medicamento_62953','2021-05-21 03:32:17.419734+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7395858521','medicamento_116482','2021-05-21 03:32:17.620259+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6690359214','medicamento_423922','2021-05-21 03:32:17.703270+00:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2824593651','medicamento_515712','2021-05-21 03:32:17.917797+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('1','4789220888','86056765124','37.39','Checar batimentos','2021-05-21 03:32:18.231837+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('2','2824593651','86056765124','60.89','Aplicar doses em braÃ§os diferentes','2021-05-21 03:32:18.517373+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('3','3774394752','02484301543','64.69','','2021-05-21 03:32:18.917424+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('4','5460201450','71706660167','51.1','Aplicar doses em braÃ§os diferentes','2021-05-21 03:32:19.285470+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('5','5625459741','02484301543','50.74','','2021-05-21 03:32:19.604011+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('6','8786185854','72257143448','12.97','Checar batimentos','2021-05-21 03:32:19.899548+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('7','6337887104','44301834634','64.86','','2021-05-21 03:32:20.205587+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('8','2522200859','86056765124','28.68','Injetar na testa','2021-05-21 03:32:20.549631+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('9','9884092583','55614222350','58.2','','2021-05-21 03:32:20.969684+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('10','8806961712','69269418526','60.72','Injetar na testa','2021-05-21 03:32:21.574761+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('11','5800051804','65105857070','64.1','Aplicar doses em braÃ§os diferentes','2021-05-21 03:32:22.016317+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('12','5368209549','64794045636','11.37','Injetar na testa','2021-05-21 03:32:22.244346+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('13','6499672883','02484301543','33.46','Injetar na testa','2021-05-21 03:32:22.641897+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('14','2215305717','13377643987','32.34','','2021-05-21 03:32:23.056949+00:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('15','1827356608','92079719817','8.86','Aplicar doses em braÃ§os diferentes','2021-05-21 03:32:23.473002+00:00',NULL);
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('1','1','72257143448','28365997206',NULL,'71437446494','2021-05-21 03:32:24.165090+00:00',NULL,'1985-01-12 19:22:27+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('2','10','69269418526',NULL,'74255628406','16721424607','2021-05-21 03:32:25.118211+00:00',NULL,'2006-02-15 15:57:55+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('3','10','02484301543','84828333995',NULL,'41096137008','2021-05-21 03:32:26.022326+00:00',NULL,'2018-12-14 09:06:47+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('4','1','40794324231','45202282629',NULL,'5583047314','2021-05-21 03:32:26.934442+00:00',NULL,'1979-03-17 05:29:39+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('5','2','31470298935',NULL,'2573559077','41096137008','2021-05-21 03:32:27.415003+00:00',NULL,'1976-06-09 07:16:30+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('6','2','02484301543','5770720438',NULL,'71437446494','2021-05-21 03:32:28.498140+00:00',NULL,'2019-09-09 21:59:04+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('7','6','31470298935',NULL,'82996495216','75578836399','2021-05-21 03:32:29.036709+00:00',NULL,'1999-10-31 18:43:23+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('8','8','64794045636',NULL,'8307105705','29990495623','2021-05-21 03:32:30.090843+00:00',NULL,'2000-10-27 07:16:51+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('9','13','69269418526','79357174178',NULL,'25964933951','2021-05-21 03:32:31.109472+00:00',NULL,'1983-03-23 15:40:51+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('10','9','55614222350','51849909218',NULL,'41096137008','2021-05-21 03:32:31.904073+00:00',NULL,'1996-01-28 20:42:14+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('11','12','55614222350','28365997206',NULL,'5583047314','2021-05-21 03:32:32.833191+00:00',NULL,'2006-08-07 06:27:21+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('12','14','18900731843',NULL,'90948553266','75578836399','2021-05-21 03:32:33.726304+00:00',NULL,'2018-06-28 02:24:59+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('13','7','40794324231','5770720438',NULL,'71437446494','2021-05-21 03:32:34.656922+00:00',NULL,'2004-08-02 20:23:05+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('14','14','86056765124',NULL,'47015360570','97441463814','2021-05-21 03:32:35.966589+00:00',NULL,'2002-09-08 20:44:16+00:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('15','7','57743031673','79357174178',NULL,'44201821435','2021-05-21 03:32:36.426147+00:00',NULL,'1991-06-22 20:39:50+00:00');