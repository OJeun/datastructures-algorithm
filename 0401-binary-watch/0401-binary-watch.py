from collections import defaultdict 
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        hour = [8,4,2,1]
        minute = [32,16,8,4,2,1]

        # key: count, value: string hours
        hour_bit_count = defaultdict(list) 
        # key: count, value: string minutes
        minute_bit_count = defaultdict(list) 
        result = []
        
        for hour in range(0, 12):
            count = bin(hour).count("1")
            hour_bit_count[count].append(str(hour))

        for minute in range(0, 60):
            count = bin(minute).count("1")
            if 0 <= minute < 10:
                minute = "0" + str(minute)
            minute_bit_count[count].append(str(minute))

        # h_bit=(0,1,2,3) m_bit=(3,2,1,0)
        for h_bit in range(max(0, turnedOn-6), min(4, turnedOn) + 1):
            m_bit = turnedOn - h_bit

            hours = hour_bit_count[h_bit]
            minutes = minute_bit_count[m_bit]

            for h in hours:
                for m in minutes:
                    time = h + ":" + m
                    result.append(time)
        
        return result