class Escuela:
    def __init__(self, id, nombre, direccion, profesores, alumnos, materias) -> None:
        self.__id = id # llave primaria
        self.__nombre = nombre
        self.__direccion = direccion
        self._profesores = profesores #estos se pueden cambiar
        self._alumnos = alumnos #estos se pueden cambiar
        self._materias = materias #estos se pueden cambiar
    
    #Getters and Setters
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre =nombre
    
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
    
    @property
    def profesores(self):
        return self._profesores
    
    @property
    def alumnos(self):
        return self._alumnos
    
    @property
    def materias(self):
        return self._materias
    
    def agregar_profesor():
        pass

    def eliminar_profesor():
        pass

    def matricular_estudiante():
        pass

    def expulsar_estudiante():
        pass

    def agregar_materia():
        pass

    def eliminar_materia():
        pass
