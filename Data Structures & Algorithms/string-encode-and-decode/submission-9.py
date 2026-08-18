class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find the '#' separating length and word
            j = i

            while s[j] != "#":
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the word
            word = s[j:j + length]

            result.append(word)

            # Move to the beginning of the next encoded word
            i = j + length

        return result


