from datetime import date
from Genre import GENRE  # Importamos la clase GENRE desde el archivo correspondiente

class Book:
    """
    Constructor de la clase.

    El constructor de la clase Book se usa para crear un nuevo libro.

    Sintaxis
    ------
      book = Book(id, title, author, pages, publication_date, genres)

    Parámetros
    ----------
      id : int
        El identificador único del libro.
      title : str
        El título del libro.
      author : str
        El autor del libro.
      pages : int
        El número de páginas del libro.
      publication_date : date
        La fecha de publicación del libro.
      genres : list
        Los géneros del libro.

    Retorna
    -------
      El nuevo libro.

    Ejemplo
    -------
      book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])
    """

    def __init__(self, id, title, author, pages, publication_date, genres=None):
        if not isinstance(id, int):
            raise TypeError("ID must be an integer.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(author, str):
            raise TypeError("Author must be a string.")
        if not isinstance(pages, int) or pages <= 1:
            raise ValueError("Pages must be a positive integer greater than 1.")
        if not isinstance(publication_date, date) or publication_date > date.today():
            raise ValueError("Publication date cannot be in the future.")
        if genres is not None:
            if not all(isinstance(genre, GENRE) for genre in genres):
                raise ValueError("All genres must be instances of the GENRE enum.")
            if len(genres) != len(set(genres)):
                raise ValueError("Genres must be unique.")
        else:
            genres = []

        self._id = id
        self._title = title
        self._author = author
        self._pages = pages
        self._publication_date = publication_date
        self._genres = genres

    # Getters
    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_pages(self):
        return self._pages

    def get_publication_date(self):
        return self._publication_date

    def get_genres(self):
        return self._genres

    # Setters (only if needed, here getters are sufficient)
    # If there are no setters, it is to keep the object immutable once created.

    def add_genre(self, genre):
        if genre not in self._genres:
            self._genres.append(genre)

    def __eq__(self, other):
        if isinstance(other, Book):
            return self._id == other._id
        return False

    def __str__(self):
        return f"{self._title} de {self._author} con {self._pages} páginas."

def main():
    """Función principal del módulo.

    La función principal de este módulo se usa para probar la clase Book.

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
    print("Test Case 1: Create a Book.")
    print("=================================================================.")
    book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if book.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_title() == "Harry Potter":
        print("Test PASS. The parameter title has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_author() == "J.K. Rowling":
        print("Test PASS. The parameter author has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_pages() == 345:
        print("Test PASS. The parameter pages has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_publication_date() == date.today():
        print("Test PASS. The parameter publication_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_genres() == [GENRE.FANTASY]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    book2 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if str(book2) == "Harry Potter de J.K. Rowling con 345 páginas.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(book2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(book2))


    print("=================================================================.")
    print("Test Case 3: book add_genre")
    print("=================================================================.")
    book2.add_genre(GENRE.FICTION)
    genres = book2.get_genres()
    if genres == [GENRE.FANTASY, GENRE.FICTION]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    book3 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])
    if book2 == book3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")

# Comprobar si este módulo se ejecuta solo.
if __name__ == "__main__":
    main()
