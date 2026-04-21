from quart import Blueprint
from asyncio import sleep

from helpers.queue import jobQueue

test = Blueprint("test", __name__)


@jobQueue.job
async def testJob():
	print(1)
	await sleep(10)
	print(2)


@test.route("/")
async def testRoute():
	print("starting")
	testJob.enqueue()
	print("queued")
	return "job queued"
