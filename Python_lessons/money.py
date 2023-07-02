class ValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class Money:
    def __init__(self, amount=0, currency='USD'):
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        self.__amount = value
    
    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self, value):
        self.__currency = value
    
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def exchange_currency(self, new_currency):
        exchange_rates = {
            ('USD', 'AMD'): 520,  # 1 USD = 520 AMD
            ('AMD', 'USD'): 0.0019,  # 1 AMD = 0.0019 USD
            ('USD', 'EURO'): 0.85,  # 1 USD = 0.85 EURO
            ('EURO', 'USD'): 1.18,  # 1 EURO = 1.18 USD
            ('AMD', 'EURO'): 0.0016,  # 1 AMD = 0.0016 EURO
            ('EURO', 'AMD'): 625  # 1 EURO = 625 AMD
        }
        
        if (self.currency, new_currency) in exchange_rates:
            exchange_rate = exchange_rates[(self.currency, new_currency)]
            new_amount = self.amount * exchange_rate
            return Money(new_amount, new_currency)
        else:
            raise ValueError(f"Unsupported currency exchange: {self.currency} to {new_currency}")
    
    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            new_amount = self.amount + other.amount
            return Money(new_amount, self.currency)
        else:
            raise ValueError("Unsupported operand type for +: 'Money' and '{type(other).__name__}'")
    
    def __sub__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            new_amount = self.amount - other.amount
            return Money(new_amount, self.currency)
        else:
            raise ValueError("Unsupported operand type for -: 'Money' and '{type(other).__name__}'")
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            return Money(new_amount, self.currency)
        else:
            raise ValueError("Unsupported operand type for *: 'Money' and '{type(other).__name__}'")
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount / other
            return Money(new_amount, self.currency)
        else:
            raise ValueError("Unsupported operand type for /: 'Money' and '{type(other).__name__}'")
    
    def __eq__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount == other.amount
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        else:
            raise ValueError("Unsupported operand type for <: 'Money' and '{type(other).__name__}'")
    
    def __gt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount > other.amount
        else:
            raise ValueError("Unsupported operand type for >: 'Money' and '{type(other).__name__}'")
        
        
money = Money(100, 'USD')
print(money)  # Output: 100 USD

new_money = money.exchange_currency('AMD')
print(new_money)  # Output: 52000 AMD