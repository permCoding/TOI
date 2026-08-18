userA = [1, "Мишкин", 217, 1, "2002-08-23", "Кунгур"]
userB = [202, "Бортич", 224, 0, "2002-06-03", "Лысьва"]
userC = [33, "Кротов", 217, 1, "2002-07-13", "Кунгур"]

users = [userA, userB, userC]

f = open("./csv/users.txt", "w", encoding="utf-8")

# f.write("111111"+"\n")
# f.write("222222")


filtred_users = [user for user in users if user[3] == 1]
# print(filtred_users)

# check = lambda user: user[3] == 1
# filtred_users = list(filter(check, users))
# print(filtred_users)

# filtred_users = list(filter(lambda user: user[3] == 1, users))
# print(filtred_users)


for user in filtred_users:
    
    # f.write(user)
    
    # line = "-".join(["11", "22", "33"]) + "\n"
    # f.write(line)
    
    # f.write( ",".join(user) )
    
    # line = ",".join(str(elm) for elm in user) + "\n"
    # f.write( line )  # good
    
    # line = ",".join( map(lambda u: "_"+str(u), user) ) + "\n"
    line = ",".join( map(str, user) ) + "\n"
    f.write( line )

f.close()