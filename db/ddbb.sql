-- DATABASE credentials

DROP DATABASE credentials;
CREATE DATABASE credentials;
USE credentials;

#                           
# Table structure for table 'login'
#

CREATE TABLE IF NOT EXISTS login (
  username varchar(64) NOT NULL default '',
  pass varchar(64) NOT NULL default '',
  PRIMARY KEY (username),
  KEY username (username(32))
);


-- Insertamos usuario admin para la conexión entre servidores

INSERT INTO login VALUES ('admin','admin')



#                           
# Table structure for table 'tarifas'
#

CREATE TABLE IF NOT EXISTS tarifas (
  tarifa varchar(64) NOT NULL default '',
  control varchar(64) NOT NULL default '',
  ratio INTEGER(16) NOT NULL default '',
  PRIMARY KEY (tarifa),
  KEY tarifa (tarifa(32))
);

INSERT INTO tarifas VALUES ('default','paquetes',1)

#                           
# Table structure for table 'usuarios'
#

CREATE TABLE IF NOT EXISTS usuarios (
  nombre varchar(64) NOT NULL default '',
  apellidos varchar(64) NOT NULL default '',
  tarifa varchar(64) NOT NULL default '',
  dinero INTEGER(64) NOT NULL default '',
  paquetes INTEGER(64) NOT NULL default '',
  tiempo INTEGER(64) NOT NULL default '',
  PRIMARY KEY (username),
  FOREIGN KEY (tarifa) REFERENCES tarifas(tarifa),
  KEY username (username(32))
);
