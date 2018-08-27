user_input = 'I want to demonstrate reverse cipher using this text.'
reversed_user_input = '' 

i = len(user_input) - 1

while i >= 0:
   reversed_user_input = reversed_user_input + user_input[i]
   i = i - 1
print('Our cipher text : ', reversed_user_input)