class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0

        day = 0 

        while day < len(s):
            if s[day] == "A":
                absent += 1
                if absent > 1:
                    return False
                day += 1

            elif s[day] == "P":
                day += 1

            else:
                while day < len(s) and s[day] == "L":
                    late += 1
                    day += 1

                    if late > 2:
                        return False
                
                late = 0

        return True
            




