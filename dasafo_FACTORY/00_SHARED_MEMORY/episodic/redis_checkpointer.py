import redis
import os
from langgraph.checkpoint.redis import RedisSaver
from langgraph.checkpoint.memory import MemorySaver

class EpisodicMemory:
    def __init__(self):
        self.host = os.getenv("REDIS_HOST", "localhost")
        self.port = int(os.getenv("REDIS_PORT", 6379))

    def get_saver(self):
        try:
            r = redis.Redis(host=self.host, port=self.port, socket_timeout=2)
            r.ping()
            return RedisSaver(r)
        except:
            return MemorySaver()
