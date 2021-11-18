import time
siNo = ["si", "no"]
answer = ""

def choice(aQuestion, aYesBranch, aNoBranch):
    answer = ""
    answer = input(aQuestion + '\n').lower()
    while answer not in siNo:
        answer = input(aQuestion)
    if answer == "si":
        printLine("")
        aYesBranch()
    elif answer == "no":
        printLine("")    
        aNoBranch()

def printLine(aString):
    for character in aString:
        print(character, end='', flush=True)
        time.sleep(0.05)
    print()




def printIntro():
    printLine("---------Genocalipsis---------")
    printLine("-----Por Matias Fernandez-----")
    time.sleep(1)
    printLine("")
    printLine("Bienvenidx al juego, para tomar decisiones simplemente escribí Si/No")
    time.sleep(1)
    printLine("El año es 2130, la atmosfera se vio gravemente afectada gracias a la contaminación")
    printLine("generada por los humanos en los últimos cientos de años, los problemas son muchos,")
    printLine("pero uno de los que más nos preocupa es de los más difíciles de resolver")
    printLine("rayos cósmicos.")
    time.sleep(1)
    printLine("No, no son ataques alien, partículas cósmicas que viajan a grandes velocidades que antes eran")
    printLine("detenidas por las moléculas de la atmosfera, ahora chocan libremente contra los humanos,")
    printLine("generando incontables mutaciones genéticas y problemas de salud. ")
    printLine("Peeero")
    time.sleep(0.75)
    printLine("Acaban de crear una solución")
    time.sleep(1)
    printLine("¡Vos!")
    time.sleep(1)
    printLine("Un Nanobot consciente y diminuto, encargado de vivir dentro de las células para corregir")
    printLine("las mutaciones genéticas generadas por la radiación cósmica, si cumplís con tu misión")
    printLine("los humanos podrán volver al exterior sin miedo de sufrir mutaciones.")
    printLine("¡Suerte!")
    time.sleep(1)
    printLine("")
    

def printPrologue():
    printLine("Estas dentro del núcleo de la célula, ves lo que según tu base de datos llaman “ARN polimerasa”")
    printLine("pareciera estar transcribiendo sin problemas…")
    printLine("Una cadena de ARN pasa cerca y parece estar saliendo del núcleo.")

def printRiboChoice():
    printLine("Saliste del núcleo, ves como el ARN mensajero esta empezando a ser leído por un Ribosoma,")
    printLine("Al acercarte más notas que el ARN transferencia no se está conectando como debería,") 
    printLine("al ARN le faltaba una base lo que hizo que toda la cadena se corriera una posición.")
    printLine("Podes detener el proceso, para evitar que se generen proteínas indeseadas")
    printLine("O")
    printLine("Podes permitir que siga, quizás pase algo interesante. ¿Humanos con ojos violeta?")
    printLine("")

def printLawfulPath():
    printLine("¡¡Bien!!")
    printLine("")
    printLine("¡Estás haciendo tu trabajo!")
    printLine("(Como esperábamos...)")
    printLine("No sabemos que daños podría haber generado esa proteína si se creaba, está bien ser precavido. ")
    printLine("El trabajo no termina ahí, flota a tu lado un ARN transferencia que parece haber ")
    printLine("perdido su aminoácido, sus bases son U-C-A")
    printLine("Por suerte, cerca suyo podés ver una glutamina flotando libremente")

def gameOver():
    printLine("")
    printLine("¡Menos mal que estabas dentro de una pobre rata!")
    printLine("Nunca sabremos si por maldad (no sería la primera vez) o por incompetencia, pero")
    printLine("generaste posibles problemas en tu organismo anfitrión, tu viaje termina acá.")
    printLine("")
    printLine("Perdiste :(")
    printLine("")
    input()

def chaoticEnding():
    printLine("¡¡Felicidades!! ")
    printLine("Esa mutación acaba de crear una proteína que no tenias en tu base de datos.")
    printLine("Lamentablemente la proteína generada no era la necesaria para que los humanos tengan")
    printLine("ojos color violeta, pero si descubriste una enzima extremadamente efectiva en disolver")
    printLine("tejidos, no es una buena noticia para tu organismo anfitrion.")
    gameOver()

def nerdyPlayerEnding():
    printLine("Bien!")
    printLine("Claramente ese no era el aminoácido necesario para ese ARN")
    printLine("¡Felicidades!")
    printLine("Completaste la prueba")
    printLine("¿Quién diría que la generación 68.549.235 iba a ser la correcta?")
    printLine("Creo que ya tuviste suficiente con las pruebas en ratones, tus copias van a ser muy")
    printLine("Útiles en las primeras pruebas en humanos")
    printLine("")
    printLine("Felicidades, Ganaste :)")
    input()

def shouldHaveStudiedEnding():
    printLine("Noooo")
    printLine("¿Tu base de datos está fallando? ")
    printLine("Ese ARN necesitaba una Serina, no deberías andar cambiando aminoácidos porque sí")
    printLine("Claramente necesitamos algunas generaciones mas para que funcionen como deberian")
    gameOver()


def lawfulPath():
    printLawfulPath()
    choice("¿Los deberías unir?",shouldHaveStudiedEnding,nerdyPlayerEnding)

def riboChoice():
    printRiboChoice()
    choice("¿Detener el proceso?",lawfulPath,chaoticEnding)

    
def prologue():
    printPrologue()
    choice("¿La seguís?",riboChoice,prologue)



    
printIntro()
prologue()
