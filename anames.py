import array as arr

currentName = ""
i = 0
aNames = []
n = 0

while currentName != "print":
    currentName = input("Name: ")
    index = 0
    firstLetter = False
    lastLetter = False
    for c in currentName:
        if index == 0 and c == "A":
            firstLetter = True
        if c == " ":
            spaceIndex = index
            primeIndex = 0
            for c in currentName:
                if primeIndex == spaceIndex - 1 and c == "a":
                    lastLetter = True
                primeIndex+=1
        index+=1
    if currentName[-1] == "a":
        lastLetter = True

    if firstLetter == True and lastLetter == True:
        aNames.append(currentName)

aNamesSize = len(aNames)
if currentName == "print":
    print("Names beginning with A and ending with a:")

    n = 0
    while n < aNamesSize:
        print(aNames[n])
        n+=1
