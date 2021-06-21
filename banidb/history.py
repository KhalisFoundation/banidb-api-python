import os
import pickle
from collections import OrderedDict

'''
Checks if cache.dat exists or not
If exists, self.cache = OrderedDict from the .dat file
If doesn't, new cache OrderedDict is created and then dumped in .dat
'''


class LRUCache:

    # initialising capacity
    def __init__(self, target, capacity: int = 25):
        self.empty = False  # check for empty or non-existing file
        self.target = target
        if os.path.exists(target):
            if os.path.getsize(target) > 0:
                with open(target, "rb") as f:
                    data = pickle.load(f)
                    self.cache = data[0]
                    self.capacity = data[1]
            else:
                self.empty = True
        else:
            self.empty = True
        if self.empty:
            self.cache = OrderedDict()
            self.capacity = capacity
            with open(target, 'wb') as f:
                data = [self.cache, self.capacity]
                pickle.dump(data, f)

    # Gives whole history since last cleared
    # And also move the key to the end
    # to show that it was recently used.
    def get(self) -> dict:
        if os.path.getsize(self.target) > 0:
            with open(self.target, "rb") as f:
                data = pickle.load(f)
                self.cache = data[0]
                if dict(self.cache) == {}:
                    result = {'empty': True}
                else:
                    result = dict(self.cache)
        else:
            result = {'empty': True}
        return result

    # moves the key to the end to show that it was recently used.
    # But here we also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def put(self, key, value: dict) -> None:
        if os.path.getsize(self.target) > 0:
            with open(self.target, "rb") as f:
                data = pickle.load(f)
                self.cache = data[0]
                self.capacity = data[1]
                self.cache[key] = value
                self.cache.move_to_end(key)
                if len(self.cache) > self.capacity:
                    self.cache.popitem(last=False)
        f = open(self.target, 'wb')
        res = [self.cache, self.capacity]
        pickle.dump(res, f)
        f.close()

    def check(self, key) -> list:
        if os.path.getsize(self.target) > 0:
            with open(self.target, "rb") as f:
                data = pickle.load(f)
                self.cache = data[0]
                self.capacity = data[1]
                if key in self.cache.keys():
                    return [True, self.cache[key]]
                else:
                    return [False]
        else:
            return [False]

    def clear(self):
        if os.path.getsize(self.target) > 0:
            with open(self.target, "rb") as f:
                data = pickle.load(f)
                self.cache = data[0]
                result = dict(self.cache)
        for i in result.keys():
            self.cache.popitem(i)
        f = open(self.target, 'wb')
        result = [self.cache, self.capacity]
        pickle.dump(result, f)
        f.close()
