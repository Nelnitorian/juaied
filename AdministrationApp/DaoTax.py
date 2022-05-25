import pymysql

class DaoTax:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='company'
        )
        self.cursor = self.connection.cursor()

    # Método que introduce nueva tarifa

    def new_tarifa(self, tarifa, control, ratio):
        sql = "INSERT INTO tarifa_inf (tarifa, control, ratio) VALUES ('{}','{}','{}')".format(tarifa, control, ratio)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    # Método que devuelve control 

    def select_control(self,tarifa):
        sql = "SELECT control FROM tarifa_inf WHERE tarifa = '{}'".format(tarifa)

        try:
            self.cursor.execute(sql)
            control = self.cursor.fetchone()

            return control[0]

        except Exception as e:
            return False

    # Método que modifica control

    def update_control(self, tarifa, control):
        sql = "UPDATE tarifa_inf SET control='{}' WHERE tarifa = '{}'".format(control, tarifa)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve ratio

    def select_control(self,tarifa):
        sql = "SELECT ratio FROM tarifa_inf WHERE tarifa = '{}'".format(tarifa)

        try:
            self.cursor.execute(sql)
            ratio = self.cursor.fetchone()

            return ratio[0]

        except Exception as e:
            return False

    # Método que modifica ratio

    def update_control(self, tarifa, ratio):
        sql = "UPDATE tarifa_inf SET ratio='{}' WHERE tarifa = '{}'".format(ratio, tarifa)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    # Método que devuelve todas las tarifas

    def select_tarifas(self):
        sql = "SELECT tarifa FROM tarifa_inf"

        try:
            self.cursor.execute(sql)
            tarifas = self.cursor.fetchall()

            return tarifas
        except Exception as e:
            raise