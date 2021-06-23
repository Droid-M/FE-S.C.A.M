--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-06-10 00:11:28

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
-- TOC entry 644 (class 1247 OID 253130)
-- Name: tipofuncionario; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.tipofuncionario AS ENUM (
    'ENFERMEIRO',
    'ESTAGIARIO',
    'ADMINISTRADOR',
    'ENFERMEIRO_CHEFE'
);


ALTER TYPE public.tipofuncionario OWNER TO postgres;

--
-- TOC entry 641 (class 1247 OID 253122)
-- Name: tipogenero; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.tipogenero AS ENUM (
    'cis',
    'trans',
    'non-b'
);


ALTER TYPE public.tipogenero OWNER TO postgres;

--
-- TOC entry 638 (class 1247 OID 253102)
-- Name: tiposangue; Type: TYPE; Schema: public; Owner: postgres
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


ALTER TYPE public.tiposangue OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 253180)
-- Name: administrador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.administrador (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.administrador OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 253178)
-- Name: administrador_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.administrador_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administrador_id_seq OWNER TO postgres;

--
-- TOC entry 3115 (class 0 OID 0)
-- Dependencies: 206
-- Name: administrador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.administrador_id_seq OWNED BY public.administrador.id;


--
-- TOC entry 215 (class 1259 OID 253224)
-- Name: agendamento; Type: TABLE; Schema: public; Owner: postgres
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


ALTER TABLE public.agendamento OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 253222)
-- Name: agendamento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.agendamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agendamento_id_seq OWNER TO postgres;

--
-- TOC entry 3116 (class 0 OID 0)
-- Dependencies: 214
-- Name: agendamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.agendamento_id_seq OWNED BY public.agendamento.id;


--
-- TOC entry 203 (class 1259 OID 253160)
-- Name: enfermeiro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enfermeiro (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.enfermeiro OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 253158)
-- Name: atendente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.atendente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atendente_id_seq OWNER TO postgres;

--
-- TOC entry 3117 (class 0 OID 0)
-- Dependencies: 202
-- Name: atendente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.atendente_id_seq OWNED BY public.enfermeiro.id;


--
-- TOC entry 205 (class 1259 OID 253170)
-- Name: enfermeirochefe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enfermeirochefe (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.enfermeirochefe OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 253168)
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.enfermeirochefe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enfermeirochefe_id_seq OWNER TO postgres;

--
-- TOC entry 3118 (class 0 OID 0)
-- Dependencies: 204
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.enfermeirochefe_id_seq OWNED BY public.enfermeirochefe.id;


--
-- TOC entry 209 (class 1259 OID 253190)
-- Name: estagiario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estagiario (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.estagiario OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 253188)
-- Name: estagiario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.estagiario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estagiario_id_seq OWNER TO postgres;

--
-- TOC entry 3119 (class 0 OID 0)
-- Dependencies: 208
-- Name: estagiario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.estagiario_id_seq OWNED BY public.estagiario.id;


--
-- TOC entry 201 (class 1259 OID 253149)
-- Name: funcionario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionario (
    cpf character(11) NOT NULL,
    nome character varying NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    senha character varying(80) NOT NULL,
    tipo public.tipofuncionario
);


ALTER TABLE public.funcionario OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 253200)
-- Name: medicamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medicamento (
    codigo bigint NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    nome character varying NOT NULL
);


ALTER TABLE public.medicamento OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 253198)
-- Name: medicamento_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.medicamento_codigo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medicamento_codigo_seq OWNER TO postgres;

--
-- TOC entry 3120 (class 0 OID 0)
-- Dependencies: 210
-- Name: medicamento_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.medicamento_codigo_seq OWNED BY public.medicamento.codigo;


--
-- TOC entry 200 (class 1259 OID 253139)
-- Name: paciente; Type: TABLE; Schema: public; Owner: postgres
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
    nome_atendente character(11) NOT NULL
);


ALTER TABLE public.paciente OWNER TO postgres;

--
-- TOC entry 3121 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.sexo; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.paciente.sexo IS 'Sexo biológico';


--
-- TOC entry 3122 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.genero; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.paciente.genero IS 'Gênero com o qual a pessoa se identifica';


--
-- TOC entry 3123 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.dados; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.paciente.dados IS 'Informações a respeito do diagnóstico do paciente';


