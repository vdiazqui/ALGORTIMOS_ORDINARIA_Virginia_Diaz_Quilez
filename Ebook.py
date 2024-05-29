from datetime import date
from Genre import GENRE  # Importamos la clase GENRE desde el archivo correspondiente
from BookFile import Book  # Importamos la clase Book desde el archivo correspondiente

class EBook(Book):
    """
    Constructor de la clase.

    El constructor de la clase EBook se usa para crear un nuevo ebook.

    Sintaxis
    ------
      ebook = EBook(id, title, author, pages, publication_date, genres, format)

    Parámetros
    ----------
      id : int
        El identificador único del ebook.
      title : str
        El título del ebook.
      author : str
        El autor del ebook.
      pages : int
        El número de páginas del ebook.
      publication_date : date
        La fecha de publicación del ebook.
      genres : list
        Los géneros del ebook.
      format : str
        El formato del archivo del ebook (ej. PDF, EPUB, MOBI).

    Retorna
    -------
      El nuevo ebook.

    Ejemplo
    -------
      ebook = EBook(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY], "EPUB")
    """

    def __init__(self, id, title, author, pages, publication_date, genres=None, format="PDF"):
        # Inicializamos las propiedades heredadas usando super()
        super().__init__(id, title, author, pages, publication_date, genres)
        
        # Validación del parámetro format y asignación del atributo
        if not isinstance(format, str):
            raise TypeError("Format must be a string.")
        if format not in ["PDF", "EPUB", "MOBI"]:
            raise ValueError("Format must be one of the following: PDF, EPUB, MOBI.")
        self._format = format

    # Getter para el formato del ebook
    def get_format(self):
        return self._format

    # Método para representar el ebook en formato de cadena legible
    def __str__(self):
        return f"{self.get_title()} de {self.get_author()} con {self.get_pages()} páginas en formato {self._format}."

def main():
    """Función principal del módulo.

    La función principal de este módulo se usa para probar la clase EBook.

    Sintaxis
    ------
      [ ] = main()

    Parámetros
    ----------
      Null .

    Retorna
    -------
      Null .

    Ejemplo
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create an EBook.")
    print("=================================================================.")
    # Crear un objeto EBook y realizar pruebas para validar su correcta creación
    ebook = EBook(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY], "EPUB")

    if ebook.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_title() == "Harry Potter":
        print("Test PASS. The parameter title has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_author() == "J.K. Rowling":
        print("Test PASS. The parameter author has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_pages() == 345:
        print("Test PASS. The parameter pages has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_publication_date() == date.today():
        print("Test PASS. The parameter publication_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_genres() == [GENRE.FANTASY]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_format() == "EPUB":
        print("Test PASS. The parameter format has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    # Crear otro objeto EBook y probar su representación en cadena legible
    ebook2 = EBook(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY], "EPUB")

    if str(ebook2) == "Harry Potter de J.K. Rowling con 345 páginas en formato EPUB.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(ebook2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(ebook2))


# Comprobar si este módulo se ejecuta solo.
if __name__ == "__main__":
    main()
