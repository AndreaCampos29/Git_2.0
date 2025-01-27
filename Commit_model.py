class Commit:
    def __init__(self,id, mensaje,archivos, old_Commit):
        self.id = id
        self.mensaje = mensaje
        self.archivos = archivos
        self.old_Commit = old_Commit