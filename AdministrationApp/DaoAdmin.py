import pymysql

class DaoAdmin:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='credentials'
        )
        self.cursor = self.connection.cursor()

    #Método que devuelve la contraseña del usuario

    def select_pass(self,username):
        sql = "SELECT pass FROM users WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            password = self.cursor.fetchone()

            return password[0]

        except Exception as e:
            return False
    

    #Método que modifica la contraseña del usuario

    def update_pass(self, username, password):
        sql = "UPDATE users SET pass='{}' WHERE username = '{}'".format(password, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    #Método que modifica el username de usuario

    def update_username(self, oldusername, newusername):
        sql = "UPDATE users SET username='{}' WHERE username = '{}'".format(newusername, oldusername)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 
    
    #Método que devuelve el email de usuario

    def select_email(self,username):
        sql = "SELECT email FROM users WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            email = self.cursor.fetchone()

            return email[0]

        except Exception as e:
            return False

    # Método que modifica el email de usuario

    def update_email(self, username, email):
        sql = "UPDATE users SET email='{}' WHERE username = '{}'".format(email, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 
