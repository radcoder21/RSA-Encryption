def kerator():
    key = []
    for i in range(97,123):
        key.append(chr(i))
    return key
def freqFinder(kerfunc):
    lowercase = kerfunc
    file = input('\nEnter the name of the file you would like to analyze: ')
    file_name = open(file+'.txt', 'r')
    text = file_name.read()
    lowerlis = []
    total = 0
    
    for letter in lowercase:
        count = text.count(letter)
        lowerlis.append((letter,count))
    lowerlis.sort(key = lambda x : x[1])
    lowerlis.reverse()

    for i in range(26):
        print(lowerlis[i][0], end="")
    print()
        
def main():
    stop = "go"
    while stop != "":
        print("\nThis program will take a text file as input and print\nout the frequency of the letters in this text file.")
        freqFinder(kerator())
        stop = input("\nPress Enter to Quit, input anything to continue\nusing the program: ")


main()

