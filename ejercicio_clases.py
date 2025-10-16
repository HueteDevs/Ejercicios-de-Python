class Libro:
    # def __init__....:
    def __init__(self, titulo,autor,paginas, disponible = True):
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible
        estado = "disponible" if self.disponible else "prestado"
        
    
    # def prestar...
    def prestar(self):
    
        if self.disponible:
           self.disponible = False
           return"El libro ha sido prestado"
        else:
            return"El libro no está disponible"
    
        
    
    # def devolver...
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return"El libro ha sido devuelto"
        else:
            return"El libro ya estaba en la biblioteca"
        
    
    # def informacion...
    def informacion(self):
        estado = "DISPONIBLE" if self.disponible else "PRESTADO"
        return f"Libro: {self.titulo} \nAutor: {self.autor} \nPáginas: {self.paginas} \nDisponibilidad: {estado}"



# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    
    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")
    
    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")
    
    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()
        