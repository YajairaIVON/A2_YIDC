class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1 # izquierda
        self.p2 = p2 # derecha
    
    # perímetro del rectángulo
    def perimetro(self):
        lado1 = abs(self.p1[0] - self.p2[0]) 
        lado2 = abs(self.p1[1] - self.p2[1]) 
        return 2 * (lado1 + lado2)
    
    # área del rectángulo
    def area(self):
        lado1 = abs(self.p1[0] - self.p2[0])
        lado2 = abs(self.p1[1] - self.p2[1])
        return lado1 * lado2
    
    # indicar si el rectángulo es un cuadrado
    def es_cuadrado(self):
        lado1 = abs(self.p1[0] - self.p2[0]) 
        lado2 = abs(self.p1[1] - self.p2[1]) 
        return lado1 == lado2
