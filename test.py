from Estudiante import Estudiante
from Escuela import Escuela
from Profesor import Profesor
#from BD.connection import DAO

if __name__ == '__main__':
    #pablo = Estudiante('Pablo', 12, 11, 7, 'hola')
    cole = Escuela(12, 'hola', 'ddd', [],[],[])
    p = Estudiante('pablo',2, 2222, 4, '["matematicas"]', '[]')
    dani = Profesor('dani', 23, 33, 'Biologia', 3, 300000)

    cole.contratar_profesor(dani)