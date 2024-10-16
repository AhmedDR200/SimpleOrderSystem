import json

# Load products from the JSON file
def load_products():
    with open('products.json') as f:
        return json.load(f)

# Stock Management
def check_stock(product_id, quantity):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            return product['stock'] >= quantity
    return False

# Update stock
def update_stock(product_id, quantity):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            product['stock'] -= quantity
            break
    # Save updated products back to the JSON file
    with open('products.json', 'w') as f:
        json.dump(products, f)
