from random import randint

choice=int(input('Введите длинну пороля'))

choice_num_chr=input('Делать ли фильтрацию по цифрам (y,n):')

if choice_num_chr.lower()=='y':
    choice_num_chr=True
elif choice_num_chr.lower()=='n':
    choice_num_chr=False
else:
    print('Необходимо вводить лишь y или n')
    exit()

password=""
chars='fdfhfghgfhffffffffffffffffffffffffhf'
nums="9876543210"

if choice_num_chr:
    chars+=nums

if choice<=0:
    print('Длинна пороля должна быть меньше нуля')
    exit()

for i in range(choice):
    password+=chars[randint(0,len(chars)-1)]

print(password)