def find_highest_frequency_word_length(string):
    word_list = string.split()
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_frequency = max(word_count.values())
    highest_frequency_word = [word for word, count in word_count.items() if count == max_frequency]
    highest_frequency_word_length = len(highest_frequency_word[0])

    return highest_frequency_word_length

# Test Case 1
string1 = "write write write all the number from from from 1 to 100"
print(find_highest_frequency_word_length(string1))
# Output: 5

# Test Case 2
string2 = "hello world hello world hello"
print(find_highest_frequency_word_length(string2))
# Output: 5

# Test Case 3
string3 = "Our goal is to make education and experiential skills affordable and accessible to everyone"
print(find_highest_frequency_word_length(string3))
# Output: 2

