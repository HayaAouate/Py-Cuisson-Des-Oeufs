import time
import wave
import sys
print(sys.version)
# import pygame

w = wave.open("C:\\Users\\admin\\OneDrive\\Documents\\support_img_video_son\\son\\clochette_micro_onde.wav", "r")
frames = w.readframes(w.getnframes())
#


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
    return ()
        # w.close()
        # pygame.mixer.init()
        # pygame.mixer.music.load("sample.mp3")
        # pygame.mixer.music.play()



def cuisson_en_cours():
    print("Cuisson en cours : ", end="")
    pointille()
    print()
    return ()


print("Option de cuisson")
a = "a - Oeuf à la coque : 3min "
b = "b - Oeuf mollets: 6min "
c = "c - Oeuf durs : 9min "

# Boucle while pour demander à l'utilisateur de saisir un choix valide
while True:
    choix = input(f"{a} \n{b}\n{c} \nVotre choix : ")

    # Vérifier si le choix de l'utilisateur est valide
    if choix in ["a", "b", "c"]:
        try:
            if choix == "a":
                cuisson_en_cours()
                cuisson_voulu(1)

            elif choix == "b":
                cuisson_en_cours()
                cuisson_voulu(6)
            else:
                cuisson_en_cours()
                cuisson_voulu(9)
        except ValueError:
            print(f"Erreur : veuillez saisir une lettre ")
            break
    elif choix.isdigit():
        print('Veuillez saisir une lettre')
    else:
        print(f"Erreur : veuillez saisir entre a, b ou c ")
    break
print("Cuisson terminé")

# recursion c rappeler la fonction a la fin dune fonction apres un exept pour que ca raffiche