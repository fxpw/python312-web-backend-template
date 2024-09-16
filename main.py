import os
import threading
import asyncio

import datetime
import logging

from constants import LAUNCH_MODE,BACKEND_PORT,DEBUG_PORT
from flask import Flask, jsonify, request
from flask_cors import CORS
from db import (
	ASYNC_SESSION,
)

from localization import L

flask_web_app = Flask(__name__)
CORS(flask_web_app)


async def StartWebApp() -> None:
	flask_web_app.db_async_session = ASYNC_SESSION().session

	def run_app() -> None:
		flask_web_app.run(
			host="0.0.0.0",
			port=BACKEND_PORT,
			debug=LAUNCH_MODE == "development",
			use_reloader=LAUNCH_MODE == "development",
		)

	run_app()


@flask_web_app.route("/api")
async def api():
	try:
		if LAUNCH_MODE == "production":
			return jsonify(
				{
					"message": "Hello from the python312-production-server!",
				}
			)
		else:
			return jsonify(
				{
					"message": "Hello from the python312-test-server!",
				}
			)
	except:
		pass


async def main():
	when_start = datetime.datetime.now()
	if not os.path.exists("./logs"):
		os.makedirs("./logs")
	logging.basicConfig(
		level=logging.INFO,
		filename=None
		if LAUNCH_MODE == "development"
		else f"./logs/{when_start}_logfile.log",
		filemode=None if LAUNCH_MODE == "development" else "a",
		format=None
		if LAUNCH_MODE == "development"
		else "%(asctime)s - %(levelname)s - %(message)s",
	)
	await StartWebApp()


if __name__ == "__main__":
	asyncio.run(main())
