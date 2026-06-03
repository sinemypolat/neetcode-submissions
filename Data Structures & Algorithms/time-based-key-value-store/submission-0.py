class TimeMap:

    def __init__(self):
        self.records = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = {
                "timestamps": [timestamp],
                "values": [value]
                }
        else:
            self.records[key]["timestamps"].append(timestamp)
            self.records[key]["values"].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""

        timestamps = self.records[key]["timestamps"]
        values = self.records[key]["values"]

        left, right = 0, len(timestamps) - 1

        while left <= right:
            mid = (left + right) // 2

            if timestamps[mid] == timestamp:
                return values[mid]
            elif timestamps[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        # right is now the index of the largest timestamp <= timestamp 
        # if there is no valid ts
        if right >= 0:
            return values[right]

        return ""
