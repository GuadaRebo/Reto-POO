from figuras import Rectangulo, Circulo, probar_figura


def main():
    while True:
        menu = """
         AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
         1-Rectangulo
         2-Circulo
         3-Salir
         Ingrese una Opcion: """
        opcion = input(menu)
        if opcion == "1":
            base = float(input("Ingrese base:"))
            altura = float(input("Ingrese altura:"))
            rectangulo = Rectangulo(base, altura)
            probar_figura(rectangulo)
        elif opcion == "2":
            radio = float(input("Ingrese radio:"))
            circulo = Circulo(radio)
            probar_figura(circulo)
        elif opcion == "3":
            print("Cerrando sistema")    
            break
        else:
            print("Opcion incorrecta!!")
            print("Elige una opcion del menu")

if __name__ == '__main__':
    main()       
