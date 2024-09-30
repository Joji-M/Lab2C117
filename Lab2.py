def  isIsogram(word):

    for i in word:
        count = 0
        for j in word:
           if(i == j):
               count = count + 1;
        if count >= 2:
            return False
    return True



def isAbedecerrian(word):

    index = 0
    while(index < (len(word) -1)):
        if(word[index] > word[index +1]):
            return False;
        index = index + 1;

    return True

def  isDobloon(word):

    for i in word:
        count = 0
        for j in word:
           if(i == j):
               count = count + 1;
        if count != 2:
            return False
    return True

if __name__ == "__main__":
    print("abcdefg")
    print(isIsogram("abcdefg"))
    print("abcdefgg")
    print(isIsogram("abcdefgg"))
    print("hello my name is")
    print(isIsogram("hello my name is"))
    print("blah og")
    print(isIsogram("blah og"))
    print("break")

    print("bijoux, pass:", isAbedecerrian("bijoux") )
    #isAbedecerrian("bijoux")
    print("biopsy, pass:",  isAbedecerrian("biopsy"))

    print("dimpsy, pass:", isAbedecerrian("dimpsy"))
   # isAbedecerrian("dimpsy")
    print("zebra,  fail :", isAbedecerrian("zebra"))

    print("murmur, pass: ", isDobloon("murmur"))
    print("noon, pass: ", isDobloon("noon"))
    print("reappear, pass: ", isDobloon("reappear"))
    print("donkey, fail: ", isDobloon("donkey"))
    print("clown, fail: ", isDobloon("clown"))

