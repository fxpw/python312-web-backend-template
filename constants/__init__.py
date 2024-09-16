from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
import os

load_dotenv(find_dotenv())


LAUNCH_MODE = str(os.environ.get("APP_ENV"))

BACKEND_PORT = int(os.environ.get("BACKEND_PORT"))
DEBUG_PORT = int(os.environ.get("DEBUG_PORT"))

TYPE_HINT_SESSION = async_sessionmaker[AsyncSession]
