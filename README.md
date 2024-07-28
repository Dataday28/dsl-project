<h1> Sauri </h1>

# Proposito

El propósito de este DSL (Lenguaje Específico de Dominio) es proporcionar una forma estructurada y simplificada de realizar operaciones comunes de gestión de archivos, operaciones matematicas y criptografía. 
Está diseñado para facilitar tareas como la creación y eliminación de directorios y archivos, 
la lectura y listado de contenido de archivos, operaciones basicas de matematicas como suma, resta, multiplicacion y division, y operaciones criptográficas como generación de claves y encriptación/desencriptación de texto y archivos.

# Ejecucion
Para poder ejecutar el codigo se nesesita python y hay un archivo 'requirements.txt' que contiene las bibliotecas necesarias para su ejecucion.

Una vez teniendo lo necesario solo tienes que ejecutar el archivo 'parser.py' mas el documento donde este el codigo del DSL.

Ejemplo:

```python
python parser.py example.dsl
```

# Estructura General
El programa consiste en una serie de expresiones, cada una de las cuales puede contener una o más sentencias. Cada sentencia debe terminar con un punto y coma (;).

## Tipos de Declaraciones

## Declaraciones de Variables
Declaración de Variable: Define una nueva variable opcionalmente asignándole un valor.


```python
var nombre_variable = valor;
```

Ejemplo: 

```python
# Se puede declarar la variable sin asignarle un valor
var x = 10;
var y;
```

Asignación de Variable: Asigna un valor a una variable existente.

```python
nombre_variable = valor;
```

Ejemplo: 

```python
x = 5;
```

## Operaciones de Entrada/Salida

Imprimir en consola: Imprime en la consola un valor que le asignes.

```python
outln(valor);
```

Ejemplo: 

```python
outln("Hola, mundo");
outln(x);
```

Comentarios: Puedes agregar comentarios o codigo que quieras que el DSL ignore.

Ejemplo: 

```python
# Este es un comentario
```

## Operaciones de Sistema de Archivos

Crear Directorio: Crea un nuevo directorio.

```python
CreateDirectory('nombre_del_directorio');
```

Ejemplo: 

```python
CreateDirectory('/path/to/directory');
```

Eliminar Directorio: Elimina un directorio existente.

```python
DeleteDirectory('nombre_del_directorio');
```

Ejemplo: 

```python
DeleteDirectory('<ruta>');
```

Crear Archivo: Crea un nuevo archivo.

```python
CreateFile('nombre_del_archivo');
```

Ejemplo: 

```python
CreateFile('/path/to/file.txt');
```

Escribir en Archivo: Escribe dentro de un archivo.

```python
WriteFile('nombre_del_archivo');
```

Ejemplo: 

```python
WriteFile('Contenido del archivo', '/path/to/file.txt');
```

Mover Archivo: Mueve un archivo a una nueva ubicación.

```python
MoveFile('ruta_del_archivo', 'nueva_ruta');
```

Ejemplo: 

```python
MoveFile('/path/to/file.txt', '/new/path/to/file.txt');
```

Copiar Archivo: Copia un archivo a una nueva ubicación.

```python
CopyFile('ruta_del_archivo', 'nueva_ruta');
```

Ejemplo: 

```python
CopyFile('/path/to/file.txt', '/copy/path/to/file.txt');
```

Listar Directorio: Lista los archivos en un directorio.

```python
List('ruta_del_directorio');
```
```python
# Lista los archivos del directorio actual
List();
```

Ejemplo: 

```python
List('/path/to/directory');
List();
```

Leer Archivo: Lee el contenido de un archivo.

```python
ReadFile('ruta_del_archivo');
```

Ejemplo: 

```python
ReadFile('/path/to/file.txt');
```

## Operaciones de Criptografía

Generar Clave: Genera una nueva clave.

```python
GenerateKey('ruta_de_la_clave');
```

Ejemplo: 

```python
GenerateKey('/path/to/keyfile');
```

Encriptar Texto: Encripta un texto con una clave.

```python
CrypText('ruta_de_la_clave', 'texto_a_encriptar');
```

Ejemplo: 

```python
CrypText('/path/to/keyfile', 'Texto a encriptar');
```

Encriptar Archivo: Encripta un archivo con una clave.

```python
CrypFile('ruta_de_la_clave', 'archivo_a_encriptar');
```

Ejemplo: 

```python
CrypFile('/path/to/keyfile', '/path/to/file.txt');
```

Desencriptar Texto: Desencripta un texto con una clave.

```python
DesText('ruta_de_la_clave', 'texto_encriptado');
```

Ejemplo: 

```python
DesText('/path/to/keyfile', 'Texto encriptado');
```

Desencriptar Archivo: Desencripta un archivo con una clave.

```python
DesFile('ruta_de_la_clave', 'archivo_encriptado');
```

Ejemplo: 

```python
DesFile('/path/to/keyfile', '/path/to/encrypted_file.txt');
```

## Operaciones Matematicas

Suma

```python
numero + numero;
```

Ejemplo: 

```python
result = 5 + 3;
```

Resta

```python
numero - numero;
```

Ejemplo: 

```python
result = 5 - 3;
```

Multiplicacion

```python
numero * numero;
```

Ejemplo: 

```python
result = 5 * 3;
```

Division

```python
numero / numero;
```

Ejemplo: 

```python
result = 5 / 3;
```