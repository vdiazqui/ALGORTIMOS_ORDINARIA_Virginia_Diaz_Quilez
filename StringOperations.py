from functools import partial

class StringOperations:
    """
    Clase para realizar operaciones simples en cadenas de texto.
    """

    def capitalize_text(self, text):
        """
        Recibe una cadena de texto y retorna la cadena con la primera letra de cada palabra en mayúsculas.
        
        Parámetros:
        text (str): La cadena de texto a modificar.

        Retorna:
        str: La cadena con la primera letra de cada palabra en mayúsculas.
        """
        return text.title()

    def replace_substring(self, text, old, new):
        """
        Recibe una cadena de texto, una subcadena a ser reemplazada y la nueva subcadena que la reemplazará.
        Retorna la cadena de texto con las sustituciones realizadas.

        Parámetros:
        text (str): La cadena de texto original.
        old (str): La subcadena a ser reemplazada.
        new (str): La nueva subcadena que reemplazará a la subcadena antigua.

        Retorna:
        str: La cadena con las sustituciones realizadas.
        """
        return text.replace(old, new)

    def capitalize_first_word(self, text):
        """
        Capitaliza solo la primera palabra de la cadena.

        Parámetros:
        text (str): La cadena de texto a modificar.

        Retorna:
        str: La cadena con la primera palabra en mayúscula.
        """
        return text.capitalize()


# Crear una instancia de StringOperations
str_ops = StringOperations()

# Crear versiones especializadas usando functools.partial
# capitalize_first_word utilizará el método capitalize_first_word de la instancia str_ops
capitalize_first_word = partial(str_ops.capitalize_first_word)
# replace_spaces_with_underscore utilizará el método replace_substring de la instancia str_ops
# con los parámetros old=' ' y new='_'
replace_spaces_with_underscore = partial(str_ops.replace_substring, old=' ', new='_')

# Ejemplos de uso
def main():
    text = "hola mundo"
    
    # Usando capitalize_text
    print("Usando capitalize_text:")
    resultado_capitalize_text = str_ops.capitalize_text(text)
    print(f"Resultado: {resultado_capitalize_text}")  # Output: "Hola Mundo"

    # Usando replace_substring
    print("Usando replace_substring:")
    resultado_replace_substring = str_ops.replace_substring(text, "hola", "adios")
    print(f"Resultado: {resultado_replace_substring}")  # Output: "adios mundo"
    
    # Usando capitalize_first_word
    print("Usando capitalize_first_word:")
    resultado_capitalize_first_word = capitalize_first_word(text)
    print(f"Resultado: {resultado_capitalize_first_word}")  # Output: "Hola mundo"
    
    # Usando replace_spaces_with_underscore
    print("Usando replace_spaces_with_underscore:")
    resultado_replace_spaces = replace_spaces_with_underscore(text)
    print(f"Resultado: {resultado_replace_spaces}")  # Output: "hola_mundo"

if __name__ == "__main__":
    main()
