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
    """
        0 = estudiante 
        1= profesor 
        2 = materia
        
    """
    def __init__(self, nombre, codigo, id, grado, notas=None) -> None:
        Persona.__init__(self, nombre, codigo, id)
        self._grado = grado
        self._notas = notas #Las notas vienen por tuplas 

    @property
    def grado(self):
        return self._grado

    @property
    def notas(self):
        return self._notas
    @notas.setter
    def notas(self, notas):
        self._notas = notas

    def promedio_notas(self):
        promedio = 0
        notas = list(eval(self.notas))
        for _ , nota in notas:
            promedio +=nota
        promedio = promedio/len(notas)
        return promedio
        
    
    def __str__(self) -> str:
        estudiante=f"El estudiante {self.nombre} del grado {self.grado} "
        return estudiante

if __name__ == '__main__':
    estudiante1 = Estudiante("Juan",1234,5678,8,[("matematica",4),("biologia",5)])
    print(estudiante1)
    pass