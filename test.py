from Estudiante import Estudiante
from Profesor import Profesor

if __name__ == '__main__':
    pablo = Estudiante('Pablo', 12, 11, 7, 'hola')
    dani = Profesor('dani', 23, 33, 'Biologia', 3000)

    print(pablo.notas)
    dani.colocar_nota(pablo, 5.0)
    print(pablo.notas)
    pablo.promedio_notas()