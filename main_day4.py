start = 245182
stop = 790572

my_input_list = list(map(str, range(start, stop+1)))

def get_pwd(password_list):
	password_container = []
	for password in password_list:
		if (password[0]<=password[1]<=password[2]<=password[3]<=password[4]<=password[5]):
			counter = 0
			while counter < len(password)-1: 
				if password[counter] == password[counter+1]:
					password_container.append(password)
					break
				counter += 1
	return password_container

print(len(get_pwd(my_input_list)))