--
-- TOC entry 3124 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN paciente.nome_atendente; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.paciente.nome_atendente IS 'Funcionario que cadastrou esse paciente. Restringir no código quais tipos de funionário podem cadastrar pacientes';


--
-- TOC entry 213 (class 1259 OID 253212)
-- Name: posologia; Type: TABLE; Schema: public; Owner: postgres
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


ALTER TABLE public.posologia OWNER TO postgres;

--
-- TOC entry 3125 (class 0 OID 0)
-- Dependencies: 213
-- Name: COLUMN posologia.quantidade; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.posologia.quantidade IS 'A quantidade diária a ser administrada';


--
-- TOC entry 212 (class 1259 OID 253210)
-- Name: posologia_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posologia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posologia_id_seq OWNER TO postgres;

--
-- TOC entry 3126 (class 0 OID 0)
-- Dependencies: 212
-- Name: posologia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posologia_id_seq OWNED BY public.posologia.id;


--
-- TOC entry 2912 (class 2604 OID 253183)
-- Name: administrador id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador ALTER COLUMN id SET DEFAULT nextval('public.administrador_id_seq'::regclass);


--
-- TOC entry 2918 (class 2604 OID 253227)
-- Name: agendamento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento ALTER COLUMN id SET DEFAULT nextval('public.agendamento_id_seq'::regclass);


--
-- TOC entry 2910 (class 2604 OID 253163)
-- Name: enfermeiro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeiro ALTER COLUMN id SET DEFAULT nextval('public.atendente_id_seq'::regclass);


--
-- TOC entry 2911 (class 2604 OID 253173)
-- Name: enfermeirochefe id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeirochefe ALTER COLUMN id SET DEFAULT nextval('public.enfermeirochefe_id_seq'::regclass);


--
-- TOC entry 2913 (class 2604 OID 253193)
-- Name: estagiario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estagiario ALTER COLUMN id SET DEFAULT nextval('public.estagiario_id_seq'::regclass);


--
-- TOC entry 2914 (class 2604 OID 253203)
-- Name: medicamento codigo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicamento ALTER COLUMN codigo SET DEFAULT nextval('public.medicamento_codigo_seq'::regclass);


--
-- TOC entry 2916 (class 2604 OID 253215)
-- Name: posologia id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posologia ALTER COLUMN id SET DEFAULT nextval('public.posologia_id_seq'::regclass);


--
-- TOC entry 3101 (class 0 OID 253180)
-- Dependencies: 207
-- Data for Name: administrador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.administrador (id, func_id) FROM stdin;
1	44049744591
2	26966471321
3	28199244086
4	15354957176
5	34557698361
6	51127455004
7	64367891470
8	42709278450
9	03130641541
10	56369183807
11	72729879268
12	86786396454
\.


--
-- TOC entry 3109 (class 0 OID 253224)
-- Dependencies: 215
-- Data for Name: agendamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.agendamento (id, posologia, paciente, enfermeiro, estagiario, enferchefe, created_on, updated_on, horario) FROM stdin;
1	7	61537729784	89412446295	\N	58521560360	2021-06-09 23:47:59.627872-03	\N	2015-07-10 13:12:32-03
2	9	57296140697	\N	21470406355	93816146824	2021-06-09 23:47:59.995893-03	\N	2006-04-08 15:35:33-03
3	11	24535573920	\N	41840804321	93816146824	2021-06-09 23:48:00.271909-03	\N	1990-08-27 13:14:31-03
4	5	13241859531	88413667621	\N	93816146824	2021-06-09 23:48:00.544925-03	\N	1977-12-09 21:01:41-03
5	11	80897338369	\N	56760430164	70632159907	2021-06-09 23:48:00.845942-03	\N	1981-04-28 00:08:45-03
6	7	13241859531	20598254059	\N	58521560360	2021-06-09 23:48:01.118958-03	\N	1999-01-14 11:54:31-02
7	7	17277322774	55406404824	\N	70632159907	2021-06-09 23:48:01.414975-03	\N	2015-04-03 19:13:00-03
8	11	18527115092	\N	83906679928	93816146824	2021-06-09 23:48:01.69299-03	\N	2019-08-24 09:45:12-03
9	9	18527115092	20598254059	\N	93816146824	2021-06-09 23:48:02.008008-03	\N	1978-07-22 01:02:33-03
10	10	24535573920	\N	22004035166	70632159907	2021-06-09 23:48:02.293025-03	\N	2000-06-06 13:57:03-03
11	11	01802415658	92629504311	\N	70632159907	2021-06-09 23:48:02.600042-03	\N	1975-12-31 18:04:37-03
12	10	17676366333	\N	21470406355	70632159907	2021-06-09 23:48:02.90606-03	\N	1991-02-28 07:13:53-03
\.


