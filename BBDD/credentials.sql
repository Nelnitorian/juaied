-- DATABASE credentials

DROP DATABASE credentials;
CREATE DATABASE credentials;
USE credentials;

#                           
# Table structure for table 'users'
#

CREATE TABLE IF NOT EXISTS users (
  username varchar(64) NOT NULL default '',
  pass varchar(64) NOT NULL default '',
  email varchar(64) NOT NULL default '',
  PRIMARY KEY (username),
  KEY username (username(32))
);


-- Insertamos usuario admin

INSERT INTO users VALUES ('admin','admin','admin@gmail.com')