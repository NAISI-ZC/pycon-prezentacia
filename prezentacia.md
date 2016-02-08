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

#### virtualenv a virtualenvwrapper
Ak čokoľvek robíte s pythonom, a tým myslím čokoľvek. Skúšanie novej knižnice,
výpočítať koľko je 2+2, keď potrebujete niečo vyskúšať alebo spúšťate aplikáciu
na produkčnom servery, vždy používajte virtualenv.

Ja osobne väčšinou nainštalujem system-wide na pc na ktorom pracujem iba python,
pip a virtualenv. Všetko ostatné inštalujem cez virtualenv.

Virtualenv funguje veľmi jednoducho a prináša so sebou nespočetne veľa výhod.
Celý trik spočíva v tom, že keď aktivujete nejaké python virtual prostredie,
prepíšu sa globálne systémové premenné a tým pádom sa zmení pár ciest.
Vytovrí sa priečinok, ktorý obsahuje symbolické linky na python a iné súčasti.
Potom už môžete inštalovať akékoľvek veci cez pip, python setup.py alebo inými
spôsobmi. pip je v tomto prípade industrial standart.

Jednoduchý príkaz, a máte pripravené python prostredie.

    pip install -r requirements.txt

Navyše človek nemusí používať sudo a tým pádom, všetky systémové balíky ostávajú
nedotknuté.


virtualenv odporúčam používať aj na testovacom a produkčnom prostredí.
V jenkinse je to len otázka vytvorenia virtualenv a nainštalovania závislostí
pred spustením testov.

Na produkčnom servery sa tieto veci stávajú trošku tricky, pretože musia bežať
bez interakcie užívateľa s obmedzeným fungovaním env premenných, ale nieje to
nič neprekonateľné.

Ďalším levelom je používanie vagrantu.


#### vagrant
Vagrant poskytuje automatické vytvorenie kompletnej virtuálnej mašiny,
na ktorom potom človek pracuje. Keďže sa snažíme priblížiť produkčnému
prostrediu čo najviac, vagrant je ďalším krokom k tomuto cieľu.

Jednoducho povedané, vagrant za vás nastaví virtuálnu mašinu, nakonfiguruje
zdieľaný priečinok s vaším projektovým root priečinkom, spraví forwardovanie
portov, nastaví ssh a plno iných vecí, čo sa nikomu nechce robiť. Teda prípravu
dev prostredia sme zdredukovali na 2 príkazy.

    vagrant up
    vagrant ssh

Po tomto som prihlásený na mašinu, ktorá je skoro identická s mojou produkčnou
mašinou. 

Samozrejme, aj túto mašinu treba nastaviť podla naších potrieb. V tomto prípade
máme veľa možností. Vagrant poskytuje API pre rôzne config management služby.
Čiže ak máte napríklad Chef recept na nastavenie produkčnej mašiny, tento istý
môžete použiť na nastavenie cez vagrant. Ja často kvôli jednoduchosti a rýchlosti
používam obyčajný shell script, ktorý definujem aby sa spustil počas prápavy
mašiny.

Tento set up skript - na začiatok to nemusí byť nič sofistikované.
najlepšie je si to manuálne prejsť, čo treba spraviť na čistom OS, aby som
mohol spustiť svoju appku. Spísať si to a potom spraviť nejaký skript, ktorý
to tam všetko nainštaluje a nastaví.


#### Fabric

Je python nástroj, pomocou ktorého vieme písať užitočné skripty na balíčkovanie,
deploy skripty na server a mnohé iné. Prirovnal by som to k Make


### CI environment

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


Potom, čo už máme takýto server nahodený, vieme ho využiť na niekoľko potrebných,
(v budúcnosti užitočných) úloh. Napríklad kompilovanie našej aplikácie do
nejakého balíka, ktorý vieme ďalej nainštalovať.

Tieto balíčky si potom ukladáme do tzv Binary Repository. Čiže niečo ako verziovanie
zdrojového kódu. Principiálne ide o to isté, ale pozadie funguje inak pretože sa
jedná o binárne súbory a nie textové.

Prečo ale robíme tieto balíčky? Robíme to preto, aby sme oddelili našu aplikáciu
od zrojového kódu, dokumentácie, kadejakých pomocných skriptov a bez žiadnych
iných zbytočných vecí. Toto je dobrý spôsob na odhalovanie rôznych chýb typu,
mám commitnutý súbor, ktorý je treba na bez aplikácie, ale na produkčný server
viem dostať len balíček. Odelením, získame len to potrebné na beh applikácie.


Kúsok lepším spôsobom ako vytvárať python balíčky, je robiť nativne balíčky
pre daný systém, na ktorom bude aplikácia bežať. Uľahčuje to potom správu
produkčného servera. Ak máme spojazdnený vlastný aptitude server, inštalácia
novej verzie je otázkou 1 príkazu. O všetko ostatné vrátane inštalácie
závislostí, sa postará package manager systému.

S CI potom orchestrujeme aj ďalšie veci ako sú testy.


### Test environment

Test env je často úzko spätý s predchádzajúcimi úlohami. Tu treba rozlišovať
medzi niekoľkými typmi testovania.


Unit testy sa zvyknú bežať na zdrojovom kóde. Zdrojáky si checkoutneme z git
repozitára, nainštalujeme všetky závislosti potrebné na beh testov (napr nejaký
testovací framework) a testy zbehneme. Často používaný formát je xUnit xml,
kde sú popísané testy, ktoré zbehli aj iné štatistiky.

