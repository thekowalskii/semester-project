from backend.application import App

from backend.api.routers import auth_r, painting_r, carts_r, perfumes_r, products_r


# main entrypoint
app = App().get_app(auth_r, carts_r, painting_r, perfumes_r, products_r)
