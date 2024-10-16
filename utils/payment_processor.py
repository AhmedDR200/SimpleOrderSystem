import uuid

def process_payment(amount, payment_method="credit_card"):
    # Validate payment method
    if payment_method not in ["credit_card", "paypal"]:
        return {"success": False, "message": "Unsupported payment method."}

    # Simulate payment processing
    payment_success = True
    transaction_id = str(uuid.uuid4()) 

    if payment_success:
        return {"success": True, "transaction_id": transaction_id}
    else:
        return {"success": False, "message": "Payment processing failed."}
