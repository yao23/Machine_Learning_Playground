# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
      """
      :type intervals: List[Interval]
      :rtype: int

      https://leetcode.com/problems/meeting-rooms-ii/discuss/293855/Java%3A-2D-Array-Input-2ms.-Faster-than-100.-%40magicyuli-algorithm
      https://github.com/yao23/Java_Playground/blob/master/src/com/leetcode/www/MeetingRoomsII.java
      
      every time start a meeting, number of needed rooms has to add 1 
      
      every time end a meeting, add end index by 1

      beats 67.03%
      """
      starts = []
      ends = []
      for i in intervals:
          starts.append(i.start)
          ends.append(i.end)

      starts.sort()
      ends.sort()
      rooms = 0
      endIndex = 0
      for start in starts:
        if start < ends[endIndex]:
          rooms += 1
        else:
          endIndex += 1
      return rooms

    def minMeetingRoomsV0(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int

        every time start a meeting, number of needed rooms has to add 1 if there are no available rooms (used before)
        every time end a meeting, number of available rooms could add by 1

        beats 67.03%
        """
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()
        s = e = 0
        num_rooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    num_rooms += 1
                else:
                    available -= 1

                s += 1
            else:
                available += 1
                e += 1

        return num_rooms

# Very similar with what we do in real life. Whenever you want to start a meeting,
# you go and check if any empty room available (available > 0) and
# if so take one of them ( available -=1 ). Otherwise,
# you need to find a new room someplace else ( numRooms += 1 ).
# After you finish the meeting, the room becomes available again ( available += 1 ).
