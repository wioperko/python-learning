import argparse
import json
import sys
from decimal import Decimal
from solution import Product, ExtraProduct, ProductService

def parse_args():
    parser = argparse.ArgumentParser(description="Product Service CLI Runner")
    parser.add_argument(
        'file', 
        type=str, 
        help="Path to the JSON file containing product data"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    service = ProductService()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for entry in data:
            # Basic data extraction
            name = entry['name']
            category = entry['category']
            price = Decimal(str(entry['price']))
            tax = Decimal(str(entry['tax']))
            day = int(entry['day'])

            # Determine product type
            if 'discount' in entry:
                product = ExtraProduct(
                    name=name,
                    category=category,
                    price=price,
                    tax=tax,
                    discount=Decimal(str(entry['discount'])),
                    discount_days=set(entry['discount_days'])
                )
            else:
                product = Product(name, category, price, tax)

            service.add_product(product, day)

        # Output the results
        print("\n" + "="*40)
        print(service)
        print("="*40)
        print(f"TOTAL REVENUE: {service.calc_total_price()}")
        print("="*40)

    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check your file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()