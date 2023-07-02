class RationalError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class Rational:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator
    
    @numerator.setter
    def numerator(self, value):
        self.__numerator = value
    
    @property
    def denominator(self):
        return self.__denominator
    
    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise RationalError("Denominator cannot be zero", value)
        self.__denominator = value
    
    def __repr__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
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
            raise RationalError("Unsupported operand type for +: 'Rational' and '{type(other).__name__}'")
    
    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise RationalError("Unsupported operand type for -: 'Rational' and '{type(other).__name__}'")
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            raise RationalError("Unsupported operand type for *: 'Rational' and '{type(other).__name__}'")
    
    def __truediv__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        else:
            raise RationalError("Unsupported operand type for /: 'Rational' and '{type(other).__name__}'")
    
    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < self.denominator * other.numerator
        else:
            raise RationalError("Unsupported operand type for <: 'Rational' and '{type(other).__name__}'")
    
    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > self.denominator * other.numerator
        else:
            raise RationalError("Unsupported operand type for >: 'Rational' and '{type(other).__name__}'")