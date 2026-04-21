# Requirements:

- [Python](https://www.python.org/) (check [.python-version](/.python-version))
- [uv](https://docs.astral.sh/uv/)
- [Redis](https://redis.io/docs/latest/get-started/) or similar alternative

Alternatively, use [Docker](https://docs.docker.com/get-started/get-docker/) with the provided [build.sh](./build.sh) script

# Steps:

1. Create a [.env](./.env) file from the [.env.template](./.env.template).
2. (Optionally) Build the Docker container using the provided [build.sh](./build.sh) script and enter into it with your preferred method. I recommend the VSCode [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension. After installing the extension, open the Command Pallete with `ctrl + shift + p`, run `Dev Containers: Attach to Running Container`, and select `/flask_rq_test`. The code is located in `/flask_rq_test`.
3. Run `uv run quart rq worker` to begin the RQ worker.
4. Run `uv run bash scripts/dev.sh` to begin running the server on the port specified in your [.env](./.env)

The last two steps will be automated in the actual project, but I haven't done that yet and it's also important to see the output for this test case.

# Reproduce issue

1. Ping the server at `/test` to trigger the test route.
2. Observe in the output for the server that the request was received.
3. Observe in the output for the RQ worker that the job was queued, however no output was printed, and the job immediately returned the Coroutine instead of executing the Coroutine.
4. (Optional) Ping the server at `/test/working` to see what should happen.

# Important files
- [main.py](main.py) - Entry point
- [test.py](routes/test.py) - Route for testing
- [app.py](app.py) - App factory
- [queue.py](helpers/queue.py) - RQ initialization