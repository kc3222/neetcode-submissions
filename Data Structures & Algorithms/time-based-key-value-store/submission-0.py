import bisect

class TimeMap:

    def __init__(self):
        self.hashMapTime = {} # {key: [times]} sorted
        self.hashMapValue = {} # {key: [values]} parallel to times

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMapTime:
            times = self.hashMapTime[key]
            vals = self.hashMapValue[key]
            idx = bisect.bisect_left(times, timestamp) # search on times
            if idx < len(times) and times[idx] == timestamp:
                vals[idx] = value # same timestamp: overwrite
            else:
                times.insert(idx, timestamp) # keep both lists aligned
                vals.insert(idx, value)
        else:
            self.hashMapTime[key] = [timestamp]
            self.hashMapValue[key] = [value]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMapTime:
            return "" # unknown key
        times = self.hashMapTime[key]
        idx = bisect.bisect_right(times, timestamp) # first time > timestamp
        if idx == 0:
            return "" # every stored time is > timestamp
        return self.hashMapValue[key][idx - 1] # largest time <= timestamp