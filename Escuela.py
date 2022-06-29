from BD.connection import DAO
from Estudiante import Estudiante
class Escuela:
    def __init__(self, id, nombre, direccion, profesores=[], alumnos=[], materias=[]) -> None:
        self.__id = id # llave primaria
        self.__nombre = nombre
        self.__direccion = direccion
        self.__profesores = profesores #estos se pueden cambiar
        self.__alumnos = alumnos #estos se pueden cambiar
        self.__materias = materias #estos se pueden cambiar
    
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

    def eliminar_profesor(self):
        dao = DAO()
        #Mostar una lista con los estudiantes, viendo su codigo
        cod_profesor_del = int(input('ingrese codigo del profesor a eliminar: '))
        dao.eliminar_profesor(cod_profesor_del)

    def matricular_estudiante(self, estudiante):
        dao = DAO()
        dao.agregar_estudiante(estudiante)
        

    def expulsar_estudiante(self):
        dao = DAO()
        #Mostar una lista con los estudiantes, viendo su codigo
        cod_estudiante_del = int(input('ingrese codigo de estudiante a eliminar: '))

        dao.eliminar_estudiante(cod_estudiante_del)


    def generar_boletin(self,estudiante):
        # mirar manejo de archivos 
        # faltaría codigo estudiante o nombre estudiante
        if len(estudiante.notas) != 0:
            entrada = open(f'boletin_{estudiante.nombre}.txt','a')
            i=0

            notas = list(eval(estudiante.notas))
            for materia, nota in notas:
                entrada.write(f"{materia}   {nota} \n")
                i+=1
            
            entrada.write(f"Promedio notas {estudiante.promedio_notas()}")  
            entrada.close()
        else:
            print(f'el estudiante {estudiante.nombre} no tiene notas actualmente')

if __name__ == '__main__':
    cole = Escuela(12, 'hola', 'ddd', [],[],[])
    p = Estudiante('pablo',2, 2222, 4, [("matematicas",5),("biologia",4)])
    cole.generar_boletin(p)
    
    #cole.matricular_estudiante(p)