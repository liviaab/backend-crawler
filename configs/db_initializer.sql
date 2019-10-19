\echo 'Creating tables...'

-- Courts
CREATE TABLE courts (
  id serial PRIMARY KEY,
  name varchar(255) NOT NULL,
  initials varchar(10) NOT NULL UNIQUE
);

-- Processes
CREATE TABLE processes (
  id serial PRIMARY KEY,
  process_number varchar(50) NOT NULL,
  class varchar(255) NOT NULL,
  area varchar(255) NOT NULL,
  subject varchar(255) NOT NULL,
  distribution_date DATE NOT NULL,
  judge varchar(255) NOT NULL,
  value varchar(50) NOT NULL,
  last_access TIMESTAMP NOT NULL,
  changes json NULL,
  court_id integer NOT NULL,
  UNIQUE(process_number, court_id)
);

-- Roles
CREATE TABLE roles (
  id serial PRIMARY KEY,
  name varchar(100) NOT NULL
);

-- Parties_Involved
CREATE TABLE parties_involved (
  id serial PRIMARY KEY,
  process_id integer NOT NULL,
  name varchar(255) NOT NULL,
  role_id integer NOT NULL,

  CONSTRAINT parties_involved_process_process_id_fkey FOREIGN KEY (process_id)
      REFERENCES processes (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,

  CONSTRAINT parties_involved_role_role_id_fkey FOREIGN KEY (role_id)
      REFERENCES roles (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);


\echo 'Inserting seeds...'
-- SEEDS

INSERT INTO roles VALUES
(1, 'Exequente'),
(2, 'Apelante'),
(3, 'Advogado(a) envolvido(a)');

INSERT INTO courts VALUES (1, 'Tribunal de Justiça do Estado de Alagoas', 'TJAL')

\echo 'Done!'
