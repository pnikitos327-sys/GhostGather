import random
import time
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
]
class Rotator:
    def __init__(self):
        self.stealth = False
        self.min_delay = 1
        self.max_delay = 3
    def get_headers(self):
        return {'User-Agent': random.choice(USER_AGENTS)}
    def wait(self):
        if self.stealth:
            time.sleep(random.uniform(self.min_delay, self.max_delay))
rotator = Rotator()
