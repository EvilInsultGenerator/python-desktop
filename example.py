#A simple insult generation script with the help of Evil Insult API


def generate_insult():
    import requests      
    evil=requests.get(url='https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data=evil.json()
    insult=data['insult']
    print("Insult :",insult)
    

while True:
    try:
        var=input("Generate Insult? (y/n)\n>>")
        if var=="y":
            generate_insult()
        elif var=="n":
            break
        else:
            print("You can't even select between 2 options! Dumbass!")
    except:
        print("Evil Insult Generator is down, you may try again later, dickhead.")
