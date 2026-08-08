import os

from dotenv import load_dotenv
from flask import Flask, jsonify


app_env = os.getenv("APP_ENV", "dev")

env_file = f".env.{app_env}"
load_dotenv(env_file)


app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(
        {
            "message": "Hello World!",
            "status": "ok",
            "version": "1.0.0",
            "environment": app_env,
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "environment": app_env,
        }
    )


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "5000"))
    debug = os.getenv("APP_DEBUG", "false").lower() == "true"

    app.run(
        host=host,
        port=port,
        debug=debug,
    )