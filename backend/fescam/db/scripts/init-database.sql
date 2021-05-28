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






INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('71375160116','Carlos Eduardo da ConceiÃƒÂ§ÃƒÂ£o','3mNCHI60%@','2021-05-21 00:31:47.708961-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('40181898460','Leonardo Souza','5xR%2OhhuJ','2021-05-21 00:31:47.919488-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('51849909218','Kamilly da Cunha','+5!JqC8J^w','2021-05-21 00:31:48.989623-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('45202282629','Luiz Miguel Pereira','&Vu7IAe3+r','2021-05-21 00:31:49.736218-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('05770720438','Dr. Thiago Cavalcanti','5qCM8fJC!a','2021-05-21 00:31:50.172274-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('28365997206','Augusto Barros','_1#V1eGk00','2021-05-21 00:31:51.286415-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('34984954627','Sr. Fernando Nogueira','5py0p#Fr!A','2021-05-21 00:31:51.842986-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('69839219802','Ana JÃƒÂºlia Rezende','6)1GjSfVJ&','2021-05-21 00:31:52.227535-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('84828333995','CauÃƒÂ£ Pinto','9shJWMxD^2','2021-05-21 00:31:52.457064-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('79357174178','LavÃƒÂ­nia da Rocha','+!9Z#2ezL1','2021-05-21 00:31:52.740600-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('32108412377','Nina Castro','@R2&PQhUwl','2021-05-21 00:31:53.274668-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('21148074068','Mirella Sales','Kl8GXrzB#D','2021-05-21 00:31:53.991259-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('82996495216','Kevin Correia','(+6GfYynd!','2021-05-21 00:31:54.706849-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('85174297656','Carlos Eduardo Porto','&6GGHw+yx6','2021-05-21 00:31:55.071896-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('47015360570','Murilo Moreira','p_iF08CeaT','2021-05-21 00:31:55.366433-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('02573559077','Sr. Miguel Santos','(zonAgNmn2','2021-05-21 00:31:55.711977-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('74957236822','Ana Beatriz da Costa','0JjMIx2z^s','2021-05-21 00:31:56.070023-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('15580080774','JoÃƒÂ£o Vitor da Luz','31$CPEzI@9','2021-05-21 00:31:56.309053-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('90948553266','Catarina Duarte','&oBV$fqiX2','2021-05-21 00:31:56.723105-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('74255628406','Luiz Felipe Costa','aO5ExztC8@','2021-05-21 00:31:56.916130-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('09477601436','Heitor Ferreira','u(3YtX227x','2021-05-21 00:31:57.069649-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('08307105705','Sra. Maria VitÃƒÂ³ria Teixeira','*0U+^Ujl&3','2021-05-21 00:31:57.236671-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('44201821435','Gabriela Campos','92dGZkEg@n','2021-05-21 00:31:57.495704-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('05583047314','Francisco Pinto','$lNN1qVH42','2021-05-21 00:31:57.760737-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('16721424607','BÃƒÂ¡rbara Nogueira','Z+BN8L5eaR','2021-05-21 00:31:58.031772-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('75578836399','Renan Farias','_VhS6MmZ$T','2021-05-21 00:31:58.366314-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('71437446494','Maysa da Cruz','Ob&G2Hn^M&','2021-05-21 00:31:58.650350-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('25964933951','Diogo Correia','1#7sCT^mQU','2021-05-21 00:31:59.083405-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('29990495623','Augusto Moura','@H1Qom0nfb','2021-05-21 00:31:59.526961-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('97441463814','Vitor Gabriel Costa','65uUqlDO%A','2021-05-21 00:31:59.840501-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('60464837851','Lívia Caldeira','V6xroZB%#o','2021-05-28 01:07:55.499831-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('50104270229','Dr. João Miguel Alves','QQK8R1hZ@9','2021-05-28 01:07:55.588843-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('32550073146','Luiza Peixoto','s@z8YWYwTh','2021-05-28 01:07:55.677854-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('72501229429','Levi Porto','^m5eZzwRX4','2021-05-28 01:07:55.777867-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('38603000363','Yago Cardoso','@2O%e9T%3*','2021-05-28 01:07:55.884380-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('31126167698','Srta. Rebeca Correia','*1^CA@6+8f','2021-05-28 01:07:55.973892-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('74387952643','Alexia Vieira','0zmsCkTu$S','2021-05-28 01:07:56.072404-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('17617685291','Dr. Lucca Souza','$vKGmKhXN5','2021-05-28 01:07:56.162416-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('69850050065','Luiz Henrique Nunes','b)4AFAz3$i','2021-05-28 01:07:56.258928-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('10614412839','Sophia Correia','^2M%B#1B)n','2021-05-28 01:07:56.349939-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('29538973159','Enzo da Cunha','*F2ZVJIr)m','2021-05-28 01:07:56.441951-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('91609733024','Lucas Gabriel Cavalcanti',')X5OEMnoNY','2021-05-28 01:07:56.531462-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('13659350101','João Correia','&vnVhLfqV0','2021-05-28 01:07:56.621974-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('60302213111','Giovanna Gonçalves','!41UDw8RYv','2021-05-28 01:07:56.713486-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('04679040588','Davi Luiz da Rosa','!65aXkx@9q','2021-05-28 01:07:56.816999-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('39826920458','Maria Alice da Rosa','s41cYkAkU^','2021-05-28 01:07:56.912511-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('28969381242','João Nunes','%W&IR8dlp3','2021-05-28 01:07:57.002522-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('96285466477','Marina da Paz','c$0P061THr','2021-05-28 01:07:57.092534-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('97988917927','Ian Lima','!+N&u2(xY2','2021-05-28 01:07:57.186046-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('49128010350','Pedro Lucas Moreira','WqV_E3Bd+(','2021-05-28 01:07:57.278057-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('59894766366','Isabella Rocha','*5Sap5AP29','2021-05-28 01:07:57.368069-03:00',NULL);
INSERT INTO public.Funcionario(CPF,nome,senha,created_on,updated_on) VALUES ('79669858721','Raquel da Costa','QNGrLana_0','2021-05-28 01:07:57.460580-03:00',NULL);
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('1','71375160116');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('2','40181898460');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('3','51849909218');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('4','45202282629');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('5','05770720438');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('6','28365997206');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('7','34984954627');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('8','69839219802');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('9','84828333995');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('10','79357174178');
INSERT INTO public.Enfermeiro(id,func_id) VALUES ('11','32108412377');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('1','44201821435');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('2','05583047314');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('3','16721424607');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('5','75578836399');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('6','71437446494');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('7','25964933951');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('8','29990495623');
INSERT INTO public.EnfermeiroChefe(id,func_id) VALUES ('9','97441463814');
INSERT INTO public.Estagiario(id,func_id) VALUES ('1','21148074068');
INSERT INTO public.Estagiario(id,func_id) VALUES ('2','82996495216');
INSERT INTO public.Estagiario(id,func_id) VALUES ('3','85174297656');
INSERT INTO public.Estagiario(id,func_id) VALUES ('4','47015360570');
INSERT INTO public.Estagiario(id,func_id) VALUES ('5','02573559077');
INSERT INTO public.Estagiario(id,func_id) VALUES ('6','74957236822');
INSERT INTO public.Estagiario(id,func_id) VALUES ('7','15580080774');
INSERT INTO public.Estagiario(id,func_id) VALUES ('8','90948553266');
INSERT INTO public.Estagiario(id,func_id) VALUES ('9','74255628406');
INSERT INTO public.Estagiario(id,func_id) VALUES ('10','09477601436');
INSERT INTO public.Estagiario(id,func_id) VALUES ('11','08307105705');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('18900731843','Daniel Porto','True','non-b','1958-05-04','o-','Setor Eduardo Peixoto
Nova Vista
98373095 Mendes Verde / ES','82633428109','2021-05-21 00:32:00.725614-03:00',NULL,'','40181898460');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('40794324231','Yago Nascimento','False','cis','1983-08-26','a+','Lago de Lopes
Pantanal
23337-424 Cardoso / RN','14465283871','2021-05-21 00:32:01.816252-03:00',NULL,'','16721424607');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('57743031673','Maria Clara Ferreira','True','trans','1934-12-28','o+','Lagoa de Santos, 50
Pilar
76196-268 Nascimento / CE','23879968782','2021-05-21 00:32:02.170297-03:00',NULL,'','16721424607');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('13377643987','Gabriel Lima','True','trans','1954-12-10','ab+','Viaduto Emanuella Sales, 80
Vila Nova Gameleira 2Ã‚Âª SeÃƒÂ§ÃƒÂ£o
64305-143 Oliveira da Prata / PR','15399729749','2021-05-21 00:32:02.648358-03:00',NULL,'','34984954627');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('86056765124','Alice Duarte','False','non-b','1936-07-31','b+','Largo de Moreira
Marilandia
24854-742 Teixeira / SE','93580554293','2021-05-21 00:32:03.071412-03:00',NULL,'','05770720438');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('49475995813','AlÃƒÂ­cia Moura','False','non-b','1927-10-25','ab-','Largo Renan Silveira
Oeste
06619031 Pinto de Cunha / MA','66789382551','2021-05-21 00:32:03.391952-03:00',NULL,'','71375160116');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('55614222350','Maria Fernandes','False','non-b','1991-07-08','o+','Fazenda Teixeira, 6
Taquaril
10383661 Caldeira / SC','37982936204','2021-05-21 00:32:03.858011-03:00',NULL,'','05583047314');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('64794045636','Diogo da Rosa','True','cis','1944-08-11','ab-','Travessa de Fernandes, 98
Trevo
53720-932 Lima / BA','01666849964','2021-05-21 00:32:04.334572-03:00',NULL,'','84828333995');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('69269418526','Maria CecÃƒÂ­lia Rocha','False','cis','1926-09-02','o+','ColÃƒÂ´nia de da Mota, 376
Salgado Filho
18093801 Correia Paulista / SP','24694276520','2021-05-21 00:32:04.593605-03:00',NULL,'','28365997206');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('72257143448','Dr. Noah Moura','False','cis','1923-03-06','null_rh','PÃƒÂ¡tio de Farias
Barroca
00974939 Pinto do Sul / ES','76195962809','2021-05-21 00:32:04.856138-03:00',NULL,'','75578836399');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('02484301543','Rodrigo Duarte','True','trans','1928-11-03','ab-','PÃƒÂ¡tio da Cruz, 23
SÃƒÂ£o Jorge 3Ã‚Âª SeÃƒÂ§ÃƒÂ£o
10694673 da Luz Grande / AM','35652068553','2021-05-21 00:32:05.093668-03:00',NULL,'','51849909218');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('62419002277','Stella da Cruz','False','non-b','1925-06-08','o+','Feira Freitas, 24
Monsenhor Messias
43921-405 Rocha de Porto / ES','19254320585','2021-05-21 00:32:05.330198-03:00',NULL,'','29990495623');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('92079719817','Sr. Emanuel Ribeiro','True','cis','1946-05-24','b-','Conjunto de Nogueira, 6
Nazare
84866-719 Ramos / GO','35505917646','2021-05-21 00:32:05.549226-03:00',NULL,'','79357174178');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('71706660167','Pedro Henrique Pereira','False','cis','1988-03-27','b-','Conjunto CecÃƒÂ­lia Santos, 99
Atila De Paiva
90173834 Rezende / PB','54292352984','2021-05-21 00:32:06.092795-03:00',NULL,'','51849909218');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('65105857070','Lucas Gabriel da Paz','True','trans','1977-03-30','null_rh','PÃƒÂ¡tio LÃƒÂ­via Silva, 5
Vila ParaÃƒÂ­so
79603776 Lopes / RN','16786996057','2021-05-21 00:32:06.988409-03:00',NULL,'','05770720438');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('95081054653','Diego Cavalcanti','True','non-b','1943-11-27','o-','Passarela de Pinto, 920
Aarão Reis
64276-617 Pereira Paulista / ES','20054555947','2021-05-28 01:07:57.639103-03:00',NULL,'','34984954627');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('54364467457','Luna Novaes','False','cis','1957-01-15','o-','Residencial Carvalho, 7
Vila Petropolis
73109092 Moraes de Barros / PB','13941080447','2021-05-28 01:07:57.788622-03:00',NULL,'','05583047314');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('59530357006','Pietro da Mota','True','trans','1990-04-01','null_rh','Lagoa de Viana, 81
Lagoa
11853-066 da Cruz de Viana / PI','54575940565','2021-05-28 01:07:57.935641-03:00',NULL,'','05583047314');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('62441419367','Esther Viana','False','cis','1936-01-28','b+','Estação de da Cunha, 98
Vila Maria
48479237 Lima Grande / AC','26358214802','2021-05-28 01:07:58.065657-03:00',NULL,'','45202282629');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('50778537074','Luna Martins','False','non-b','1993-03-01','b+','Lago Matheus Cardoso, 3
São Luiz
64780-633 Gomes Verde / AM','29751626812','2021-05-28 01:07:58.194674-03:00',NULL,'','45202282629');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('26368196213','Henrique Rodrigues','False','cis','1937-05-18','b-','Jardim Luiz Otávio Souza, 74
Lajedo
37272208 Oliveira de Rezende / PB','67165224704','2021-05-28 01:07:58.337692-03:00',NULL,'','97441463814');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('81337642561','Ana Julia Barbosa','True','cis','1923-10-12','a-','Parque Rebeca Ribeiro, 3
Vila Tirol
14350834 Araújo Grande / AL','78182347032','2021-05-28 01:07:58.472209-03:00',NULL,'','84828333995');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('97489772180','Julia Moraes','False','cis','1948-04-25','null_rh','Via de Araújo, 7
Palmeiras
25873830 Barbosa de da Paz / AM','01400631106','2021-05-28 01:07:58.607226-03:00',NULL,'','34984954627');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('71725887739','Leandro Farias','False','non-b','1976-03-10','a-','Parque de Freitas
Marieta 3ª Seção
19858-403 Pereira / TO','41720889674','2021-05-28 01:07:58.736242-03:00',NULL,'','71437446494');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('31470298935','João Martins','True','non-b','1987-10-03','a-','Quadra de Lopes, 50
Araguaia
91712846 da Paz / DF','89074166474','2021-05-21 00:32:01.404700-03:00',NULL,'','25964933951');
INSERT INTO public.Paciente(CPF,nome,sexo,genero,data_nascimento,tipo_sangue,endereco,telefone,created_on,updated_on,dados,enfermeiro_id) VALUES ('44301834634','Bruno Aragão','True','non-b','1983-03-25','null_rh','Vila Emanuel Peixoto, 448
Penha
76461514 Teixeira / SC','08257559781','2021-05-21 00:32:00.459580-03:00',NULL,'','97441463814');
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4978491995','medicamento_143226','2021-05-21 00:32:08.536105-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4789220888','medicamento_960973','2021-05-21 00:32:11.484480-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6318994394','medicamento_872476','2021-05-21 00:32:12.760142-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2438099985','medicamento_995527','2021-05-21 00:32:12.892159-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5884950027','medicamento_590527','2021-05-21 00:32:13.103686-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8806961712','medicamento_178110','2021-05-21 00:32:13.280708-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1742314767','medicamento_31626','2021-05-21 00:32:13.366219-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8050890714','medicamento_113797','2021-05-21 00:32:13.566244-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3774394752','medicamento_216106','2021-05-21 00:32:13.652255-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7094368104','medicamento_413962','2021-05-21 00:32:13.798774-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6533947832','medicamento_605315','2021-05-21 00:32:13.881784-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7964541904','medicamento_131760','2021-05-21 00:32:14.014801-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2522200859','medicamento_206962','2021-05-21 00:32:14.207826-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2285145013','medicamento_541385','2021-05-21 00:32:14.289336-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9184702822','medicamento_427496','2021-05-21 00:32:14.361845-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2215305717','medicamento_856847','2021-05-21 00:32:14.477860-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6499672883','medicamento_774164','2021-05-21 00:32:14.563871-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7283695928','medicamento_609432','2021-05-21 00:32:14.673385-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1443692943','medicamento_402464','2021-05-21 00:32:14.786899-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5307225915','medicamento_139879','2021-05-21 00:32:14.877911-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8786185854','medicamento_862246','2021-05-21 00:32:14.964422-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4813460180','medicamento_889244','2021-05-21 00:32:15.172948-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6415562395','medicamento_677247','2021-05-21 00:32:15.258459-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6337887104','medicamento_527279','2021-05-21 00:32:15.345470-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5368209549','medicamento_263013','2021-05-21 00:32:15.452484-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8116114259','medicamento_125475','2021-05-21 00:32:15.555997-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9884092583','medicamento_316742','2021-05-21 00:32:15.629006-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1827356608','medicamento_761148','2021-05-21 00:32:15.788026-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('735161311','medicamento_912428','2021-05-21 00:32:15.929044-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1350946825','medicamento_476595','2021-05-21 00:32:16.179576-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2258882167','medicamento_306476','2021-05-21 00:32:16.260586-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2558556285','medicamento_216006','2021-05-21 00:32:16.343597-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5460201450','medicamento_909773','2021-05-21 00:32:16.470613-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('828255939','medicamento_945597','2021-05-21 00:32:16.632134-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3648993786','medicamento_344667','2021-05-21 00:32:16.745148-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4976370672','medicamento_713391','2021-05-21 00:32:16.862663-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5800051804','medicamento_743987','2021-05-21 00:32:16.948174-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2932647887','medicamento_714740','2021-05-21 00:32:17.019683-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5625459741','medicamento_418216','2021-05-21 00:32:17.094692-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3007557411','medicamento_429608','2021-05-21 00:32:17.185204-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3802760722','medicamento_634120','2021-05-21 00:32:17.253712-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9550447357','medicamento_682949','2021-05-21 00:32:17.333723-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3057128783','medicamento_62953','2021-05-21 00:32:17.419734-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7395858521','medicamento_116482','2021-05-21 00:32:17.620259-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6690359214','medicamento_423922','2021-05-21 00:32:17.703270-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('2824593651','medicamento_515712','2021-05-21 00:32:17.917797-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1028523689','medicamento_455787','2021-05-28 01:07:58.779748-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1812763566','medicamento_183748','2021-05-28 01:07:58.837755-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5851788805','medicamento_372574','2021-05-28 01:07:58.880761-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('565878471','medicamento_779843','2021-05-28 01:07:58.924766-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3192140337','medicamento_660310','2021-05-28 01:07:58.967772-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7099831668','medicamento_343540','2021-05-28 01:07:59.010277-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3219501865','medicamento_812255','2021-05-28 01:07:59.051782-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4818716306','medicamento_885124','2021-05-28 01:07:59.093788-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5905745905','medicamento_987226','2021-05-28 01:07:59.136793-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8169032761','medicamento_626383','2021-05-28 01:07:59.178799-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3198837481','medicamento_446269','2021-05-28 01:07:59.220804-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8247036135','medicamento_9101','2021-05-28 01:07:59.263309-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5053252591','medicamento_176139','2021-05-28 01:07:59.317816-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4476108088','medicamento_552577','2021-05-28 01:07:59.359322-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8832532684','medicamento_146953','2021-05-28 01:07:59.402827-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('117586023','medicamento_698906','2021-05-28 01:07:59.445833-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7324105325','medicamento_412559','2021-05-28 01:07:59.488838-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7965181038','medicamento_121196','2021-05-28 01:07:59.531843-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5406126294','medicamento_243146','2021-05-28 01:07:59.574849-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5957660380','medicamento_976919','2021-05-28 01:07:59.617854-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5234238166','medicamento_263201','2021-05-28 01:07:59.659860-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4804520969','medicamento_102789','2021-05-28 01:07:59.701865-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4426323407','medicamento_290862','2021-05-28 01:07:59.744870-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('4572433988','medicamento_882462','2021-05-28 01:07:59.787876-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7583322789','medicamento_799182','2021-05-28 01:07:59.846383-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('9668395872','medicamento_804591','2021-05-28 01:07:59.893389-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7963628990','medicamento_277602','2021-05-28 01:07:59.936895-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('17117094','medicamento_379523','2021-05-28 01:07:59.978900-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3620390413','medicamento_530483','2021-05-28 01:08:00.023906-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3765594792','medicamento_946446','2021-05-28 01:08:00.066411-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3152588154','medicamento_823965','2021-05-28 01:08:00.111917-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3662532858','medicamento_270490','2021-05-28 01:08:00.153422-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('8903369766','medicamento_512256','2021-05-28 01:08:00.195928-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6724573762','medicamento_297724','2021-05-28 01:08:00.238433-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1416111705','medicamento_755775','2021-05-28 01:08:00.280939-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('477256669','medicamento_718672','2021-05-28 01:08:00.328945-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5476908370','medicamento_923515','2021-05-28 01:08:00.371450-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5129659556','medicamento_85729','2021-05-28 01:08:00.420956-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7131892020','medicamento_402738','2021-05-28 01:08:00.463962-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7171763690','medicamento_728716','2021-05-28 01:08:00.506467-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1902133322','medicamento_914446','2021-05-28 01:08:00.549473-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('3649001855','medicamento_556212','2021-05-28 01:08:00.592478-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5798590250','medicamento_820422','2021-05-28 01:08:00.634483-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('7476507203','medicamento_146884','2021-05-28 01:08:00.675489-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('6458633494','medicamento_802356','2021-05-28 01:08:00.717494-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1664107952','medicamento_387855','2021-05-28 01:08:00.759499-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('1567295228','medicamento_364352','2021-05-28 01:08:00.801505-03:00',NULL);
INSERT INTO public.Medicamento(codigo,nome,created_on,updated_on) VALUES ('5681249970','medicamento_820092','2021-05-28 01:08:00.853011-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('1','4789220888','86056765124','37.39','Checar batimentos','2021-05-21 00:32:18.231837-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('2','2824593651','86056765124','60.89','Aplicar doses em braÃƒÂ§os diferentes','2021-05-21 00:32:18.517373-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('3','3774394752','02484301543','64.69','','2021-05-21 00:32:18.917424-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('4','5460201450','71706660167','51.1','Aplicar doses em braÃƒÂ§os diferentes','2021-05-21 00:32:19.285470-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('5','5625459741','02484301543','50.74','','2021-05-21 00:32:19.604011-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('6','8786185854','72257143448','12.97','Checar batimentos','2021-05-21 00:32:19.899548-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('7','6337887104','44301834634','64.86','','2021-05-21 00:32:20.205587-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('8','2522200859','86056765124','28.68','Injetar na testa','2021-05-21 00:32:20.549631-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('9','9884092583','55614222350','58.2','','2021-05-21 00:32:20.969684-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('10','8806961712','69269418526','60.72','Injetar na testa','2021-05-21 00:32:21.574761-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('11','5800051804','65105857070','64.1','Aplicar doses em braÃƒÂ§os diferentes','2021-05-21 00:32:22.016317-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('12','5368209549','64794045636','11.37','Injetar na testa','2021-05-21 00:32:22.244346-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('13','6499672883','02484301543','33.46','Injetar na testa','2021-05-21 00:32:22.641897-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('14','2215305717','13377643987','32.34','','2021-05-21 00:32:23.056949-03:00',NULL);
INSERT INTO public.Posologia(id,medicamento,paciente,quantidade,notas,created_on,updated_on) VALUES ('15','1827356608','92079719817','8.86','Aplicar doses em braÃƒÂ§os diferentes','2021-05-21 00:32:23.473002-03:00',NULL);
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('1','1','72257143448','28365997206',NULL,'71437446494','2021-05-21 00:32:24.165090-03:00',NULL,'1985-01-12 16:22:27-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('2','10','69269418526',NULL,'74255628406','16721424607','2021-05-21 00:32:25.118211-03:00',NULL,'2006-02-15 12:57:55-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('3','10','02484301543','84828333995',NULL,'41096137008','2021-05-21 00:32:26.022326-03:00',NULL,'2018-12-14 06:06:47-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('4','1','40794324231','45202282629',NULL,'5583047314','2021-05-21 00:32:26.934442-03:00',NULL,'1979-03-17 02:29:39-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('5','2','31470298935',NULL,'2573559077','41096137008','2021-05-21 00:32:27.415003-03:00',NULL,'1976-06-09 04:16:30-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('6','2','02484301543','5770720438',NULL,'71437446494','2021-05-21 00:32:28.498140-03:00',NULL,'2019-09-09 18:59:04-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('7','6','31470298935',NULL,'82996495216','75578836399','2021-05-21 00:32:29.036709-03:00',NULL,'1999-10-31 16:43:23-02:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('8','8','64794045636',NULL,'8307105705','29990495623','2021-05-21 00:32:30.090843-03:00',NULL,'2000-10-27 05:16:51-02:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('9','13','69269418526','79357174178',NULL,'25964933951','2021-05-21 00:32:31.109472-03:00',NULL,'1983-03-23 12:40:51-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('10','9','55614222350','51849909218',NULL,'41096137008','2021-05-21 00:32:31.904073-03:00',NULL,'1996-01-28 18:42:14-02:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('11','12','55614222350','28365997206',NULL,'5583047314','2021-05-21 00:32:32.833191-03:00',NULL,'2006-08-07 03:27:21-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('12','14','18900731843',NULL,'90948553266','75578836399','2021-05-21 00:32:33.726304-03:00',NULL,'2018-06-27 23:24:59-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('13','7','40794324231','5770720438',NULL,'71437446494','2021-05-21 00:32:34.656922-03:00',NULL,'2004-08-02 17:23:05-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('14','14','86056765124',NULL,'47015360570','97441463814','2021-05-21 00:32:35.966589-03:00',NULL,'2002-09-08 17:44:16-03:00');
INSERT INTO public.Agendamento(id,posologia,paciente,enfermeiro,estagiario,enferchefe,created_on,updated_on,horario) VALUES ('15','7','57743031673','79357174178',NULL,'44201821435','2021-05-21 00:32:36.426147-03:00',NULL,'1991-06-22 17:39:50-03:00');