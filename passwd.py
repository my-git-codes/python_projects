import random
import string

def passwd_generator(pass_len):
    global passwd
    if pass_len < 8 or pass_len > 15 :
        print("Enter valid length between 8 - 15 !!")
        pass_len = int(input("Please enter the length of password: "))
        passwd_generator(pass_len)


    else:
        vals = string.ascii_letters + string.digits + string.punctuation
        passwd = "".join([random.choice(vals) for i in range(pass_len)])

    return passwd


pass_len = int(input("Please enter the length of password: "))
result = passwd_generator(pass_len)
print("Here's your password: ", result)
