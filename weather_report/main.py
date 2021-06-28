from views import home
from api import weather_api
import uvicorn
import fastapi

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


configure()
if __name__ == '__main__':
    uvicorn.run(api)
