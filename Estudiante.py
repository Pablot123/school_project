from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, codigo, id, grado, materias, notas) -> None:
        super().__init__(nombre, codigo, id)
        self._grado = grado
        self._materias = materias
        self._notas = notas

    @property
    def grado(self):
        return self._grado
    @grado.setter
    def grado(self, grado):
        self._grado = grado
    
    @property
    def materias(self):
        return self._materias
    @materias.setter
    def materias(self, materias):
        self._materias = materias
    
    @property
    def notas(self):
        return self._notas
    @notas.setter
    def notas(self, notas):
        self._notas = notas
    
    def promedio_notas():
        pass