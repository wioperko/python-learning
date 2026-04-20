from dataclasses import dataclass, field
from decimal import Decimal
from typing import ClassVar, override
from collections import defaultdict



@dataclass
class Product:
    name: str
    category: str
    price: Decimal
    tax: Decimal

    # Class atributes
    TAX_MIN: ClassVar[Decimal] = Decimal('0.0')
    TAX_MAX: ClassVar[Decimal] = Decimal('1.0')

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
    
@dataclass
class ExtraProduct(Product):
    discount_days:set[int] = field(default_factory=set)
    discount: Decimal = Decimal('0.0')
    _current_day: int = field(init=False, default=0)


    DISCOUNT_MIN: ClassVar[Decimal] = Decimal('0.0')
    DISCOUNT_MAX: ClassVar[Decimal] = Decimal('1.0')
    DAY_MIN: ClassVar[int] = 0
    DAY_MAX: ClassVar[int] = 6

    def __post_init__(self):
        super().__post_init__()
        if not (ExtraProduct.DISCOUNT_MIN <= self.discount <= ExtraProduct.DISCOUNT_MAX):
            raise ValueError(f"Discount must be between {self.DISCOUNT_MIN} and {self.DISCOUNT_MAX}")
        if not(all(self.DAY_MIN <= day <= self.DAY_MAX for day in self.discount_days)):
            raise ValueError(f"Days must be between {ExtraProduct.DAY_MIN} and {ExtraProduct.DAY_MAX}")
   
    def set_current_day(self, day: int) -> None:
        if not(ExtraProduct.DAY_MIN <= day <= ExtraProduct.DAY_MAX):
            raise ValueError(f"Day must be between {ExtraProduct.DAY_MIN} and {ExtraProduct.DAY_MAX}")
        self._current_day = day

    @override
    def final_price(self) -> Decimal:
        if self._current_day in self.discount_days:
            return super().final_price() * (Decimal('1.0') - self.discount)
        return super().final_price()
    
    def __str__(self) -> str:
        return f"Extra product (name:{self.name}, category:{self.category}, price: {self.price}, tax: {self.tax}," \
            f"discount: {self.discount}, discount days: {self.discount_days})"


class ProductService:

    def __init__(self):
        self.products_by_day = defaultdict(list[Product])

    def add_product(self, product: Product, day: int) -> None:
        if not (0 <= day <= 6):
            raise ValueError("Day must be between 0 and 6")
        self.products_by_day[day].append(product)

    def calc_total_price(self) -> Decimal:
        total_price = Decimal('0.0')
        for day, products in self.products_by_day.items():
            for product in products:
                    if isinstance(product, ExtraProduct):
                        product.set_current_day(day)
                    total_price += product.final_price()
        return total_price
    
    def __str__(self) -> str:
        lines = ["Products:"]
        for day, products in sorted(self.products_by_day.items()):
            lines.append(f"Day {day}:")
            for p in products:
                lines.append(f"  - {p}")
        return "\n".join(lines)


def main():
    try:

        p1 = Product('PA1', 'A', Decimal('100'), Decimal('0.0'))
        p2 = Product('PA2', 'A', Decimal('100'), Decimal('0.0'))
        ep1 = ExtraProduct('PB1', 'B', Decimal('100'), Decimal('0.1'), {0, 1}, Decimal('0.05'))
        ep2 = ExtraProduct('PB2', 'B', Decimal('100'), Decimal('0.1'), {2, 3}, Decimal('0.05'))

        productservice = ProductService()
        productservice.add_product(p1, 0)
        productservice.add_product(p2, 0)
        productservice.add_product(ep1, 1)
        productservice.add_product(ep2, 1)
        print(productservice)
        print(productservice.calc_total_price())
     
    except Exception as e:
       print(e.args[0])


if __name__ == "__main__":
    main()
