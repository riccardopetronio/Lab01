import random
import domande
from domande import Domanda


lista_domande = domande.trasforma_in_lista('domande.txt')

def domande_per_il_livello_attuale(diff: int):
    risultato: list[Domanda] = []
    for d in lista_domande:
        if d.difficolta == diff:
            risultato.append(d)
    random.shuffle(risultato)
    return risultato


difficolta_attuale = 0
sbagliato = False
risposte_corrette = 0

while sbagliato == False and len(domande_per_il_livello_attuale(difficolta_attuale)) != 0:

    vTemp = domande_per_il_livello_attuale(difficolta_attuale)[0]
    risposte = vTemp.risposte_disponibili()

    print(f"{vTemp.domanda}\n1) {risposte[0]}\n2) {risposte[1]}\n3) {risposte[2]}\n4) {risposte[3]}\n")
    scelta_utente = risposte[int(input("quale numero scegli?  "))-1]
    print("")

    if scelta_utente == vTemp.risp_gius:
        difficolta_attuale += 1
        risposte_corrette += 1
    else:
        sbagliato = True

print(f"il tuo punteggio è: {risposte_corrette}")
nikname = input("nikneme: ")

punteggi = []
punteggi.append([nikname, str(risposte_corrette)])
with open('punti.txt', 'r', encoding='utf-8') as file:
    for riga in file:
        vTemp = riga.strip().split(" ")
        punteggi.append(vTemp)
punteggi.sort(key=lambda x: x[1], reverse=True)

with open('punti.txt', 'w', encoding='utf-8') as file:
    for r in punteggi:
        file.write(f"{r[0]} {r[1]}\n")
