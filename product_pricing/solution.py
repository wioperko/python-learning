from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Product:
    name: str
    category: str
    price: Decimal
    tax: Decimal

    # Class atributes
    TAX_MIN: Decimal = Decimal('0.0')
    TAX_MAX: Decimal = Decimal('1.0')

    # Validation of component string correctness
    def __post_init__(self):
        if not (self.TAX_MIN <= self.tax <= self.TAX_MAX):
            raise ValueError(f"Tax must be between {self.TAX_MIN} and {self.TAX_MAX}")
        if self.price < Decimal('0.0'):
            raise ValueError("Price cannot be negative")
        
    
    def final_price(self) -> Decimal:
        return self.price + (self.price * self.tax)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.category}): {self.final_price():.2f}"
    

def main():
    try:
        p1 = Product('Face cleanser', 'DRUG', Decimal('100'), Decimal('0.1'))
        print(p1)
        print(p1.final_price())
    except Exception as e:
       print(e.args[0])


if __name__ == "__main__":
    main()
