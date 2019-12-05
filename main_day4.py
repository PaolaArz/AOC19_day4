from functools import reduce 

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

my_password_list = (get_pwd(my_input_list))

print(len(my_password_list))

#part two
def get_pwd2(pwd_list):
	counter = 0
	for pwd in pwd_list:
		for i in pwd:
			if pwd.count(i) == 2:
				counter += 1
				break
	return counter

print(get_pwd2(my_password_list))

