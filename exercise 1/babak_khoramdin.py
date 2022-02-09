message = 'Babak Khorramdin'
print(message[0])
looked_char = 'K'
if looked_char in message:
    print('K')
name, family = message.split()
print('name:', name, '\n', 'family:', family)
print(message[:12:2])
for i in message:
    if i == 'm':
        print(True)
        break
