from lark import Transformer, v_args
from classes.Variables import Variables
from classes.Crypt import Crypt
from classes.HandleFiles import HandleFiles


@v_args(inline=True)
class DSL(Transformer):

    def __init__(self):
        self.variables = {}


    def start(self, *expr):
        return expr
    
    def expr(self, *statement):
        return statement
    
    def statement(self, state):
        return state
    
    def var_declaration(self, name, value):
        # Implementar la lógica para declarar una variable
        Variables().var_declaration(self.variables, name, value)

    def var_assigment(self, name, value):
        # Implementar la lógica para asignar un valor a una variable
        Variables().var_assigment(self.variables, name, value)

    def outln(self, name=None):
        print(name)
    
    def mkdir(self, path):
        # Implementar la lógica para crear un directorio
        HandleFiles().mkdir(path)

    def rmdir(self, path):
        # Implementar la lógica para eliminar un directorio
        HandleFiles().rmdir(path)

    def touch(self, path):
        # Implementar la lógica para crear un archivo vacío
        HandleFiles().touch(path)

    def move(self, src_path, dst_path):
        # Implementar la lógica para mover un archivo
        HandleFiles().move(src_path, dst_path)

    def copy(self, src_path, dst_path):
        # Implementar la lógica para copiar un archivo
        HandleFiles().copy(src_path, dst_path)

    def list(self, dst_path='.'):
        # Implementar la lógica para listar archivos y directorios
        HandleFiles().list(dst_path)

    def cat(self, path):
        # Implementar la lógica para mostrar el contenido de un archivo
        HandleFiles().cat(path)

    def genkey(self, dst_path):
        # Implementar la lógica para generar una clave de encriptación
        Crypt().genkey(dst_path)

    def cryptext(self, dst_path, *path):
        # Implementar la lógica para cifrar un texto
        Crypt().cryptext(dst_path, " ".join(path))

    def crypfile(self, dst_path, path):
        # Implementar la lógica para cifrar un archivo
        Crypt().crypfile(dst_path, path)

    def destext(self, dst_path, cryp):
        # Implementar la lógica para descifrar un texto
        Crypt().destext(dst_path, cryp)

    def desfile(self, dst_path, path):
        # Implementar la lógica para descifrar un archivo
        Crypt().desfile(dst_path, path)

    def path(self, pat):
        return pat
    
    def src_path(self, src):
        return src
    
    def dst_path(self, *dst):
        return "/".join(dst)
    
    def cryp(self, cry):
        return cry
    
    def var_name(self, name):
        return name
    
    def name(self, var):
        return self.variables[var]
    
    def value(self, val):
        return val
    
    def string(self, value):
        return str(value[1:-1])
    
    def NUMERIC(self, value):
        return int(value)
    
    def BOOLEAN(self, value):
        if value == 'true':
            return True
        elif value == 'false':
            return False