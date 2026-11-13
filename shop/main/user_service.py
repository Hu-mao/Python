
from main.models import User


class UserService:

    @staticmethod
    def create_user(name, email, phone, avatar=None):
        user = User(
            name=name,
            email=email,
            phone=phone
        )

        if avatar:
            user.avatar = avatar

        user.save()
        return user

    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    def delete_user(user_id):
        User.objects.filter(id=user_id).delete()
