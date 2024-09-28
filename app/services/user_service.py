from app.models import User, Video


class UserService:
    def __init__(self, db):
        self.db = db

    async def create_user(self, user_data):
        user = User(**user_data)
        self.db.add(user)
        await self.db.commit()
        return user

    def search_by_author(self, author: str):
        return self.db.query(Video).join(Video.author).filter(User.name_usr.ilike(f"%{author}%")).all()