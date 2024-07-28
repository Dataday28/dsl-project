from lark import Lark, UnexpectedInput
from transformer import DSL


# Cargar la gramática desde el archivo grammar.lark
with open('grammar/grammar.lark', 'r') as f:
    grammar_file = f.read()

# Parsea la gramática
parser = Lark(grammar_file, parser='lalr', transformer=DSL())

## Leer el archivo
with open('example2.dsl', 'r') as file:
    dsl_code = file.read()

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

# Ejecutar el código DSL y obtener el árbol AST
evaluate(dsl_code)