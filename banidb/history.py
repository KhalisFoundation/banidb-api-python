import pickle
from collections import OrderedDict

'''
Checks if cache.dat exists or not
If exists, self.cache = OrderedDict from the .dat file
If doesn't, new cache OrderedDict is created and then dumped in .dat
'''


class LRUCache:

    # initialising capacity
    def __init__(self, capacity: int):
        try:
            f = open('cache.dat', 'rb')
            data = pickle.load(f)
            self.cache = data[0]
            self.capacity = data[1]
        except (FileNotFoundError, EOFError):
            self.cache = OrderedDict()
            self.capacity = capacity
            f = open('cache.dat', 'wb')
            data = [self.cache, self.capacity]
            pickle.dump(data, f)
        finally:
            f.close()

    # Gives whole history since last cleared
    # And also move the key to the end
    # to show that it was recently used.
    def _get(self) -> dict:
        f = open('cache.dat', 'rb')
        data = pickle.load(f)
        self.cache = data[0]
        return self.cache

    # moves the key to the end to show that it was recently used.
    # But here we also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def _put(self, key, value) -> None:
        f = open('cache.dat', 'rb')
        data = pickle.load(f)
        self.cache = data[0]
        self.capacity = data[1]
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        f.close()
        f = open('cache.dat', 'wb')
        res = [self.cache, self.capacity]
        pickle.dump(res, f)
        f.close()


def clear():
    f = open('cache.dat', 'wb')
    f.close()
