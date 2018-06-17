import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*_-+=`|\(){}[]:;"\'<>,.?/'

n = input('number of passwords?')
n = int(n)

length = input('password length?')
length = int(length)

for p in range(n):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
