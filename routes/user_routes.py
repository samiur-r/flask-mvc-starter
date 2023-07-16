from flask import Blueprint, jsonify, request
from controllers.user_controller import UserController

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"message": "Name and email are required fields"}), 400

    user = user_controller.create_user(name, email)
    return jsonify(user), 201

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_controller.get_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"message": "Name and email are required fields"}), 400

    user = user_controller.update_user(user_id, name, email)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_controller.delete_user(user_id)
    if user:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404
