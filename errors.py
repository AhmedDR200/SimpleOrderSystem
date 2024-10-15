import traceback
from flask import jsonify

# Custom error handler for 404 Not Found
def not_found(error):
    return jsonify(
        message="Resource not found",
        error=str(error),
        stack=traceback.format_exc()
    ), 404

# Custom error handler for 400 Bad Request
def bad_request(error):
    return jsonify(
        message="Bad request. Please check your input.",
        error=str(error),
        stack=traceback.format_exc()
    ), 400

# Custom error handler for 401 Unauthorized
def unauthorized(error):
    return jsonify(
        message="Unauthorized access.",
        error=str(error),
        stack=traceback.format_exc()
    ), 401

# Custom error handler for 500 Internal Server Error
def internal_error(error):
    return jsonify(
        message="An unexpected error occurred. Please try again later.",
        error=str(error),
        stack=traceback.format_exc()
    ), 500

# General error handler for all uncaught exceptions
def handle_exception(e):
    return jsonify(
        message="An unexpected error occurred: " + str(e),
        error=str(e),
        stack=traceback.format_exc()
    ), 500
