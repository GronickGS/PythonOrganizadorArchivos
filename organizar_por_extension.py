import os
import shutil

# Carpeta de origen
carpeta_origen = "./"  # Carpeta actual (donde se ejecuta el script)

# Obtener la lista de archivos en la carpeta de origen
archivos = os.listdir(carpeta_origen)

# Crear una carpeta para cada extensión
for archivo in archivos:
    if os.path.isfile(archivo):  # Verificar si es un archivo
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()  # Convertir la extensión a minúsculas

        # Crear una carpeta para la extensión si no existe
        carpeta_extension = os.path.join(carpeta_origen, extension[1:])  # Ignorar el punto inicial
        if not os.path.exists(carpeta_extension):
            os.makedirs(carpeta_extension)

        # Mover el archivo a la carpeta de la extensión
        shutil.move(archivo, os.path.join(carpeta_extension, archivo))

print("Archivos organizados por extensión.")
