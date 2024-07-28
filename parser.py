from lark import Lark, UnexpectedInput
from transformer import DSL
import sys


# Cargar la gramática desde el archivo grammar.lark
with open('grammar/grammar.lark', 'r') as f:
    grammar_file = f.read()

# Parsea la gramática
parser = Lark(grammar_file, parser='lalr', transformer=DSL())

## Analizar el código DSL
def evaluate(dsl_code):
    try:
        return parser.parse(dsl_code)
    except UnexpectedInput as e:
        print(f"\n Error en la sintaxis de la entrada: {e} \n")
    except NameError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    if len(sys.argv) != 2:
        print("Uso: parser.py <archivo.dsl>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            dsl_code = file.read()
            result = evaluate(dsl_code)
            return result
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except IOError as e:
        print(f"Error al leer el archivo {file_path}: {e}")

if __name__ == "__main__":
    main()