--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-22 21:45:00

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 3112 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 641 (class 1247 OID 199928)
-- Name: tipogenero; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.tipogenero AS ENUM (
    'cis',
    'trans',
    'non-b'
);


--
-- TOC entry 638 (class 1247 OID 199909)
-- Name: tiposangue; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.tiposangue AS ENUM (
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


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 199976)
-- Name: administrador; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.administrador (
    id bigint NOT NULL,
    func_id character(11)
);


--
-- TOC entry 206 (class 1259 OID 199974)
-- Name: administrador_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.administrador_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3113 (class 0 OID 0)
-- Dependencies: 206
-- Name: administrador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.administrador_id_seq OWNED BY public.administrador.id;


--
-- TOC entry 215 (class 1259 OID 200020)
-- Name: agendamento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.agendamento (
    id bigint NOT NULL,
    posologia bigint NOT NULL,
    paciente character(11) NOT NULL,
    enfermeiro bigint,
    estagiario bigint,
    enferchefe bigint NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    horario timestamp with time zone
);


--
-- TOC entry 214 (class 1259 OID 200018)
-- Name: agendamento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.agendamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3114 (class 0 OID 0)
-- Dependencies: 214
-- Name: agendamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.agendamento_id_seq OWNED BY public.agendamento.id;


--
-- TOC entry 203 (class 1259 OID 199956)
-- Name: enfermeiro; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.enfermeiro (
    id bigint NOT NULL,
    func_id character(11)
);


--
-- TOC entry 202 (class 1259 OID 199954)
-- Name: enfermeiro_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.enfermeiro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3115 (class 0 OID 0)
-- Dependencies: 202
-- Name: enfermeiro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.enfermeiro_id_seq OWNED BY public.enfermeiro.id;


--
-- TOC entry 205 (class 1259 OID 199966)
-- Name: enfermeirochefe; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.enfermeirochefe (
    id bigint NOT NULL,
    func_id character(11)
);


--
-- TOC entry 204 (class 1259 OID 199964)
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.enfermeirochefe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3116 (class 0 OID 0)
-- Dependencies: 204
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.enfermeirochefe_id_seq OWNED BY public.enfermeirochefe.id;


--
-- TOC entry 209 (class 1259 OID 199986)
-- Name: estagiario; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.estagiario (
    id bigint NOT NULL,
    func_id character(11)
);


--
-- TOC entry 208 (class 1259 OID 199984)
-- Name: estagiario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.estagiario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3117 (class 0 OID 0)
-- Dependencies: 208
-- Name: estagiario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.estagiario_id_seq OWNED BY public.estagiario.id;


--
-- TOC entry 201 (class 1259 OID 199945)
-- Name: funcionario; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.funcionario (
    cpf character(11) NOT NULL,
    nome character varying NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    senha character varying(80) NOT NULL
);


--
-- TOC entry 211 (class 1259 OID 199996)
-- Name: medicamento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.medicamento (
    codigo bigint NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    nome character varying NOT NULL
);


--
-- TOC entry 210 (class 1259 OID 199994)
-- Name: medicamento_codigo_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.medicamento_codigo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3118 (class 0 OID 0)
-- Dependencies: 210
-- Name: medicamento_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.medicamento_codigo_seq OWNED BY public.medicamento.codigo;


--
-- TOC entry 200 (class 1259 OID 199935)
-- Name: paciente; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.paciente (
    cpf character(11) NOT NULL,
    nome character varying NOT NULL,
    sexo boolean,
    genero public.tipogenero,
    data_nascimento date,
    tipo_sangue public.tiposangue,
    endereco character varying,
    telefone character(11) DEFAULT NULL::bpchar,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    dados character varying,
    enfermeiro_id character(11) NOT NULL
);


--
-- TOC entry 3119 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.sexo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.paciente.sexo IS 'Sexo biolÃƒÂ³gico';


--
-- TOC entry 3120 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.genero; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.paciente.genero IS 'GÃƒÂªnero com o qual a pessoa se identifica';


--
-- TOC entry 3121 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.dados; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.paciente.dados IS 'InformaÃƒÂ§ÃƒÂµes a respeito do diagnÃƒÂ³stico do paciente';


--
-- TOC entry 3122 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.enfermeiro_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.paciente.enfermeiro_id IS 'Funcionario que cadastrou esse paciente. Restringir no cÃƒÂ³digo quais tipos de funionÃƒÂ¡rio podem cadastrar pacientes';


--
-- TOC entry 213 (class 1259 OID 200008)
-- Name: posologia; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.posologia (
    id bigint NOT NULL,
    medicamento bigint,
    paciente character(11) NOT NULL,
    quantidade double precision NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    notas character varying
);


--
-- TOC entry 3123 (class 0 OID 0)
-- Dependencies: 213
-- Name: COLUMN posologia.quantidade; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.posologia.quantidade IS 'A quantidade diÃƒÂ¡ria a ser administrada';


