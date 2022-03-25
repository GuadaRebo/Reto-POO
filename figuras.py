from math import pi
class Figuras:

    def __init__(self, nombre):
        self.nombre = nombre
        
    def area(self):
        pass  

    def perimetro(self):
        pass
      
    
class Rectangulo(Figuras):
    
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.altura * self.base
    
    def perimetro(self):
        return 2 * self.altura + 2 * self.base    

    def __str__(self):
        return f"{self.nombre} [Base: {self.base} Altura: {self.altura}]"   

class Circulo(Figuras):
    
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * pi
    
    def perimetro(self):
        return 2 * self.radio * pi    

    def __str__(self):
        return f"{self.nombre} [Radio: {self.radio}]"     

def probar_figura(figuras):
    print(figuras)
    print("Area:", figuras.area())
    print("Perimetro:", figuras.perimetro())   
