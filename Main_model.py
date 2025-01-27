from Repositorio import Repo

# Inicializar el repositorio
repo = Repo()

# Crear la rama principal y hacer un commit inicial
repo.crear_rama('main')
repo.cambiar_rama('main')
repo.hacer_commit('Initial commit')

# Crear una nueva rama y trabajar en ella
repo.crear_rama('develop')
repo.cambiar_rama('develop')
repo.hacer_commit('Added new feature')

# Cambiar a la rama principal y hacer un merge
repo.cambiar_rama('main')
repo.merge('develop')

# Mostrar el historial de commits
repo.mostrar_historial()