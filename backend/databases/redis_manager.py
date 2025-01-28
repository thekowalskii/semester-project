import redis


class RedisManager:
    '''
    This is `Redis` database manager. Here you can see different classes those are used in this project to `initialize`,
    `connect`, `close` database and get `database session`.
    '''

    def __init__(self):
        self._engine: redis.Redis | None = None


    def init(self):
        self._engine = redis.from_url('redis://localhost')


    def add_photo(self, title, photo):
        self._engine.set(title, photo)

        photo_id = self._engine.get(title)

        print()

    def get_photo(self, title):
        photo: bytes = self._engine.get(title)

        return photo
    
    def clear_all(self):
        'CLEAR'

        self._engine.flushdb(asynchronous=False)

redis_manager = RedisManager()
