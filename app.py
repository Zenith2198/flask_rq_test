from quart import Quart

from helpers.queue import jobQueue
from routes.test import test


def create_app():
	app = Quart(__name__)
	app.register_blueprint(test, url_prefix="/test")
	jobQueue.init_app(app)

	return app
