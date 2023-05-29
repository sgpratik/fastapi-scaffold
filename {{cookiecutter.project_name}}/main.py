from app import create_app
from uvicorn import run

fastapi_app = create_app()

if __name__ == '__main__':
    run("main:fastapi_app", debug=True, reload=True)
