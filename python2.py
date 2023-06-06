from collections import Counter


def is_valid_string(s):
    char_count = Counter(s)
    char_frequencies = Counter(char_count.values())
    if len(char_frequencies) == 1:
        # All characters appear the same number of times
        return "YES"
    elif len(char_frequencies) == 2:
        char_frequencies = dict(char_frequencies)
        min_val = min(char_frequencies.values())
        key_list = list(char_frequencies.keys())
        val_list = list(char_frequencies.values())

        # print key with val 100
        position = val_list.index(min_val)

        if key_list[position] == 1:
            return "YES"
    return "NO"

# Test Case 1
s1 = "abc"
print(is_valid_string(s1))  # Output: YES

# Test Case 2
s2 = "abcc"
print(is_valid_string(s2))  # Output: NO

# Test Case 3
s3 = "aabbcc"
print(is_valid_string(s3))  # Output: YES

# Test Case 4
s4 = "aabbccd"
print(is_valid_string(s4))  # Output: YES

