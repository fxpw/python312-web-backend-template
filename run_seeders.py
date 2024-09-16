import os
import importlib
import asyncio

# Функция для запуска сидеров
async def run_seeders():
	from db import ASYNC_SESSION

	async_session = ASYNC_SESSION(True)
	session = async_session.session

	# Получите список файлов в папке seeders
	seeders_folder = "seeders"
	for filename in os.listdir(seeders_folder):
		if filename.endswith("_seeder.py"):
			# Импортируйте модуль из папки seeders
			module_name = filename[:-3]  # Убираем '.py'
			module = importlib.import_module(f"{seeders_folder}.{module_name}")

			# Проверяем наличие функции сидера и вызываем её
			if hasattr(module, "main_seed"):
				await module.main_seed(session)
				print(f"Сидеры из {filename} выполнены.")
			else:
				print(f"В {filename} не найдено функции 'main_seed'.")

if __name__ == "__main__":
    asyncio.run(run_seeders())
