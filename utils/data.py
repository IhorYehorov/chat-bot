from aiogram.types import User

from models import User as UserModel, db


class DBInterface:
    @staticmethod
    def get_user_by_id(user_id: int) -> UserModel:
        return UserModel.query.filter_by(user_id=user_id).first()

    @staticmethod
    def create_user(user: User) -> UserModel:
        new_user = UserModel(
            user_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            mention=user.mention,
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