--
-- TOC entry 3097 (class 0 OID 253160)
-- Dependencies: 203
-- Data for Name: enfermeiro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enfermeiro (id, func_id) FROM stdin;
1	20598254059
2	88413667621
3	06147206928
4	89412446295
5	82432294883
6	92629504311
7	01470287463
8	55406404824
9	30236342464
\.


--
-- TOC entry 3099 (class 0 OID 253170)
-- Dependencies: 205
-- Data for Name: enfermeirochefe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enfermeirochefe (id, func_id) FROM stdin;
1	70632159907
2	93816146824
3	58521560360
\.


--
-- TOC entry 3103 (class 0 OID 253190)
-- Dependencies: 209
-- Data for Name: estagiario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estagiario (id, func_id) FROM stdin;
1	56760430164
2	22004035166
3	90007834322
4	52465019004
5	58886838126
6	41840804321
7	29078550271
8	05984283630
9	83906679928
10	21470406355
11	53943982187
\.


--
-- TOC entry 3095 (class 0 OID 253149)
-- Dependencies: 201
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.funcionario (cpf, nome, created_on, updated_on, senha, tipo) FROM stdin;
44049744591	Luana Freitas	2021-06-09 23:47:31.754278-03	\N	$2b$12$rp41AnFVw7brF2hlAlrXNO.LqddVxmFe/NEKFLjLkAdW4IIZ0Ovv.	ADMINISTRADOR
26966471321	Augusto Lopes	2021-06-09 23:47:32.325311-03	\N	$2b$12$nEWLiMYFAAWSy6OWJ9gzxuZP7a3.EL1YJO4PYokIMjJpTDA7IkO2W	ADMINISTRADOR
28199244086	Luiz Felipe Moreira	2021-06-09 23:47:32.911344-03	\N	$2b$12$1qTXNv3GA4ns6KL1hz23I.iWGyOpJ8YWtRia7cfzh02Ujh.9NwIN.	ADMINISTRADOR
15354957176	Emanuel Teixeira	2021-06-09 23:47:33.487377-03	\N	$2b$12$GpdbjnINHvsshOnjAIHp6OdlNudDx09ES1YtNWw/MB6j96XUBiq2S	ADMINISTRADOR
34557698361	Maria Vitória da Conceição	2021-06-09 23:47:34.05341-03	\N	$2b$12$xM2ukmgWLECm1JcJON8lC.WTGuEqZukXEwL/zHw4COcWgWRY5OgWa	ADMINISTRADOR
51127455004	Nicole Oliveira	2021-06-09 23:47:34.628442-03	\N	$2b$12$ns299D4eNO7zDNLESu.A9.aE4lse8dK1IHEhXiDi4mj2yUBBt/TUm	ADMINISTRADOR
64367891470	Olivia Lima	2021-06-09 23:47:35.187474-03	\N	$2b$12$WI5Yt9lzx83KeCf.G7HpeOvfCLyO0uKNxmEQbTTRH5TGPuXMN7MYy	ADMINISTRADOR
42709278450	Nicole Cavalcanti	2021-06-09 23:47:36.041523-03	\N	$2b$12$LGvLFg5zu3GrGXCAEIrfjejYUXhyaWpYAfU38pZV0YHlh0ni1sKJ2	ADMINISTRADOR
03130641541	Sr. Pedro Sales	2021-06-09 23:47:36.621556-03	\N	$2b$12$q2W.zB4S7kMtL/bE/g/W7.6zOHzLgfrq.3quxp4co7mEopafeQrMO	ADMINISTRADOR
56369183807	Melissa Ferreira	2021-06-09 23:47:37.168588-03	\N	$2b$12$JZJnygt4D1ilB4o.f/weEeQZJl92UdlQILRU1ENmm21MNRHrunj9.	ADMINISTRADOR
72729879268	Diogo da Rocha	2021-06-09 23:47:37.750621-03	\N	$2b$12$XYYIKUN96nFkSh2lDYW5JOxMOW4x7nKymBut7SpSMrawWZhao6Viy	ADMINISTRADOR
86786396454	Pedro Henrique Gomes	2021-06-09 23:47:38.311653-03	\N	$2b$12$Mw8Jb9h4J3UVG8H1ckD5p.i9ozZhObYKf9MyVDYaCmWhy/ww/Exge	ADMINISTRADOR
20598254059	Caio Alves	2021-06-09 23:47:38.857684-03	\N	$2b$12$om7UGXD64XBY3evK4Zo7mej4e8O7DeP.ME7uDMx/wIqcU4RUFVDTq	ENFERMEIRO
88413667621	Maria Alice Jesus	2021-06-09 23:47:39.422717-03	\N	$2b$12$Stg/cqx1KUdIdDbJ67d5Ne0bV8Pp5VEdTEZ3AkK8Ih8GUzInMH/Mq	ENFERMEIRO
06147206928	Maria Eduarda Martins	2021-06-09 23:47:39.990749-03	\N	$2b$12$IZoiTOsr28k3lm1EvytsjenfKwTOIBa5X6TuaPcVEfpvaqyMapaju	ENFERMEIRO
89412446295	Rodrigo Gonçalves	2021-06-09 23:47:40.574783-03	\N	$2b$12$gQPUGztSA0CLePJDeTioLuMfQ7RIPXS7lp3Dgd/orG7j41Sr9942q	ENFERMEIRO
82432294883	Lorena Pereira	2021-06-09 23:47:41.244821-03	\N	$2b$12$D9BzjmTbQUblWBIxyFVILO5ICzoqiKxbK3CTjd8jy7g7Gz4S9VKqC	ENFERMEIRO
92629504311	Giovanna da Cunha	2021-06-09 23:47:41.831854-03	\N	$2b$12$dupVQJGMVwY/AsvIlW6MLucs19YHA52r7UtS476k0l0fwO/7LPx3a	ENFERMEIRO
01470287463	Theo Silva	2021-06-09 23:47:42.377886-03	\N	$2b$12$7u2vUFbtpNWY4jg8RYk2quASfRWrksbE.uwYJa6t.D85yCOGlOpJG	ENFERMEIRO
55406404824	Fernanda da Mata	2021-06-09 23:47:42.936918-03	\N	$2b$12$aOzVsnk1UbZsBg3T4CV8CuF4hlK80tSdE/mcFCQeeN9Zexw2q2YKK	ENFERMEIRO
30236342464	Cauã da Conceição	2021-06-09 23:47:43.50695-03	\N	$2b$12$I0MOS7xsyD8SmOqH3zhvVO43cynXdX34ENXiNY3cPtrViBOiKqQ3G	ENFERMEIRO
56760430164	Eduardo Pinto	2021-06-09 23:47:44.130986-03	\N	$2b$12$oJpuqO/X3Hk2H9hb.FcQHOIejidJUerUAwUjEHiGtgJ.61M9ZdUy2	ESTAGIARIO
22004035166	Sra. Daniela Vieira	2021-06-09 23:47:44.71902-03	\N	$2b$12$tW48wNamuLiT3lBpwTl5DOJR9lnVLxm8XKjnPgvkuaybJGysecerm	ESTAGIARIO
90007834322	Igor Oliveira	2021-06-09 23:47:45.398058-03	\N	$2b$12$y.3gd.sXyrQYn1Tg1JuxHOBEjWDixYpR3RDl8i.1TBBqqBM7OKUnu	ESTAGIARIO
52465019004	Davi Lucca Gonçalves	2021-06-09 23:47:46.081097-03	\N	$2b$12$jLEgmKse/ua93MVr.VuViO70fmcS/edTeXb52neGYCfLxjsinim8K	ESTAGIARIO
58886838126	Diogo Moraes	2021-06-09 23:47:46.65513-03	\N	$2b$12$IBqF24hCJQlBwf3FDTQ1SOtisWxd/MqWtPOkd7Gv3VRyuv4BrDVmy	ESTAGIARIO
41840804321	Manuela das Neves	2021-06-09 23:47:47.224163-03	\N	$2b$12$PBCP5Ny5Wut3msHSTP7ahu5p/lF/2RWRMcZXP.RFE18figv6YQi8m	ESTAGIARIO
29078550271	Davi Lucca Campos	2021-06-09 23:47:47.8772-03	\N	$2b$12$sc.lXwVRnLPSLemhlqpFrOc59xhkmVmoKlUShYKOYQozkYKMVTs3u	ESTAGIARIO
05984283630	João Lucas Gonçalves	2021-06-09 23:47:48.514237-03	\N	$2b$12$rrpH/fcEvclTs1cPhiZRPeBGBqYkxeMw3iQdhVk8Dl4wo.n/0VGHa	ESTAGIARIO
83906679928	Natália Ferreira	2021-06-09 23:47:49.199276-03	\N	$2b$12$HolrmNSCZOCc4YrgslNjE.zrzZt6Wb/rcZ87SAHpos5xNAvVjoXxK	ESTAGIARIO
21470406355	Amanda Nogueira	2021-06-09 23:47:49.771309-03	\N	$2b$12$sjG20WTZIdMN1gF7df9LA.WYiqfiurQXbHUeZURxT4KwWbbO1g35q	ESTAGIARIO
53943982187	Dr. Heitor Farias	2021-06-09 23:47:50.354342-03	\N	$2b$12$uIqtGZQ0iULh2fotwnrKQu2JrVJULLntzIk3PS1qO.Aa3wYvoEh6y	ESTAGIARIO
70632159907	Sr. Paulo Cavalcanti	2021-06-09 23:47:51.783424-03	\N	$2b$12$ti1WXhKY/C0IJPyqvEJMgOB5q8zUN5mSgiYhW/kpDQ9UxBYtKyftC	ENFERMEIRO_CHEFE
93816146824	Dr. Joaquim Monteiro	2021-06-09 23:47:52.354456-03	\N	$2b$12$3kRyH995acu.nozsilVOZOCBe3hlxmdIyrxNTTIsQccs513Jz2STK	ENFERMEIRO_CHEFE
58521560360	Ana Laura Nascimento	2021-06-09 23:47:52.924489-03	\N	$2b$12$CGDNzKytuTHXYnzgXJ2lT.by/jfh2Li1ZkqzmoYNYysvBcgnwmK9a	ENFERMEIRO_CHEFE
\.


