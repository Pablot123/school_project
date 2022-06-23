import mysql.connector
from mysql.connector import Error
class DAO:
    def __init__(self) -> None:

        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'admin123',
                db = 'escuela'
            )
        except Error as ex:
            print(f'error al intentar la conexion: {ex}')