--
-- TOC entry 212 (class 1259 OID 200006)
-- Name: posologia_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.posologia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3124 (class 0 OID 0)
-- Dependencies: 212
-- Name: posologia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.posologia_id_seq OWNED BY public.posologia.id;


--
-- TOC entry 2909 (class 2604 OID 199979)
-- Name: administrador id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrador ALTER COLUMN id SET DEFAULT nextval('public.administrador_id_seq'::regclass);


--
-- TOC entry 2915 (class 2604 OID 200023)
-- Name: agendamento id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.agendamento ALTER COLUMN id SET DEFAULT nextval('public.agendamento_id_seq'::regclass);


--
-- TOC entry 2907 (class 2604 OID 199959)
-- Name: enfermeiro id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeiro ALTER COLUMN id SET DEFAULT nextval('public.enfermeiro_id_seq'::regclass);


--
-- TOC entry 2908 (class 2604 OID 199969)
-- Name: enfermeirochefe id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeirochefe ALTER COLUMN id SET DEFAULT nextval('public.enfermeirochefe_id_seq'::regclass);


--
-- TOC entry 2910 (class 2604 OID 199989)
-- Name: estagiario id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.estagiario ALTER COLUMN id SET DEFAULT nextval('public.estagiario_id_seq'::regclass);


--
-- TOC entry 2911 (class 2604 OID 199999)
-- Name: medicamento codigo; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.medicamento ALTER COLUMN codigo SET DEFAULT nextval('public.medicamento_codigo_seq'::regclass);


--
-- TOC entry 2913 (class 2604 OID 200011)
-- Name: posologia id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posologia ALTER COLUMN id SET DEFAULT nextval('public.posologia_id_seq'::regclass);


--
-- TOC entry 3098 (class 0 OID 199976)
-- Dependencies: 207
-- Data for Name: administrador; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 3106 (class 0 OID 200020)
-- Dependencies: 215
-- Data for Name: agendamento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.agendamento VALUES (1, 1, '72257143448', 28365997206, NULL, 71437446494, '2021-05-21 00:32:24.16509-03', NULL, '1985-01-12 16:22:27-03');
INSERT INTO public.agendamento VALUES (2, 10, '69269418526', NULL, 74255628406, 16721424607, '2021-05-21 00:32:25.118211-03', NULL, '2006-02-15 12:57:55-03');
INSERT INTO public.agendamento VALUES (3, 10, '02484301543', 84828333995, NULL, 41096137008, '2021-05-21 00:32:26.022326-03', NULL, '2018-12-14 06:06:47-03');
INSERT INTO public.agendamento VALUES (4, 1, '40794324231', 45202282629, NULL, 5583047314, '2021-05-21 00:32:26.934442-03', NULL, '1979-03-17 02:29:39-03');
INSERT INTO public.agendamento VALUES (5, 2, '31470298935', NULL, 2573559077, 41096137008, '2021-05-21 00:32:27.415003-03', NULL, '1976-06-09 04:16:30-03');
INSERT INTO public.agendamento VALUES (6, 2, '02484301543', 5770720438, NULL, 71437446494, '2021-05-21 00:32:28.49814-03', NULL, '2019-09-09 18:59:04-03');
INSERT INTO public.agendamento VALUES (7, 6, '31470298935', NULL, 82996495216, 75578836399, '2021-05-21 00:32:29.036709-03', NULL, '1999-10-31 16:43:23-02');
INSERT INTO public.agendamento VALUES (8, 8, '64794045636', NULL, 8307105705, 29990495623, '2021-05-21 00:32:30.090843-03', NULL, '2000-10-27 05:16:51-02');
INSERT INTO public.agendamento VALUES (9, 13, '69269418526', 79357174178, NULL, 25964933951, '2021-05-21 00:32:31.109472-03', NULL, '1983-03-23 12:40:51-03');
INSERT INTO public.agendamento VALUES (10, 9, '55614222350', 51849909218, NULL, 41096137008, '2021-05-21 00:32:31.904073-03', NULL, '1996-01-28 18:42:14-02');
INSERT INTO public.agendamento VALUES (11, 12, '55614222350', 28365997206, NULL, 5583047314, '2021-05-21 00:32:32.833191-03', NULL, '2006-08-07 03:27:21-03');
INSERT INTO public.agendamento VALUES (12, 14, '18900731843', NULL, 90948553266, 75578836399, '2021-05-21 00:32:33.726304-03', NULL, '2018-06-27 23:24:59-03');
INSERT INTO public.agendamento VALUES (13, 7, '40794324231', 5770720438, NULL, 71437446494, '2021-05-21 00:32:34.656922-03', NULL, '2004-08-02 17:23:05-03');
INSERT INTO public.agendamento VALUES (14, 14, '86056765124', NULL, 47015360570, 97441463814, '2021-05-21 00:32:35.966589-03', NULL, '2002-09-08 17:44:16-03');
INSERT INTO public.agendamento VALUES (15, 7, '57743031673', 79357174178, NULL, 44201821435, '2021-05-21 00:32:36.426147-03', NULL, '1991-06-22 17:39:50-03');


