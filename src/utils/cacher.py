import redis
from django.core.cache import cache

class Cacher:
    cache = None
    def __init__(self) -> None:
        self.cache = redis.Redis(host='localhost', port=6379, db=0)

    async def get():
        pass
    
    async def set():
        cache.aset('my_key', 'hello, world!', 30)
        
    async def clear():
        cache.clear()