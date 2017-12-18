def fileInputs():
    try:
        fileread = input("\nPlease enter the name of the file\nyou wish to read for decryption(no .txt): ")
        file1 = open(fileread+".txt","r")
    except:
        print("\nYour file won't open, please try agin...")
    filewrite = input("\nPlease enter the name of the file\nyou wish to create/change for decryption(no .txt): ")
    file2 = open(filewrite+".txt","w")
    return file1, file2

def dec(n,d,rdic,file1,file2):
    text1 = file1.read()
    text = text1.split()
    for letter in text:
        l1 = int(letter)
        l = int(decFunc(l1,n,d))
        letter = rdic[str(l)]
        print(letter,file=file2,end="")
    file2.close()

def decFunc(v,n,d):
        y = v**int(d)%n
        return y

def dictCreate():
    lis = list(range(1,27))
    lower = []
    dic = {}
    rdic = {}
    dic[" "] = 27
    dic["\n"] = 28
    rdic['27'] = " "
    rdic['28'] = "\n"
    for i in range(97,123):
        lower.append(chr(i))
    for i in range(26):
        dic[lower[i]] = lis[i]
        rdic[str(lis[i])] = lower[i]

    return dic , rdic

def main():
    dic, rdic = dictCreate()
    print("Welcome to our private decrypter where authorized personal can\nproperly decrypt a text file using the correct private key.")
    go = 'go'
    while go != "":
        try:
            n,d = eval(input("\nPlease enter the private key seperated by a comma: "))
            go = input('\nPress enter if you are okay with your private key,\notherwise enter anything to change the key..')
        except:
            print("\nSomething was wrong with your input..")
    file, file2 = fileInputs()
    dec(n,d,rdic,file,file2)
    print("\nYour file was succesfully processed!")
main()
