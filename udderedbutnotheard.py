cowphabet = input()
said = input()

counter = 0
while len(said) > 0:
    for letter in cowphabet:
        if said == "":
            break
        if letter == said[0]:
            said = said[1:]
    counter += 1

print(counter)