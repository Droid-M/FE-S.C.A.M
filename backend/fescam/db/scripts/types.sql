CREATE TYPE tipoSangue AS ENUM (
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

CREATE TYPE tipoGenero AS ENUM (
  'cis',
  'trans',
  'non-b'
);