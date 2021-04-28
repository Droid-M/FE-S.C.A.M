CREATE TYPE "tipoSangue" AS ENUM (
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

CREATE TYPE "tipoGenero" AS ENUM (
  'cis',
  'trans',
  'non-b'
);

CREATE TABLE "Paciente" (
  "CPF" char(11) PRIMARY KEY,
  "nome" varchar NOT NULL,
  "sexo" boolean DEFAULT null,
  "genero" tipoGenero DEFAULT null,
  "dataDeNascimento" date DEFAULT null,
  "sangue" tipoSangue DEFAULT null,
  "endereco" varchar DEFAULT null,
  "telefone" char(11) DEFAULT null,
  "createdOn" timestamptz DEFAULT (now()),
  "updatedOn" timestamptz DEFAULT (now()),
  "dados" varchar,
  "enfermeiro_id" bigint
);

CREATE TABLE "Funcionario" (
  "CPF" char(11) PRIMARY KEY,
  "nome" varchar NOT NULL
);

CREATE TABLE "Enfermeiro" (
  "id" bigserial PRIMARY KEY,
  "func_id" char(11) UNIQUE
);

CREATE TABLE "EnfermeiroChefe" (
  "id" bigserial PRIMARY KEY,
  "func_id" char(11) UNIQUE
);

CREATE TABLE "Estagiario" (
  "id" bigserial PRIMARY KEY,
  "func_id" char(11) UNIQUE
);

CREATE TABLE "Medicamento" (
  "codigo" bigserial PRIMARY KEY,
  "nome" varchar NOT NULL
);

CREATE TABLE "Posologia" (
  "id" bigserial PRIMARY KEY,
  "medicamento" bigint,
  "paciente" char(11) NOT NULL,
  "quantidade" float NOT NULL
);

CREATE TABLE "Agendamento" (
  "posologia" bigit NOT NULL,
  "paciente" char(11) NOT NULL,
  "enfermeiro" bigint NOT NULL,
  "estagiario" bigint NOT NULL,
  "enferchefe" bigint NOT NULL,
  "horario" timestamptz DEFAULT null
);

ALTER TABLE "Paciente" ADD FOREIGN KEY ("enfermeiro_id") REFERENCES "Enfermeiro" ("id");

ALTER TABLE "Enfermeiro" ADD FOREIGN KEY ("func_id") REFERENCES "Funcionario" ("CPF");

ALTER TABLE "EnfermeiroChefe" ADD FOREIGN KEY ("func_id") REFERENCES "Funcionario" ("CPF");

ALTER TABLE "Estagiario" ADD FOREIGN KEY ("func_id") REFERENCES "Funcionario" ("CPF");

ALTER TABLE "Posologia" ADD FOREIGN KEY ("medicamento") REFERENCES "Medicamento" ("codigo");

ALTER TABLE "Posologia" ADD FOREIGN KEY ("paciente") REFERENCES "Paciente" ("CPF");

ALTER TABLE "Agendamento" ADD FOREIGN KEY ("posologia") REFERENCES "Posologia" ("id");

ALTER TABLE "Agendamento" ADD FOREIGN KEY ("paciente") REFERENCES "Paciente" ("CPF");

ALTER TABLE "Agendamento" ADD FOREIGN KEY ("enfermeiro") REFERENCES "Enfermeiro" ("id");

ALTER TABLE "Agendamento" ADD FOREIGN KEY ("estagiario") REFERENCES "Estagiario" ("id");

ALTER TABLE "Agendamento" ADD FOREIGN KEY ("enferchefe") REFERENCES "EnfermeiroChefe" ("id");

CREATE INDEX ON "Paciente" ("CPF");

CREATE INDEX ON "Funcionario" ("CPF");

CREATE INDEX ON "Enfermeiro" ("func_id");

CREATE INDEX ON "EnfermeiroChefe" ("func_id");

CREATE INDEX ON "Estagiario" ("func_id");

CREATE INDEX ON "Medicamento" ("codigo");

CREATE INDEX ON "Posologia" ("paciente", "medicamento");

CREATE INDEX ON "Agendamento" ("paciente");

CREATE INDEX ON "Agendamento" ("horario");

COMMENT ON COLUMN "Paciente"."sexo" IS 'Sexo biológico';

COMMENT ON COLUMN "Paciente"."genero" IS 'Gênero com o qual a pessoa se identifica';

COMMENT ON COLUMN "Paciente"."dados" IS 'Informações a respeito do diagnóstico do paciente';

COMMENT ON COLUMN "Paciente"."enfermeiro_id" IS 'Funcionario que cadastrou esse paciente. Restringir no código quais tipos de funionário podem cadastrar pacientes';

COMMENT ON COLUMN "Posologia"."quantidade" IS 'A quantidade diária a ser administrada';