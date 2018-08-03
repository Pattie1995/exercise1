'''height = input("How tall are you? ")
height=int(height)
if height>=10:
    print('tall enough!')
else:
    print('not tall enough!')
'''

'''
message=''
if message !='quit':
    message=input(prompt)
    print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt  += "\nEnter 'quit' to end the program. "
active=True
while active:
    message=input(prompt)
    if message=='quit':
       #active=False
       break
    else:
        print(message)
'''
number=0
while number<10:
    number+=1
    if number%2==0:
        continue
    print(number)
