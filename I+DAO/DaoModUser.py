import pymysql

class DaoModUser:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='company'
        )
        self.cursor = self.connection.cursor()

    #PageModUser --- Método que devuelve apellidos y nombre de todos los usuarios

    def select_users(self):
        sql = "SELECT apellidos FROM user_inf"

        try:
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()

            return usuarios

        except Exception as e:
            return False


    #PageModUser --- Metodo que devuelve un array con toda la información de usuarios

    def select_user_information(self,apellidos):
        sql = "SELECT tarifa,username,pass FROM user_inf WHERE apellidos = '{}'".format(apellidos)

        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()

            return data

        except Exception as e:
            return False

    #PageModUser --- Método que actualiza la información de usuario

    def update_user_data(self,username, password,tarifa,apellidos):
        sql = "UPDATE user_inf SET username='{}', pass='{}',tarifa='{}' WHERE apellidos='{}'".format(username,password,tarifa,apellidos)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise
