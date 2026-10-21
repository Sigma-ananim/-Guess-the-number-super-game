import random
TrueFalse=True
pop=3
number_random=random.randint(1,5)
while TrueFalse:
    hii=int(input("напишите число"))
    if hii==number_random:
        TrueFalse=False
        print("ты угодал!!!")
    elif hii>number_random:
        print("ваше число больше")
    elif hii<number_random:
        print("ваше число меньше")

    pop=pop-1
    if pop==0:
        print("игра ококнчена")
        TrueFalse=False
