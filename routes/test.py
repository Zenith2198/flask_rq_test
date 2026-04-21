from quart import Blueprint
from asyncio import sleep, run

from helpers.queue import jobQueue

test = Blueprint("test", __name__)


# doesn't work, but should
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


# does work, but is cumbersome (and probably shouldn't work)
async def testInnerAsync():
	print(1)
	await sleep(10)
	print(2)


@jobQueue.job
def testSync():
	run(testInnerAsync())


@test.route("/working")
async def testRouteWorking():
	print("starting")
	testSync.enqueue()
	print("queued")
	return "job queued"