Ďalším krokom by mohla byť statická analýza a tiež code coverage unit testov.
Aj keď na toto sa často dôraz nekladie, udržiavať zdravý code base, ktorý
neporušuje konvencie sa môže veľmi vyplatiť v budúcnosti, keď projekt naberie
viacej ľudí a narastie.


Takzvané package testy sa starajú o to, aby otestovali či balíčkovanie zbehlo
vporiadku a balíček obsahuje všetko potrebné. Často sa totiž stáva, že nejaké
statické súbory (flask templates) niesu súčasťou balíčka. Zrejme je jasné, že
tieto testy sa už neprevádzajú na zdrojovom kóde ale na balíčkoch, ktoré sme si
predtým pripravili.


Integračné testy sa zameriavajú na to, či sa applikácia dá nainštalovať a
spolupracuje s ostatnými systémami. Napríklad s takým web serverom. Teda či sa
applikácia integruje do prostredia s ostatnými vecami. Je dobré pripomenúť, že
tieto testy by sa mali robiť v prostredí, ktoré je ešte bližšie produkčnému.
Jenkins podporuje mechanizmus slaveov. Ide o to, že master jenkins server
už obsahuje nejaké dev nástroje, knižnice a iné veci, ktoré na produkčnom servery
nebudú. Slave vieme nastaviť veľmi podobne produkčnému serveru.
Tieto testy sú taktiže veľmi podobné so systémovými testami. Setup systémových
testov je tiež rovnaký ako pre integračné testy. V tomto prípade ale testujeme
systém skrz na skrz. Simulujeme reálne úlohy, ktoré používateľ chce spraviť od
prihlásenia, cez operáciu až po odhlásenie.
Na toto sa dá použiť napríklad robot framework + selénium, ktoré pekne
spolupracujú s jenkinsom.RF je napísaný v pythone, takže tu je treba minimálny
setup z našej strany.

Na koniec prichádzajú akceptačné testy. Akceptačné testy sú zväčša bránou,
za ktorou je produkt otestovaný a pripavený na deploy do produkcie.

Uvediem príklad. Pokiaľ ide o komplexný projekt, tento systém môže obsahovať
rôzne dev nástroje, nadmerné logovanie, nástroje na debugovanie ktoré sú build in.
Ak sa rozhodneme poslať build cez túto quality bránu, toto všetko by malo byť
z buildu odstránené. Aby sa nestalo, že v systéme ostane nejaký zabudnutý
backdoor.


### Production environment

Hlavnou odlišnosťou produkčného prostredia je to, že by malo obsahovať len
to nevyhnutné. Žiadny git a iné dev nástroje.

Ak máme závislosti aplikácie v requirements, treba z nich vybrať to čo je treba
pre našu apliáciu, dať to do setup.py a pip sa už postará o ostatné. Čiže
rozdelíme DEV závislosti a PRODUCTION závislosti.


Často sa používa nasledujúci anti-pattern. Vo Fabric si spravým deploy
script, ktorý sa prihlási na mašinu na ktorú idem deploynuť, vykoná
git pull a nainštaluje aplikáciu takto. Toto sa môže stať problematické (výpadok
siete), zbytočne sa sťahuje celá história prjektu nehovoriac o tom, že keď niekto
hackne server, má celý code base. Toto je presný príklad antipattern. Zo začiatku
to vyzerá ako super nápad, ale keď máte toto robiť pre 100 serverov ručne...

Oproti tomu, balík nainštaluje pip alebo apt-get a jediné čo je treba spraviť
je v configuration managemente prepísať verziu balíka, ktorý sa má stiahnuť.


Odlišnosti od vývojového prostredia (tu som mal na mysli to, že na
produkčnom servery by nemali čo hľadať dev nástroje a knižnice a žiadny
iný sw. V podstate len to, čo je potreba na chod aplikácia (všetko ostatné
je zvyšovaním pravdepodobnosti, že sa niečo rozbije)


### Continuous Delivery
Aký je rozdieľ medzi continuous integration a continuous delivery??

Ide v princípe o veľmi podobné veci a rozdieľ je len v tom, že otestované a
pripravené balíčky sa automaticky deploynú na produkčný server.
Množstvo práce, ktoré sa za týmto malým rozdieľom skrýva je však veľké.

Release candidate by mal prejsť cez sériu akceptačných testov, ktoré skutočne
zaručia, že aplikácia bude fungovať.

Ak používame viacero serverov a nejaký balancer, treba deployovať postupne po
serveroch s nejakým rozostupom aby sme nespôsobili veľký down time.

Taktiež treba mať v rukáve monitoring a upozorňovanie ak sa niečo pokazí, aby sme
deploy mohli včas zastaviť a spraviť rollback na pôvodnú verziu.

Jeden z príkladov ako sa to dá spraviť je ten, že každý produkčný web server
alebo iné servery, sa pravideľne pozerajú na nejaký metadata súbor, ktorý popisuje
aktuálnu verziu applikácie poslednej verzie vhodnej pre release. Tieto servery
si tak prevezmú svoju verziu asynchrónne čo umožňuje mnoho iných praktík.


#### Zero down time releases and roll backs

Celkom veľké momentum zbiera docker, ktorý sa tiež dá použiť na CD.
TODO: čo je docker
TODO: výhoda toho je tá, že celé produkčné prostredie len hot swap za inú verziu.
to je všetko. Veľmi rýchle konzistentné a ak sa niečo pokazí, stačí spustiť
kontajner so starou verziou.

## Otázky (5 min)
?

## Zdroje

[1]: http://martinfowler.com/bliki/AntiPattern.html
[2]: http://martinfowler.com/bliki/TechnicalDebt.html
