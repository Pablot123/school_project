from BD.connection import DAO
from Estudiante import Estudiante
class Escuela:
    def __init__(self, id, nombre, direccion, profesores=[], alumnos=[], materias=[]) -> None:
        self.__id = id # llave primaria
        self.__nombre = nombre
        self.__direccion = direccion
        self._profesores = profesores #estos se pueden cambiar
        self._alumnos = alumnos #estos se pueden cambiar
        self._materias = materias #estos se pueden cambiar
    
    # __del__ es el metodo desstructor
    #Getters and Setters
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre =nombre
    
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
    
    @property
    def profesores(self):
        dao = DAO()
        profes = dao.lista_profesores()
        return profes
    
    @property
    def alumnos(self):
        dao = DAO()
        alumnos = dao.lista_estudiantes()
        return alumnos
    
    @property
    def materias(self):
        dao = DAO()
        materias = dao.lista_materias()
        return materias
    
    def contratar_profesor(self, profesor):
        dao = DAO()
        dao.agregar_profesor(profesor)

    def eliminar_profesor():
        pass

    def matricular_estudiante(self, estudiante):
        dao = DAO()
        dao.agregar_estudiante(estudiante)
        

    def expulsar_estudiante():
        pass

    def agregar_materia():
        pass

    def eliminar_materia():
        pass

    def generar_boletin():
        # mirar manejo de archivos 
        pass

if __name__ == '__main__':
    cole = Escuela(12, 'hola', 'ddd', [],[],[])
    p = Estudiante('pablo',2, 2222, 4, '["matematicas"]', '[]')
    
    #cole.matricular_estudiante(p)