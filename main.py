# Product class to represent individual items in the store
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category


# Currency Converter for handling multi-currency payments
class CurrencyConverter:
    conversion_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75
    }

    @staticmethod
    def convert(amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency not in CurrencyConverter.conversion_rates or to_currency not in CurrencyConverter.conversion_rates:
            raise ValueError(f"Unsupported currency conversion from {from_currency} to {to_currency}.")
        usd_amount = amount / CurrencyConverter.conversion_rates[from_currency]
        return usd_amount * CurrencyConverter.conversion_rates[to_currency]


# Discount logic for applying discounts to items in the cart
class Discount:
    @staticmethod
    def list_discounts():
        discounts = [
            "Buy 1 Get 1 Free on Fashion items",
            "10% Off on Electronics"
        ]
        return discounts

    @staticmethod
    def apply_discounts(cart):
        total_discount = 0.0

        # Buy 1 Get 1 Free on Fashion items
        for product_id, cart_item in cart.items.items():
            product = cart_item['product']
            if product.category == 'Fashion':
                free_items = cart_item['quantity'] // 2
                discount = free_items * product.price
                total_discount += discount

        # 10% Off on Electronics
        for product_id, cart_item in cart.items.items():
            product = cart_item['product']
            if product.category == 'Electronics':
                discount = 0.1 * cart_item['quantity'] * product.price
                total_discount += discount

        return total_discount


# Cart class to manage items and handle checkout
class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_from_cart(self, product_id, quantity=None):
        if product_id in self.items:
            if quantity is None or self.items[product_id]['quantity'] <= quantity:
                del self.items[product_id]
            else:
                self.items[product_id]['quantity'] -= quantity

    def view_cart(self):
        total_cost = 0
        print("Your Cart:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total_price = product.price * quantity
            total_cost += total_price
            print(f"{product.name} - Quantity: {quantity}, Price: {product.price} USD, Total: {total_price:.2f} USD")
        print(f"Total (before discounts): {total_cost:.2f} USD")
        return total_cost

    def checkout(self):
        total_before_discount = self.view_cart()
        total_discount = Discount.apply_discounts(self)
        final_total = total_before_discount - total_discount
        print(f"Applying discounts...")
        print(f"Total Discount: {total_discount:.2f} USD")
        print(f"Final Total in USD: {final_total:.2f}")
        return final_total


# Ecommerce System to manage product catalog and interaction with the cart
class EcommerceSystem:
    def __init__(self):
        self.product_catalog = {
            "P001": Product("P001", "Laptop", 1000.00, "Electronics"),
            "P002": Product("P002", "Phone", 500.00, "Electronics"),
            "P003": Product("P003", "T-Shirt", 20.00, "Fashion")
        }
        self.cart = Cart()

    def list_products(self):
        print("Available Products:")
        for product in self.product_catalog.values():
            print(f"{product.product_id}: {product.name}, Price: {product.price} USD, Category: {product.category}")

    def list_discounts(self):
        discounts = Discount.list_discounts()
        print("Available Discounts:")
        for idx, discount in enumerate(discounts, 1):
            print(f"{idx}. {discount}")

    def add_to_cart(self, product_id, quantity):
        if product_id in self.product_catalog:
            product = self.product_catalog[product_id]
            self.cart.add_to_cart(product, quantity)
            print(f"Added {quantity} x {product.name} to your cart.")
        else:
            print(f"Product with ID {product_id} not found.")

    def remove_from_cart(self, product_id, quantity=None):
        self.cart.remove_from_cart(product_id, quantity)
        print(f"Removed item {product_id} from your cart.")

    def view_cart(self):
        self.cart.view_cart()

    def checkout(self):
        final_total = self.cart.checkout()
        response = input("Would you like to view it in a different currency? (yes/no): ")
        if response.lower() == 'yes':
            print("Available Currencies: EUR, GBP")
            currency = input("Enter currency: ").upper()
            if currency in CurrencyConverter.conversion_rates:
                converted_total = CurrencyConverter.convert(final_total, 'USD', currency)
                print(f"Final Total in {currency}: {converted_total:.2f}")
            else:
                print("Unsupported currency.")


# Command-line interaction (driver code)
def main():
    system = EcommerceSystem()

    while True:
        print("\nCommands: list_products, list_discounts, add_to_cart, remove_from_cart, view_cart, checkout, quit")
        command = input("> ").strip().lower()

        if command == "list_products":
            system.list_products()
        elif command == "list_discounts":
            system.list_discounts()
        elif command.startswith("add_to_cart"):
            parts = command.split()
            if len(parts) == 3:
                product_id = parts[1]
                quantity = int(parts[2])
                system.add_to_cart(product_id, quantity)
            else:
                print("Usage: add_to_cart <product_id> <quantity>")
        elif command.startswith("remove_from_cart"):
            parts = command.split()
            if len(parts) >= 2:
                product_id = parts[1]
                quantity = int(parts[2]) if len(parts) == 3 else None
                system.remove_from_cart(product_id, quantity)
            else:
                print("Usage: remove_from_cart <product_id> [quantity]")
        elif command == "view_cart":
            system.view_cart()
        elif command == "checkout":
            system.checkout()
        elif command == "quit":
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
