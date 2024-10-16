import traceback
from flask import jsonify

class ErrorHandlers:
    @staticmethod
    def not_found(error):
        return jsonify(
            message="Resource not found",
            error=str(error),
            stack=traceback.format_exc()
        ), 404

    @staticmethod
    def bad_request(error):
        return jsonify(
            message="Bad request. Please check your input.",
            error=str(error),
            stack=traceback.format_exc()
        ), 400

    @staticmethod
    def unauthorized(error):
        return jsonify(
            message="Unauthorized access.",
            error=str(error),
            stack=traceback.format_exc()
        ), 401

    @staticmethod
    def internal_error(error):
        return jsonify(
            message="An unexpected error occurred. Please try again later.",
            error=str(error),
            stack=traceback.format_exc()
        ), 500

    @staticmethod
    def handle_exception(e):
        return jsonify(
            message="An unexpected error occurred: " + str(e),
            error=str(e),
            stack=traceback.format_exc()
        ), 500
