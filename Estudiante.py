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
    def __init__(self, nombre, codigo, id, grado, materias) -> None:
        Persona.__init__(self, nombre, codigo, id)
        self._grado = grado
        self._materias = materias

    @property
    def grado(self):
        return self._grado
    @grado.setter
    def grado(self, grado):
        self._grado = grado
    
    @property
    def materias(self):
        return self._materias
    @materias.setter
    def materias(self, materias):
        self._materias = materias
    
    def promedio_notas():
        pass


if __name__ == '__main__':
    pass