class Persona:
    """
    Clase padre de estudiante y profesor
    """
    def __init__(self, nombre, codigo, id) -> None:
        self.__nombre = nombre
        self.__codigo = codigo
        self.__id = id
    
    #----Metodos getter and setters privados
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id