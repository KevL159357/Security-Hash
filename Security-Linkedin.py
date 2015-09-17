#!C:\Python27\python.exe
'''
Kevin Li <kl1983@nyu.edu>
Linkedin hash cracker

Uses john.txt to find common passwords and hashes them to check. Matched
passwords are written to linkedinCracked.txt

Runtime O(n^2)
'''
import hashlib

def append(word):           #This function is used to sha1 hash the string given to it
    x = word.strip('\n')
    h = hashlib.sha1()
    h.update(x)
    return (h.hexdigest())

def loop():
    wordFile = open("john.txt")
    linkedin = open("Linkedin.txt")
    linkCracked = open("linkedinCracked.txt",'w')
    i = 0               #Count the number of attempted passwords
    counter = 0         #Used to see how many passwords were cracked
    
    linkCracked.write("The left column contains the hash and the right are passwords \n\n")
    for theWord in wordFile:
        i = i+1
        hasher = append(theWord) 
        print "Password attempt number :%i " %(i)
        for line in linkedin:
            if('00000' == line[:5]):
                k = ('00000' + hasher[5:])
                if(k.strip() == line.strip()):
                    print "We Got a match : " + theWord + '  ' + line + '\n'
                    hasher = ''
                    linkCracked.write(line.strip() + "  " + theWord)
                    counter = counter + 1
            else:
                if(hasher.strip() == line.strip()):
                    print "We Got a match : " + theWord + '  ' + line + '\n'
                    hasher = ''
                    linkCracked.write(line.strip() + "  " + theWord)
                    counter = counter + 1
        linkedin.seek(0)

    linkCracked.write("\n\n The total number of passwords cracked is : " + str(counter) +" \n\n")
   
    
def main():
    loop()

if __name__ == '__main__':
    main()
