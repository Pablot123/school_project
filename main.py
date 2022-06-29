from BD.connection import DAO
from Estudiante import Estudiante
from Escuela import Escuela
from Materia import Materia
from Profesor import Profesor
dao = DAO() # creacion del objeto para conectar base de datos
def menu_principal(nombre_escuela):
    '''
    muestra del menu principal
    return: el valor de la opcion seleccionada
    '''
    print(f"""
          Bienvenido a la escuela {nombre_escuela}, elija una opcion para realizar alguna actividad
           1. Profesores
           2. Alumnos
           3. Comite
           4. Salir 
           """)
    opcion = int(input ('ingrese la opcion: '))
    return opcion
    
def menu_profesores():
    '''
    muestra del menu de profesores
    return: el valor de la opcion seleccionada
    '''
    print(f"""
        Elija una opcion para los profesores:
        1. Lista de alumnos por grado
        2. colocar nota
        3. Volver
        4. Salir del sistema
        """)
    opcion_profesor = int(input('Ingrese la opcion: '))
    return opcion_profesor

def menu_estudiante():
    '''
    muestra del menu estudiante
    return: el valor de la opcion seleccionada
    '''
    print(f"""
        Elija una opcion para los estudiantes:
        1. Ver notas
        2. Ver promedio
        3. Volver
        4. Salir del sistema
        """)
    opcion_estudiante = int(input('Ingrese la opcion: '))
    return opcion_estudiante

def menu_comite():
    print(f"""
        Elija una opcion del comite:
        -----Estudiante-----
        1. Agregar estudiantes
        2. Actualizar estudiantes
        3. Lista de estudiantes
        4. Eliminar estudiantes
        5. Obtener boletin estudiante en ,txt
        -----Profesor-------
        6. Agregar profesor
        7. Actualizar profesor
        8. Lista de profesores
        9. Eliminar profesor
        10. volver
        11. Salir
        """)
    opcion_comite = int(input('Ingrese la opcion: '))
    return opcion_comite

def list_prof():
    '''
    Imprime la lista de profesores que se encuentran en la base de datos
    '''
    print('codigo		id		nombre		grado		materia		salario')
    for codigo, id_p, nombre_p, grado_p, materia_p, salario_p in dao.lista_profesores():
        print(f'{codigo}		{id_p}		{nombre_p}		{grado_p}		{materia_p}		{salario_p}')


def list_est():
    '''
    Imprime la lista de estudiantes que se encuentran en la base de datos
    '''
    print('codigo		id		nombre		grado		notas		')
    for codigo, id, nombre, grado, notas in dao.lista_estudiantes():
        print(f'{codigo}		{id}		{nombre}        {grado}     {notas}		')


def obtener_profesor(cod):
    '''
    recibe: El codigo de un profesor
    Retorna: la instancia de la clase profesor, del profesor con el codio dado
    '''
    for codigo, id_p, nombre_p, grado_p, materia_p, salario_p in dao.lista_profesores():
        if cod == codigo:
            return Profesor( nombre_p, 0, id_p, materia_p, grado_p, salario_p)


def obtener_estudiante(cod):
    '''
    recibe: El codigo de un estudiante
    retorna: La instancia de la clase estudiante, del estudiante con el codigo dado
    '''
    for codigo, id_p, nombre_p, grado_p, notas_p in dao.lista_estudiantes():
        if codigo == cod:
            return Estudiante(nombre_p, 0, id_p, grado_p, notas_p)

