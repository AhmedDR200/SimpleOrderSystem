![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=ffffff)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=ffffff)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=ffffff)
![JWT](https://img.shields.io/badge/JWT-black?style=flat-square&logo=jsonwebtokens)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=ffffff)

# Order Processing System API

This project is an Order Processing System built with Flask, using MongoDB Atlas for data storage, Flask-JWT-Extended for authentication, and Flask-Mail for sending order confirmation emails. The application is designed to manage stock, process payments.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [Live Demo](#live-demo)
- [Postman Documentation](#postman-documentation)
- [Docker Image](#docker-image)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- User authentication with JWT
- MongoDB for data management
- Payment processing integration (mock payment gateway)
- Sending order confirmation emails
- Dynamic `transaction_id` and `order_id` generation
- Error handling middleware
- Swagger documentation for the API

## Technologies
- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-PyMongo
- Flask-Mail
- MongoDB Atlas
- Docker
- dotenv (for environment variables)
- Logging

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AhmedDR200/SimpleOrderSystem
   cd your-repo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root directory and add the following variables:
   ```env
   FLASK_APP=your_app
   FLASK_ENV=your_env
   MONGODB_URI=your_mongodb_uri
   JWT_SECRET_KEY=your_jwt_secret_key
   MAIL_SERVER=your_mail_server
   MAIL_PORT=your_mail_port
   MAIL_USE_TLS=true_or_false
   MAIL_USERNAME=your_email_username
   MAIL_PASSWORD=your_email_password
   ```

5. **Run the application:**
   ```bash
   python src/app.py
   ```

## Usage
- After running the application, navigate to `http://localhost:5000/` to see the welcome message.
- Use tools like Postman or Curl to interact with the API endpoints.

## API Endpoints
### Authentication
- `POST /signup` - Create a new user
- `POST /login` - User login

### Orders
- `POST /order` - Place the Order

### Payments
- `POST /payment` - Process a payment for an order

## Error Handling
This application implements custom error handling for various HTTP errors. The following error handlers are registered:
- 404 Not Found
- 400 Bad Request
- 401 Unauthorized
- 500 Internal Server Error

## Logging
The application uses logging to keep track of important events and errors. Logs are saved to `app.log` and also output to the console.

## Live Demo
You can access a live demo of the API at: [Live Demo Link](https://simpleordersystem-production.up.railway.app)

## Postman Documentation
The Postman documentation for the API can be found here: [Postman Documentation Link](https://documenter.getpostman.com/view/28938696/2sAXxV5pyg)

## Docker Image
You can find the Docker image for this project on Docker Hub: [Docker Hub Image Link](https://hub.docker.com/r/ahmedmagdy007/flask-app)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please submit a pull request for any enhancements or bug fixes.

## Contact
For any inquiries, feedback, or collaboration opportunities, please feel free to reach out via email at [alshwwhy212@example.com](mailto:alshwwhy212@example.com). I look forward to connecting with you!