--
-- TOC entry 3105 (class 0 OID 253200)
-- Dependencies: 211
-- Data for Name: medicamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medicamento (codigo, created_on, updated_on, nome) FROM stdin;
1192525998	2021-06-09 23:47:55.080612-03	\N	medicamento_132325
1386546905	2021-06-09 23:47:55.131615-03	\N	medicamento_12180
6293068054	2021-06-09 23:47:55.174618-03	\N	medicamento_513886
9834177877	2021-06-09 23:47:55.22562-03	\N	medicamento_316843
8122350700	2021-06-09 23:47:55.269623-03	\N	medicamento_523154
8908676662	2021-06-09 23:47:55.314626-03	\N	medicamento_83913
5643375004	2021-06-09 23:47:55.367629-03	\N	medicamento_117368
8360639553	2021-06-09 23:47:55.420632-03	\N	medicamento_657484
4998420047	2021-06-09 23:47:55.465634-03	\N	medicamento_84142
3167656605	2021-06-09 23:47:55.514637-03	\N	medicamento_113006
5447914097	2021-06-09 23:47:55.557639-03	\N	medicamento_389936
8925948000	2021-06-09 23:47:55.600642-03	\N	medicamento_112359
716230710	2021-06-09 23:47:55.644644-03	\N	medicamento_241950
6789374916	2021-06-09 23:47:55.696647-03	\N	medicamento_963712
4251943327	2021-06-09 23:47:55.74865-03	\N	medicamento_873167
7274353064	2021-06-09 23:47:55.798653-03	\N	medicamento_953490
3706309257	2021-06-09 23:47:55.847656-03	\N	medicamento_891089
6439157673	2021-06-09 23:47:55.895659-03	\N	medicamento_298843
2087107885	2021-06-09 23:47:55.941661-03	\N	medicamento_834178
6662394926	2021-06-09 23:47:55.989664-03	\N	medicamento_473517
3844522213	2021-06-09 23:47:56.040667-03	\N	medicamento_325846
97550314	2021-06-09 23:47:56.08567-03	\N	medicamento_817278
3630664391	2021-06-09 23:47:56.137673-03	\N	medicamento_739419
2592254520	2021-06-09 23:47:56.183675-03	\N	medicamento_605124
8604758137	2021-06-09 23:47:56.247679-03	\N	medicamento_770788
5870104837	2021-06-09 23:47:56.295682-03	\N	medicamento_725144
132704754	2021-06-09 23:47:56.345685-03	\N	medicamento_542902
7685310988	2021-06-09 23:47:56.393687-03	\N	medicamento_230422
1726502006	2021-06-09 23:47:56.44569-03	\N	medicamento_301429
297807769	2021-06-09 23:47:56.489693-03	\N	medicamento_486810
8865740052	2021-06-09 23:47:56.534695-03	\N	medicamento_903212
5307491878	2021-06-09 23:47:56.577698-03	\N	medicamento_345547
7434221548	2021-06-09 23:47:56.6217-03	\N	medicamento_691682
9058083540	2021-06-09 23:47:56.665703-03	\N	medicamento_78935
5347247046	2021-06-09 23:47:56.738707-03	\N	medicamento_55087
3605481991	2021-06-09 23:47:56.828712-03	\N	medicamento_90635
7003478777	2021-06-09 23:47:56.897716-03	\N	medicamento_47139
8360995784	2021-06-09 23:47:56.942719-03	\N	medicamento_629150
8453246801	2021-06-09 23:47:56.990721-03	\N	medicamento_796182
4512666685	2021-06-09 23:47:57.038724-03	\N	medicamento_525270
8954799218	2021-06-09 23:47:57.084727-03	\N	medicamento_30516
9130111037	2021-06-09 23:47:57.129729-03	\N	medicamento_850867
960730104	2021-06-09 23:47:57.180732-03	\N	medicamento_27264
7028829866	2021-06-09 23:47:57.228735-03	\N	medicamento_711545
5759931485	2021-06-09 23:47:57.275738-03	\N	medicamento_199805
7351534698	2021-06-09 23:47:57.32074-03	\N	medicamento_469530
4287474486	2021-06-09 23:47:57.366743-03	\N	medicamento_662232
317410744	2021-06-09 23:47:57.415746-03	\N	medicamento_183724
6577170825	2021-06-09 23:47:57.467749-03	\N	medicamento_222384
2270436883	2021-06-09 23:47:57.512751-03	\N	medicamento_787962
4809282657	2021-06-09 23:47:57.556754-03	\N	medicamento_110855
\.


