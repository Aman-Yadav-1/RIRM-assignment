import re
 
def isValid(s):
    Pattern = re.compile("[+](212)?[-][1-9]{3}[-][0-9]{4}")
    return Pattern.match(s)

s = "+212-456-7890"
if (isValid(s)):
    print ("Valid Number")    
else :
    print ("Invalid Number")