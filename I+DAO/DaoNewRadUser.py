import pymysql

class DaoNewRadUser:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='radius'
        )
        self.cursor = self.connection.cursor()

    #Método que devuelve la contraseña del usuario

    def add_user(self,username, password):
        sql = "INSERT INTO radcheck (username, attribute, op, value) VALUES ('{}','Cleartext-Password',':=','{}')".format(username, password)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def delete_user(self,username):
        sql = "DELETE FROM radcheck where username='{}'".format(username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_user(self,username,password,oldusername):
        sql = "UPDATE radcheck SET username='{}', value='{}' WHERE username='{}'".format(username,password,oldusername)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except:
            raise