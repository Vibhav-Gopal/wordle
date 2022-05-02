file= open('Python Scripts/Wordle/words.txt','a+')
while True:
    x = input()
    if len(x) == 5:
        file.write(x+'\n')
        