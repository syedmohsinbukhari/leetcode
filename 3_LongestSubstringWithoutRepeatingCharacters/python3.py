class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_arr = {}
        st_pt = 0
        str_len = 0
        max_str_len = 0

        for i in range(len(s)):
            ch = s[i]

            if ch in letter_arr.keys():
                if letter_arr[ch] >= st_pt:
                    st_pt = letter_arr[ch] + 1

            if str_len > max_str_len:
                max_str_len = str_len

            str_len = i - st_pt + 1

            letter_arr[ch] = i

        if str_len > max_str_len:
            max_str_len = str_len

        return max_str_len


if __name__ == '__main__':
    sol_obj = Solution()
    test_cases = ['abcabcbb', 'a', 'abc', 'au', 'xyzxxxx', '', ' ', 'abba']
    for i in range(len(test_cases)):
        test_inp = test_cases[i]
        len_str = sol_obj.lengthOfLongestSubstring(test_inp)
        print(f"Max substring length: {len_str}")
