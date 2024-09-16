import os

from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey, select, update, func, and_, delete, or_
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from constants import TYPE_HINT_SESSION, LAUNCH_MODE

Base = declarative_base()


class ClassUsersDB(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
	username: Mapped[str] = mapped_column(nullable=True)
	firstname: Mapped[str] = mapped_column(nullable=True)
	middlename: Mapped[str] = mapped_column(nullable=True)
	lastname: Mapped[str] = mapped_column(nullable=True)
	balance: Mapped[float] = mapped_column(nullable=False, default=0)

	async def AddEntry(
		async_session: TYPE_HINT_SESSION,
		username: str,
		first_name: str,
		last_name: str,
	):
		async with async_session() as session:
			user_entry = ClassUsersDB(
				username=username,
				firstname=first_name,
				lastname=last_name,
			)
			session.add(user_entry)
			await session.commit()
			return user_entry


class ASYNC_SESSION:
	__is_init = False
	session = None

	def __init__(self,for_migarte=False) -> None:
		if self.__is_init is False:
			self.__is_init = True
			engine = create_async_engine(
				url=str(os.environ.get("DATABASE_URL" if not for_migarte else "DATABASE_URL_FOR_MIGRATIONS")), echo=False
			)
			async_session = async_sessionmaker(engine, expire_on_commit=False)
			self.session: TYPE_HINT_SESSION = async_session
