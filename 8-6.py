class UserIQTooLow(Exception): pass

try:
      hold_conversation(user)
except UserIQTooLow:
	if user != boss:
    	  print('User IQ too low')
	else:
    	  raise
