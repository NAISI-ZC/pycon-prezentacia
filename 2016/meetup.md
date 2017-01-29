# Meetup demo

Niekoľko poznámok ohľadom ukážky na pycon meetupe


## Použitý hardware

Použiť by som chcel svoj virtualizačný lab. Lepšie bude, ak ho ponechám doma a
radšej si spristupnim DMZ


## Obsah ukážky

Išlo by o jednoduchú applikáciu na poznámky. Táto web applikácia by bola dobrá
ukážka ako sa robí taká aplikácia, aké nátroje môžem použiť, ktoré by
v budúcnosti uľahšia niektoré kroky.


Applikácia sa volá - NoteB00k

backend je spravený vo Flasku. Backend sprístupňuje REST API, pomocou ktorého
klient pristupuje k dátam.

Klient bude napísaný v javascripte, CSS, HTML a už bude hotový, tak isto ako
backend.

Backend sa bude testovať pomocou RAML. RAML slúži na definíciu API. Pomocou
tohto jazyka vieme designovať a zároveň testovať naše API. Zároveň vieme
jednoducho spraviť mocking server.


Potrebovali by sme vytvoriť izolovanejšie prostredie na svojej mašine.Môžeme
použiť virtualenv na správu svojich potrebných python balíčkov. Mne osobne sa
už veľa krát stalo, že na dev používam mac os x ale služba beží na linux.
Dokonca niekedy potrebujem pracovať aj na windows os. Po čase začne byť
nastavovanie python po rôznych os únavné. A navyše nie všetko funguje rovnako
pod každým OS. Preto radšej používam Vagrant. Takýmto spôsobom sa dokážem
najviac priblížiť produkčnému prostrediu a zároveň mať zhotovené funkčné dev
prostredie behom prá minúť. Stačí virtualizácia cez virtualbox a som vybavený.

Ja osobne nemám veľa skúseností s config managementom, stále je to vec, ktorú
sa mi nepodarilo poriadne uchopiť. Preto na nastavenie cez vagrant používam
obyčajný shell script. Je to jednoduché a rýchle.

Väčšinou postupuje tak, že si spravím nejaký basic script na prípravu pythonu,
nejkých základných balíčkov, pip, virtualenv 

Ďalšou výhodou ako som už spomenul je niele to, že pracujem na podobnom prostredí
ako je produkčné, môžem si dokonca skúšať priamo konfigurácie web serverov
s mojou aplikáciou a podobne.


Existuje [tool][1], pomocou ktorého sa dá automatizovať aj vytváranie virtuálnych
mašín, ktoré sa používajú. Toto je užitočné v prípade, keď človek potrebuje
aktualizované prostredie na pravideľnej báze. Ľahko sa to dá automatizovať
a prináša to so sebou mnohé výhody.


__note: dev prostredie je nastavené__
Takže momentálne mám nastavené svoje DEV prostredie.

Potreboval by som nájsť spôsob ako balíčkovať svoju aplikáciu aby som mohol
tento balíček jednoducho deployovať do test prostredia a samozrejme do produkčného
prostredia.

Použijem na to CI server.
__note: stretávame s CI__


TODO:
 * codecov
 * embedable build status
 * github plugin for build status updates 
 * [How to make python package][2]
 * building python on [travis CI][3]
 * odtazka - musim pouzit virtualenv ked aj tak pouzivam vagrant? [ano][4]




[1]: https://www.packer.io/intro/use-cases.html
[2]: https://docs.python.org/2/distutils/index.html#distutils-index
[3]: https://docs.travis-ci.com/user/languages/python
[4]: http://stackoverflow.com/a/18273476/1589921
