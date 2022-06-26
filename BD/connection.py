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
    #-------CRUD ESTUDIANTES-----------
    def lista_estudiantes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT * FROM Estudiante ORDER BY codigo')
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f'error al intentar conexion: {ex}')
    
    def agregar_estudiante(self, estu):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f'INSERT INTO Estudiante (ID, NOMBRE, GRADE, MATERIAS, NOTAS) VALUE ({estu.id}, \'{estu.nombre}\', {estu.grado}, \'{estu.materias}\', \'{estu.notas}\')'
                cursor.execute(sql)
                self.conexion.commit()
                print('Registro de estudiante, exitoso')
            except Error as ex:
                print(f'error al intentar conexion: {ex}')
    #------CRUD PROFESORES---------
    def lista_profesores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT * FROM Profesor ORDER BY codigo')
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f'error al intentar conexion: {ex}')
    
    def agregar_profesor(self, profe):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f'INSERT INTO Profesor (ID, NOMBRE, GRADE, MATERIA, SALARIO) VALUE ({profe.id}, \'{profe.nombre}\', {profe.grado}, \'{profe.materia}\', {profe.salario})'
                cursor.execute(sql)
                self.conexion.commit()
                print('Registro de profesor, exitoso')
            except Error as ex:
                print(f'error al intentar conexion: {ex}')
    
    #-------CRUD MATERIAS--------
    def lista_materias(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT * FROM Materia ORDER BY codigo')
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f'error al intentar conexion: {ex}')
    def agregar_materia(self):
        pass