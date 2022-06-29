class Materia:

    def __init__(self, nombre, codigo) -> None:
        self.__nombre = nombre
        self.__codigo = codigo
    #Getters and setters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo