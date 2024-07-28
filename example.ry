# En este ejemplo se muestra la creacion de archivos y directorios, y la genracion de key para poder cifrar

# Asignacion de variables
# Tambien se pueder declar las variables y despues asignarles un valor por ejemplo: var x;  x = 2;
# Para poder utilizar las variables en las funciones se tiene que declarar en comillas simples: '', las comillas dobles: "" son para valores de tipo string
# En caso de las rutas puedes poner la ruta completa, pero usando las barras: '/', por ejemplo: C:/usuario/documentos/documentos
var directory = 'carpeta2';
var fileText = 'carpeta2/prueba2.txt';
var text = 'War never changes';
var key = 'carpeta2/clave.key';

# Creacion de directorio
CreateDirectory(directory);

# Creacion del archivo
CreateFile(fileText);

# Escribir en el archivo
WriteFile(text, fileText);

# Creacion de la llave de cifrado
# Para generar la Key solo se ponen los directorios, sin necesidad de poner el archivo, por ejemplo: C:/usuario/documentos/documentos
GenerateKey(directory);

# Cifrado del archivo
# En este caso si es nesesario especificar el archivo, por ejemplo: C:/usuario/documentos/documentos/clave.key
CrypFile(key, fileText);

outln("Archivo Cifrado con exito");

