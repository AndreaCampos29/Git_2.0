from Archivo_model import Archivo
from Commit_model import Commit
from Rama_model import Rama

class Repo:
    def __init__(self):
        self.ramas = {}
        self.commits = []
        self.rama_actual = None

    def crear_rama(self, nombre):
        if nombre not in self.ramas:
            self.ramas[nombre] = Rama(nombre)
        else:
            raise ValueError('La rama ya existe')

    def cambiar_rama(self, nombre):
        if nombre in self.ramas:
            self.rama_actual = self.ramas[nombre]
        else:
            raise ValueError('Rama no existe')

    def hacer_commit(self, mensaje):
        id_commit = len(self.commits) + 1
        archivos = []  # Aquí se pueden agregar archivos al commit
        nuevo_commit = Commit(id_commit,mensaje, archivos, self.rama_actual.current_commit)
        self.commits.append(nuevo_commit)
        self.rama_actual.current_commit = nuevo_commit

    def merge(self, nombre_rama):
        if nombre_rama in self.ramas:
            rama_a_fusionar = self.ramas[nombre_rama]
            # Para simplificar, solo se actualiza el commit reciente de la rama actual.
            self.rama_actual.current_commit = rama_a_fusionar.current_commit
        else:
            raise ValueError('Rama no existe')

    def mostrar_historial(self):
        for commit in self.commits:
            print(f'Commit ID: {commit.id}')
