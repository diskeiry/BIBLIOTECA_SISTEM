class Biblioteca:
    #inicializar dos atributos
    def __init__(self):
        self.libros = {} #Un diccionario que almacena los libros disponibles y su estado (prestado o no).
        self.usuarios = [] #Una lista que registra los nombres de los usuarios.
        
    #Agrega un libro al diccionario libros si no existe previamente.
    #Si el libro ya existe, muestra un mensaje indicando que el libro ya está en la biblioteca.
    def agregar_libro(self, titulo):
        if titulo not in self.libros:
            self.libros[titulo] = {'disponible': True, 'usuario': None}
            print(f"Libro '{titulo}' añadido.")
        else:
            print(f"Libro '{titulo}' ya existe.")
            
  
    #Si el libro existe, muestra si está disponible o prestado.
    #Si el libro no existe, muestra un mensaje indicando que no se encontró.
    def buscar_libro(self, titulo):
        if titulo in self.libros:
            estado = "disponible" if self.libros[titulo]['disponible'] else f"prestado a {self.libros[titulo]['usuario']}"
            print(f"'{titulo}' está {estado}.")
        else:
            print(f"Libro '{titulo}' no encontrado.")
            
    
    #Si el libro no está disponible, muestra un mensaje indicando que no se puede prestar.
    #Si el libro no existe, muestra un mensaje indicando que no se encontró.
    def prestar_libro(self, titulo, usuario):
        if titulo in self.libros and self.libros[titulo]['disponible']:
            self.libros[titulo]['disponible'] = False
            self.libros[titulo]['usuario'] = usuario
            print(f"'{titulo}' prestado a {usuario}.")
        elif titulo in self.libros:
            print(f"'{titulo}' no disponible.")
        else:
            print(f"Libro '{titulo}' no encontrado.")
            
    #Si el libro ya está disponible, muestra un mensaje indicando que no se puede devolver.
    #Si el libro no existe, muestra un mensaje indicando que no se encontró.
    def devolver_libro(self, titulo):
        if titulo in self.libros and not self.libros[titulo]['disponible']:
            self.libros[titulo]['disponible'] = True
            usuario = self.libros[titulo]['usuario']
            self.libros[titulo]['usuario'] = None
            print(f"'{titulo}' devuelto por {usuario}.")
        elif titulo in self.libros:
            print(f"'{titulo}' Devolver Libro.")
        else:
            print(f"Libro '{titulo}' no encontrado.")


    #i el usuario ya está registrado, muestra un mensaje indicando que ya existe.
    def registrar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios.append(nombre)
            print(f"Usuario '{nombre}' registrado.")
        else:
            print(f"Usuario '{nombre}' ya está registrado.")

#Crea una instancia de la clase Biblioteca.
#Muestra un menú con opciones para buscar, prestar, devolver, registrar usuarios, agregar libros o salir.
#Lee la opción seleccionada por el usuario y ejecuta la función correspondiente.
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nOpciones:")
        print("1. Buscar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Registrar nuevo usuario")
        print("5. Agregar nuevo libro")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            titulo = input("Introduce el título del libro: ")
            biblioteca.buscar_libro(titulo)#Busca un libro por título y muestra su estado.
        elif opcion == '2':
            titulo = input("Introduce el título del libro: ")
            usuario = input("Introduce el nombre del usuario: ")
            if usuario in biblioteca.usuarios:
                biblioteca.prestar_libro(titulo, usuario)#Presta un libro a un usuario registrado.
            else:
                print(f"Usuario '{usuario}' no registrado.")
        elif opcion == '3':
            titulo = input("Introduce el título del libro: ")
            biblioteca.devolver_libro(titulo)#Devuelve un libro previamente prestado
        elif opcion == '4':
            nombre = input("Introduce el nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)#Registra un nuevo usuario.
        elif opcion == '5':
            titulo = input("Introduce el título del libro: ")
            biblioteca.agregar_libro(titulo)#Agrega un nuevo libro a la biblioteca.
        elif opcion == '6':
            print("Saliendo del programa...")
            break #Sale del bucle y finaliza el programa.
        else:
            print("Opción no válida.")
            
#En resumen, la función menu() proporciona una interfaz interactiva para interactuar con la biblioteca, permitiendo buscar, prestar, devolver, registrar usuarios y agregar libros.


#Ejecuta el menú cuando el script se ejecuta directamente (no cuando se importa como módulo).
if __name__ == "__main__":
    menu()