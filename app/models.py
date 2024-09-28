from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from app.database import Base, engine
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id_usr = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name_usr = Column(String(45), nullable=False)
    email_usr = Column(String(45), unique=True, nullable=False)

    videos = relationship("Video", back_populates="author", cascade="all, delete-orphan")
    likes_usr = relationship("Likes", back_populates="user_lk", cascade="all, delete-orphan")
    comments_usr = relationship("Comments", back_populates="user_cmt", cascade="all, delete-orphan")


class Video(Base):
    __tablename__ = 'videos'

    id_vd = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name_vd = Column(String(128), nullable=False)
    date_vd = Column(DateTime, default=datetime.utcnow, nullable=False)
    url_vd = Column(String(255), nullable=False)
    description_vd = Column(Text, nullable=True)
    id_autor_vd = Column(Integer, ForeignKey('users.id_usr', name="fk_autor_vd", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)

    author = relationship('User', back_populates="videos")
    thumbnails = relationship('Thumbnail', back_populates="video", cascade="all, delete-orphan")
    likes_vd = relationship('Likes', back_populates="video_lk", cascade="all, delete-orphan")
    comments_vd = relationship('Comments', back_populates="video_cmt", cascade="all, delete-orphan")


class Thumbnail(Base):
    __tablename__ = 'thumbnails'

    id_thn = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name_thn = Column(String(128), nullable=False)
    date_thn = Column(DateTime, default=datetime.utcnow, nullable=False)
    url_thn = Column(String(255), nullable=False)
    description_thn = Column(Text, nullable=True)
    id_video_thn = Column(Integer, ForeignKey('videos.id_vd', name="fk_video_thn", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)

    video = relationship('Video', back_populates="thumbnails")


class Likes(Base):
    __tablename__ = 'likes'

    id_lk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    num_video_lk = Column(Integer, default=0)
    id_user_lk = Column(Integer, ForeignKey('users.id_usr', name="fk_user_lk", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    id_video_lk = Column(Integer, ForeignKey('videos.id_vd', name="fk_video_lk", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)

    video_lk = relationship('Video', back_populates="likes_vd")
    user_lk = relationship('User', back_populates="likes_usr")


class Comments(Base):
    __tablename__ = 'comments'

    id_cmt = Column(Integer, primary_key=True, index=True, autoincrement=True)
    detail_cmt = Column(Text, nullable=False)
    date_cmt = Column(DateTime, default=datetime.utcnow, nullable=False)
    id_video_cmt = Column(Integer, ForeignKey('videos.id_vd', name="fk_video_cmt", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    id_user_cmt = Column(Integer, ForeignKey('users.id_usr', name="fk_user_cmt", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    id_comment_cmt = Column(Integer, nullable=True)

    video_cmt = relationship('Video', back_populates="comments_vd")
    user_cmt = relationship('User', back_populates="comments_usr")


Base.metadata.create_all(bind=engine)