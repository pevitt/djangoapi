from .models import Profile, User, Role


class UserServices:

    @staticmethod
    def create_user(data):
        return User.objects.create_user(
            username=data['username'],
            email=data['email'].lower(),
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

    @staticmethod
    def create_profile(user, role):

        return Profile.objects.create(
            user=user,
            role=role
        )