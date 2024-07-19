El propósito de este DSL (Lenguaje Específico de Dominio) es proporcionar una forma estructurada y simplificada de realizar operaciones comunes de gestión de archivos y criptografía. 
Está diseñado para facilitar tareas como la creación y eliminación de directorios y archivos, 
la lectura y listado de contenido de archivos, y operaciones criptográficas como generación de claves y encriptación/desencriptación de texto y archivos.

# Tipos de Declaraciones

## Declaraciones de Variables
Declaración de Variable: Define una nueva variable opcionalmente asignándole un valor.


```python
var nombre_variable = valor;
```
```python
# Se puede declarar la variable sin asignarle un valor
var nombre_variable;
```

Asignación de Variable: Asigna un valor a una variable existente.

```python
nombre_variable = valor;
```

## Operaciones de Entrada/Salida

```python
outln(valor);
```

## Operaciones de Sistema de Archivos

Crear Directorio: Crea un nuevo directorio.

```python
CreateDirectory('nombre_del_directorio');
```

Eliminar Directorio: Elimina un directorio existente.

```python
DeleteDirectory('nombre_del_directorio');
```

Crear Archivo: Crea un nuevo archivo.

```python
CreateFile('nombre_del_archivo');
```

Mover Archivo: Mueve un archivo a una nueva ubicación.

```python
MoveFile('ruta_del_archivo', 'nueva_ruta');
```

Copiar Archivo: Copia un archivo a una nueva ubicación.

```python
CopyFile('ruta_del_archivo', 'nueva_ruta');
```

Listar Directorio: Lista los archivos en un directorio.

```python
List('ruta_del_directorio');
```
```python
# Lista los archivos del directorio actual
List();
```

Leer Archivo: Lee el contenido de un archivo.

```python
ReadFile('ruta_del_archivo');
```

## Operaciones de Criptografía

Generar Clave: Genera una nueva clave.

```python
GenerateKey('ruta_de_la_clave');
```

Encriptar Texto: Encripta un texto con una clave.

```python
CrypText('ruta_de_la_clave', 'texto_a_encriptar');
```

Encriptar Archivo: Encripta un archivo con una clave.

```python
CrypFile('ruta_de_la_clave', 'archivo_a_encriptar');
```

Desencriptar Texto: Desencripta un texto con una clave.

```python
DesText('ruta_de_la_clave', 'texto_encriptado');
```

Desencriptar Archivo: Desencripta un archivo con una clave.

```python
DesFile('ruta_de_la_clave', 'archivo_encriptado');
```
