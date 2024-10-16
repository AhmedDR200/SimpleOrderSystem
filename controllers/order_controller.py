import uuid
from flask import Blueprint, request, jsonify
from middlewares.orderMiddlewares import check_stock, update_stock, load_products
from utils.sendMail import send_confirmation_email
from utils.payment_processor import process_payment

order_bp = Blueprint('order_bp', __name__)

# Route to place an order
@order_bp.route('/order', methods=['POST'])
def place_order():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    email = data.get('email')
    payment_method = data.get('payment_method', 'credit_card') 

    if not check_stock(product_id, quantity):
        return jsonify({'message': 'The Product is out of Stock !'}), 400

    # Generate a dynamic order ID
    order_id = str(uuid.uuid4())

    # Calculate total
    total = load_products()[0]['price'] * quantity

    # Process payment
    payment_result = process_payment(total, payment_method)

    if payment_result['success']:
        # Update stock
        update_stock(product_id, quantity)

        # Send confirmation email
        send_confirmation_email(order_id, email, [{"product_id": product_id, "quantity": quantity}], total)

        return jsonify({
            'message': 'Order placed successfully, confirmation email sent.',
            'order_id': order_id,
            'transaction_id': payment_result['transaction_id']
        }), 201

    return jsonify({'message': payment_result['message']}), 500
