import strawberry
from app.models.user import User as UserModel
from app.database import SessionLocal

db_session = SessionLocal()


@strawberry.type
class UserType:
    id: int
    username: str
    password: str


def get_all_users(info) -> list[UserType]:
    return db_session.query(UserModel).all()


def get_user_by_id(info, id: int) -> UserType:
    return db_session.query(UserModel).get(id)


def get_user_by_username(info, username: str) -> UserType:
    return db_session.query(UserModel).filter(UserModel.username == username).first()


@strawberry.type
class Query:
    users = strawberry.field(resolver=get_all_users)
    user_get_by_id = strawberry.field(resolver=get_user_by_id)
    user_get_by_username = strawberry.field(resolver=get_user_by_username)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, username: str, password: str) -> UserType:
        user = UserModel(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        return user


schema = strawberry.Schema(query=Query, mutation=Mutation)
