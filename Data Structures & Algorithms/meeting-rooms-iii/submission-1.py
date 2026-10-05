class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busyRooms = [] # endTime, room
        availableRooms = [] # Room
        # Build rooms
        for i in range(n):
            heapq.heappush(availableRooms, i)
        meetings = sorted(meetings, key = lambda x: x[0], reverse=True) # Sort by start time
        counter = [0 for i in range(n)]
        
        while meetings:
            meetingStartTime, meetingEndTime = meetings.pop()
            while busyRooms and busyRooms[0][0] <= meetingStartTime:
                _, room = heapq.heappop(busyRooms)
                heapq.heappush(availableRooms, room)

            if availableRooms:
                room = heapq.heappop(availableRooms)
                heapq.heappush(busyRooms, (meetingEndTime, room))
                counter[room] += 1
            else:
                endTime, room = heapq.heappop(busyRooms)
                heapq.heappush(busyRooms, (endTime + meetingEndTime - meetingStartTime, room))
                counter[room] += 1
        return counter.index(max(counter))