--
-- TOC entry 3094 (class 0 OID 199956)
-- Dependencies: 203
-- Data for Name: enfermeiro; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.enfermeiro VALUES (1, '71375160116');
INSERT INTO public.enfermeiro VALUES (2, '40181898460');
INSERT INTO public.enfermeiro VALUES (3, '51849909218');
INSERT INTO public.enfermeiro VALUES (4, '45202282629');
INSERT INTO public.enfermeiro VALUES (5, '05770720438');
INSERT INTO public.enfermeiro VALUES (6, '28365997206');
INSERT INTO public.enfermeiro VALUES (7, '34984954627');
INSERT INTO public.enfermeiro VALUES (8, '69839219802');
INSERT INTO public.enfermeiro VALUES (9, '84828333995');
INSERT INTO public.enfermeiro VALUES (10, '79357174178');
INSERT INTO public.enfermeiro VALUES (11, '32108412377');


--
-- TOC entry 3096 (class 0 OID 199966)
-- Dependencies: 205
-- Data for Name: enfermeirochefe; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.enfermeirochefe VALUES (1, '44201821435');
INSERT INTO public.enfermeirochefe VALUES (2, '05583047314');
INSERT INTO public.enfermeirochefe VALUES (3, '16721424607');
INSERT INTO public.enfermeirochefe VALUES (5, '75578836399');
INSERT INTO public.enfermeirochefe VALUES (6, '71437446494');
INSERT INTO public.enfermeirochefe VALUES (7, '25964933951');
INSERT INTO public.enfermeirochefe VALUES (8, '29990495623');
INSERT INTO public.enfermeirochefe VALUES (9, '97441463814');


--
-- TOC entry 3100 (class 0 OID 199986)
-- Dependencies: 209
-- Data for Name: estagiario; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.estagiario VALUES (1, '21148074068');
INSERT INTO public.estagiario VALUES (2, '82996495216');
INSERT INTO public.estagiario VALUES (3, '85174297656');
INSERT INTO public.estagiario VALUES (4, '47015360570');
INSERT INTO public.estagiario VALUES (5, '02573559077');
INSERT INTO public.estagiario VALUES (6, '74957236822');
INSERT INTO public.estagiario VALUES (7, '15580080774');
INSERT INTO public.estagiario VALUES (8, '90948553266');
INSERT INTO public.estagiario VALUES (9, '74255628406');
INSERT INTO public.estagiario VALUES (10, '09477601436');
INSERT INTO public.estagiario VALUES (11, '08307105705');


