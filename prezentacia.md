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


## Hlavný blok (20 min)

Hlavný blok som sa rozhodol rozdeliť na časti podľa prostredií.
Rozdelenie teda bude: Development env, CI env, Test env, Production env

V nasledujúcich slajdoch si povieme čo sa v každom prostredí zvykne robiť,
načo to slúži a kedy je vhodné použiť niektoré nástroje.

### Development environment

Python je dobrý v tom, že zdrojový kód sa dá pustiť na všemožných operačných
systémoch.

Ja osobne zvyknem pracovať na OS X a Linuxe. Keď som chcel začať nejaké projekt
proste som si nainštalovať nejaké potrebné balíčky (už neviem aké verzie),
myslím, že tam boli nejaký python 2.7. Pomocou sudo som nainštalovať všemožný
bordel medzi systémové balíčky.

Potom som chcel robiť iný projekt v škole. V tomto projekte bolo treba najnovšiu
verziu Djanga. Ale ja som mal nainštalovanú tú z pred pol roka. Veci zrazu
prestali fungovať. Viacej času som trávil fixovaním svojho systému. A kým som
vyriešil jeden problém, rozbil som si ďalších x vecí.

    99 little bugs in the code
    99 little bugs in the code
    Take one down, patch it around
    117 little bugs in the code

Takto prešlo nejaké obdobie a z môjho pracovného kompu sa stal mess. Nič tam
nefungovalo, stále som musel hladať nejaké riešenia ako to rozbehať. Človek už
potom nainštaluje čokoľvek len aby sa už konečne dostal k tomu čo potrebuje.

V tomto prípade ide o nekontrolované vývojové prostredie. Takýmto spôsobom,
človek nemá šancu usledovať ktoré balíky reálne používa. Riešením je izolovať
vývojové prostredie čo najviac.

TODO: virtualenv a virtualenvwrapper

TODO: vagrant

TODO: set up skript - na začiatok to nemusí byť nič sofistikované.
najlepšie je si to manuálne prejsť, čo treba spraviť na čistom OS, aby som
mohol spustiť svoju appku. Spísať si to a potom spraviť nejaký skript, ktorý
to tam všetko nainštaluje


### CI environment

TODO: Review
Continuous Integration slúži na to aby sme si vyhradili nejaký server (prostredie)
ktoré je kontrolované oveľa prísnejšie ako Development Env. Na toto prostredie
väčšinou slúži change management aby sme predišli zmenám, ktoré nám toto prostredie
rozbijú prípadne privedú nejaké nežiadúce vedlajšie efekty.

Je oveľa jednoduchšie vniesť chybu do programu zlou konfiguráciou ako zlým kódom.
Navyše konfigurácia ostane dlho bez povšimnutia. K tomuto CI serveru sa tiež
drží prísna politika, kto naň môže pristupovať. Spravuje ho vzäčša jeden človek.
Táto metóda je určite dobrá, no prináša závyslosť na 1 človeku, ktorý má kľúče
od miešačky. Ak sa niečo pokazí, treba na to jeho. Ak treba niečo pridať, treba
jeho. Jeden človek sa teda stáva bottleneckom pre ostatných.

Lepším prístupom je definovať konfiguráciu CI servera pomocou nejakého skriptu
aby bol tento server možné jednoducho zreplikovať. Všetky závislosti sú presne
definované a jasné. Každý priečinok ktorý treba je vytvorený automatickým skriptom,
každý balík má presnú verziu. Všetci majú prístup k tejto konfigurácií a každý
si môže spraviť svôj vlastný CI server ak chce. Virtualizácia poskytuje obrovské
možnosti. Navyše je skript verziovaný, takže nad všetkým máme kontrolu a prehľad.


Potom, čo už máme takýto server nahodený, vieme ho využiť na tvorbu balíkov.
Pre každý commit vieme presne zreplikovať daný balíček, pretože vieme aká je
konfigurácia CI servera a presne vieme čo sa na balíčkovanie použilo.


Tieto balíčky si potom ukladáme do tzv Binary Repository. Čiže niečo ako verziovanie
zdrojového kódu. Principiálne ide o to isté, ale pozadie funguje inak pretože sa
jedná o binárne súbory a nie textové.

Prečo ale robíme tieto balíčky?
TODO: odpovedať na otázku...

### Test environment

TODO: add content


### Production environment

odlišnosti od vývojového prostredia (tu som mal na mysli to, že na
produkčnom servery by nemali čo hľadať dev nástroje a knižnice a žiadny
iný sw. V podstate len to, čo je potreba na chod aplikácia. Všetko ostatné
je zvyšovaním pravdepodobnosti, že sa niečo rozbije)


### Continuous Delivery
Aký je rozdieľ medzi continuous integration a continuous delivery??

Ide v princípe o veľmi podobné veci a rozdieľ je len v tom, že otestované a
pripravené balíčky sa automaticky deploynú na produkčný server.
Množstvo práce, ktoré sa za týmto malým rozdieľom skrýva je však veľké.

Release candidate by mal prejsť cez sériu akceptačných testov, ktoré skutočne
zaručia, že aplikácia bude fungovať.

Ak používame viacero serverov a nejaký balancer, treba deployovať postupne po
serveroch s nejakým rozostupom aby sme nespôsobili down time.

Taktiež treba mať v rukáve monitoring a upozorňovanie ak sa niečo pokazý, aby sme
deploy mohli včas zastaviť a spraviť rollback na pôvodnú verziu.

Jeden z príkladov ako sa to dá spraviť je ten, že každý produkčný web server
alebo iné servery, sa pravideľne pozerajú na nejaký metadata súbor, ktorý popisuje
aktuálnu verziu applikácie poslednej verzie vhodnej pre release. Tieto servery
si tak prevezmú svoju verziu asynchrónne čo umožňuje mnoho iných praktík.

Zero down time releases and roll backs



## Otázky (5 min)



[1]: http://martinfowler.com/bliki/AntiPattern.html
[2]: http://martinfowler.com/bliki/TechnicalDebt.html
