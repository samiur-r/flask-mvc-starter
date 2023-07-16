from services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self, name, email):
        return self.user_service.create_user(name, email)

    def get_user(self, user_id):
        return self.user_service.get_user(user_id)

    def update_user(self, user_id, name, email):
        return self.user_service.update_user(user_id, name, email)

    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)
