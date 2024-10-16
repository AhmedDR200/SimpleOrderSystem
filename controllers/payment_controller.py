from flask import Blueprint, request, jsonify
from utils.payment_processor import process_payment
from utils.sendMail import send_confirmation_email
from middlewares.orderMiddlewares import load_products, update_stock

payment_bp = Blueprint('payment_bp', __name__)

# Route to process payment for a specific order
@payment_bp.route('/payment', methods=['POST'])
def process_order_payment():
    data = request.json
    order_id = data.get('order_id')
    email = data.get('email')
    payment_method = data.get('payment_method', 'credit_card')

    product_id = data.get('product_id')
    quantity = data.get('quantity') 

    # Calculate total amount for the order
    total = load_products()[0]['price'] * quantity

    # Process payment
    payment_result = process_payment(total, payment_method)

    if payment_result['success']:
        # Update stock after successful payment
        update_stock(product_id, quantity)

        # Send confirmation email
        send_confirmation_email(order_id, email, [{"product_id": product_id, "quantity": quantity}], total)

        return jsonify({
            'message': 'Payment processed successfully.',
            'transaction_id': payment_result['transaction_id']
        }), 200

    return jsonify({'message': payment_result['message']}), 500
