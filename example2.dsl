# En este ejemplo se muestra el descifrado de un archivo

# Asignacion de variables
# Tambien se pueder declar las variables y despues asignarles un valor por ejemplo: var x;  x = 2;
# Para poder utilizar las variables en las funciones se tiene que declarar en comillas simples: '', las comillas dobles: "" son para valores de tipo string
# En caso de las rutas puedes poner la ruta completa, pero usando las barras: '/', por ejemplo: C:/usuario/documentos/documentos
var key = 'carpeta2/clave.key';
var fileText = 'carpeta2/prueba2.txt';

# Descifrado del archivo
DesFile(key, fileText);

# Impresion en la consola
outln("archivo descifrado con exito");

# Muestra el archivo ya descifrado
ReadFile(fileText);

