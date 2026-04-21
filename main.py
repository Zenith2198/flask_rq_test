from os import getenv
from dotenv import load_dotenv

from app import create_app
from customTypes.printColors import bcolors, colorText

load_dotenv()

app = create_app()


@app.route("/")
async def serverStatus():
	return "Server is currently online"


# only run in development
if __name__ == "__main__":
	print(colorText("App is now running", bcolors.OKGREEN))
	port = getenv("PORT")
	if not port:
		raise Exception("Port missing from environment")
	app.run(host="0.0.0.0", port=int(port))
