# Obsah prezentácie


## Intro (5 min)

Na úvod sa treba predstaviť, spomenúť v akej firme pracujem (a že sa tu taktiež
zdržuje niekoľko mojich kolegov?)
Treba povedať ako som sa s pythonom zoznámil ako som sa v ňom snažil spraviť
svoju diplomovú prácu a čo ma nakoniec posunulo v mojich schopnostiach ďalej.

Na úvod by sme mohli definovať, čo to vlastne [anti-pattern je][1]? Treba ale 
upozorniť na to a klásť na to dôraz, že niektoré všetko záleží od kontextu a 
tam kde jedna technika nieje dobrá, inde môže byť práve tým správnym riešením.  
TODO: pridaj obrázok  
TODO: pridaj referencie


Aké zlé praktiky zvyknú ľudia robiť. Vyvíjanie SW sa deje často v
nekontrolovanom prostredí. Človek nevie zaručiť aké knižnice používa, aké verzie
a čo vlastne jeho aplikácia vyžaduje na chod. Tu naráža na problém, keď chce
aplikáciu pustiť inde ako na svojom počítači. Po tomto nastáva fáza, kedy človek
inštaluje všemožné veci na stroji na ktorom chce aby aplikácia bežala. Toto môže
byť celkom frustrujúce ale nakoniec sa to podarí.

TODO: ďalšie anti patterns z knihy


Riešenia? čo by som tu chcel povedať? Riešením je predsa istá disciplína.
Riešením, je používanie tých správnych postupov a princípov, tam kde sa to hodí.
A to nieje jednoduché vedieť odhadnúť.

Riešením je dávať si pozor na svoj technologický dlh a zakaždým si nájsť čas
aby sme ho mohli spraviť alebo vymazať.

TODO: [ Tuto ][2] je veľmi pekná metafora a veľmi pekne vysvetlené, čo to
technologický dlh je. 

čo by mohlo byť riešením na tieto problémy, ktoré máme? na antipatterns
Je to znalosť nejakých praktík. človek nepotrebuje každú z nich ovládať. Stačí
aby o nej vedel a aby vedel na čo slúži. Pri najbližšej príležitosti, kedy
by sa dala takáto technika použiť, tomu dá človek šancu. A tak sa tiež posunie
nejako ďalej. 

Samozrejme riešením je aj spomínaná disciplína. Musíme platiť svoj dlh, ktorý
zvykneme robiť.

Continuous improvement. To čo som sa naučil s knižky o scrume. Alebo
Toyota-Production-System. To je technika, ktorá sa dá uplatniť skoro na všetko.
A vlastne z tejto metodológie je odvodený aj scrum. Tvorca scrumu sa inšpiroval
z tohto systému a upravil ho tak, aby sedel na vývoj SW. V skutočnosti je ale
scrum postavených na takých pravidlách, ktoré sa dajú použiť takmer v akomkoľvek
prostredí.

Čo som tým chcel povedať, že každý systém má nejaké svoje zákonitosti a nejaké
pravidlá, ktorými sa riadi. Ľudia ako Ford a Toyota mali tú možnosť, že stáli
pri zrode industrialneho priemyslu a odpozorovali tieto zákonitosti. Na základe
svojich skúseností tak postavili svoje metodológie, ktoré fungujú dodnes.
Treba si však dávať pozor, pretože nieje jednoduché tento sytém uplatniť. Na
to treba tú spomínanú disciplínu a cit, kedy použiť v akej situácií a v akom
čase aké pravidlá.


## Hlavný blok (15 min)

 * Hlavný blok (15 min)
   * vývojové prostredie
     * nástroje & praktiky
   * produkčné prostredie
     * odlišnosti od vývojového prostredia (tu som mal na mysli to, že na
       produkčnom servery by nemali čo hľadať dev nástroje a knižnice a žiadny
       iný sw. V podstate len to, čo je potreba na chod aplikácia. Všetko ostatné
       je zvyšovaním pravdepodobnosti, že sa niečo rozbije)
       
     * ako dostať našu appku na produkčný server
   * continuous integration (CI)
     * vytváranie balíčkov
     * spúšťanie testov rôznych úrovní
     * deploy do test prostredia
   * continuous deployment (CD)
     * rozdiely medzi CI a CD
   * configuration management

# Demo (5 min)

 * Demo (5 min)
   * video ukážka s komentárom

# Otázky (5 min)

 * Otázky (5 min)



[1]: http://martinfowler.com/bliki/AntiPattern.html
[2]: http://martinfowler.com/bliki/TechnicalDebt.html
