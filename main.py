class circulo:
    PI=3.1416
    def __init__(self,radio):
        self.radio = radio
    def circunferencia(self):
        return 2 * self.PI * self.radio
    def area(self):
        return self.PI  *self.radio**2

if __name__ == "__main__":
    c1=circulo(10)
    print(f"La circunferencia es {c1.circunferencia()}")
    print(f"El area es {c1.area()}")