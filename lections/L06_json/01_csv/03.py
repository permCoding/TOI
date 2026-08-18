def save_to_csv(lst, filename, sep=','):
    f = open(filename, "w", encoding="utf-8")
    # sorted()
    
    lines = []
    for obj in lst:
        line = sep.join(str(elm) for elm in obj) + "\n"
        lines.append(line)
        # lines += [lines]
    
    f.writelines(lines)
    f.close()


userA = [1, "Мишкин", 217, 1, "2002-08-23", "Кунгур"]
userB = [202, "Бортич", 224, 0, "2002-06-03", "Лысьва"]
userC = [33, "Кротов", 217, 1, "2002-07-13", "Кунгур"]
users = [userA, userB, userC]

save_to_csv(users, "./csv/users.csv")
# save_to_csv(users, "./csv/users.csv", " ")

# GIU