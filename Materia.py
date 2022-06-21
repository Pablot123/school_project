class Materia:
    def __init__(self, nombre, codigo) -> None:
        self._nombre = nombre
        self.__codigo = codigo
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def codigo(self):
        return self.__codigo