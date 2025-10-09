# import random
# import string

# a = random.choice(string.ascii_letters)
# b = random.choice(string.ascii_letters)
# c = random.choice(string.ascii_letters)
# d = random.choice(string.ascii_letters)
# e = random.choice(string.ascii_letters)
# f = random.choice(string.ascii_letters)
# word = input("Enter any word")
# if len(word)>3:
#     initial = word[::-1]
#     word = list(word)
#     word.append(word[0])
#     del word[0]
#     word = ''.join(word)#It combines every elemnt in list with what we wrote in ''
#     print(f"Encoded word is {a}{b}{c}{word}{d}{e}{f}")
# else:
#     encoded = word[::-1]
#     print(f"Encoded word is {encoded}")


# Creating encoded of length 10+user if user = 5 split to 3 if 10 split to 4 if 15 split to 5
# import random
# import string

# word = input("Enter the word to be encoded\nNote:- Word length should be less that 15")
# if len(word) <5:
#     lis = []
#     sp1 = word[0:(len(word))/2]
#     sp2 = word[(len(word))/2:]
#     for i in range(4):
#         if i==1:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp1)
#         elif i==3:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp2)
#         else:
#             lis.append(random.choice(string.ascii_letters))
#     print(''.join(lis))

# elif len(word)<10:
#     sp = len(word))/3
#     sp1 = word[0:sp]
#     sp2 = word[sp:2*sp]
#     sp3 = word[2*sp:]
#     for i in range(9):
#         if i==2:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp1)
#         elif i==5:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp2)
#         elif i==8:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp3)
#         else:
#             lis.append(random.choice(string.ascii_letters))
#     print(''.join(lis))

# elif len(word)<=15:
#     sp = len(word))/3
#     sp1 = word[0:sp]
#     sp2 = word[sp:2*sp]
#     sp3 = word[2*sp:3*sp]
#     sp4 = word[3*sp:4*sp]
#     sp5 = word[4*sp:]
#     for i in range(14):
#         if i==2:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp1)
#         elif i==5:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp2)
#         elif i==8:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp3)
#         elif i==11:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp4)
#         elif i==14:
#             lis.append(random.choice(string.ascii_letters))
#             lis.append(sp5)
#         else:
#             lis.append(random.choice(string.ascii_letters))
#     print(''.join(lis))