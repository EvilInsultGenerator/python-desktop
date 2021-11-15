#A simple insult generation script with the help of Evil Insult API


def generate_insult(lang):
    import requests      
    evil=requests.get(url='https://evilinsult.com/generate_insult.php?lang='+lang+'&type=json')
    data=evil.json()
    insult=data['insult']
    print("Insult :",insult)


language="en" # default language of the insult

while True:
    try:
        var=input("Generate Insult? (y/n)\n>>")
        if var=="y":
            generate_insult(language) 
        elif var=="n":
            break
        elif var=="lang" or var=="language": #for changing language
            print("Available languages are :\n1.en(English)\n2.cn(Chinese)\n3.de(German)\n4.el(Greek)\n5.es(Spanish)\n6.fr(French)\n7.ru(Russian)\n8.sw(Swahili)")
            language=input("Enter language code :\n>>")
            if language=="en" or language=="cn" or language=="de" or language=="el" or language=="es" or language=="fr" or language=="ru" or language=="sw":
                continue
            else:
                print("Invalid language code, IDOT mf")
                continue
        else:
            print("You can't even select between 2 options! Dumbass!")
    except :
        print("Evil Insult Generator is down, you may try again later, dickhead.")