--
-- TOC entry 3092 (class 0 OID 199945)
-- Dependencies: 201
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.funcionario VALUES ('71375160116', 'Carlos Eduardo da ConceiÃ§Ã£o', '2021-05-21 00:31:47.708961-03', NULL, '3mNCHI60%@');
INSERT INTO public.funcionario VALUES ('40181898460', 'Leonardo Souza', '2021-05-21 00:31:47.919488-03', NULL, '5xR%2OhhuJ');
INSERT INTO public.funcionario VALUES ('51849909218', 'Kamilly da Cunha', '2021-05-21 00:31:48.989623-03', NULL, '+5!JqC8J^w');
INSERT INTO public.funcionario VALUES ('45202282629', 'Luiz Miguel Pereira', '2021-05-21 00:31:49.736218-03', NULL, '&Vu7IAe3+r');
INSERT INTO public.funcionario VALUES ('05770720438', 'Dr. Thiago Cavalcanti', '2021-05-21 00:31:50.172274-03', NULL, '5qCM8fJC!a');
INSERT INTO public.funcionario VALUES ('28365997206', 'Augusto Barros', '2021-05-21 00:31:51.286415-03', NULL, '_1#V1eGk00');
INSERT INTO public.funcionario VALUES ('34984954627', 'Sr. Fernando Nogueira', '2021-05-21 00:31:51.842986-03', NULL, '5py0p#Fr!A');
INSERT INTO public.funcionario VALUES ('69839219802', 'Ana JÃºlia Rezende', '2021-05-21 00:31:52.227535-03', NULL, '6)1GjSfVJ&');
INSERT INTO public.funcionario VALUES ('84828333995', 'CauÃ£ Pinto', '2021-05-21 00:31:52.457064-03', NULL, '9shJWMxD^2');
INSERT INTO public.funcionario VALUES ('79357174178', 'LavÃ­nia da Rocha', '2021-05-21 00:31:52.7406-03', NULL, '+!9Z#2ezL1');
INSERT INTO public.funcionario VALUES ('32108412377', 'Nina Castro', '2021-05-21 00:31:53.274668-03', NULL, '@R2&PQhUwl');
INSERT INTO public.funcionario VALUES ('21148074068', 'Mirella Sales', '2021-05-21 00:31:53.991259-03', NULL, 'Kl8GXrzB#D');
INSERT INTO public.funcionario VALUES ('82996495216', 'Kevin Correia', '2021-05-21 00:31:54.706849-03', NULL, '(+6GfYynd!');
INSERT INTO public.funcionario VALUES ('85174297656', 'Carlos Eduardo Porto', '2021-05-21 00:31:55.071896-03', NULL, '&6GGHw+yx6');
INSERT INTO public.funcionario VALUES ('47015360570', 'Murilo Moreira', '2021-05-21 00:31:55.366433-03', NULL, 'p_iF08CeaT');
INSERT INTO public.funcionario VALUES ('02573559077', 'Sr. Miguel Santos', '2021-05-21 00:31:55.711977-03', NULL, '(zonAgNmn2');
INSERT INTO public.funcionario VALUES ('74957236822', 'Ana Beatriz da Costa', '2021-05-21 00:31:56.070023-03', NULL, '0JjMIx2z^s');
INSERT INTO public.funcionario VALUES ('15580080774', 'JoÃ£o Vitor da Luz', '2021-05-21 00:31:56.309053-03', NULL, '31$CPEzI@9');
INSERT INTO public.funcionario VALUES ('90948553266', 'Catarina Duarte', '2021-05-21 00:31:56.723105-03', NULL, '&oBV$fqiX2');
INSERT INTO public.funcionario VALUES ('74255628406', 'Luiz Felipe Costa', '2021-05-21 00:31:56.91613-03', NULL, 'aO5ExztC8@');
INSERT INTO public.funcionario VALUES ('09477601436', 'Heitor Ferreira', '2021-05-21 00:31:57.069649-03', NULL, 'u(3YtX227x');
INSERT INTO public.funcionario VALUES ('08307105705', 'Sra. Maria VitÃ³ria Teixeira', '2021-05-21 00:31:57.236671-03', NULL, '*0U+^Ujl&3');
INSERT INTO public.funcionario VALUES ('44201821435', 'Gabriela Campos', '2021-05-21 00:31:57.495704-03', NULL, '92dGZkEg@n');
INSERT INTO public.funcionario VALUES ('05583047314', 'Francisco Pinto', '2021-05-21 00:31:57.760737-03', NULL, '$lNN1qVH42');
INSERT INTO public.funcionario VALUES ('16721424607', 'BÃ¡rbara Nogueira', '2021-05-21 00:31:58.031772-03', NULL, 'Z+BN8L5eaR');
INSERT INTO public.funcionario VALUES ('75578836399', 'Renan Farias', '2021-05-21 00:31:58.366314-03', NULL, '_VhS6MmZ$T');
INSERT INTO public.funcionario VALUES ('71437446494', 'Maysa da Cruz', '2021-05-21 00:31:58.65035-03', NULL, 'Ob&G2Hn^M&');
INSERT INTO public.funcionario VALUES ('25964933951', 'Diogo Correia', '2021-05-21 00:31:59.083405-03', NULL, '1#7sCT^mQU');
INSERT INTO public.funcionario VALUES ('29990495623', 'Augusto Moura', '2021-05-21 00:31:59.526961-03', NULL, '@H1Qom0nfb');
INSERT INTO public.funcionario VALUES ('97441463814', 'Vitor Gabriel Costa', '2021-05-21 00:31:59.840501-03', NULL, '65uUqlDO%A');


