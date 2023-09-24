import os
import shutil

# Directorio donde se encuentra el script
directorio_actual = os.getcwd()

# Define las carpetas de destino para cada tipo de archivo
carpeta_fotos = os.path.join(directorio_actual, "Fotos")
carpeta_videos = os.path.join(directorio_actual, "Videos")
carpeta_instaladores = os.path.join(directorio_actual, "Instaladores")
carpeta_documentos = os.path.join(directorio_actual, "Documentos")
carpeta_adobe = os.path.join(directorio_actual, "Adobe")
carpeta_scripts = os.path.join(directorio_actual, "Scripts")
carpeta_audio = os.path.join(directorio_actual, "Audio")
carpeta_otros = os.path.join(directorio_actual, "Otros")

# Lista de carpetas de destino
carpetas_destino = [
    carpeta_fotos, carpeta_videos, carpeta_instaladores,
    carpeta_adobe, carpeta_scripts,
    carpeta_audio, carpeta_otros
]

# Crea las carpetas de destino si no existen
for carpeta in carpetas_destino:
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

# Carpeta de destino para documentos
carpeta_documentos_destino = os.path.join(carpeta_documentos, "PDF")

# Verifica y crea la carpeta de destino para documentos si no existe
if not os.path.exists(carpeta_documentos_destino):
    os.makedirs(carpeta_documentos_destino)

# Extensiones de archivo para documentos de Microsoft
extensiones_microsoft = {
    ".pdf": "PDF",
    ".doc": "Word",
    ".docx": "Word",
    ".ppt": "PowerPoint",
    ".pptx": "PowerPoint",
    ".xls": "Excel",
    ".xlsx": "Excel"
}

# Extensiones de archivo para scripts de programación
extensiones_scripts = (".py", ".cs", ".java", ".cpp", ".rb", ".js", ".html", ".css", ".php", ".sql")

# Extensiones de archivo para archivos de audio
extensiones_audio = (".mp3", ".wav", ".flac", ".aac")

# Itera a través de los archivos en el directorio de entrada (directorio_actual)
for archivo in os.listdir(directorio_actual):
    ruta_archivo = os.path.join(directorio_actual, archivo)

    # Ignora si es un directorio
    if os.path.isdir(ruta_archivo):
        continue

    # Determina el tipo de archivo según su extensión
    extension = os.path.splitext(archivo)[1].lower()

    try:
        # Mueve el archivo a la carpeta correspondiente
        if extension in (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"):
            shutil.move(ruta_archivo, os.path.join(carpeta_fotos, archivo))
        elif extension in (".mp4", ".avi", ".mov", ".mkv"):
            shutil.move(ruta_archivo, os.path.join(carpeta_videos, archivo))
        elif extension in (".exe", ".iso"):
            shutil.move(ruta_archivo, os.path.join(carpeta_instaladores, archivo))
        elif extension in extensiones_microsoft:
            # Si es un documento de Microsoft, organiza en subcarpetas
            subcarpeta = extensiones_microsoft[extension]
            carpeta_destino = os.path.join(carpeta_documentos, subcarpeta)
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
        elif extension in extensiones_scripts:
            shutil.move(ruta_archivo, os.path.join(carpeta_scripts, archivo))
        elif extension in extensiones_audio:
            shutil.move(ruta_archivo, os.path.join(carpeta_audio, archivo))
        elif extension in (".pdf", ".ai", ".eps", ".indd", ".psd"):
            shutil.move(ruta_archivo, os.path.join(carpeta_adobe, archivo))
        else:
            shutil.move(ruta_archivo, os.path.join(carpeta_otros, archivo))
    except Exception as e:
        print(f"Error al mover el archivo {archivo}: {e}")

print("Archivos organizados con éxito en el directorio actual.")
