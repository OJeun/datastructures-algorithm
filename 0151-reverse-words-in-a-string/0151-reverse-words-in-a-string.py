class Solution:
    def reverseWords(self, s: str) -> str:
        trimmed_s = " ".join(s.split())
        string_list = list(trimmed_s)
        self.reverseString(string_list, 0, len(string_list) - 1)
        start = 0
        end = 0

        while end < len(string_list):
            if string_list[end] == " ":
                self.reverseString(string_list, start, end - 1)
                start = end + 1

            if end == len(string_list) - 1:
                self.reverseString(string_list, start, end)
            end += 1
        
        return "".join(string_list)

    def reverseString(self, s_list:list, start:int, end:int):
        while start < end:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
    


        
