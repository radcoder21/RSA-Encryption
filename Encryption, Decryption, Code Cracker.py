def setKey():
    key = []
    new_key = ('z', 'a', 'q', 'w', 's', 'x', 'e', 'd', 'c', 'v', 'f', 'r', 't', 'g', 'b', 'n', 'h', 'y', 'u', 'j', 'm', 'k', 'i', 'o', 'l', 'p')   
    try_key = input("\nEnter a list of the alphabet.\n\nBe careful because if your key isn't composed of 26 different\nletters, a new key will be provided for you.\n\nNow enter your new key: ")
    if (set(try_key) == set(new_key)):
        new_key = try_key
        print("\nYour new key is:","\n",new_key[:13],"\n",new_key[13:26])
    else:
        print("\nYou were given the default key because the key provided is invalid.")
        print("\nYour new key is:","\n",new_key[:13],"\n",new_key[13:26])
    dic_key = []
    opp_key = []
    for i in range(97,123):
        key.append(chr(i))
    for i in range(26):
        dic_key.append((key[i], new_key[i]))
    for i in range(26):
        opp_key.append((new_key[i], key[i]))
        
    return dict(dic_key), dict(opp_key)

def fileInput():
    option = 'go'
    while option != 'enc' or option != 'dec' or option != 'cdc':
        try:
            old = input('\nEnter the name of the file you would like to process: ')
            in_file = open(old+'.txt','r')
            new = input('\nEnter a name for your new file (Careful, if a file already\nexist with the name you enter, the file will be altered,\notherwise a newfile will be created with the name you provide .txt): ')
            out_file = newfile = open(new+'.txt','w')
            option = input("\nEnter 'enc' for the encrypter, 'dec' for the decrypter, or 'cdc' for the code cracker:  ")
            in_file.close()
            return out_file, option, old
        except:
            print('\nWe are unable to open this file, please input the name of an existing text file.')
    

def fileReader(file1, fileout, option, keyy, oppkey, low):
    file = open(file1+'.txt', 'r')
    if option == 'enc':
        for line in file:
            for i in range(len(line)):
                old_letter = line[i]
                new_letter = encrypter(old_letter,keyy)
                print(new_letter, file=fileout, end="")
    elif option == 'dec':
        for line in file:
            for i in range(len(line)):
                old_letter = line[i]
                new_letter = decrypter(old_letter,oppkey)
                print(new_letter, file=fileout, end="")
    else:
        for line in file:
            for i in range(len(line)):
                old_letter = line[i]
                new_letter = codeCracker(old_letter, low)
                print(new_letter, file=fileout, end="")
    fileout.close()
        
 
def encrypter(letter,key_):
    letter = key_.get(letter, letter)
    return letter
 
def decrypter(letter, newkey):
    letter = newkey.get(letter, letter)
    return letter
 
def codeCracker(letter,fun1):
    if letter in fun1:
        letter = fun1.get(letter, letter)
        return letter
    else:
        return letter

def kerator():
    key = []
    for i in range(97,123):
        key.append(chr(i))
    return key

def freqFinder(kerfunc, file_name):
    file = open(file_name+'.txt',"r")
    lowercase = kerfunc
    expfreqlis = 'etnaosirdhlmucygfwpvbkxjqz'
    tryfreqlis = input("\nEnter a frequency list of the english alphabet.\n\nBe careful because if your list isn't composed of 26 different\nletters, a new list will be provided for you.\n\nNow enter your frequency list: ")
    if (set(tryfreqlis) == set(expfreqlis)):
        expfreqlis = tryfreqlis
        print("\nYour new frequency list is:","\n",expfreqlis[:13],"\n",expfreqlis[13:26])
    else:
        print("\nYou were given the default frequency list because the one provided is invalid.")
        print("\nYour new frequency list is:","\n",expfreqlis[:13],"\n",expfreqlis[13:26])
    text = file.read()
    lowerdic = {}
    total = 0
    lowerlis1 = []
    
    for letter in lowercase:
        count = text.count(letter)
        lowerlis1.append((letter,count))
        total += count
        lowerdic[letter] = count
        
    lowerlis1.sort(key = lambda x : x[1])
    lowerlis1.reverse()

    for i in range(len(lowerlis1)):
        new = lowerlis1[i][0]
        lowerdic[new] = expfreqlis[i]

    file.close()

    
    return lowerdic

def intro():
    print('\nThis program contains an encryption/decryption serviced using\na rearrangement of the english alphabet.')
    print('\nThere is also a code cracker available for decrypting\nencrypted files using a frequency list provided by you or the program.')
        


def main():
    intro()
    program = 'open'
    key, opp_key = setKey()
    while program != "":
        new_file, options, old = fileInput()
        if options == 'cdc':
            lowdic = freqFinder(kerator(),old)
        else:
            lowdic = {}
        fileReader(old, new_file, options, key, opp_key, lowdic)
        print('\nYour file was succesfully processed!')
        program = input("\nPress Enter to Quit and lose your key,\ninput anything to continue using the program with the same key: ")
        print()

main()    
