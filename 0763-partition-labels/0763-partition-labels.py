class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_index = [-1] * 26
        output = []
        partition = 0
        start = 0

        for position, char in enumerate(s):
            index = ord(char) - ord('a')
            char_index[index] = position

        for index, char in enumerate(s): 
            if partition == 0:
                start = index

            position = ord(char) - ord('a')
            max_index = char_index[position]

            if index <= max_index:
                partition = max(partition, max_index)

            if index == partition:
                partition_length = partition - start + 1
                output.append(partition_length)
                partition = 0

        return output

                