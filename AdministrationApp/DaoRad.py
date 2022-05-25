import pymysql

class DaoRad:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='radius'
        )
        self.cursor = self.connection.cursor()

    #Método que introduce un nuevo usuario

    def add_user(self,username, password):
        sql = "INSERT INTO radcheck (username, attribute, op, value) VALUES ('{}','Cleartext-Password',':=','{}')".format(username, password)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    #Método que borra un usuario

    def delete_user(self,username):
        sql = "DELETE FROM radcheck where username='{}'".format(username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    #Método que actualiza datos de un usario

    def update_user(self,username,password,oldusername):
        sql = "UPDATE radcheck SET username='{}', value='{}' WHERE username='{}'".format(username,password,oldusername)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except:
            raise

    #Método que devuelve el tiempo de sesión de un usuario

    def select_tiempo(self,username):
        sql = "SELECT acctsessiontime FROM radacct where username='{}'".format(username)

        try:
            self.cursor.execute(sql)
            tiempo = self.cursor.fetchone()

            return tiempo[0]

        except Exception as e:
            raise
    
    #Método que devuelve el número de octetos enviados por el usuario

    def select_paquetes_in(self,username):
        sql = "SELECT acctinputoctets FROM radacct WHERE username='{}'".format(username)
        
        try:
            self.cursor.execute(sql)
            paquetes = self.cursor.fetchone()

            return paquetes[0]

        except Exception as e:
            raise

    #Método que devuelve el numero de octetos recibidos por el usuairo        

    def select_paquetes_out(self,username):
        sql = "SELECT acctoutputoctets FROM radacct WHERE username='{}'".format(username)
        
        try:
            self.cursor.execute(sql)
            paquetes = self.cursor.fetchone()

            return paquetes[0]

        except Exception as e:
            raise
