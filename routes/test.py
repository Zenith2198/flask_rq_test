from quart import Blueprint
from asyncio import sleep

from helpers.queue import jobQueue

test = Blueprint("test", __name__)


# doesn't work
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


# does work
async def testJobWorking():
	print(1)
	await sleep(10)
	print(2)


@test.route("/working")
async def testRouteWorking():
	print("starting")
	jobQueue.queue.enqueue(testJobWorking)
	print("queued")
	return "job queued"
