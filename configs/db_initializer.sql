
-- Courts
CREATE TABLE courts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) NOT NULL,
  initials varchar(10) NOT NULL UNIQUE
);

-- Processes
CREATE TABLE processes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  process_number varchar(50) NOT NULL,
  process_class varchar(255) NOT NULL,
  area varchar(255) NOT NULL,
  subject varchar(255) NOT NULL,
  distribution_date varchar(255) NOT NULL,
  judge varchar(255) NOT NULL,
  value varchar(50) NOT NULL,
  last_access TIMESTAMP NOT NULL,
  court_id INT NOT NULL,
  UNIQUE(process_number, court_id)
);

-- Parties_Involved
CREATE TABLE parties_involved (
  id INT AUTO_INCREMENT PRIMARY KEY,
  process_id INT NOT NULL,
  name varchar(255) NOT NULL,
  role varchar(255) NOT NULL,
  CONSTRAINT parties_involved_process_process_id_fkey FOREIGN KEY (process_id)
      REFERENCES processes (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Movimentations
CREATE TABLE movimentations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  process_id INT NOT NULL,
  date varchar(255) NOT NULL,
  description TEXT NOT NULL,
  CONSTRAINT movimentations_process_process_id_fkey FOREIGN KEY (process_id)
      REFERENCES processes (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- SEEDS

INSERT INTO courts VALUES (1, 'Tribunal de Justiça do Estado de Alagoas', 'TJAL')