--
-- TOC entry 3094 (class 0 OID 253139)
-- Dependencies: 200
-- Data for Name: paciente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paciente (cpf, nome, sexo, genero, data_nascimento, tipo_sangue, endereco, telefone, created_on, updated_on, dados, nome_atendente) FROM stdin;
02295602357	Pietro Nunes	t	non-b	2002-06-08	ab-	Quadra de Rezende, 775\nVila Trinta E Um De Março\n26990535 Vieira de Farias / CE	44451182505	2021-06-09 23:47:53.1155-03	\N		92629504311
24535573920	Vitor Gabriel Martins	t	non-b	1975-01-31	b+	Fazenda Davi Lucca da Cunha, 7\nVila Bandeirantes\n22653443 Vieira / PA	84946712174	2021-06-09 23:47:53.266508-03	\N		92629504311
61537729784	Sr. Thales Oliveira	t	trans	1982-06-09	o-	Ladeira Moura, 156\nJardim Alvorada\n95114818 Barros do Galho / PA	56006357515	2021-06-09 23:47:53.437518-03	\N		89412446295
97083957658	Ana Luiza Souza	t	non-b	1944-11-16	ab+	Avenida de Pereira, 6\nVila Canto Do Sabiá\n98806513 Souza Grande / ES	16058542112	2021-06-09 23:47:53.571526-03	\N		55406404824
38936755718	Dr. Paulo da Conceição	f	non-b	1984-06-17	null_rh	Distrito Lucas Freitas, 4\nJoão Paulo Ii\n44133061 Rodrigues da Praia / SC	14700559577	2021-06-09 23:47:53.718534-03	\N		06147206928
17676366333	Isabella Dias	f	trans	1955-10-07	o-	Fazenda Ramos, 797\nSalgado Filho\n12539-765 Cavalcanti de Goiás / PI	41208169260	2021-06-09 23:47:53.870543-03	\N		92629504311
80897338369	Yasmin Cardoso	t	trans	1992-12-31	null_rh	Morro Dias, 29\nDelta\n26792-808 da Conceição Verde / RS	99936518360	2021-06-09 23:47:54.013551-03	\N		55406404824
32899623383	Pietra Cavalcanti	f	cis	1933-12-12	a+	Núcleo da Paz, 60\nMarilandia\n71096034 Farias / MG	59616385881	2021-06-09 23:47:54.154559-03	\N		01470287463
13241859531	Luiz Gustavo Barros	t	trans	1926-02-15	o+	Área Isabella Melo, 95\nVila Novo São Lucas\n04205287 Lima dos Dourados / AP	57717829683	2021-06-09 23:47:54.290567-03	\N		88413667621
50296955810	Ana Souza	f	non-b	1965-04-23	a+	Passarela Almeida, 41\nVila Nova Cachoeirinha 1ª Seção\n83963-861 Pires / RN	75722181768	2021-06-09 23:47:54.437575-03	\N		70632159907
01802415658	Sr. Isaac Sales	t	non-b	2000-11-22	ab-	Avenida Melo, 221\nErmelinda\n66389482 Cunha Verde / MT	94982244699	2021-06-09 23:47:54.585584-03	\N		06147206928
17277322774	Mariane Freitas	t	cis	1988-03-06	b-	Rua de Martins, 78\nVila Ouro Minas\n81357-797 Vieira / MS	50068865083	2021-06-09 23:47:54.759594-03	\N		70632159907
57296140697	Lorenzo Moura	t	trans	1957-12-20	o-	Núcleo Lima, 577\nVila Canto Do Sabiá\n26923713 Nunes / RS	08717351147	2021-06-09 23:47:54.897602-03	\N		89412446295
18527115092	Vitória da Conceição	f	non-b	1929-10-30	ab-	Setor Maria Clara Moraes\nCanadá\n48120920 Aragão Alegre / PB	08127341920	2021-06-09 23:47:55.03361-03	\N		88413667621
\.


