--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Debian 13.2-1.pgdg100+1)
-- Dumped by pg_dump version 13.2 (Debian 13.2-1.pgdg100+1)

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
-- Name: tipogenero; Type: TYPE; Schema: public; Owner: fescam
--

CREATE TYPE public.tipogenero AS ENUM (
    'cis',
    'trans',
    'non-b'
);


ALTER TYPE public.tipogenero OWNER TO fescam;

--
-- Name: tiposangue; Type: TYPE; Schema: public; Owner: fescam
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


ALTER TYPE public.tiposangue OWNER TO fescam;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: administrador; Type: TABLE; Schema: public; Owner: fescam
--

CREATE TABLE public.administrador (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.administrador OWNER TO fescam;

--
-- Name: administrador_id_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.administrador_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administrador_id_seq OWNER TO fescam;

--
-- Name: administrador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.administrador_id_seq OWNED BY public.administrador.id;


--
-- Name: agendamento; Type: TABLE; Schema: public; Owner: fescam
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


ALTER TABLE public.agendamento OWNER TO fescam;

--
-- Name: agendamento_id_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.agendamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agendamento_id_seq OWNER TO fescam;

--
-- Name: agendamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.agendamento_id_seq OWNED BY public.agendamento.id;


--
-- Name: enfermeiro; Type: TABLE; Schema: public; Owner: fescam
--

CREATE TABLE public.enfermeiro (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.enfermeiro OWNER TO fescam;

--
-- Name: enfermeiro_id_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.enfermeiro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enfermeiro_id_seq OWNER TO fescam;

--
-- Name: enfermeiro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.enfermeiro_id_seq OWNED BY public.enfermeiro.id;


--
-- Name: enfermeirochefe; Type: TABLE; Schema: public; Owner: fescam
--

CREATE TABLE public.enfermeirochefe (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.enfermeirochefe OWNER TO fescam;

--
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.enfermeirochefe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enfermeirochefe_id_seq OWNER TO fescam;

--
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.enfermeirochefe_id_seq OWNED BY public.enfermeirochefe.id;


--
-- Name: estagiario; Type: TABLE; Schema: public; Owner: fescam
--

CREATE TABLE public.estagiario (
    id bigint NOT NULL,
    func_id character(11)
);


ALTER TABLE public.estagiario OWNER TO fescam;

--
-- Name: estagiario_id_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.estagiario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estagiario_id_seq OWNER TO fescam;

--
-- Name: estagiario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.estagiario_id_seq OWNED BY public.estagiario.id;


--
-- Name: funcionario; Type: TABLE; Schema: public; Owner: fescam
--

CREATE TABLE public.funcionario (
    cpf character(11) NOT NULL,
    nome character varying NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    senha bytea
);


ALTER TABLE public.funcionario OWNER TO fescam;

--
-- Name: medicamento; Type: TABLE; Schema: public; Owner: fescam
--

CREATE TABLE public.medicamento (
    codigo bigint NOT NULL,
    created_on timestamp with time zone DEFAULT now(),
    updated_on timestamp with time zone,
    nome character varying NOT NULL
);


ALTER TABLE public.medicamento OWNER TO fescam;

--
-- Name: medicamento_codigo_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.medicamento_codigo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medicamento_codigo_seq OWNER TO fescam;

--
-- Name: medicamento_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.medicamento_codigo_seq OWNED BY public.medicamento.codigo;


--
-- Name: paciente; Type: TABLE; Schema: public; Owner: fescam
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


ALTER TABLE public.paciente OWNER TO fescam;

--
-- Name: COLUMN paciente.sexo; Type: COMMENT; Schema: public; Owner: fescam
--

COMMENT ON COLUMN public.paciente.sexo IS 'Sexo biológico';


--
-- Name: COLUMN paciente.genero; Type: COMMENT; Schema: public; Owner: fescam
--

COMMENT ON COLUMN public.paciente.genero IS 'Gênero com o qual a pessoa se identifica';


--
-- Name: COLUMN paciente.dados; Type: COMMENT; Schema: public; Owner: fescam
--

COMMENT ON COLUMN public.paciente.dados IS 'Informações a respeito do diagnóstico do paciente';


--
-- Name: COLUMN paciente.enfermeiro_id; Type: COMMENT; Schema: public; Owner: fescam
--

COMMENT ON COLUMN public.paciente.enfermeiro_id IS 'Funcionario que cadastrou esse paciente. Restringir no código quais tipos de funionário podem cadastrar pacientes';


--
-- Name: posologia; Type: TABLE; Schema: public; Owner: fescam
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


ALTER TABLE public.posologia OWNER TO fescam;

--
-- Name: COLUMN posologia.quantidade; Type: COMMENT; Schema: public; Owner: fescam
--

COMMENT ON COLUMN public.posologia.quantidade IS 'A quantidade diária a ser administrada';


--
-- Name: posologia_id_seq; Type: SEQUENCE; Schema: public; Owner: fescam
--

CREATE SEQUENCE public.posologia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posologia_id_seq OWNER TO fescam;

--
-- Name: posologia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fescam
--

ALTER SEQUENCE public.posologia_id_seq OWNED BY public.posologia.id;


--
-- Name: administrador id; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.administrador ALTER COLUMN id SET DEFAULT nextval('public.administrador_id_seq'::regclass);


--
-- Name: agendamento id; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.agendamento ALTER COLUMN id SET DEFAULT nextval('public.agendamento_id_seq'::regclass);


--
-- Name: enfermeiro id; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeiro ALTER COLUMN id SET DEFAULT nextval('public.enfermeiro_id_seq'::regclass);


--
-- Name: enfermeirochefe id; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeirochefe ALTER COLUMN id SET DEFAULT nextval('public.enfermeirochefe_id_seq'::regclass);


--
-- Name: estagiario id; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.estagiario ALTER COLUMN id SET DEFAULT nextval('public.estagiario_id_seq'::regclass);


--
-- Name: medicamento codigo; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.medicamento ALTER COLUMN codigo SET DEFAULT nextval('public.medicamento_codigo_seq'::regclass);


--
-- Name: posologia id; Type: DEFAULT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.posologia ALTER COLUMN id SET DEFAULT nextval('public.posologia_id_seq'::regclass);


--
-- Data for Name: administrador; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.administrador (id, func_id) FROM stdin;
\.


--
-- Data for Name: agendamento; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.agendamento (id, posologia, paciente, enfermeiro, estagiario, enferchefe, created_on, updated_on, horario) FROM stdin;
1	1	72257143448	28365997206	\N	71437446494	2021-05-21 03:32:24.16509+00	\N	1985-01-12 19:22:27+00
2	10	69269418526	\N	74255628406	16721424607	2021-05-21 03:32:25.118211+00	\N	2006-02-15 15:57:55+00
3	10	02484301543	84828333995	\N	41096137008	2021-05-21 03:32:26.022326+00	\N	2018-12-14 09:06:47+00
4	1	40794324231	45202282629	\N	5583047314	2021-05-21 03:32:26.934442+00	\N	1979-03-17 05:29:39+00
5	2	31470298935	\N	2573559077	41096137008	2021-05-21 03:32:27.415003+00	\N	1976-06-09 07:16:30+00
6	2	02484301543	5770720438	\N	71437446494	2021-05-21 03:32:28.49814+00	\N	2019-09-09 21:59:04+00
7	6	31470298935	\N	82996495216	75578836399	2021-05-21 03:32:29.036709+00	\N	1999-10-31 18:43:23+00
8	8	64794045636	\N	8307105705	29990495623	2021-05-21 03:32:30.090843+00	\N	2000-10-27 07:16:51+00
9	13	69269418526	79357174178	\N	25964933951	2021-05-21 03:32:31.109472+00	\N	1983-03-23 15:40:51+00
10	9	55614222350	51849909218	\N	41096137008	2021-05-21 03:32:31.904073+00	\N	1996-01-28 20:42:14+00
11	12	55614222350	28365997206	\N	5583047314	2021-05-21 03:32:32.833191+00	\N	2006-08-07 06:27:21+00
12	14	18900731843	\N	90948553266	75578836399	2021-05-21 03:32:33.726304+00	\N	2018-06-28 02:24:59+00
13	7	40794324231	5770720438	\N	71437446494	2021-05-21 03:32:34.656922+00	\N	2004-08-02 20:23:05+00
14	14	86056765124	\N	47015360570	97441463814	2021-05-21 03:32:35.966589+00	\N	2002-09-08 20:44:16+00
15	7	57743031673	79357174178	\N	44201821435	2021-05-21 03:32:36.426147+00	\N	1991-06-22 20:39:50+00
\.


--
-- Data for Name: enfermeiro; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.enfermeiro (id, func_id) FROM stdin;
\.


--
-- Data for Name: enfermeirochefe; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.enfermeirochefe (id, func_id) FROM stdin;
\.


--
-- Data for Name: estagiario; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.estagiario (id, func_id) FROM stdin;
\.


--
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.funcionario (cpf, nome, created_on, updated_on, senha) FROM stdin;
71375160116	Carlos Eduardo da ConceiÃ§Ã£o	2021-05-21 03:31:47.708961+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
40181898460	Leonardo Souza	2021-05-21 03:31:47.919488+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
51849909218	Kamilly da Cunha	2021-05-21 03:31:48.989623+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
45202282629	Luiz Miguel Pereira	2021-05-21 03:31:49.736218+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
05770720438	Dr. Thiago Cavalcanti	2021-05-21 03:31:50.172274+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
28365997206	Augusto Barros	2021-05-21 03:31:51.286415+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
34984954627	Sr. Fernando Nogueira	2021-05-21 03:31:51.842986+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
69839219802	Ana JÃºlia Rezende	2021-05-21 03:31:52.227535+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
84828333995	CauÃ£ Pinto	2021-05-21 03:31:52.457064+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
79357174178	LavÃ­nia da Rocha	2021-05-21 03:31:52.7406+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
32108412377	Nina Castro	2021-05-21 03:31:53.274668+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
21148074068	Mirella Sales	2021-05-21 03:31:53.991259+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
82996495216	Kevin Correia	2021-05-21 03:31:54.706849+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
85174297656	Carlos Eduardo Porto	2021-05-21 03:31:55.071896+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
47015360570	Murilo Moreira	2021-05-21 03:31:55.366433+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
02573559077	Sr. Miguel Santos	2021-05-21 03:31:55.711977+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
74957236822	Ana Beatriz da Costa	2021-05-21 03:31:56.070023+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
15580080774	JoÃ£o Vitor da Luz	2021-05-21 03:31:56.309053+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
90948553266	Catarina Duarte	2021-05-21 03:31:56.723105+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
74255628406	Luiz Felipe Costa	2021-05-21 03:31:56.91613+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
09477601436	Heitor Ferreira	2021-05-21 03:31:57.069649+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
08307105705	Sra. Maria VitÃ³ria Teixeira	2021-05-21 03:31:57.236671+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
44201821435	Gabriela Campos	2021-05-21 03:31:57.495704+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
05583047314	Francisco Pinto	2021-05-21 03:31:57.760737+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
16721424607	BÃ¡rbara Nogueira	2021-05-21 03:31:58.031772+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
75578836399	Renan Farias	2021-05-21 03:31:58.366314+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
71437446494	Maysa da Cruz	2021-05-21 03:31:58.65035+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
25964933951	Diogo Correia	2021-05-21 03:31:59.083405+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
29990495623	Augusto Moura	2021-05-21 03:31:59.526961+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
97441463814	Vitor Gabriel Costa	2021-05-21 03:31:59.840501+00	2021-06-02 19:48:50.296929+00	\\x2432622431322458554a694a6d52353277695668515654756359736e75474176632e2f3062486951536a65374f674757773435436d6f4a70742e7079
\.


--
-- Data for Name: medicamento; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.medicamento (codigo, created_on, updated_on, nome) FROM stdin;
4978491995	2021-05-21 03:32:08.536105+00	\N	medicamento_143226
4789220888	2021-05-21 03:32:11.48448+00	\N	medicamento_960973
6318994394	2021-05-21 03:32:12.760142+00	\N	medicamento_872476
2438099985	2021-05-21 03:32:12.892159+00	\N	medicamento_995527
5884950027	2021-05-21 03:32:13.103686+00	\N	medicamento_590527
8806961712	2021-05-21 03:32:13.280708+00	\N	medicamento_178110
1742314767	2021-05-21 03:32:13.366219+00	\N	medicamento_31626
8050890714	2021-05-21 03:32:13.566244+00	\N	medicamento_113797
3774394752	2021-05-21 03:32:13.652255+00	\N	medicamento_216106
7094368104	2021-05-21 03:32:13.798774+00	\N	medicamento_413962
6533947832	2021-05-21 03:32:13.881784+00	\N	medicamento_605315
7964541904	2021-05-21 03:32:14.014801+00	\N	medicamento_131760
2522200859	2021-05-21 03:32:14.207826+00	\N	medicamento_206962
2285145013	2021-05-21 03:32:14.289336+00	\N	medicamento_541385
9184702822	2021-05-21 03:32:14.361845+00	\N	medicamento_427496
2215305717	2021-05-21 03:32:14.47786+00	\N	medicamento_856847
6499672883	2021-05-21 03:32:14.563871+00	\N	medicamento_774164
7283695928	2021-05-21 03:32:14.673385+00	\N	medicamento_609432
1443692943	2021-05-21 03:32:14.786899+00	\N	medicamento_402464
5307225915	2021-05-21 03:32:14.877911+00	\N	medicamento_139879
8786185854	2021-05-21 03:32:14.964422+00	\N	medicamento_862246
4813460180	2021-05-21 03:32:15.172948+00	\N	medicamento_889244
6415562395	2021-05-21 03:32:15.258459+00	\N	medicamento_677247
6337887104	2021-05-21 03:32:15.34547+00	\N	medicamento_527279
5368209549	2021-05-21 03:32:15.452484+00	\N	medicamento_263013
8116114259	2021-05-21 03:32:15.555997+00	\N	medicamento_125475
9884092583	2021-05-21 03:32:15.629006+00	\N	medicamento_316742
1827356608	2021-05-21 03:32:15.788026+00	\N	medicamento_761148
735161311	2021-05-21 03:32:15.929044+00	\N	medicamento_912428
1350946825	2021-05-21 03:32:16.179576+00	\N	medicamento_476595
2258882167	2021-05-21 03:32:16.260586+00	\N	medicamento_306476
2558556285	2021-05-21 03:32:16.343597+00	\N	medicamento_216006
5460201450	2021-05-21 03:32:16.470613+00	\N	medicamento_909773
828255939	2021-05-21 03:32:16.632134+00	\N	medicamento_945597
3648993786	2021-05-21 03:32:16.745148+00	\N	medicamento_344667
4976370672	2021-05-21 03:32:16.862663+00	\N	medicamento_713391
5800051804	2021-05-21 03:32:16.948174+00	\N	medicamento_743987
2932647887	2021-05-21 03:32:17.019683+00	\N	medicamento_714740
5625459741	2021-05-21 03:32:17.094692+00	\N	medicamento_418216
3007557411	2021-05-21 03:32:17.185204+00	\N	medicamento_429608
3802760722	2021-05-21 03:32:17.253712+00	\N	medicamento_634120
9550447357	2021-05-21 03:32:17.333723+00	\N	medicamento_682949
3057128783	2021-05-21 03:32:17.419734+00	\N	medicamento_62953
7395858521	2021-05-21 03:32:17.620259+00	\N	medicamento_116482
6690359214	2021-05-21 03:32:17.70327+00	\N	medicamento_423922
2824593651	2021-05-21 03:32:17.917797+00	\N	medicamento_515712
\.


--
-- Data for Name: paciente; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.paciente (cpf, nome, sexo, genero, data_nascimento, tipo_sangue, endereco, telefone, created_on, updated_on, dados, enfermeiro_id) FROM stdin;
44301834634	Bruno AragÃ£o	t	non-b	1983-03-25	null_rh	Vila Emanuel Peixoto, 448\nPenha\n76461514 Teixeira / SC	08257559781	2021-05-21 03:32:00.45958+00	\N		97441463814
18900731843	Daniel Porto	t	non-b	1958-05-04	o-	Setor Eduardo Peixoto\nNova Vista\n98373095 Mendes Verde / ES	82633428109	2021-05-21 03:32:00.725614+00	\N		40181898460
31470298935	JoÃ£o Martins	t	non-b	1987-10-03	a-	Quadra de Lopes, 50\nAraguaia\n91712846 da Paz / DF	89074166474	2021-05-21 03:32:01.4047+00	\N		25964933951
40794324231	Yago Nascimento	f	cis	1983-08-26	a+	Lago de Lopes\nPantanal\n23337-424 Cardoso / RN	14465283871	2021-05-21 03:32:01.816252+00	\N		16721424607
57743031673	Maria Clara Ferreira	t	trans	1934-12-28	o+	Lagoa de Santos, 50\nPilar\n76196-268 Nascimento / CE	23879968782	2021-05-21 03:32:02.170297+00	\N		16721424607
13377643987	Gabriel Lima	t	trans	1954-12-10	ab+	Viaduto Emanuella Sales, 80\nVila Nova Gameleira 2Âª SeÃ§Ã£o\n64305-143 Oliveira da Prata / PR	15399729749	2021-05-21 03:32:02.648358+00	\N		34984954627
86056765124	Alice Duarte	f	non-b	1936-07-31	b+	Largo de Moreira\nMarilandia\n24854-742 Teixeira / SE	93580554293	2021-05-21 03:32:03.071412+00	\N		05770720438
49475995813	AlÃ­cia Moura	f	non-b	1927-10-25	ab-	Largo Renan Silveira\nOeste\n06619031 Pinto de Cunha / MA	66789382551	2021-05-21 03:32:03.391952+00	\N		71375160116
55614222350	Maria Fernandes	f	non-b	1991-07-08	o+	Fazenda Teixeira, 6\nTaquaril\n10383661 Caldeira / SC	37982936204	2021-05-21 03:32:03.858011+00	\N		05583047314
64794045636	Diogo da Rosa	t	cis	1944-08-11	ab-	Travessa de Fernandes, 98\nTrevo\n53720-932 Lima / BA	01666849964	2021-05-21 03:32:04.334572+00	\N		84828333995
69269418526	Maria CecÃ­lia Rocha	f	cis	1926-09-02	o+	ColÃ´nia de da Mota, 376\nSalgado Filho\n18093801 Correia Paulista / SP	24694276520	2021-05-21 03:32:04.593605+00	\N		28365997206
72257143448	Dr. Noah Moura	f	cis	1923-03-06	null_rh	PÃ¡tio de Farias\nBarroca\n00974939 Pinto do Sul / ES	76195962809	2021-05-21 03:32:04.856138+00	\N		75578836399
02484301543	Rodrigo Duarte	t	trans	1928-11-03	ab-	PÃ¡tio da Cruz, 23\nSÃ£o Jorge 3Âª SeÃ§Ã£o\n10694673 da Luz Grande / AM	35652068553	2021-05-21 03:32:05.093668+00	\N		51849909218
62419002277	Stella da Cruz	f	non-b	1925-06-08	o+	Feira Freitas, 24\nMonsenhor Messias\n43921-405 Rocha de Porto / ES	19254320585	2021-05-21 03:32:05.330198+00	\N		29990495623
92079719817	Sr. Emanuel Ribeiro	t	cis	1946-05-24	b-	Conjunto de Nogueira, 6\nNazare\n84866-719 Ramos / GO	35505917646	2021-05-21 03:32:05.549226+00	\N		79357174178
71706660167	Pedro Henrique Pereira	f	cis	1988-03-27	b-	Conjunto CecÃ­lia Santos, 99\nAtila De Paiva\n90173834 Rezende / PB	54292352984	2021-05-21 03:32:06.092795+00	\N		51849909218
65105857070	Lucas Gabriel da Paz	t	trans	1977-03-30	null_rh	PÃ¡tio LÃ­via Silva, 5\nVila ParaÃ­so\n79603776 Lopes / RN	16786996057	2021-05-21 03:32:06.988409+00	\N		05770720438
\.


--
-- Data for Name: posologia; Type: TABLE DATA; Schema: public; Owner: fescam
--

COPY public.posologia (id, medicamento, paciente, quantidade, created_on, updated_on, notas) FROM stdin;
1	4789220888	86056765124	37.39	2021-05-21 03:32:18.231837+00	\N	Checar batimentos
2	2824593651	86056765124	60.89	2021-05-21 03:32:18.517373+00	\N	Aplicar doses em braÃ§os diferentes
3	3774394752	02484301543	64.69	2021-05-21 03:32:18.917424+00	\N	
4	5460201450	71706660167	51.1	2021-05-21 03:32:19.28547+00	\N	Aplicar doses em braÃ§os diferentes
5	5625459741	02484301543	50.74	2021-05-21 03:32:19.604011+00	\N	
6	8786185854	72257143448	12.97	2021-05-21 03:32:19.899548+00	\N	Checar batimentos
7	6337887104	44301834634	64.86	2021-05-21 03:32:20.205587+00	\N	
8	2522200859	86056765124	28.68	2021-05-21 03:32:20.549631+00	\N	Injetar na testa
9	9884092583	55614222350	58.2	2021-05-21 03:32:20.969684+00	\N	
10	8806961712	69269418526	60.72	2021-05-21 03:32:21.574761+00	\N	Injetar na testa
11	5800051804	65105857070	64.1	2021-05-21 03:32:22.016317+00	\N	Aplicar doses em braÃ§os diferentes
12	5368209549	64794045636	11.37	2021-05-21 03:32:22.244346+00	\N	Injetar na testa
13	6499672883	02484301543	33.46	2021-05-21 03:32:22.641897+00	\N	Injetar na testa
14	2215305717	13377643987	32.34	2021-05-21 03:32:23.056949+00	\N	
15	1827356608	92079719817	8.86	2021-05-21 03:32:23.473002+00	\N	Aplicar doses em braÃ§os diferentes
\.


--
-- Name: administrador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.administrador_id_seq', 1, false);


--
-- Name: agendamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.agendamento_id_seq', 1, false);


--
-- Name: enfermeiro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.enfermeiro_id_seq', 1, false);


--
-- Name: enfermeirochefe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.enfermeirochefe_id_seq', 1, false);


--
-- Name: estagiario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.estagiario_id_seq', 1, false);


--
-- Name: medicamento_codigo_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.medicamento_codigo_seq', 1, false);


--
-- Name: posologia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fescam
--

SELECT pg_catalog.setval('public.posologia_id_seq', 1, false);


--
-- Name: administrador administrador_func_id_key; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_func_id_key UNIQUE (func_id);


--
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id);


--
-- Name: agendamento agendamento_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id);


--
-- Name: enfermeiro enfermeiro_func_id_key; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_func_id_key UNIQUE (func_id);


--
-- Name: enfermeiro enfermeiro_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_pkey PRIMARY KEY (id);


--
-- Name: enfermeirochefe enfermeirochefe_func_id_key; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_func_id_key UNIQUE (func_id);


--
-- Name: enfermeirochefe enfermeirochefe_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_pkey PRIMARY KEY (id);


--
-- Name: estagiario estagiario_func_id_key; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_func_id_key UNIQUE (func_id);


--
-- Name: estagiario estagiario_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_pkey PRIMARY KEY (id);


--
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (cpf);


--
-- Name: medicamento medicamento_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.medicamento
    ADD CONSTRAINT medicamento_pkey PRIMARY KEY (codigo);


--
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (cpf);


--
-- Name: posologia posologia_pkey; Type: CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_pkey PRIMARY KEY (id);


--
-- Name: administrador_func_id_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX administrador_func_id_idx ON public.administrador USING btree (func_id);


--
-- Name: agendamento_horario_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX agendamento_horario_idx ON public.agendamento USING btree (horario);


--
-- Name: agendamento_id_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX agendamento_id_idx ON public.agendamento USING btree (id);


--
-- Name: agendamento_paciente_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX agendamento_paciente_idx ON public.agendamento USING btree (paciente);


--
-- Name: enfermeiro_func_id_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX enfermeiro_func_id_idx ON public.enfermeiro USING btree (func_id);


--
-- Name: enfermeirochefe_func_id_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX enfermeirochefe_func_id_idx ON public.enfermeirochefe USING btree (func_id);


--
-- Name: estagiario_func_id_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX estagiario_func_id_idx ON public.estagiario USING btree (func_id);


--
-- Name: funcionario_cpf_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX funcionario_cpf_idx ON public.funcionario USING btree (cpf);


--
-- Name: medicamento_codigo_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX medicamento_codigo_idx ON public.medicamento USING btree (codigo);


--
-- Name: paciente_cpf_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX paciente_cpf_idx ON public.paciente USING btree (cpf);


--
-- Name: posologia_paciente_medicamento_idx; Type: INDEX; Schema: public; Owner: fescam
--

CREATE INDEX posologia_paciente_medicamento_idx ON public.posologia USING btree (paciente, medicamento);


--
-- Name: administrador administrador_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: enfermeiro enfermeiro_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeiro
    ADD CONSTRAINT enfermeiro_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: enfermeirochefe enfermeirochefe_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.enfermeirochefe
    ADD CONSTRAINT enfermeirochefe_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: estagiario estagiario_func_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.estagiario
    ADD CONSTRAINT estagiario_func_id_fkey FOREIGN KEY (func_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: paciente paciente_enfermeiro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_enfermeiro_id_fkey FOREIGN KEY (enfermeiro_id) REFERENCES public.funcionario(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: posologia posologia_medicamento_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_medicamento_fkey FOREIGN KEY (medicamento) REFERENCES public.medicamento(codigo) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: posologia posologia_paciente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fescam
--

ALTER TABLE ONLY public.posologia
    ADD CONSTRAINT posologia_paciente_fkey FOREIGN KEY (paciente) REFERENCES public.paciente(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

