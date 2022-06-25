from hashlib import new
from select import select
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
    def __init__(self, nombre, codigo, id, grado, materias, notas=[]) -> None:
        Persona.__init__(self, nombre, codigo, id)
        self._grado = grado
        self._materias = materias
        self._notas = notas #Las notas vienen por tuplas 

    @property
    def grado(self):
        return self._grado

    
    @property
    def materias(self):
        return self._materias

    
    @property
    def notas(self):
        return self._notas
    #Le quite el metodo set a notas para que el estudiante no pueda cambiar la nota

    def promedio_notas(self):
        promedio = 0
        for _ , nota in self.notas:
            promedio +=nota
        promedio = promedio/len(self.notas)
        print(f'Su promedio de notas es: {promedio}')
    
    def __str__(self) -> str:
        estudiante=f"El estudiante {self.nombre} del grado {self.grado} con las materias {self.materias} "
        return estudiante

if __name__ == '__main__':
    estudiante1 = Estudiante("Juan",1234,5678,8,["matematica","biologia"],[("matematica",4),("biologia",5)])
    print(estudiante1)
    pass