--
-- TOC entry 3107 (class 0 OID 253212)
-- Dependencies: 213
-- Data for Name: posologia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posologia (id, medicamento, paciente, quantidade, created_on, updated_on, notas) FROM stdin;
1	7003478777	50296955810	53.27	2021-06-09 23:47:57.696762-03	\N	Injetar na testa
2	8925948000	38936755718	10.73	2021-06-09 23:47:57.850771-03	\N	Checar batimentos
3	9130111037	17676366333	65.58	2021-06-09 23:47:58.01178-03	\N	
4	297807769	13241859531	28.69	2021-06-09 23:47:58.149788-03	\N	Checar batimentos
5	5870104837	01802415658	13.6	2021-06-09 23:47:58.311797-03	\N	Checar batimentos
6	297807769	01802415658	0.49	2021-06-09 23:47:58.452805-03	\N	Aplicar doses em braços diferentes
7	5870104837	17676366333	1.25	2021-06-09 23:47:58.587813-03	\N	
8	8453246801	97083957658	1.78	2021-06-09 23:47:58.726821-03	\N	Aplicar doses em braços diferentes
9	8360995784	97083957658	64.1	2021-06-09 23:47:58.89183-03	\N	Checar batimentos
10	6577170825	38936755718	35.76	2021-06-09 23:47:59.050839-03	\N	Aplicar doses em braços diferentes
11	9130111037	17676366333	40.28	2021-06-09 23:47:59.204848-03	\N	Checar batimentos
12	5870104837	18527115092	56.04	2021-06-09 23:47:59.357857-03	\N	Checar batimentos
\.