--
-- TOC entry 3102 (class 0 OID 199996)
-- Dependencies: 211
-- Data for Name: medicamento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.medicamento VALUES (4978491995, '2021-05-21 00:32:08.536105-03', NULL, 'medicamento_143226');
INSERT INTO public.medicamento VALUES (4789220888, '2021-05-21 00:32:11.48448-03', NULL, 'medicamento_960973');
INSERT INTO public.medicamento VALUES (6318994394, '2021-05-21 00:32:12.760142-03', NULL, 'medicamento_872476');
INSERT INTO public.medicamento VALUES (2438099985, '2021-05-21 00:32:12.892159-03', NULL, 'medicamento_995527');
INSERT INTO public.medicamento VALUES (5884950027, '2021-05-21 00:32:13.103686-03', NULL, 'medicamento_590527');
INSERT INTO public.medicamento VALUES (8806961712, '2021-05-21 00:32:13.280708-03', NULL, 'medicamento_178110');
INSERT INTO public.medicamento VALUES (1742314767, '2021-05-21 00:32:13.366219-03', NULL, 'medicamento_31626');
INSERT INTO public.medicamento VALUES (8050890714, '2021-05-21 00:32:13.566244-03', NULL, 'medicamento_113797');
INSERT INTO public.medicamento VALUES (3774394752, '2021-05-21 00:32:13.652255-03', NULL, 'medicamento_216106');
INSERT INTO public.medicamento VALUES (7094368104, '2021-05-21 00:32:13.798774-03', NULL, 'medicamento_413962');
INSERT INTO public.medicamento VALUES (6533947832, '2021-05-21 00:32:13.881784-03', NULL, 'medicamento_605315');
INSERT INTO public.medicamento VALUES (7964541904, '2021-05-21 00:32:14.014801-03', NULL, 'medicamento_131760');
INSERT INTO public.medicamento VALUES (2522200859, '2021-05-21 00:32:14.207826-03', NULL, 'medicamento_206962');
INSERT INTO public.medicamento VALUES (2285145013, '2021-05-21 00:32:14.289336-03', NULL, 'medicamento_541385');
INSERT INTO public.medicamento VALUES (9184702822, '2021-05-21 00:32:14.361845-03', NULL, 'medicamento_427496');
INSERT INTO public.medicamento VALUES (2215305717, '2021-05-21 00:32:14.47786-03', NULL, 'medicamento_856847');
INSERT INTO public.medicamento VALUES (6499672883, '2021-05-21 00:32:14.563871-03', NULL, 'medicamento_774164');
INSERT INTO public.medicamento VALUES (7283695928, '2021-05-21 00:32:14.673385-03', NULL, 'medicamento_609432');
INSERT INTO public.medicamento VALUES (1443692943, '2021-05-21 00:32:14.786899-03', NULL, 'medicamento_402464');
INSERT INTO public.medicamento VALUES (5307225915, '2021-05-21 00:32:14.877911-03', NULL, 'medicamento_139879');
INSERT INTO public.medicamento VALUES (8786185854, '2021-05-21 00:32:14.964422-03', NULL, 'medicamento_862246');
INSERT INTO public.medicamento VALUES (4813460180, '2021-05-21 00:32:15.172948-03', NULL, 'medicamento_889244');
INSERT INTO public.medicamento VALUES (6415562395, '2021-05-21 00:32:15.258459-03', NULL, 'medicamento_677247');
INSERT INTO public.medicamento VALUES (6337887104, '2021-05-21 00:32:15.34547-03', NULL, 'medicamento_527279');
INSERT INTO public.medicamento VALUES (5368209549, '2021-05-21 00:32:15.452484-03', NULL, 'medicamento_263013');
INSERT INTO public.medicamento VALUES (8116114259, '2021-05-21 00:32:15.555997-03', NULL, 'medicamento_125475');
INSERT INTO public.medicamento VALUES (9884092583, '2021-05-21 00:32:15.629006-03', NULL, 'medicamento_316742');
INSERT INTO public.medicamento VALUES (1827356608, '2021-05-21 00:32:15.788026-03', NULL, 'medicamento_761148');
INSERT INTO public.medicamento VALUES (735161311, '2021-05-21 00:32:15.929044-03', NULL, 'medicamento_912428');
INSERT INTO public.medicamento VALUES (1350946825, '2021-05-21 00:32:16.179576-03', NULL, 'medicamento_476595');
INSERT INTO public.medicamento VALUES (2258882167, '2021-05-21 00:32:16.260586-03', NULL, 'medicamento_306476');
INSERT INTO public.medicamento VALUES (2558556285, '2021-05-21 00:32:16.343597-03', NULL, 'medicamento_216006');
INSERT INTO public.medicamento VALUES (5460201450, '2021-05-21 00:32:16.470613-03', NULL, 'medicamento_909773');
INSERT INTO public.medicamento VALUES (828255939, '2021-05-21 00:32:16.632134-03', NULL, 'medicamento_945597');
INSERT INTO public.medicamento VALUES (3648993786, '2021-05-21 00:32:16.745148-03', NULL, 'medicamento_344667');
INSERT INTO public.medicamento VALUES (4976370672, '2021-05-21 00:32:16.862663-03', NULL, 'medicamento_713391');
INSERT INTO public.medicamento VALUES (5800051804, '2021-05-21 00:32:16.948174-03', NULL, 'medicamento_743987');
INSERT INTO public.medicamento VALUES (2932647887, '2021-05-21 00:32:17.019683-03', NULL, 'medicamento_714740');
INSERT INTO public.medicamento VALUES (5625459741, '2021-05-21 00:32:17.094692-03', NULL, 'medicamento_418216');
INSERT INTO public.medicamento VALUES (3007557411, '2021-05-21 00:32:17.185204-03', NULL, 'medicamento_429608');
INSERT INTO public.medicamento VALUES (3802760722, '2021-05-21 00:32:17.253712-03', NULL, 'medicamento_634120');
INSERT INTO public.medicamento VALUES (9550447357, '2021-05-21 00:32:17.333723-03', NULL, 'medicamento_682949');
INSERT INTO public.medicamento VALUES (3057128783, '2021-05-21 00:32:17.419734-03', NULL, 'medicamento_62953');
INSERT INTO public.medicamento VALUES (7395858521, '2021-05-21 00:32:17.620259-03', NULL, 'medicamento_116482');
INSERT INTO public.medicamento VALUES (6690359214, '2021-05-21 00:32:17.70327-03', NULL, 'medicamento_423922');
INSERT INTO public.medicamento VALUES (2824593651, '2021-05-21 00:32:17.917797-03', NULL, 'medicamento_515712');


