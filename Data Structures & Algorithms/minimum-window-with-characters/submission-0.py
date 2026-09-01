class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Characters we need
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        # Characters in current window
        window = {}

        l = 0
        have = 0
        need_count = len(need)

        min_length = float("inf")
        result = ""

        for r in range(len(s)):

            # Add current character
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # Character has reached required frequency
            if char in need and window[char] == need[char]:
                have += 1

            # Current window contains everything we need
            while have == need_count:

                # Update answer
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    result = s[l:r + 1]

                # Remove left character
                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                l += 1

        return result
            
            
        