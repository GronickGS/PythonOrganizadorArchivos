# Organizador de Archivos

Este repositorio contiene dos scripts de Python diseñados para ayudarte a organizar tus archivos en carpetas según su tipo o extensión. Estos scripts pueden ser útiles para mantener tu sistema de archivos ordenado y facilitar la búsqueda de archivos específicos. A continuación, se proporciona una breve descripción de cada script y cómo usarlos.

## Organizar por Carpetas

El script "Organizar por Carpetas" se encarga de organizar los archivos en carpetas predefinidas según su tipo. A continuación, se describe su funcionamiento:

1. **Carpetas de Destino:** El script define carpetas de destino para varios tipos de archivos, como Fotos, Videos, Instaladores, Documentos, Adobe, Scripts, Audio y Otros.

2. **Creación de Carpetas:** Si las carpetas de destino no existen, el script las crea automáticamente en el directorio actual.

3. **Clasificación de Archivos:** El script itera a través de los archivos en el directorio actual y los clasifica en las carpetas correspondientes según su extensión.

4. **Organización de Documentos de Microsoft:** Los documentos de Microsoft (como Word, Excel y PowerPoint) se organizan en subcarpetas dentro de la carpeta de Documentos.

5. **Manejo de Errores:** El script maneja posibles errores durante el proceso de organización y muestra mensajes de error en caso de problemas.

6. **Éxito:** Al finalizar, el script muestra un mensaje indicando que los archivos se han organizado con éxito en el directorio actual.

## Organizar por Extensión

El script "Organizar por Extensión" se centra en organizar los archivos en carpetas según su extensión. Aquí se explica cómo funciona:

1. **Carpeta de Origen:** El script toma como punto de partida la carpeta actual donde se ejecuta.

2. **Lista de Archivos:** Obtiene una lista de archivos en la carpeta de origen.

3. **Creación de Carpetas:** Para cada archivo, crea una carpeta correspondiente a su extensión si esta no existe aún.

4. **Mover Archivos:** Mueve cada archivo a la carpeta de la extensión a la que pertenece.

5. **Éxito:** Al finalizar, el script muestra un mensaje indicando que los archivos se han organizado por extensión.

## Uso

Para utilizar cualquiera de estos scripts, sigue estos pasos:

1. Descarga el script que deseas utilizar y guárdalo en el directorio donde deseas organizar tus archivos.

2. Abre una terminal o línea de comandos en ese directorio.

3. Ejecuta el script utilizando Python. Por ejemplo: python mi_script.py

4. Los archivos se organizarán automáticamente en las carpetas correspondientes.

## Notas Importantes

- Asegúrate de realizar copias de seguridad de tus archivos antes de utilizar estos scripts, ya que moverán los archivos en tu sistema de archivos.

- Personaliza los scripts según tus necesidades. Puedes agregar o eliminar extensiones de archivos o carpetas de destino según tus preferencias.

¡Esperamos que estos scripts te sean útiles para mantener tu sistema de archivos ordenado! Si encuentras algún problema o tienes sugerencias de mejora, no dudes en informarnos o contribuir al repositorio.
