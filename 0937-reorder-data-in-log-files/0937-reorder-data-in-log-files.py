class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digit_logs = []
        letter_logs = []

        # sort logs into digit or letter logs lits
        for log in logs:
            identifier, rest = log.split(" ", 1)

            if rest[0].isdigit():
                digit_logs.append(log)

            else:
                letter_logs.append((rest, log))
            
        letter_logs.sort()

        for i in range(len(letter_logs)):
            log = letter_logs[i]
            rest, full = log
            letter_logs[i] = full

        return letter_logs + digit_logs