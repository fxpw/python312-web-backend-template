from faker import Faker
from db import ClassUsersDB
from constants import TYPE_HINT_SESSION

fake = Faker()


async def main_seed(async_session: TYPE_HINT_SESSION):
	for _ in range(10):
		await ClassUsersDB.AddEntry(
			async_session=async_session,
			username=fake.user_name(),
			first_name=fake.first_name(),
			last_name=fake.last_name(),
		)
