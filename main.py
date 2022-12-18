import random as rd
slovar = {

}
array_user = ["Вика", "Максим", "Полина", "Стас", "Даша", "Игорь", "Катя"] #this is an array of members
array_take = [] #an array to whom they already give
for i in range(len(array_user)):
    user1 = array_user[i]
    while True:
        user2 = rd.randint(0, len(array_user)-1)
        if array_user[user2] != user1 and array_user[user2] not in array_take:
            array_take.append(array_user[user2])
            break
    slovar[user1] = f'=> {array_user[user2]}'


for i, j in slovar.items(): 
    print(i, j)
