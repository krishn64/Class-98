from fileinput import filename


def wordcounter ():
    filename=input("enter ur file name")
    file1=open(filename)
    read=file1.read()
    count=read.split()
    numberofwords=len(count)
    print(numberofwords)
wordcounter()