--
-- TOC entry 3127 (class 0 OID 0)
-- Dependencies: 206
-- Name: administrador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.administrador_id_seq', 12, true);


--
-- TOC entry 3128 (class 0 OID 0)
-- Dependencies: 214
-- Name: agendamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.agendamento_id_seq', 12, true);


--
-- TOC entry 3129 (class 0 OID 0)
-- Dependencies: 202
-- Name: atendente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.atendente_id_seq', 9, true);


--
-- TOC entry 3130 (class 0 OID 0)
-- Dependencies: 204
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.enfermeirochefe_id_seq', 3, true);


--
-- TOC entry 3131 (class 0 OID 0)
-- Dependencies: 208
-- Name: estagiario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.estagiario_id_seq', 11, true);


--
-- TOC entry 3132 (class 0 OID 0)
-- Dependencies: 210
-- Name: medicamento_codigo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.medicamento_codigo_seq', 1, false);


--
-- TOC entry 3133 (class 0 OID 0)
-- Dependencies: 212
-- Name: posologia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posologia_id_seq', 12, true);


--
-- TOC entry 2938 (class 2606 OID 253187)
-- Name: administrador administrador_func_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_func_id_key UNIQUE (func_id);


--
-- TOC entry 2940 (class 2606 OID 253185)
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id);


