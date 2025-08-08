class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0

        for state in s:
            if state == "A":
                absent += 1
                late = 0
                if absent > 1:
                    return False

            elif state == "P":
                late = 0

            else:
                late += 1
                if late > 2:
                    return False
                

        return True
            




