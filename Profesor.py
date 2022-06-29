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
        self.__grado = grado
        self.__materia = materia
        self.__salario = salario

    #Métodos getter and setter para algunos atributos
    @property
    def materia(self):
        return self.__materia
    @materia.setter
    def materia(self, materia):
        self.__materia = materia
    
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    @property
    def grado(self):
        return self.__grado
    
    
    """
        Esto es para colocar  una nota al estudiante en la tupla que indica la materia del profesor y la nota asignada a esa materia
    
    
    """
    def colocar_nota(self, estudiante, nota):
        if len(estudiante.notas) == 0:
            estudiante.notas = (self.materia, nota)
            estudiante.notas = f'[{str(estudiante.notas)}]'

            return estudiante
        else:
            estudiante.notas = estudiante.notas.replace(']', f', {str((self.materia, nota))}]')
            return estudiante
     
      
    """Método estático para sacar la lista de alumnos 
    
    Keyword arguments:
    data_resultados -- Los datos de la BD mysql 
    Return: Lista con los datos de los estudiantes
    """
      
        
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
        
#Para probar  
if __name__ == '__main__':
    estudiantes =         [(1, 123, 'Monika', 10,[("Biologia", 5)]), 
        (2, 456, 'Niharika', 8,  [("Matematicas", 4)]), 
        (3, 789, 'Vishal', 10,  []), 
        (4, 101, 'Amitabh', 5, [])]
    profesor1 = Profesor("Elkin",1234,2,"Biologia",10,1000)
    print(profesor1.lista_alumnos(estudiantes))
    
