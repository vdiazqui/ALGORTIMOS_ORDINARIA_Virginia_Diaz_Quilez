# ALGORTIMOS_ORDINARIA_Virginia_Diaz_Quilezz


# 1. Ejercicio POO - BookShare

## Descripción

La aplicación BookShare gestiona y comparte bibliotecas de libros, permitiendo catalogar y agrupar libros en base a diferentes criterios. Esta implementación simplificada en Python contiene las clases `GENRE` y `Book` para manejar los libros y sus géneros.

## Clase GENRE

### Descripción

La clase `GENRE` es una enumeración (Enum) que define los posibles géneros para los libros. Los géneros disponibles son:

- `FICTION`
- `NON_FICTION`
- `FANTASY`
- `SCIENCE_FICTION`

## Clase Book
Este proyecto implementa una clase `Book` en Python que representa un libro con diversos atributos y métodos. La clase `Book` permite crear instancias de libros con información específica y realizar operaciones sobre esos libros.

### Descripción

La clase `Book` tiene los siguientes atributos:

- `id` (int): Identificador único del libro.
- `title` (str): Título del libro.
- `author` (str): Autor del libro.
- `pages` (int): Número de páginas del libro.
- `publication_date` (date): Fecha de publicación del libro.
- `genres` (list): Lista de géneros del libro, que deben ser instancias de la enumeración `GENRE`.

### Funcionalidades

- **Constructor**: Permite la creación de un libro validando los tipos y valores de los parámetros.
- **Getters**: Métodos para obtener los valores de los atributos del libro (`get_id`, `get_title`, `get_author`, `get_pages`, `get_publication_date`, `get_genres`).
- **Método `add_genre`**: Permite añadir un género al libro, asegurando que no se repita.
- **Método `__eq__`**: Compara dos instancias de libros para verificar si son iguales basándose en su `id`.
- **Método `__str__`**: Devuelve una representación en cadena legible del libro.

### Pruebas

El módulo incluye una función principal (`main()`) que realiza pruebas sobre la clase `Book`:

1. **Test de creación**: Verifica que los parámetros se establecen correctamente al crear un libro.
2. **Formato legible**: Verifica que la representación en cadena del libro es correcta.
3. **Añadir género**: Prueba el método `add_genre` para asegurar que se añaden géneros correctamente.
4. **Igualdad de libros**: Prueba el método `__eq__` para verificar la comparación de libros.


   
# 2. Ebook
# Implementación de la Clase EBook

Este proyecto implementa una clase `EBook` en Python que hereda de la clase `Book` para representar libros electrónicos con características adicionales específicas. La clase `EBook` permite crear instancias de libros electrónicos y realizar operaciones sobre ellos, extendiendo la funcionalidad de la clase `Book`.

## Archivos

- `genre.py`: Contiene la enumeración `GENRE` que define los géneros de los libros.
- `BookFile.py`: Contiene la clase `Book` que representa un libro físico.
- `EBook.py`: Contiene la clase `EBook` que hereda de `Book` y añade funcionalidades específicas para libros electrónicos.

## Descripción de la Clase EBook

La clase `EBook` hereda de `Book` y añade un atributo adicional:

- `format` (str): El formato del archivo del libro electrónico (e.g., PDF, EPUB, MOBI).

### Funcionalidades de EBook

- **Constructor**: Inicializa un nuevo libro electrónico, validando los tipos y valores de los parámetros.
  - `id` (int): Identificador único del ebook.
  - `title` (str): Título del ebook.
  - `author` (str): Autor del ebook.
  - `pages` (int): Número de páginas del ebook.
  - `publication_date` (date): Fecha de publicación del ebook.
  - `genres` (list): Lista de géneros del ebook.
  - `format` (str): Formato del archivo del ebook.

- **Método `get_format`**: Devuelve el formato del ebook.
- **Método `__str__`**: Devuelve una representación en cadena legible del ebook.



