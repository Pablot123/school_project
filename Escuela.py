from BD.connection import DAO
from Estudiante import Estudiante

"""
    Escuela es la clase principal de nuestro programa , a partir de ella se puede hacer parte del crud para los estudiantes y profesores y crear una especie de boletín con las notas de los estudiantes
    Mediante esta accedo a otras clases como estudiante o profesor
    
    

    Returns:
        La clase principal de nuestro programa
"""
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
    
    
    ## Se usa DAO para  acceder a la base de datos y traeer los profesors 
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
    
    
    ## Método para contratar un profesor 
    def contratar_profesor(self, profesor):
        dao = DAO()
        dao.agregar_profesor(profesor)

    def eliminar_profesor(self):
        dao = DAO()
        #Mostar una lista con los estudiantes, viendo su codigo
        cod_profesor_del = int(input('ingrese codigo del profesor a eliminar: '))
        dao.eliminar_profesor(cod_profesor_del)

    #Añadir un estudiante a la lista 
    def matricular_estudiante(self, estudiante):
        dao = DAO()
        dao.agregar_estudiante(estudiante)
        
    #Eliminar un estudiante de la lista 
    def expulsar_estudiante(self):
        dao = DAO()
        #Mostar una lista con los estudiantes, viendo su codigo
        cod_estudiante_del = int(input('ingrese codigo de estudiante a eliminar: '))

        dao.eliminar_estudiante(cod_estudiante_del)


    def generar_boletin(self,estudiante):
        #Se mira si el boletín si existe o si el estudiante si tiene notas 
        if len(estudiante.notas) != 0:
            entrada = open(f'boletin_{estudiante.nombre}.txt','a') #abro el archivo en modo escritura sin sobreescribir 
            i=0


            notas = list(eval(estudiante.notas)) ## Paso de un string a una lista de tuplas [(),()]

            entrada.write(f'----BOLETIN ESCUELA {self.nombre}----')
            notas = list(eval(estudiante.notas))

            for materia, nota in notas:
                entrada.write(f"{materia}   {nota} \n") #escribo la materia en el archivo 
                i+=1
            
            entrada.write(f"Promedio notas {estudiante.promedio_notas()}")    #escribo el promedio de lasn otas del estudiante 
            entrada.close() #cierro el buffer 
        else:
            print(f'el estudiante {estudiante.nombre} no tiene notas actualmente') 


# Para hacer pruebas 
if __name__ == '__main__':
    cole = Escuela(12, 'hola', 'ddd', [],[],[])
    p = Estudiante('pablo',2, 2222, 4, [("matematicas",5),("biologia",4)])
    cole.generar_boletin(p)
    
    #cole.matricular_estudiante(p)