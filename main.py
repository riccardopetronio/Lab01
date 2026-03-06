import random


class Domanda:
    def __init__(self, domanda: str, difficolta: int, risp_gius: str, opzione2: str, opzione3: str, opzione4: str):
        self.domanda = domanda
        self.difficolta = difficolta
        self.risp_gius = risp_gius
        self.opzione2 = opzione2
        self.opzione3 = opzione3
        self.opzione4 = opzione4

    def stampati(self):
        lista_risposte = [self.risp_gius, self.opzione2, self.opzione3, self.opzione4]
        random.shuffle(lista_risposte)
        print(f"{self.domanda}")
        contatore = 1
        for r in lista_risposte:
            print(f"{contatore}) {r}")
            contatore += 1
        print("")

lista_domande: list[Domanda] = []

with open('domande.txt', 'r') as file:
    righe = file.readlines()

    contatore1 = 0
    contatore2 = 1
    contatore3 = 2
    contatore4 = 3
    contatore5 = 4
    contatore6 = 5

    while contatore5 <= len(righe):
        vTemp = Domanda(righe[contatore1].strip(), int(righe[contatore2].strip()), righe[contatore3].strip(),
                        righe[contatore4].strip(), righe[contatore5].strip(), righe[contatore6].strip())
        lista_domande.append(vTemp)
        contatore1 += 7
        contatore2 += 7
        contatore3 += 7
        contatore4 += 7
        contatore5 += 7
        contatore6 += 7

difficolta_attuale = 0


def domande_per_il_livello_attuale(diff: int):
    risultato: list[Domanda] = []
    for d in lista_domande:
        if d.difficolta == diff:
            risultato.append(d)
    random.shuffle(risultato)
    return risultato


sbagliato = False

while sbagliato == False and len(domande_per_il_livello_attuale(difficolta_attuale)) != 0:
    for d in domande_per_il_livello_attuale(difficolta_attuale):
        d.stampati()
    scelta_utente = input("quale numero scegli?  ")
    sbagliato = True
