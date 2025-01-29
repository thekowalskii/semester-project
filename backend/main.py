from backend.application import App

from backend.api.routers import auth_r, pictures_r


# main entrypoint
app = App().get_app(auth_r, pictures_r)
