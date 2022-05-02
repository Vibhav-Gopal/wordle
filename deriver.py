words = open('Python Scripts/Wordle/words.txt','r')
poss = words.readlines()
for k in range(len(poss)):
    poss[k] = (poss[k].strip())
    # poss[k].pop()   061629
    # poss[k] = ''.join(poss[k])
stg1=[]
stg2=[]
stg3=[]
stg4=[]
guess = [' ',' ',' ',' ',' ']
pos2chk = []
useable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
waste = []
must = []
totalGood=[]
mustpos = []
num = int(input("How many guesses to predict from\n"))
print("Enter guesses separated by hyphen, like words-byggg")
print("""
    b - black
    y - yellow
    g - green
""")
for i in range(num):
    x = input()
    wd,data = x.split('-')
    wd.lower()  
    data.lower()
    wd = list(wd)
    data = list(data)
    for j in range(5):
        if data[j] == 'b':
            if wd[j] not in waste:
                waste.append(wd[j])
            try:
                useable.remove(wd[j])
            except:
                pass
        elif data[j] == 'y':
            if wd[j] not in must:
                must.append(wd[j])
        elif data[j] == 'g':
            guess[j] = wd[j]
            if wd[j] not in must:
                must.append(wd[j])
            if j not in pos2chk:
                pos2chk.append(j)
for m in poss:
    if set(must).issubset(set(list(m))):
        stg1.append(m)
temp = useable
for m in must:
    if m not in temp:
        temp.append(m)
for m in stg1:
    if set(list(m)).issubset(set(temp)):
        stg2.append(m)
fin = stg2
toDel = []

for m in fin:
    for k in pos2chk:
        if m[k] != guess[k]:
            toDel.append(m)
            break
for m in fin:
    if m not in toDel:
        stg3.append(m)
print(stg3)
input()
