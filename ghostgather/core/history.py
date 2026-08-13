import os
from pathlib import Path
HISTORY_FILE = Path.home() / '.cache' / 'ghostgather' / 'history.txt'
class History:
    def __init__(self):
        self.history = []
        self.max_size = 100
        self._load()
    def _load(self):
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, 'r') as f:
                self.history = [line.strip() for line in f.readlines()[-self.max_size:]]
    def _save(self):
        HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(HISTORY_FILE, 'w') as f:
            f.write('\n'.join(self.history[-self.max_size:]))
    def add(self, command):
        self.history.append(command)
        self._save()
history = History()
