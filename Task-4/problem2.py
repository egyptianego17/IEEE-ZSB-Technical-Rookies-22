import random
password_len = int(input("Please enter password length: "))
pass_char = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789"
special_char = "@#$%&"
final_output = ""
for lista in range(0,password_len):
    random_choice = random.choice(pass_char)
    final_output = final_output + random_choice
final_output = final_output.replace(random.choice(final_output),random.choice(special_char))
print(final_output)