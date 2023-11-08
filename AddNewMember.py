newMember = input("Enter the new member to add: ")+ "\n"

members =[]
file = open("files/members.txt", 'r')
members = file.readlines()
file.close()

members.append(newMember)

file = open("files/members.txt", 'w')
file.writelines(members)
file.close