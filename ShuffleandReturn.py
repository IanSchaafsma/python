import random
def shuffle_word(original):
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)

    return original


print(shuffle_word("hallo"))
print(shuffle_word("goed"))
print(shuffle_word("slecht"))

