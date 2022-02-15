import time
import random
import string


x = random.randrange(10)
random_letter = random.choices(string.ascii_letters,k=x)

def random_letter_write(letters):
    try:
        streng = ""
        for l in letters:
            streng += l
        time.sleep(1)
        with  open("text.txt",'a+') as f:
            f.write(streng)
            time.sleep(1)
            f.close()
        return "all went good"
    except:
        return "all bad"
random_letter_write(random_letter)
