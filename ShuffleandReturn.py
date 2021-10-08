import random
def original():
    original = input()
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)

    return 3 * original


print(original())


