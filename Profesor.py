from Persona import Persona

class Profesro(Persona):

    def __init__(self, nombre, codigo, id, materia, salario) -> None:
        Persona.__init__(self, nombre, codigo, id)
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