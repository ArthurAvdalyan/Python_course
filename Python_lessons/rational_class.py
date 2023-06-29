class Rational:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for +: 'Rational' and '{type(other).__name__}'")
    
    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for -: 'Rational' and '{type(other).__name__}'")
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for *: 'Rational' and '{type(other).__name__}'")
    
    def __truediv__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for /: 'Rational' and '{type(other).__name__}'")
    
    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < self.denominator * other.numerator
        else:
            raise TypeError("Unsupported operand type for <: 'Rational' and '{type(other).__name__}'")
    
    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > self.denominator * other.numerator
        else:
            raise TypeError("Unsupported operand type for >: 'Rational' and '{type(other).__name__}'")