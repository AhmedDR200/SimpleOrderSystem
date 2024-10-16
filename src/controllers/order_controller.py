import uuid
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..middlewares.orderMiddlewares import check_stock, load_products, update_stock

order_bp = Blueprint('order_bp', __name__)

# Route to place an order
@order_bp.route('/order', methods=['POST'])
@jwt_required()
def place_order():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Load products to get the price
    products = load_products()

    # Check if the product exists and if there is sufficient stock
    if not check_stock(product_id, quantity):
        return jsonify({'message': 'The Product is out of Stock!'}), 400

    # Find the product in the loaded products
    product = next((product for product in products if product['id'] == product_id), None)

    if not product:
        return jsonify({'message': 'Product not found!'}), 404

    # Calculate total amount
    total = product['price'] * quantity

    # Generate a dynamic order ID
    order_id = str(uuid.uuid4())

    # Update stock after placing the order
    update_stock(product_id, quantity)

    return jsonify({
        'message': 'Order placed successfully. Please proceed to payment.',
        'order_id': order_id,
        'product_id': product_id,
        'quantity': quantity,
        'total': total
    }), 201
