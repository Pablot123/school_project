import mysql.connector
from mysql.connector import Error
class DAO:
    def __init__(self) -> None:

        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '123456',
                db = 'escuela'
            )
        except Error as ex:
            print(f'error al intentar la conexion: {ex}')

    def lista_estudiantes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT * FROM Estudiante ORDER BY codigo')
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f'error al intentar conexion: {ex}')