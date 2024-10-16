from flask_mail import Message, Mail

mail = Mail()

def send_confirmation_email(order_id, email, items, total):
    # Format the items as an HTML list
    items_list = "".join([f"<li style='margin-bottom: 10px;'>Product ID: <strong>{item['product_id']}</strong>, Quantity: <strong>{item['quantity']}</strong></li>" for item in items])

    # Compose the email
    msg = Message(
        subject='[Order Confirmation] Thank You for Your Purchase!',
        sender='djangotest810@gmail.com',
        recipients=[email]
    )

    # HTML template for the email body
    msg.html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 5px; background-color: #f9f9f9;">
                <h2 style="color: #4CAF50; text-align: center;">Order Confirmation</h2>
                <p style="font-size: 16px;">Dear Customer,</p>
                <p style="font-size: 16px;">Thank you for your recent purchase! We are excited to confirm your order with the following details:</p>
                <hr style="border: 1px solid #4CAF50;">
                <h3 style="color: #4CAF50;">Order Summary:</h3>
                <p><strong>Order ID:</strong> <span style="color: #333;">{order_id}</span></p>
                <ul style="list-style-type: none; padding-left: 0;">
                    {items_list}
                </ul>
                <p style="font-weight: bold; font-size: 18px;">Total Amount: <span style="color: #4CAF50;">${total:.2f}</span></p>
                <hr style="border: 1px solid #4CAF50;">
                <p style="font-size: 16px;">We are processing your order and will notify you once it has been shipped.</p>
                <p>If you have any questions or need assistance, please contact our support team at 
                   <a href="mailto:support@example.com" style="color: #4CAF50;">support@example.com</a>.</p>
                <br>
                <p style="font-size: 16px;">Thank you for choosing us. We look forward to serving you again.</p>
                <p style="font-size: small; color: #777;">
                    <em>The Online Store Team</em>
                </p>
                <hr style="border: 1px solid #e0e0e0;">
                <p style="font-size: small; color: #777;">
                    If you did not make this purchase, please contact our support team immediately.
                </p>
            </div>
        </body>
    </html>
    """

    # Send the email
    mail.send(msg)
