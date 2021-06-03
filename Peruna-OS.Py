import time
import os

print("""
╔══╦══╦═╦╗╔╦═╗╔══╗──╔══╦══╗
║╔╗║║═╣╔╣║║║╔╗╣╔╗╠══╣╔╗║══╣
║╚╝║║═╣║║╚╝║║║║╔╗╠══╣╚╝╠══║
║╔═╩══╩╝╚══╩╝╚╩╝╚╝──╚══╩══╝
║║
╚╝""")
print("""
[1] Jatka asennusta
[2] Olen jo tehnyt asennuksen
	""")
setup = input("[?]: ")
if setup == '1':
	name = input(str("Olkaa hyvä ja antakaa nimenne: "))
	pas = input(str("Olkaa hyvä ja syöttäkää salasananne: "))
	lines = [name]
	with open('user/username.txt', 'w') as f:
		f.writelines(lines)

	lines2 = [pas]
	with open('user/password.txt', 'w') as f:
		f.writelines(lines2)
		print("Asennus valmis")
		input("Paina enter poistuaksesi ikkunasta")


if setup == '2':
	login_pass = open('user/password.txt')
	login_name = open('user/username.txt')
	l_p = login_pass.read()
	l_n = login_name.read()

while True:
    login = input(str("Olkaa hyvä ja antakaa salasana osoitteeseen " + l_n + ": "))
    if login == l_p:
    	os.startfile("Minecraft.py")
    	break
    else:
    	print("Väärä salasana")

		