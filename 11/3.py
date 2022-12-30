class ComplexNumbers():
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def sum(self, other):
        result = ComplexNumbers()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result
    
    def subtraction(self, other):
        result = ComplexNumbers()
        result.real = self.real - other.real
        result.imaginary = self.imaginary - other.imaginary
        return result

    def multiplication(self, other):
        result = ComplexNumbers()
        result.real = self.real * other.real - self.imaginary * other.imaginary
        result.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return result

    def show(self):
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {abs(self.imaginary)}i")