# 3. Fibonacci Recursivo

## Descripción

La sucesión de Fibonacci es una serie de números en la cual cada número es la suma de los dos números precedentes. Por ejemplo, los primeros diez números en la sucesión de Fibonacci son:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

## Función Recursiva

La función `fibonacci` calcula el n-ésimo número en la sucesión de Fibonacci de manera recursiva.

### Parámetros

- `n` (int): La posición en la secuencia de Fibonacci.

### Retorno

- (int): El n-ésimo número de Fibonacci.

### Caso Base

- Si `n` es 0, entonces el resultado es 0.
- Si `n` es 1, entonces el resultado es 1.

### Paso Recursivo

- Si `n` es mayor que 1, la función retorna `fibonacci(n-1) + fibonacci(n-2)`.

## Explicación del Algoritmo

La función fibonacci utiliza recursión para calcular el n-ésimo número de Fibonacci. La recursión es una técnica en la que una función se llama a sí misma para resolver subproblemas más pequeños. En este caso, la función se llama a sí misma con los valores n-1 y n-2 hasta que alcanza los casos base (cuando n es 0 o 1).

El tiempo de ejecución de este algoritmo es exponencial debido a que calcula muchas veces los mismos valores. Sin embargo, es una implementación directa y sencilla de entender para la definición recursiva de la sucesión de Fibonacci.



# 4. Bubble Sort (Ordenamiento Burbuja)

### Descripción del Método
Bubble Sort, también conocido como ordenamiento burbuja, es un algoritmo de ordenación simple que funciona revisando repetidamente la lista que se necesita ordenar, comparando elementos adyacentes e intercambiándolos si están en el orden incorrecto. Este proceso se repite varias veces hasta que no se necesitan más intercambios, lo que significa que la lista está ordenada.

### Funcionamiento de Bubble Sort
El funcionamiento del Bubble Sort se basa en la comparación de pares de elementos adyacentes a lo largo de la lista, y si un par está en el orden incorrecto (el primero es mayor que el segundo), los elementos se intercambian. El proceso se repite para cada elemento de la lista, pasando repetidamente por la lista hasta que no se necesitan más intercambios, lo cual ocurre cuando la lista está completamente ordenada.

#### Pasos del Bubble Sort:
1. Comenzar en el primer elemento de la lista.
2. Comparar el elemento actual con el siguiente en la lista.
3. Si el elemento actual es mayor que el siguiente, intercambiarlos.
4. Moverse al siguiente par de elementos y repetir el proceso.
5. Al final de cada "pase" por la lista, el siguiente elemento más grande se habrá "burbujeado" a su posición correcta al final de la lista.
6. Repetir el proceso para toda la lista hasta que no se realicen más intercambios en un nuevo pase.


### Casos en los que es conveniente utilizar este método de ordenación
Bubble Sort es preferible en ciertos escenarios específicos debido a sus características únicas:
- **Listas pequeñas**: Para colecciones pequeñas, Bubble Sort puede ser rápido y eficiente en términos de tiempo de ejecución.
- **Colecciones casi ordenadas**: En listas que están casi ordenadas, Bubble Sort puede terminar en muy pocas pasadas, detectando rápidamente cuando la lista está ordenada.
- **Simplicidad y enseñanza**: Es ideal para fines educativos, ofreciendo una clara ilustración de cómo funciona la ordenación y el concepto de algoritmos.
- **Limitaciones de espacio**: Al ser un algoritmo de ordenación "in place", no requiere memoria adicional más allá del espacio de almacenamiento original, lo cual es beneficioso en entornos con restricciones de memoria.
- **Necesidad de estabilidad en la ordenación**: Su naturaleza estable lo hace adecuado para casos donde se debe preservar el orden relativo de registros equivalentes.
  

### Ejemplo Conceptual

Consideremos la lista [41, 33, 17, 80, 61] y apliquemos el método Bubble Sort para ordenarla:

