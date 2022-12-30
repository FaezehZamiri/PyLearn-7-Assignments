class Fraction:
    def __init__(self,numerator=1,denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def sum(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result

    def subtraction(self,other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result

    def multiplication(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result

    def division(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator
        result.denominator = self.denominator * other.numerator
        return result

    def fraction2number(self):
        result = self.numerator / self.denominator
        print(result) 
    
    def simplify(self):
        num1 = self.numerator
        num2 = self.denominator
        counter = max(num1 , num2) 
        bmm = None
        while ( counter > 1):
            if ( (num1 % counter) == 0 ) and ( (num2 % counter) == 0 ):
                if bmm == None:
                    bmm = counter			
            counter -= 1
        if bmm == None:
            bmm = 1
        else:
            bmm = bmm
        
        result = Fraction()
        result.numerator = self.numerator / bmm
        result.denominator = self.denominator / bmm
        return result

    def show(self):
        print(f"{self.numerator} / {self.denominator}")


