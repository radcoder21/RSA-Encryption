def fileInputs():
    try:
        fileread = input("\nPlease enter the name of the file\nyou wish to read for encryption(no .txt): ")
        file1 = open(fileread+".txt","r")
    except:
        print("\nYour file won't open, please try agin...")
    filewrite = input("\nPlease enter the name of the file\nyou wish to create/change for decryption(no .txt): ")
    file2 = open(filewrite+".txt","w")
    return file1, file2

def enc(n,e,dic,file1,file2):
    text = file1.read()
    for letter in text:
        t1 = dic[letter]
        t = encFunc(t1,n,e)
        print(t, file=file2 , end=" ")
    file2.close()

def encFunc(v,n,e):
        x = v**e%n
        return x

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
    print("\nWelcome to our public encrypter where anyone\ncan encrypt a text file using aa public key.")
    go = 'go'
    while go != "":
        try:
            n,e = eval(input("\nPlease enter the public key seperated by a comma: "))
            go = input('\nPress enter if you are okay with your public key,\notherwise enter nything to change the key..')
        except:
            print("\nSomething was wrong with your input..")
    file, file2 = fileInputs()
    enc(n,e,dic,file,file2)
    print("\nYour file was succesfully processed!")
main()
