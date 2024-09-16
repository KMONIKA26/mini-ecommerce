# Mini E-commerce Cart System

A command-line-based mini e-commerce cart system that allows users to view products, add or remove items from the cart, apply discounts, and checkout with multi-currency support.

## Features

- **Product Catalog**: View a list of available products with their prices and categories.
- **Add/Remove from Cart**: Add products to your cart and remove them if needed.
- **View Cart**: View all the items in your cart, along with the total cost.
- **Discounts**: Discounts are applied automatically during checkout.
  - Buy 1 Get 1 Free on Fashion items.
  - 10% off on Electronics.
- **Multi-Currency Support**: Convert the final checkout total to different currencies (USD, EUR, GBP) after applying discounts.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure Python 3 is installed on your machine.

### Running the Application

1. Clone or download the repository.

   ```bash
   git clone https://github.com/KMONIKA26/mini-ecommerce.git
   ```

2. Navigate to the project directory.

   ```bash
   cd mini-ecommerce
   ```

3. Run the `main.py` script.

   ```bash
   python main.py
   ```

### Commands

- **`list_products`**: View the list of available products.
- **`list_discounts`**: View current available discounts.
- **`add_to_cart <product_id> <quantity>`**: Add products to your cart.
  - Example: `add_to_cart P001 2` (adds 2 units of Laptop to the cart).
- **`remove_from_cart <product_id> [quantity]`**: Remove products from your cart.
  - Example: `remove_from_cart P001` (removes all units of Laptop from the cart).
  - Example: `remove_from_cart P001 1` (removes 1 unit of Laptop from the cart).
- **`view_cart`**: View the current contents of your cart.
- **`checkout`**: Calculate total cost and apply discounts. You can also choose to view the total in a different currency (USD, EUR, GBP).
- **`quit`**: Exit the application.

### Example Usage

1. **List Products**:
   ```
   > list_products
   Available Products:
   P001: Laptop, Price: 1000.0 USD, Category: Electronics
   P002: Phone, Price: 500.0 USD, Category: Electronics
   P003: T-Shirt, Price: 20.0 USD, Category: Fashion
   ```

2. **Add to Cart**:
   ```
   > add_to_cart P001 1
   Added 1 x Laptop to your cart.
   ```

3. **View Cart**:
   ```
   > view_cart
   Your Cart:
   Laptop - Quantity: 1, Price: 1000.0 USD, Total: 1000.00 USD
   Total (before discounts): 1000.00 USD
   ```

4. **Checkout**:
   ```
   > checkout
   Applying discounts...
   Total Discount: 0.00 USD
   Final Total in USD: 1000.00
   Would you like to view it in a different currency? (yes/no): yes
   Available Currencies: EUR, GBP
   Enter currency: EUR
   Final Total in EUR: 850.00
   ```

### Discount Details

- **Buy 1 Get 1 Free**: Applies to items in the "Fashion" category.
- **10% Off**: Applies to items in the "Electronics" category.

### Currency Conversion

Supported currencies:
- **USD** (Default)
- **EUR** (Euro)
- **GBP** (British Pound)

### Extending the Application

- **Adding New Products**: You can add more products to the `product_catalog` in the `EcommerceSystem` class.
- **Additional Discounts**: Extend the `Discount` class to include new discount rules.
- **More Currencies**: Add more currency conversion rates in the `CurrencyConverter` class.

---

## License

This project is licensed under the MIT License. Feel free to use and modify the project as needed.

---

## Contact

For any inquiries or feedback, please reach out to [raomonika343@gmail.com].
