import os
import shutil


class HandleFiles:

    def mkdir(self, path):
        # Implementar la lógica para crear un directorio
        try:
            os.makedirs(path, exist_ok=True)
            print(f" \n Se creo el directorio en: {path} \n")
        except Exception as ex:
            print(f"\n Error al crear el directorio: '{path}': {ex} \n")
        

    def rmdir(self, path):
        # Implementar la lógica para eliminar un directorio
        try:
            shutil.rmtree(path)
            print(f" \n Directorio Eliminado: {path} \n")
        except Exception as ex:
            print(f"\n Error al eliminar directorio: '{path}': {ex} \n")

    def touch(self, path):
        # Implementar la lógica para crear un archivo vacío
        try:
            with open(path, 'w') as archivo:
                pass
            print(f"\n Archivo creado: {path} \n")
        except Exception as ex:
            print(f"\n Error al crear archivo: '{path}': {ex} \n")

    def rename(self, old_path, new_path):
        # Implementar la lógica para renombrar un archivo o directorio
        try:
            os.rename(old_path, new_path)
            print(f"\n Renombrando archivo o directorio: {old_path} a {new_path} \n")
        except Exception as ex:
            print(f"\n Error al renombrar archivo o directorio: '{old_path}' a '{new_path}': {ex} \n")

    def write(self, text, dst_path):
        # Implementar la lógica para escribir un texto en un archivo
        try:
            with open(dst_path, 'w') as archivo:
                archivo.write(text)
            print(f"\n Escribiendo en archivo: {dst_path} \n")
        except Exception as ex:
            print(f"\n Error al escribir en archivo: '{dst_path}': {ex} \n")

    def move(self, src_path, dst_path):
        # Implementar la lógica para mover un archivo
        try:
            shutil.move(src_path, dst_path)
            print(f"\n Moviendo archivo: {src_path} a {dst_path} \n")
        except Exception as ex:
            print(f"Error al mover archivo: '{src_path}' a '{dst_path}' : {ex}")

    def copy(self, src_path, dst_path):
        # Implementar la lógica para copiar un archivo
        try: 
            shutil.copy(src_path, dst_path)
            print(f"\n Copiando archivo: {src_path} a {dst_path} \n")
        except Exception as ex:
            print(f"\n Error al copiar archivo: '{src_path}' a '{dst_path}': {ex} \n")

    def list(self, dst_path):
        # Implementar la lógica para listar archivos y directorios
        try:
            contenidos = os.listdir(dst_path)
            print(f"\n Directorio: '{dst_path}' : \n")
            for contenido in contenidos:
                print(f"{contenido} \n")

        except Exception as ex:
            print(f"\n Error al listar contenidos de {dst_path} : {ex} \n")

    def cat(self, path):
        # Implementar la lógica para mostrar el contenido de un archivo
        try:
            with open(path, 'r') as archivo:
                contenido = archivo.read()
            print(f"\n Contenido de '{path}': \n \n {contenido} \n ")

        except Exception as ex:
            print(f"\n Error al mostrar contenido de '{path}': {ex} \n")