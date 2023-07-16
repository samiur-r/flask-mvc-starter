from flask import Blueprint, jsonify, request
from controllers.user_controller import UserController

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    response, status_code = user_controller.create_user(data)
    return jsonify(response), status_code

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response, status_code = user_controller.get_user(user_id)
    return jsonify(response), status_code

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    response, status_code = user_controller.update_user(user_id, data)
    return jsonify(response), status_code

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response, status_code = user_controller.delete_user(user_id)
    return jsonify(response), status_code
