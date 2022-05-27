-- DATABASE company

DROP DATABASE company;
CREATE DATABASE company;
USE company;


CREATE TABLE IF NOT EXISTS user_inf (
  username varchar(64) NOT NULL default '',
  pass varchar(64) NOT NULL default '',
  nombre varchar(64) NOT NULL default '',
  apellidos varchar(64) NOT NULL default '',
  tarifa varchar(64) NOT NULL default '',
  dinero INTEGER(64) NOT NULL default 0,
  paquetes INTEGER(64) NOT NULL default 0,
  tiempo INTEGER(64) NOT NULL default 0,
  PRIMARY KEY (apellidos),
  KEY username (apellidos(64))
);

INSERT INTO user_inf VALUES ('edurubcam','password','Eduardo','Rubio Camacho','TarifaOne',13,100,100);
INSERT INTO user_inf VALUES ('manolito','passmanolo','Manolo','Marin Marmolea','TarifaOne',20,200,240);

CREATE TABLE IF NOT EXISTS tarifa_inf (
    tarifa varchar(64) NOT NULL default '',
    control varchar(64) NOT NULL default '',
    ratio varchar(64) NOT NULL default '',
    PRIMARY KEY (tarifa),
    KEY tarifa (tarifa(64))
);

INSERT INTO tarifa_inf VALUES ('default','paquetes',1);