1. **Primer Pase**:
    - Comparar 41 y 33: 41 > 33, intercambiarlos. Lista: [33, 41, 17, 80, 61]
    - Comparar 41 y 17: 41 > 17, intercambiarlos. Lista: [33, 17, 41, 80, 61]
    - Comparar 41 y 80: 41 <= 80, no hacer nada. Lista: [33, 17, 41, 80, 61]
    - Comparar 80 y 61: 80 > 61, intercambiarlos. Lista: [33, 17, 41, 61, 80]
    - Al final del primer pase, el mayor número (80) está en su lugar correcto.

2. **Segundo Pase**:
    - Comparar 33 y 17: 33 > 17, intercambiarlos. Lista: [17, 33, 41, 61, 80]
    - Comparar 33 y 41: 33 <= 41, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Comparar 41 y 61: 41 <= 61, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Comparar 61 y 80: 61 <= 80, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Al final del segundo pase, el penúltimo número (61) está en su lugar correcto.

3. **Tercer Pase**:
    - Comparar 17 y 33: 17 <= 33, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Comparar 33 y 41: 33 <= 41, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Comparar 41 y 61: 41 <= 61, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Al final del tercer pase, el antepenúltimo número (41) está en su lugar correcto.

4. **Cuarto Pase**:
    - Comparar 17 y 33: 17 <= 33, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Comparar 33 y 41: 33 <= 41, no hacer nada. Lista: [17, 33, 41, 61, 80]
    - Al final del cuarto pase, el segundo número (33) está en su lugar correcto.

Después de estos pases, la lista está completamente ordenada: [17, 33, 41, 61, 80].


Este ejemplo muestra cómo Bubble Sort "burbujea" los elementos más grandes hacia el final de la lista paso a paso, asegurando que cada elemento se coloque en su posición correcta gradualmente.



# 5. Functools (StringOperations)

## Descripción

En este ejercicio, implementamos una clase `StringOperations` que contiene métodos para manipular cadenas de texto. Posteriormente, utilizamos `functools.partial` para crear versiones especializadas de estas funciones con parámetros preconfigurados.

## Clase StringOperations

### Métodos

- **capitalize_text(self, text)**:
  - Recibe una cadena de texto y retorna la cadena con la primera letra de cada palabra en mayúsculas.
  - Uso de ejemplo:
    ```python
    str_ops = StringOperations()
    resultado = str_ops.capitalize_text("hola mundo")
    print(resultado)  # Output: "Hola Mundo"
    ```

- **replace_substring(self, text, old, new)**:
  - Recibe una cadena de texto, una subcadena a ser reemplazada (`old`) y la nueva subcadena que la reemplazará (`new`). Retorna la cadena de texto con las sustituciones realizadas.
  - Uso de ejemplo:
    ```python
    str_ops = StringOperations()
    resultado = str_ops.replace_substring("hola mundo", "hola", "adios")
    print(resultado)  # Output: "adios mundo"
    ```

## Funciones Especializadas con functools.partial

Utilizamos `functools.partial` para crear versiones especializadas de los métodos de la clase `StringOperations`.

- **capitalize_first_word**:
  - Una versión de `capitalize_text` que solo capitaliza la primera palabra de la cadena de texto.
  - Uso de ejemplo:
    ```python
    capitalize_first_word = partial(str_ops.capitalize_first_word)
    resultado = capitalize_first_word("hola mundo")
    print(resultado)  # Output: "Hola mundo"
    ```

- **replace_spaces_with_underscore**:
  - Una versión de `replace_substring` que reemplaza todos los espacios en una cadena de texto con guiones bajos.
  - Uso de ejemplo:
    ```python
    replace_spaces_with_underscore = partial(str_ops.replace_substring, old=' ', new='_')
    resultado = replace_spaces_with_underscore("hola mundo")
    print(resultado)  # Output: "hola_mundo"
    ```
