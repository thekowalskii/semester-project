from backend.application import App

from backend.api.routers import pictures_r, auth_r


# main entrypoint
app = App().get_app(pictures_r, auth_r)