if __name__ == '__main__':
    nombre_escuela = input("Ingrese el nombre de la escuela: ")
    direccion_escuela = input("Ingrese la direccion de la escuela: ")
    codigo_escuela = input("Ingrese el codigo de la escuela: ")
    escuela = Escuela(codigo_escuela, nombre_escuela, direccion_escuela)# creacion de la escuela

    #Banderas para controlar el menu
    in_menu_principal = True
    in_menu_prof = False
    in_menu_est = False
    in_menu_comi = False

    while in_menu_principal:
        opcion = menu_principal(nombre_escuela)

        if opcion == 1:
            in_menu_prof = True
            while in_menu_prof:
                opcion_profesor = menu_profesores()
                if opcion_profesor ==1:
                    print('opcion 1')
                    grado = int(input('Ingrese el grado: '))
                    print(Profesor.lista_alumnos(dao.lista_estudiantes(), grado)) # imprime la lista de alumnos de un profesor, dado el grado
                elif opcion_profesor ==2:
                    list_prof()
                    codigo_p = int(input('ingrese el codigo del perofesor: '))
                    profesor = obtener_profesor(codigo_p) #se crea la instancia de la clase profesor dado el codigo
                    list_est()
                    codigo_est = int(input('Ingrese el codigo del estudiante a agregar nota: '))
                    estudiante = obtener_estudiante(codigo_est) # se crea la instancia de la clase estudiante dado por el codigo
                    nota = float(input('ingrese la nota del estudiante: '))
                    estudiante = profesor.colocar_nota(estudiante, nota) # se actualiza la clase estudiante con la nota ya implementada
                    dao.actualizar_estudiante(estudiante, codigo_est) # se actualiza la base de datos con la nota nueva
                elif opcion_profesor == 3:
                    in_menu_prof =False
                elif opcion_profesor == 4:
                    print('Ha salido del sistema')
                    in_menu_prof = False
                    in_menu_principal =False
                else:
                    print('Opcion invalida')

        elif opcion == 2:
            in_menu_est = True
            while in_menu_est:
                opcion_estudiante = menu_estudiante()
                if opcion_estudiante ==1:
                    cod_est = int(input('Ingrese su codigo: '))
                    estudiante = obtener_estudiante(cod_est) # se crea la instancia del estudiante dado el codigo
                    print(f'Sus notas actuales son: {estudiante.notas}') # se imprimen las notas del estudiante
                elif opcion_estudiante ==2:
                    print('opcion 2')
                    cod_est = int(input('Ingrese su codigo: '))
                    estudiante = obtener_estudiante(cod_est)
                    print(f'Su promedio actual de notas es: {estudiante.promedio_notas()}') #se imprime el promedio de notas
                elif opcion_estudiante == 3:
                    in_menu_est =False
                elif opcion_estudiante == 4:
                    print('ha salido del sistema')
                    in_menu_principal =False
                    in_menu_est =False
                else:
                    print('Opcion invalida')
        
        elif opcion == 3:
            in_menu_comi = True
            while in_menu_comi:
                opcion_comi = menu_comite()
                if opcion_comi ==1:
                    print('opcion 1')
                    print("agregar estudiante")
                    nombre_estudiante=input("Ingrese el nombre del estudiante: ")
                    id_estudiante=input("Ingrese el id del estudiante: ")
                    grado_estudiante=int(input("Ingrese el grado del estudiante: "))
                    estudiante = Estudiante(nombre_estudiante, 0, id_estudiante, grado_estudiante)# se instancia la clas estudiante con los valores previamente obtenidos
                    escuela.matricular_estudiante(estudiante) # se matricula el estudiante a traves de la clase escuela, agregandolo a la base de datos
                elif opcion_comi == 2:
                    list_est()
                    codigo_estudiante = int(input('ingrese codigo de estudiante a actualizar: '))
                    nombre_estudiante=input("Ingrese el nombre del estudiante: ")
                    id_estudiante=input("Ingrese el id del estudiante: ")
                    grado_estudiante=int(input("Ingrese el grado del estudiante: "))
                    #el cero era el codigo del estudiante, pero decidimos que se generara en autoincremento en mysql
                    estudiante = Estudiante(nombre_estudiante, 0, id_estudiante, grado_estudiante)
                    dao.actualizar_estudiante(estudiante, codigo_estudiante) # se actualiza el estudiante en la base de datos
                elif opcion_comi == 3:
                    print('opcion 3')
                    list_est()#lista de estudiantes en el colegio
                elif opcion_comi == 4:
                    list_est()
                    escuela.expulsar_estudiante()# se expulsa un estudiante dado el codigo
                elif opcion_comi == 5:
                    list_est()
                    cod_est = int(input('ingrese codigo del estudiante para generar boletin: '))
                    estudiante = obtener_estudiante(cod_est)
                    escuela.generar_boletin(estudiante) #genera un archi txt con el nombre del estudiante donde estan las notas en cada materia y el rpomedio
                elif opcion_comi == 6:
                    print('opcion 6')
                    print("agregar profesor")
                    nombre_profesor=input("Ingrese el nombre del profesor: ")
                    id_profesor=input("Ingrese el id del profesor: ")
                    materia_profesor=input("Ingrese la materia del profesor: ")
                    grado_profesor=int(input("Ingrese el grado del profesor: "))
                    salario_profesor=int(input("Ingrese salario del profesor: "))
                    #el cero era el codigo del profesor, pero decidimos que se generara en autoincremento en mysql
                    profesor=Profesor(nombre_profesor,0,id_profesor,materia_profesor,grado_profesor,salario_profesor) # se crea una instancia con los valores previamente dados
                    escuela.contratar_profesor(profesor)# se contrata el profesor y se agrega a la base de datos a tra vez de la escuela
                elif opcion_comi == 7:
                    dao = DAO()
                    list_prof()
                    codigo_profe = int(input('Ingrese codigo de profesor a actualizar: '))
                    nombre_profesor=input("Ingrese el nombre del profesor: ")
                    id_profesor=input("Ingrese el id del profesor: ")
                    materia_profesor=input("Ingrese la materia del profesor: ")
                    grado_profesor=int(input("Ingrese el grado del profesor: "))
                    salario_profesor=int(input("Ingrese salario del profesor: "))
                    profesor=Profesor(nombre_profesor,0,id_profesor,materia_profesor,grado_profesor,salario_profesor)
                    dao.actualizar_profesor(profesor, codigo_profe) # se actualizan los datos del profesor en la base de datos
                elif opcion_comi == 8:
                    list_prof()
                elif opcion_comi == 9:
                    list_prof()
                    escuela.eliminar_profesor()# se eliman el profesor dado el codigo
                elif opcion_comi == 10:
                    print('opcion 10')
                    in_menu_comi =False
                elif opcion_comi == 11:
                    print('Salio del sistema')
                    in_menu_comi = False
                    in_menu_principal =False
                else:
                    print('Opcion invalida')
        elif opcion == 4:
            print('Usted ha salido del sistema')
            in_menu_principal = False

        else:
            print('Opcion invalida')