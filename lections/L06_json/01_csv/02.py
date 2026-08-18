userA = [1, "Мишкин", 217, 1, "2002-08-23", "Кунгур"]
userB = [202, "Бортич", 224, 0, "2002-06-03", "Лысьва"]
userC = [33, "Кротов", 217, 1, "2002-07-13", "Кунгур"]

users = [userA, userB, userC]

f = open("./csv/users.txt", "w", encoding="utf-8")

filtred_users = [user for user in users if user[3] == 1]

for user in filtred_users:
    f.write( ",".join( map(str, user) ) + "\n" )

f.close()