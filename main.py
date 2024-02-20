import time


def pointille():
    for i in range(0, 11):
        time.sleep(1)
        print(".", end="", flush=True)
    return ()

def cuisson_voulu(temps):
    for min in range(temps, -1, -1):
        for sec in range(50, -1, -10):
            print(f"Temps restant : {min}:{sec}", end="")
            pointille()
            print()
    print("T")
    return ()

print("Option de cuisson")
a = "a - Oeuf à la coque : 3min "
b = "b - Oeuf mollets: 6min "
c = "c - Oeuf durs : 9min "
choix = input(f"{a} \n{b}\n{c} \nVotre choix : ")
if choix == a:
    cuisson_voulu(3)
elif choix == b:
    cuisson_voulu(6)
else:
    cuisson_voulu(9)
