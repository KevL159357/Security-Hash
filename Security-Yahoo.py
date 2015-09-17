#!C:\Python27\python.exe
'''Kevin Li     
   Homework 1.2  Yahoo.txt parser

Assumed that the top and bottom information was not needed.
Rewrites the accounts with passwords in a new file called YahooNew
'''

def parse():
    newFile = open("YahooNew.txt","w")
    txt = open("Yahoo.txt")
    for text in txt:
        # All the top information
      #  newFile.write(text)
        if ('user_id   :  user_name  : clear_passwd : passwd' in text):
            txt.next()
            #Get rid of the empty line above the emails
            break
    
    for text in txt:
        text = text.strip('\n')
        if(':' in text):
            password = text.split(':')[2]  # Or text[-1]
            newFile.write(text + "  " + password + '\n')
   
        if('739853:smoker23@gmx.de:asdf1234' in text):
            break
        
   

def main():
    parse()

if __name__ == '__main__':
    main()