--
-- TOC entry 2956 (class 2606 OID 253230)
-- Name: agendamento agendamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id);


--
-- TOC entry 2928 (class 2606 OID 253167)
-- Name: enfermeiro enfermeiro_func_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_func_id_key UNIQUE (func_id);


--
-- TOC entry 2930 (class 2606 OID 253165)
-- Name: enfermeiro enfermeiro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_pkey PRIMARY KEY (id);


--
-- TOC entry 2933 (class 2606 OID 253177)
-- Name: enfermeirochefe enfermeirochefe_func_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_func_id_key UNIQUE (func_id);


--
-- TOC entry 2935 (class 2606 OID 253175)
-- Name: enfermeirochefe enfermeirochefe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_pkey PRIMARY KEY (id);


--
-- TOC entry 2943 (class 2606 OID 253197)
-- Name: estagiario estagiario_func_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_func_id_key UNIQUE (func_id);


--
-- TOC entry 2945 (class 2606 OID 253195)
-- Name: estagiario estagiario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_pkey PRIMARY KEY (id);


--
-- TOC entry 2925 (class 2606 OID 253157)
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (cpf);


--
-- TOC entry 2948 (class 2606 OID 253209)
-- Name: medicamento medicamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicamento
    ADD CONSTRAINT medicamento_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2922 (class 2606 OID 253148)
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (cpf);


--
-- TOC entry 2951 (class 2606 OID 253221)
-- Name: posologia posologia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_pkey PRIMARY KEY (id);


--
-- TOC entry 2936 (class 1259 OID 253270)
-- Name: administrador_func_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX administrador_func_id_idx ON public.administrador USING btree (func_id);


--
-- TOC entry 2952 (class 1259 OID 253276)
-- Name: agendamento_horario_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX agendamento_horario_idx ON public.agendamento USING btree (horario);


--
-- TOC entry 2953 (class 1259 OID 253274)
-- Name: agendamento_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX agendamento_id_idx ON public.agendamento USING btree (id);


--
-- TOC entry 2954 (class 1259 OID 253275)
-- Name: agendamento_paciente_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX agendamento_paciente_idx ON public.agendamento USING btree (paciente);


--
-- TOC entry 2926 (class 1259 OID 253268)
-- Name: enfermeiro_func_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX enfermeiro_func_id_idx ON public.enfermeiro USING btree (func_id);


--
-- TOC entry 2931 (class 1259 OID 253269)
-- Name: enfermeirochefe_func_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX enfermeirochefe_func_id_idx ON public.enfermeirochefe USING btree (func_id);


--
-- TOC entry 2941 (class 1259 OID 253271)
-- Name: estagiario_func_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX estagiario_func_id_idx ON public.estagiario USING btree (func_id);


--
-- TOC entry 2923 (class 1259 OID 253267)
-- Name: funcionario_cpf_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX funcionario_cpf_idx ON public.funcionario USING btree (cpf);


--
-- TOC entry 2946 (class 1259 OID 253272)
-- Name: medicamento_codigo_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX medicamento_codigo_idx ON public.medicamento USING btree (codigo);


--
-- TOC entry 2920 (class 1259 OID 253266)
-- Name: paciente_cpf_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX paciente_cpf_idx ON public.paciente USING btree (cpf);


--
-- TOC entry 2949 (class 1259 OID 253273)
-- Name: posologia_paciente_medicamento_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX posologia_paciente_medicamento_idx ON public.posologia USING btree (paciente, medicamento);


--
-- TOC entry 2960 (class 2606 OID 253246)
-- Name: administrador administrador_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2958 (class 2606 OID 253236)
-- Name: enfermeiro enfermeiro_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2959 (class 2606 OID 253241)
-- Name: enfermeirochefe enfermeirochefe_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2961 (class 2606 OID 253251)
-- Name: estagiario estagiario_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2957 (class 2606 OID 253231)
-- Name: paciente paciente_atendente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_atendente_id_fkey FOREIGN KEY (nome_atendente) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2962 (class 2606 OID 253256)
-- Name: posologia posologia_medicamento_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_medicamento_fkey FOREIGN KEY (medicamento) REFERENCES public.medicamento(codigo) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2963 (class 2606 OID 253261)
-- Name: posologia posologia_paciente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_paciente_fkey FOREIGN KEY (paciente) REFERENCES public.paciente(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2021-06-10 00:11:29

--
-- PostgreSQL database dump complete
--

