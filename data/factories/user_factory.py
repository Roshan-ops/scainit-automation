from faker import Faker
from domain.models.user import User

fake = Faker()

class UserFactory:

    @staticmethod
    def valid_user():
        return User(
            full_name="Roshan Pokharel",
            email=f"roshan_{fake.uuid4()}@gmail.com",
            password="Test@1234",
            phone=f"98{fake.random_number(digits=8, fix_len=True)}"
        )

    @staticmethod
    def user_with_email(email: str):
        user = UserFactory.valid_user()
        user.email = email
        return user

    @staticmethod
    def user_with_password(password: str):
        user = UserFactory.valid_user()
        user.password = password
        return user

    @staticmethod
    def user_with_phone(phone: str):
        user = UserFactory.valid_user()
        user.phone = phone
        return user
