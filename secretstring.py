trips = [['t','u','p'],['w','h','i'],['t','s','u'],['a','t','s'],['h','a','p'],['t','i','s'],['w','h','s']]
##first=[]
##sec=[]
##third=[]
secret=[]
letter=0
def findLetter(first,sec,third):
    for p in first:
        if p not in sec+third:
            secret.append(p)
            letter = p
    for num, i in enumerate(trips):
        if i[0] == letter:
            trips[num].remove(letter)
            trips[num].append(' ')
    print ('Завершили findLetter')
    print (secret)
    return secret, trips, letter
def recoverSecret(first=[],sec=[],third=[]):
        print ('trips на входе',trips)
        for i in trips:
            first.append(i[0])
            sec.append(i[1])
            third.append(i[2])
        first = list(set(first))
        sec = list(set(sec))
        third = list(set(third))
        

        if first == [' ']:
            return secret
        print ('first',first,'\nsec',sec,'\nthird',third)
        sec = list(set(sec))
        print ('Запускаем findLetter')
        findLetter(first,sec,third)
        print (f''' Находим secret {secret}
    Находим измененные trips {trips}''')
        return secret, trips , recoverSecret([],[],[])
recoverSecret()
print (trips)
