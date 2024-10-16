from flask_mail import Message, Mail

mail = Mail()

def send_confirmation_email(order_id, email, items, total):
    # Format the items as an HTML list
    items_list = "".join([f"<li>Product ID: {item['product_id']}, Quantity: {item['quantity']}</li>" for item in items])

    # Compose the email
    msg = Message(
        subject='[Order Confirmation] Thank you for your purchase!',
        sender='djangotest810@gmail.com',
        recipients=[email]
    )

    # HTML template for the email body
    msg.html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6;">
            <h2 style="color: #4CAF50;">Order Confirmation</h2>
            <p>Dear Customer,</p>
            <p>Thank you for your recent purchase! We are pleased to confirm your order with the following details:</p>
            <hr>
            <h3>Order Summary:</h3>
            <p><strong>Order ID:</strong> {order_id}</p>
            <ul>
                {items_list}
            </ul>
            <p><strong>Total Amount:</strong> ${total:.2f}</p>
            <hr>
            <p>We are processing your order and will notify you once it has been shipped.</p>
            <p>If you have any questions or need assistance, please contact our support team at 
               <a href="mailto:support@example.com">support@example.com</a>.</p>
            <br>
            <p>Thank you for choosing us. We look forward to serving you again.</p>
            <p style="font-size: small; color: #777;">
                <em>The Online Store Team</em>
            </p>
            <hr>
            <p style="font-size: small; color: #777;">
                If you did not make this purchase, please contact our support team immediately.
            </p>
        </body>
    </html>
    """

    # Send the email
    mail.send(msg)
