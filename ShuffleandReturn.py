import random
while True:
    print("typ 3x een woord")
    original = input()
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)

    original = input()
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)

    original = input()
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)
    break 