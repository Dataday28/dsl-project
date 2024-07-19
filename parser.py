from lark import Lark
from transformer import DSL


# Cargar la gramática desde el archivo grammar.lark
with open('grammar/grammar.lark', 'r') as f:
    grammar_file = f.read()

# Parsea la gramática
parser = Lark(grammar_file, parser='lalr', transformer=DSL())

## Leer el archivo
with open('example.dsl', 'r') as file:
    dsl_code = file.read()

## Analizar el código DSL
def evaluate(expression):
    try:
        ast = parser.parse(expression)
        return ast
    
    except Exception as e:
        print(f"Error durante la análisis: {e}")
        return exit(1)

# Ejecutar el código DSL y obtener el árbol AST
evaluate(dsl_code)