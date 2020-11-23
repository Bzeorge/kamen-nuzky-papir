import random


def game(choice):

    options = ["kamen", "nuzky", "papir"]
    bot = random.choice(options)

    if choice == "kamen" and bot == "nuzky":
        print("Ty mas kamen, ja mam nuzky. \nVyhral jsi!")
    elif choice == "kamen" and bot == "papir":
        print("Ty mas kamen, ja mam papir. \nProhral jsi.")
    elif choice == "kamen" and bot == "kamen":
        print("Oba mame kamen. \nRemiza")
    elif choice == "papir" and bot == "papir":
        print("Oba mame papir. \nRemiza")
    elif choice == "papir" and bot == "nuzky":
        print("Ty mas papir, ja mam nuzky. \nProhral jsi.")
    elif choice == "papir" and bot == "kamen":
        print("Ty mas papir, ja mam kamen. \nVyhral jsi!")
    elif choice == "nuzky" and bot == "nuzky":
        print("Oba mame nuzky. \nRemiza")
    elif choice == "nuzky" and bot == "papir":
        print("Ty mas nuzky, ja mam papir. \nVyhral jsi!")
    elif choice == "nuzky" and bot == "kamen":
        print("Ty mas nuzky, ja mam kamen. \nProhral jsi.")
    else:
        print(f"{choice} neni v nabidce, zkus to znova")


count = 1

while True:
    game(input("kamen - nuzky - papir? "))
    repeat = input("Jeste jedno kolo? ano / ne ")

    if repeat == "ano":
        count += 1
        print(f"{count}.kolo")
        continue
    else:
        break
