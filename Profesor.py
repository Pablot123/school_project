from Persona import Persona

'''
La clase profesor se crea asignandole el nombre al profesro, el codigo, el id,
la materia que va a dictar y el salario
NOTA 1: Puede un profesro dictar varias materias ?

El profesor tendra los metodos getters and setters ademas podra colocarle la nota
a un alumno especifico y podra ver la lista de alumnos que tiene en su clase
'''

class Profesor(Persona):

    def __init__(self, nombre, codigo, id, materia, grado, salario) -> None:
        Persona.__init__(self, nombre, codigo, id)
        self._grado = grado
        self._materia = materia
        self._salario = salario

    @property
    def materia(self):
        return self._materia
    @materia.setter
    def materia(self, materia):
        self._materia = materia
    
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    @property
    def grado(self):
        return self._grado
    
    
    def colocar_nota(self, estudiante, nota):
        estudiante.notas.append((self.materia, nota))

    def lista_alumnos(self):
        '''
        [(1, 123, 'Monika', 10, '["Biologia","Matematicas","Quimica"]', '[]'), 
        (2, 456, 'Niharika', 8, '["Matematicas", "Sociales", "Ingles"]', '[]'), 
        (3, 789, 'Vishal', 3, '["Español","Matematicas","Biologia"]', '[]'), 
        (4, 101, 'Amitabh', 5, '["Quimica","Fisica","Español"]', '[]')]
        '''
        pass
