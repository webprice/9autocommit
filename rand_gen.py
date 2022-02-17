import time
import random
import string

#generate random number, that will declare how many letters 
#will be added to the text.txt file. Each time we change the text.txt file
#we can made a commit and push it to the reote repo
#which will be considered as a github contribution
x = random.randrange(10)
random_letter = random.choices(string.ascii_letters,k=x)


#function which actually adding those letters t the text.txt file
def random_letter_write(letters):
    try:
        streng = ""
        for l in letters:
            streng += l
        time.sleep(1)

#opening the text.txt file, but if it doesn't exist, it will be created,
#this is why were using a+ attribute
        with  open("text.txt",'a+') as f:
            f.write(streng)
            time.sleep(1)
            f.close()
        return "all went good"
    except:
        return "all bad"
random_letter_write(random_letter)
