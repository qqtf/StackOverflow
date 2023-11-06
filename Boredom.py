from ast import Try
import collections

def verwijder_elementen_uit_lijst(getal1, getal2, getal3):
    while getal1 in lijst_gehele_getallen:
        lijst_gehele_getallen.remove(getal1)
    while getal2 in lijst_gehele_getallen:
        lijst_gehele_getallen.remove(getal2)
    while getal3 in lijst_gehele_getallen:
        lijst_gehele_getallen.remove(getal3)
        
def meet_frekwenties_en_sorteer(lijst):
# eerst element zoeken met de hoogste frekwentie
# dan overblijvende elementen aan de hand van de maximale waarde

    frekwentieWoordenboek = collections.Counter(lijst)

# The key=lambda x: (x[1],x[0]) tells sorted that for each item x in y.items(), use (x[1],x[0]) as the proxy value to be sorted. 
# Since x is of the form (key,value), (x[1],x[0]) yields (value,key). This causes sorted to sort by value first, then by key for 
# tie-breakers.
    frekwentiewoordenboek_gesorteerd_lijst = sorted(frekwentieWoordenboek.items(), key=lambda x: (x[1],x[0]), reverse=True)
# d.i. een lijst van tuples
    frekwentiewoordenboek_gesorteerd = dict(frekwentiewoordenboek_gesorteerd_lijst)
# we kennen nu de voorlopige volgorde en kunnen voor de eerste maal oogsten uit lijst 1

    eerste_key = next(iter(frekwentiewoordenboek_gesorteerd))
    try: 
        frekwentie_onderstaande_waarde = frekwentiewoordenboek_gesorteerd.get(eerste_key-1)
        frekwentie_bovenliggende_waarde = frekwentiewoordenboek_gesorteerd.get(eerste_key+1)
        frekwentie_topwaarde = frekwentiewoordenboek_gesorteerd.get(eerste_key)
        if frekwentie_onderstaande_waarde == frekwentie_topwaarde and frekwentie_bovenliggende_waarde == frekwentie_topwaarde - 1:
            tussentijdse_oogst = int(eerste_key+1)*frekwentiewoordenboek_gesorteerd.get(eerste_key+1)
            verwijder_elementen_uit_lijst(eerste_key+1, eerste_key+2, eerste_key)
            return tussentijdse_oogst
    except KeyError:
        pass
    
    tussentijdse_oogst = int(eerste_key)*frekwentiewoordenboek_gesorteerd.get(eerste_key)
    verwijder_elementen_uit_lijst(eerste_key, eerste_key+1, eerste_key-1) 

    return tussentijdse_oogst
        
aantal_elementen_in_reeks = int(input())
reeks_string = input()

reeks_string_lijst_char = reeks_string.split()

# eerste referentielijst
oogst = 0
lijst_gehele_getallen = list(map(int, reeks_string_lijst_char))

while lijst_gehele_getallen:
    oogst = oogst + meet_frekwenties_en_sorteer(lijst_gehele_getallen)
    
print(oogst)

 