--
-- TOC entry 3091 (class 0 OID 199935)
-- Dependencies: 200
-- Data for Name: paciente; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.paciente VALUES ('44301834634', 'Bruno AragÃ£o', true, 'non-b', '1983-03-25', 'null_rh', 'Vila Emanuel Peixoto, 448
Penha
76461514 Teixeira / SC', '08257559781', '2021-05-21 00:32:00.45958-03', NULL, '', '97441463814');
INSERT INTO public.paciente VALUES ('18900731843', 'Daniel Porto', true, 'non-b', '1958-05-04', 'o-', 'Setor Eduardo Peixoto
Nova Vista
98373095 Mendes Verde / ES', '82633428109', '2021-05-21 00:32:00.725614-03', NULL, '', '40181898460');
INSERT INTO public.paciente VALUES ('31470298935', 'JoÃ£o Martins', true, 'non-b', '1987-10-03', 'a-', 'Quadra de Lopes, 50
Araguaia
91712846 da Paz / DF', '89074166474', '2021-05-21 00:32:01.4047-03', NULL, '', '25964933951');
INSERT INTO public.paciente VALUES ('40794324231', 'Yago Nascimento', false, 'cis', '1983-08-26', 'a+', 'Lago de Lopes
Pantanal
23337-424 Cardoso / RN', '14465283871', '2021-05-21 00:32:01.816252-03', NULL, '', '16721424607');
INSERT INTO public.paciente VALUES ('57743031673', 'Maria Clara Ferreira', true, 'trans', '1934-12-28', 'o+', 'Lagoa de Santos, 50
Pilar
76196-268 Nascimento / CE', '23879968782', '2021-05-21 00:32:02.170297-03', NULL, '', '16721424607');
INSERT INTO public.paciente VALUES ('13377643987', 'Gabriel Lima', true, 'trans', '1954-12-10', 'ab+', 'Viaduto Emanuella Sales, 80
Vila Nova Gameleira 2Âª SeÃ§Ã£o
64305-143 Oliveira da Prata / PR', '15399729749', '2021-05-21 00:32:02.648358-03', NULL, '', '34984954627');
INSERT INTO public.paciente VALUES ('86056765124', 'Alice Duarte', false, 'non-b', '1936-07-31', 'b+', 'Largo de Moreira
Marilandia
24854-742 Teixeira / SE', '93580554293', '2021-05-21 00:32:03.071412-03', NULL, '', '05770720438');
INSERT INTO public.paciente VALUES ('49475995813', 'AlÃ­cia Moura', false, 'non-b', '1927-10-25', 'ab-', 'Largo Renan Silveira
Oeste
06619031 Pinto de Cunha / MA', '66789382551', '2021-05-21 00:32:03.391952-03', NULL, '', '71375160116');
INSERT INTO public.paciente VALUES ('55614222350', 'Maria Fernandes', false, 'non-b', '1991-07-08', 'o+', 'Fazenda Teixeira, 6
Taquaril
10383661 Caldeira / SC', '37982936204', '2021-05-21 00:32:03.858011-03', NULL, '', '05583047314');
INSERT INTO public.paciente VALUES ('64794045636', 'Diogo da Rosa', true, 'cis', '1944-08-11', 'ab-', 'Travessa de Fernandes, 98
Trevo
53720-932 Lima / BA', '01666849964', '2021-05-21 00:32:04.334572-03', NULL, '', '84828333995');
INSERT INTO public.paciente VALUES ('69269418526', 'Maria CecÃ­lia Rocha', false, 'cis', '1926-09-02', 'o+', 'ColÃ´nia de da Mota, 376
Salgado Filho
18093801 Correia Paulista / SP', '24694276520', '2021-05-21 00:32:04.593605-03', NULL, '', '28365997206');
INSERT INTO public.paciente VALUES ('72257143448', 'Dr. Noah Moura', false, 'cis', '1923-03-06', 'null_rh', 'PÃ¡tio de Farias
Barroca
00974939 Pinto do Sul / ES', '76195962809', '2021-05-21 00:32:04.856138-03', NULL, '', '75578836399');
INSERT INTO public.paciente VALUES ('02484301543', 'Rodrigo Duarte', true, 'trans', '1928-11-03', 'ab-', 'PÃ¡tio da Cruz, 23
SÃ£o Jorge 3Âª SeÃ§Ã£o
10694673 da Luz Grande / AM', '35652068553', '2021-05-21 00:32:05.093668-03', NULL, '', '51849909218');
INSERT INTO public.paciente VALUES ('62419002277', 'Stella da Cruz', false, 'non-b', '1925-06-08', 'o+', 'Feira Freitas, 24
Monsenhor Messias
43921-405 Rocha de Porto / ES', '19254320585', '2021-05-21 00:32:05.330198-03', NULL, '', '29990495623');
INSERT INTO public.paciente VALUES ('92079719817', 'Sr. Emanuel Ribeiro', true, 'cis', '1946-05-24', 'b-', 'Conjunto de Nogueira, 6
Nazare
84866-719 Ramos / GO', '35505917646', '2021-05-21 00:32:05.549226-03', NULL, '', '79357174178');
INSERT INTO public.paciente VALUES ('71706660167', 'Pedro Henrique Pereira', false, 'cis', '1988-03-27', 'b-', 'Conjunto CecÃ­lia Santos, 99
Atila De Paiva
90173834 Rezende / PB', '54292352984', '2021-05-21 00:32:06.092795-03', NULL, '', '51849909218');
INSERT INTO public.paciente VALUES ('65105857070', 'Lucas Gabriel da Paz', true, 'trans', '1977-03-30', 'null_rh', 'PÃ¡tio LÃ­via Silva, 5
Vila ParaÃ­so
79603776 Lopes / RN', '16786996057', '2021-05-21 00:32:06.988409-03', NULL, '', '05770720438');


--
-- TOC entry 3104 (class 0 OID 200008)
-- Dependencies: 213
-- Data for Name: posologia; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.posologia VALUES (1, 4789220888, '86056765124', 37.39, '2021-05-21 00:32:18.231837-03', NULL, 'Checar batimentos');
INSERT INTO public.posologia VALUES (2, 2824593651, '86056765124', 60.89, '2021-05-21 00:32:18.517373-03', NULL, 'Aplicar doses em braÃ§os diferentes');
INSERT INTO public.posologia VALUES (3, 3774394752, '02484301543', 64.69, '2021-05-21 00:32:18.917424-03', NULL, '');
INSERT INTO public.posologia VALUES (4, 5460201450, '71706660167', 51.1, '2021-05-21 00:32:19.28547-03', NULL, 'Aplicar doses em braÃ§os diferentes');
INSERT INTO public.posologia VALUES (5, 5625459741, '02484301543', 50.74, '2021-05-21 00:32:19.604011-03', NULL, '');
INSERT INTO public.posologia VALUES (6, 8786185854, '72257143448', 12.97, '2021-05-21 00:32:19.899548-03', NULL, 'Checar batimentos');
INSERT INTO public.posologia VALUES (7, 6337887104, '44301834634', 64.86, '2021-05-21 00:32:20.205587-03', NULL, '');
INSERT INTO public.posologia VALUES (8, 2522200859, '86056765124', 28.68, '2021-05-21 00:32:20.549631-03', NULL, 'Injetar na testa');
INSERT INTO public.posologia VALUES (9, 9884092583, '55614222350', 58.2, '2021-05-21 00:32:20.969684-03', NULL, '');
INSERT INTO public.posologia VALUES (10, 8806961712, '69269418526', 60.72, '2021-05-21 00:32:21.574761-03', NULL, 'Injetar na testa');
INSERT INTO public.posologia VALUES (11, 5800051804, '65105857070', 64.1, '2021-05-21 00:32:22.016317-03', NULL, 'Aplicar doses em braÃ§os diferentes');
INSERT INTO public.posologia VALUES (12, 5368209549, '64794045636', 11.37, '2021-05-21 00:32:22.244346-03', NULL, 'Injetar na testa');
INSERT INTO public.posologia VALUES (13, 6499672883, '02484301543', 33.46, '2021-05-21 00:32:22.641897-03', NULL, 'Injetar na testa');
INSERT INTO public.posologia VALUES (14, 2215305717, '13377643987', 32.34, '2021-05-21 00:32:23.056949-03', NULL, '');
INSERT INTO public.posologia VALUES (15, 1827356608, '92079719817', 8.86, '2021-05-21 00:32:23.473002-03', NULL, 'Aplicar doses em braÃ§os diferentes');


--
-- TOC entry 3125 (class 0 OID 0)
-- Dependencies: 206
-- Name: administrador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.administrador_id_seq', 1, false);


--
-- TOC entry 3126 (class 0 OID 0)
-- Dependencies: 214
-- Name: agendamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.agendamento_id_seq', 15, true);


--
-- TOC entry 3127 (class 0 OID 0)
-- Dependencies: 202
-- Name: enfermeiro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.enfermeiro_id_seq', 11, true);


--
-- TOC entry 3128 (class 0 OID 0)
-- Dependencies: 204
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.enfermeirochefe_id_seq', 9, true);


--
-- TOC entry 3129 (class 0 OID 0)
-- Dependencies: 208
-- Name: estagiario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.estagiario_id_seq', 11, true);


--
-- TOC entry 3130 (class 0 OID 0)
-- Dependencies: 210
-- Name: medicamento_codigo_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.medicamento_codigo_seq', 1, false);


--
-- TOC entry 3131 (class 0 OID 0)
-- Dependencies: 212
-- Name: posologia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.posologia_id_seq', 15, true);


--
-- TOC entry 2935 (class 2606 OID 199983)
-- Name: administrador administrador_func_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_func_id_key UNIQUE (func_id);


--
-- TOC entry 2937 (class 2606 OID 199981)
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id);


--
-- TOC entry 2953 (class 2606 OID 200026)
-- Name: agendamento agendamento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id);


--
-- TOC entry 2925 (class 2606 OID 199963)
-- Name: enfermeiro enfermeiro_func_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_func_id_key UNIQUE (func_id);


--
-- TOC entry 2927 (class 2606 OID 199961)
-- Name: enfermeiro enfermeiro_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_pkey PRIMARY KEY (id);


--
-- TOC entry 2930 (class 2606 OID 199973)
-- Name: enfermeirochefe enfermeirochefe_func_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_func_id_key UNIQUE (func_id);


--
-- TOC entry 2932 (class 2606 OID 199971)
-- Name: enfermeirochefe enfermeirochefe_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_pkey PRIMARY KEY (id);


--
-- TOC entry 2940 (class 2606 OID 199993)
-- Name: estagiario estagiario_func_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_func_id_key UNIQUE (func_id);


--
-- TOC entry 2942 (class 2606 OID 199991)
-- Name: estagiario estagiario_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_pkey PRIMARY KEY (id);


--
-- TOC entry 2922 (class 2606 OID 199953)
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (cpf);


--
-- TOC entry 2945 (class 2606 OID 200005)
-- Name: medicamento medicamento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.medicamento
    ADD CONSTRAINT medicamento_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2919 (class 2606 OID 199944)
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (cpf);


--
-- TOC entry 2948 (class 2606 OID 200017)
-- Name: posologia posologia_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_pkey PRIMARY KEY (id);


--
-- TOC entry 2933 (class 1259 OID 200066)
-- Name: administrador_func_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX administrador_func_id_idx ON public.administrador USING btree (func_id);


--
-- TOC entry 2949 (class 1259 OID 200072)
-- Name: agendamento_horario_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX agendamento_horario_idx ON public.agendamento USING btree (horario);


--
-- TOC entry 2950 (class 1259 OID 200070)
-- Name: agendamento_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX agendamento_id_idx ON public.agendamento USING btree (id);


--
-- TOC entry 2951 (class 1259 OID 200071)
-- Name: agendamento_paciente_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX agendamento_paciente_idx ON public.agendamento USING btree (paciente);


--
-- TOC entry 2923 (class 1259 OID 200064)
-- Name: enfermeiro_func_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX enfermeiro_func_id_idx ON public.enfermeiro USING btree (func_id);


--
-- TOC entry 2928 (class 1259 OID 200065)
-- Name: enfermeirochefe_func_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX enfermeirochefe_func_id_idx ON public.enfermeirochefe USING btree (func_id);


--
-- TOC entry 2938 (class 1259 OID 200067)
-- Name: estagiario_func_id_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX estagiario_func_id_idx ON public.estagiario USING btree (func_id);


--
-- TOC entry 2920 (class 1259 OID 200063)
-- Name: funcionario_cpf_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX funcionario_cpf_idx ON public.funcionario USING btree (cpf);


--
-- TOC entry 2943 (class 1259 OID 200068)
-- Name: medicamento_codigo_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX medicamento_codigo_idx ON public.medicamento USING btree (codigo);


--
-- TOC entry 2917 (class 1259 OID 200062)
-- Name: paciente_cpf_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX paciente_cpf_idx ON public.paciente USING btree (cpf);


--
-- TOC entry 2946 (class 1259 OID 200069)
-- Name: posologia_paciente_medicamento_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX posologia_paciente_medicamento_idx ON public.posologia USING btree (paciente, medicamento);


--
-- TOC entry 2957 (class 2606 OID 200042)
-- Name: administrador administrador_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2955 (class 2606 OID 200032)
-- Name: enfermeiro enfermeiro_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2956 (class 2606 OID 200037)
-- Name: enfermeirochefe enfermeirochefe_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2958 (class 2606 OID 200047)
-- Name: estagiario estagiario_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2954 (class 2606 OID 200027)
-- Name: paciente paciente_enfermeiro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_enfermeiro_id_fkey FOREIGN KEY (enfermeiro_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2959 (class 2606 OID 200052)
-- Name: posologia posologia_medicamento_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_medicamento_fkey FOREIGN KEY (medicamento) REFERENCES public.medicamento(codigo) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2960 (class 2606 OID 200057)
-- Name: posologia posologia_paciente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_paciente_fkey FOREIGN KEY (paciente) REFERENCES public.paciente(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2021-05-22 21:45:00

--
-- PostgreSQL database dump complete
--

