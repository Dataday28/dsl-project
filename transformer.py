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
    
    def var_declaration(self, name, value = None):
        # Implementar la lógica para declarar una variable
        Variables().var_declaration(self.variables, name, value)

    def var_assigment(self, name, value):
        # Implementar la lógica para asignar un valor a una variable
        Variables().var_assigment(self.variables, name, value)

    def outln(self, name=None):
        print(name)
        return name

    def sum(self, a, b):
        # Implementar la lógica para sumar dos números
        return a + b

    def rest(self, a, b):
        # Implementar la lógica para restar dos números
        return a - b

    def mul(self, a, b):
        # Implementar la lógica para multiplicar dos números
        return a * b

    def div(self, a, b):
        # Implementar la lógica para dividir dos números
        if b!= 0:
            return a / b
        else:
            raise ZeroDivisionError("\n Error: División por cero \n")
    
    def mkdir(self, files):
        # Implementar la lógica para crear un directorio
        HandleFiles().mkdir(files)

    def rmdir(self, files):
        # Implementar la lógica para eliminar un directorio
        HandleFiles().rmdir(files)

    def touch(self, files):
        # Implementar la lógica para crear un archivo vacío
        HandleFiles().touch(files)

    def move(self, files, src_path):
        # Implementar la lógica para mover un archivo
        HandleFiles().move(files, src_path)

    def copy(self, files, src_path):
        # Implementar la lógica para copiar un archivo
        HandleFiles().copy(files, src_path)

    def list(self, src_path='.'):
        # Implementar la lógica para listar archivos y directorios
        HandleFiles().list(src_path)

    def cat(self, files):
        # Implementar la lógica para mostrar el contenido de un archivo
        HandleFiles().cat(files)

    def genkey(self, dst_key):
        # Implementar la lógica para generar una clave de encriptación
        Crypt().genkey(dst_key)

    def cryptext(self, dst_key, *files):
        # Implementar la lógica para cifrar un texto
        Crypt().cryptext(dst_key, " ".join(files))

    def crypfile(self, dst_key, files):
        # Implementar la lógica para cifrar un archivo
        Crypt().crypfile(dst_key, files)

    def destext(self, dst_key, cryp):
        # Implementar la lógica para descifrar un texto
        Crypt().destext(dst_key, cryp)

    def desfile(self, dst_key, files):
        # Implementar la lógica para descifrar un archivo
        Crypt().desfile(dst_key, files)

    def text(self, *fil):
        return " ".join(fil)
    
    def files(self, fil):
        return fil
    
    def dst_key(self, *dst):
        return "/".join(dst)
    
    def src_path(self, *src):
        return "/".join(src)
    
    def cryp(self, cry):
        return cry
    
    def var_name(self, name):
        return name
    
    def name(self, var):
        if str(var) not in self.variables:
            raise NameError(f"\n Error: Variable '{var}' no definida \n")
        return self.variables[str(var)]
    
    def value(self, val):
        return val
    
    def string(self, value):
        return str(value[1:-1])
    
    def NUMERIC(self, value):
        return int(value)
    
    def FLOT(self, value):
        return float(value)
    
    def number(self, n):
        return float(n)
    
    def BOOLEAN(self, value):
        if value == 'true':
            return True
        elif value == 'false':
            return False