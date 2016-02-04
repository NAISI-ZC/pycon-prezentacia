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

Všetky tieto súbory si verziujeme v gite.

Potrebovali by sme vytvoriť izolovanejšie prostredie na svojej mašine.Môžeme
použiť virtualenv na správu svojich potrebných python balíčkov. Mne osobne sa
už veľa krát stalo, že na dev používam mac os x ale služba beží na linux.
Dokonca niekedy potrebujem pracovať aj na windows os. Po čase začne byť
nastavovanie python po rôznych os únavné. A navyše nie všetko funguje rovnako
pod každým OS. Preto radšej používam Vagrant. Takýmto spôsobom sa dokážem
najviac priblížiť produkčnému prostrediu a zároveň mať zhotovené funkčné dev
prostredie behom prá minúť. Stačí virtualizácia cez virtualbox a som vybavený.

Ďalšou výhodou ako som už spomenul je niele to, že pracujem na podobnom prostredí
ako je produkčné, môžem si dokonca skúšať priamo konfigurácie web serverov
s mojou aplikáciou a podobne.

__note: dev prostredie je nastavené__
Takže momentálne mám nastavené svoje DEV prostredie.

Potreboval by som nájsť spôsob ako balíčkovať svoju aplikáciu aby som mohol
tento balíček jednoducho deployovať do test prostredia a samozrejme do produkčného
prostredia.

Použijem na to CI server.
__note: stretávame s CI__


