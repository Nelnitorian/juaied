import pymysql

class DaoUserInf:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='company'
        )
        self.cursor = self.connection.cursor()

    """
    PageModUser métodos
    """
    #Método que devuelve apellidos de todos los usuarios

    def select_users(self):
        sql = "SELECT apellidos FROM user_inf"

        try:
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()

            return usuarios

        except Exception as e:
            return False

    # Método que devuelve username mediante apellidos

    def select_username_by_apellidos(self, apellidos):
        sql = "SELECT username FROM user_inf WHERE apellidos = '{}'".format(apellidos)

        try:
            self.cursor.execute(sql)
            username = self.cursor.fetchone()

            return username[0]

        except Exception as e:
            return False

    """
    PageUserInf métodos
    """

    def select_rows(self):
        sql = "SELECT count(*) FROM user_inf"
        
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchone()

            return rows[0]
        except Exception as e:
            raise
  
    """
    MÉTODOS DAO
    """

    # Método para insertar nuevo usuario

    def new_user(self, username, password, apellidos, nombre, tarifa):
        sql = "INSERT INTO user_inf (username, pass, apellidos, nombre, tarifa) VALUES ('{}','{}','{}','{}','{}')".format(username, password,apellidos, nombre, tarifa)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    # Método que modifica username

    def update_username(self, oldusername, newusername):
        sql = "UPDATE user_inf SET username='{}' WHERE username = '{}'".format(newusername, oldusername)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise 

    # Método que devuelve password

    def select_pass(self,username):
        sql = "SELECT pass FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            password = self.cursor.fetchone()

            return password[0]

        except Exception as e:
            return False

    # Método que modifica password

    def update_pass(self, username, password):
        sql = "UPDATE user_inf SET pass='{}' WHERE username = '{}'".format(password, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise 

    # Método que devuelve nombre

    def select_nombre(self,username):
        sql = "SELECT nombre FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            nombre = self.cursor.fetchone()

            return nombre[0]

        except Exception as e:
            return False

    # Método que modifica nombre

    def update_nombre(self, username, nombre):
        sql = "UPDATE user_inf SET nombre='{}' WHERE username = '{}'".format(nombre, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve apellidos

    def select_apellidos(self,username):
        sql = "SELECT apellidos FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            apellidos = self.cursor.fetchone()

            return apellidos[0]

        except Exception as e:
            return False

    # Método que modifica apellidos

    def update_apellidos(self, username, apellidos):
        sql = "UPDATE user_inf SET apellidos='{}' WHERE username = '{}'".format(apellidos, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve tarifa

    def select_tarifa(self,username):
        sql = "SELECT tarifa FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            tarifa = self.cursor.fetchone()

            return tarifa[0]

        except Exception as e:
            return False

    # Método que modifica tarifa

    def update_tarifa(self, username, tarifa):
        sql = "UPDATE user_inf SET tarifa='{}' WHERE username = '{}'".format(tarifa, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve dinero

    def select_dinero(self,username):
        sql = "SELECT dinero FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            dinero = self.cursor.fetchone()

            return dinero[0]

        except Exception as e:
            return False

    # Método que modifica dinero

    def update_dinero(self, username, dinero):
        sql = "UPDATE user_inf SET dinero='{}' WHERE username = '{}'".format(dinero, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve paquetes

    def select_paquetes(self,username):
        sql = "SELECT paquetes FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            paquetes = self.cursor.fetchone()

            return paquetes[0]

        except Exception as e:
            return False

    # Método que modifica paquetes

    def update_paquetes(self, username, paquetes):
        sql = "UPDATE user_inf SET paquetes='{}' WHERE username = '{}'".format(paquetes, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve tiempo

    def select_tiempo(self,username):
        sql = "SELECT tiempo FROM user_inf WHERE username = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            tiempo = self.cursor.fetchone()

            return tiempo[0]

        except Exception as e:
            return False

    # Método que modifica tiempo

    def update_tiempo(self, username, tiempo):
        sql = "UPDATE user_inf SET tiempo='{}' WHERE username = '{}'".format(tiempo, username)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 