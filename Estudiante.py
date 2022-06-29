from Materia import Materia
from Persona import Persona
'''
La clase estudiantes pretende crear al objeto estudiantes, asignandole el nombre
el codigo, el id, el grado al que entrará o que cursa y las materias que vera.
NOTA 1: Se puede hacer un diccionario en el cual la llave sean los cursos y los
        valores sea una lista con las materias que se ven por curso.
El estudiante tendra los metodos getters and setters, ademas podra consultar las notas que tiene
y el promedio que tiene
'''

class Estudiante(Persona):

    #codigo = id de mysql 
    #id= cédula de la persona


 
    def __init__(self, nombre, codigo, id, grado, notas='') -> None:
        Persona.__init__(self, nombre, codigo, id)
        self.__grado = grado
        self.__notas = notas #Las notas vienen por tuplas 

    #métodos getter para lagunos atributos 
    @property
    def grado(self):
        return self.__grado

    @property
    def notas(self):
        return self.__notas
    #Métodos setter para algunas atributos
    @notas.setter
    def notas(self, notas):
        self.__notas = notas

    # Para sacar el promedio de notas de un estudiante 
    def promedio_notas(self):
        promedio = 0
        notas = list(eval(self.notas))
        for _ , nota in notas:
            promedio +=nota
        promedio = promedio/len(notas)
        return promedio
        

#Para probar 
if __name__ == '__main__':
    estudiante1 = Estudiante("Juan",1234,5678,8,[("matematica",4),("biologia",5)])
    print(estudiante1)
    pass