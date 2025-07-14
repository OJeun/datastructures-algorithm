class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = 'balloon'
        alphabets = [0] * 26
        count = len(text)

        for char in text:
            index = ord(char) - ord('a')
            alphabets[index] += 1

        number_of_l = ord('l') - ord('a')
        number_of_o = ord('o') - ord('a')

        alphabets[number_of_l] //= 2
        alphabets[number_of_o] //= 2

        for char in target:
            index = ord(char) - ord('a')
            if alphabets[index] == 0:
                return 0
            
            count = min(count, alphabets[index])

        return count
