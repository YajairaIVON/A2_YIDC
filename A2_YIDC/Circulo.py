import math

class Circulo:
  def __init__(self, centro, radio):
    self.centro = centro
    self.radio = radio
  
  def area(self):
    return math.pi * self.radio ** 2
  
  def perimetro(self):
    return 2 * math.pi * self.radio
  
  def contiene_punto(self, punto):
    return math.dist(self.centro, punto) <= self.radio
