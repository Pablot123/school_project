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
        if len(estudiante.notas) == 0:
            estudiante.notas = (self.materia, nota)
            estudiante.notas = str(estudiante.notas)

            return estudiante
        else:
            estudiante.notas += f', {str((self.materia, nota))}'
            return estudiante
        
        
    @classmethod
    def lista_alumnos(self, data_resultados, grado_in):
        '''
        [(1, 123, 'Monika', 10,'[("Biologia", 5)]'), 
        (2, 456, 'Niharika', 8,  '[("Matematicas", 4)]'), 
        (3, 789, 'Vishal', 3,  '[]'), 
        (4, 101, 'Amitabh', 5, '[]')]
        '''
        lista_x_grado=[]
        for _,_,nombre,grado,_ in data_resultados:
            if grado == grado_in:
                lista_x_grado.append(nombre)
            else:
                pass
        return  lista_x_grado
        
if __name__ == '__main__':
    estudiantes =         [(1, 123, 'Monika', 10,[("Biologia", 5)]), 
        (2, 456, 'Niharika', 8,  [("Matematicas", 4)]), 
        (3, 789, 'Vishal', 10,  []), 
        (4, 101, 'Amitabh', 5, [])]
    profesor1 = Profesor("Elkin",1234,2,"Biologia",10,1000)
    print(profesor1.lista_alumnos(estudiantes))
    
