from BD.connection import DAO
from Estudiante import Estudiante
from Escuela import Escuela
from Materia import Materia
from Profesor import Profesor
#from BD.connection import DAO

if __name__ == '__main__':
    nombre_escuela = input("Ingrese el nombre de la escuela: ")
    direccion_escuela = input("Ingrese la direccion de la escuela: ")
    codigo_escuela = input("Ingrese la direccion de la escuela: ")
    escuela = Escuela(codigo_escuela, nombre_escuela, direccion_escuela)
    opcion = int(input (f"""
          Bienvenido a la escuela {escuela.nombre}, elija una opcion para realizar alguna actividad
          1. Profesores
          2. Alumnos 
          """))
    if opcion==1:
        opcion_profesor = int(input(f"""
                                Elija una opcion para los profesores:
                                1. Agregar profesor
                                2. Actualizar profesor
                                3. Obtener datos profesor 
                                4. Eliminar profesor
                                """))
        if opcion_profesor==1:
            print("agregar profesor")
            nombre_profesor=input("Ingrese el nombre del profesor: ")
            id_profesor=input("Ingrese el id del profesor: ")
            materia_profesor=input("Ingrese la materia del profesor: ")
            grado_profesor=int(input("Ingrese el grado del profesor: "))
            salario_profesor=int(input("Ingrese salario del profesor: "))
            profesor=Profesor(nombre_profesor,__,id_profesor,materia_profesor,grado_profesor,salario_profesor)
            escuela.contratar_profesor(profesor)
            
        elif opcion_profesor==2:
            print("actualizar profesor")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            pass
        elif opcion_profesor==3:
            print("obtener datos profesor")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            pass
        elif opcion_profesor==4:
            print("eliminar profesor")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            escuela.eliminar_profesor()
        else: print ("La opcion de profesores no es valida")

    elif opcion==2:
        opcion_estudiante = int(input(f"""
                                Elija una opcion para los estudiantes:
                                1. Agregar estudiantes
                                2. Actualizar estudiantes
                                3. Obtener datos estudiantes 
                                4. Eliminar estudiantes
                                5. Obtener boletin estudiante en ,txt
                                """))
        if opcion_estudiante==1:
            print("agregar estudiante")
            nombre_profesor=input("Ingrese el nombre del profesor: ")
            id_profesor=input("Ingrese el id del profesor: ")
            materia_profesor=input("Ingrese la materia del profesor: ")
            grado_profesor=int(input("Ingrese el grado del profesor: "))
            salario_profesor=int(input("Ingrese salario del profesor: "))
            profesor=Profesor(nombre_profesor,__,id_profesor,materia_profesor,grado_profesor,salario_profesor)
            escuela.contratar_profesor(profesor)
            
        elif opcion_estudiante==2:
            print("actualizar estudiante")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            pass
        elif opcion_estudiante==3:
            print("obtener datos estudiante")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            pass
        elif opcion_estudiante==4:
            print("eliminar estudiante")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            escuela.eliminar_profesor()
        elif opcion_estudiante==5:
            print("obtener boletin estudiante en .txt")
            # profesor=Profesor()
            # nombre_profesor=input()
            # id_profesor=input()
            # materia_profesor=input()
            # grado_profesor=input()
            # salario_profesor=input()
            escuela.eliminar_profesor()
        else: print ("La opcion de estudiante no es valida")
        
    else: print ("La opcion no es valida")
        
        
    
    
    
    
    
    
    
    
    
    
    # #pablo = Estudiante('Pablo', 12, 11, 7, 'hola')
    # cole = Escuela(12, 'hola', 'ddd', [],[],[])
    # p = Estudiante('pablo',2, 2222, 4, '[]')
    # dani = Profesor('dani', 23, 33, 'Biologia', 3, 300000)
    # #cole.matricular_estudiante(p)
    # #cole.expulsar_estudiante()
    # dao = DAO()
    # print(dao.lista_estudiantes())
    # #cole.contratar_profesor(dani)
    # #cole.eliminar_profesor()