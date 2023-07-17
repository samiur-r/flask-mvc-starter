# from services.user_service import UserService
#
# class UserController:
#     def __init__(self):
#         self.user_service = UserService()
#
#     def create_user(self, data):
#         name = data.get('name')
#         email = data.get('email')
#         if not name or not email:
#             return {"message": "Name and email are required fields"}, 400
#
#         return self.user_service.create_user(name, email), 201
#
#     def get_user(self, user_id):
#         user = self.user_service.get_user(user_id)
#         if user:
#             return user, 200
#         return {"message": "User not found"}, 404
#
#     def update_user(self, user_id, data):
#         name = data.get('name')
#         email = data.get('email')
#         if not name or not email:
#             return {"message": "Name and email are required fields"}, 400
#
#         user = self.user_service.update_user(user_id, name, email)
#         if user:
#             return user, 200
#         return {"message": "User not found"}, 404
#
#     def delete_user(self, user_id):
#         user = self.user_service.delete_user(user_id)
#         if user:
#             return {"message": "User deleted successfully"}, 200
#         return {"message": "User not found"}, 404

import sys
from flask import render_template, redirect, url_for, request, abort
from models.User import User
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
def index():
    return {"message": "User found"}, 201
def store():
    ...
def show(userId):
    ...
def update(userId):
    ...
def destroy(userId):
    ...