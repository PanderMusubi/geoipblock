_For English, see [README.md](README.md)_

# geoipblock

Blokkeer netwerkverkeer voor IP-adressen van bepaalde landen.

> <em>Het enige goed is kennis en het enige kwaad is onwetendheid.</em> — Socrates (469 – 399 v.Chr.) Griekse filosoof in Athene

## 1 Inleiding

In onze steeds meer onderling verbonden wereld worden wereldwijde IT-infrastructuren geconfronteerd met meedogenloze bedreigingen van hackers, malware en de complexiteit van het handhaven van internationale sancties. Dit is gemiddeld 30%-60% van al het netwerkverkeer. Het is mogelijk om verkeer voor webservers, e-mailservers, etc. te filteren op basis van het IP-adres van een land, maar elk vereist een aparte installatie, configuratie en onderhoud en biedt geen volledige bescherming.

Het blokkeren van hele landen op de netwerklaag biedt een robuustere oplossing om verstorend en gesanctioneerd verkeer volledig buiten te houden.

Deze documentatie, genaamd geoipblock, legt uit hoe je xtables-addons kunt gebruiken om al het inkomende en uitgaande verkeer op alle poorten op Linux-servers voor IP-gebaseerde geografische locaties te blokkeren, wat een sterkere, gecentraliseerde barrière creëert.

Het installeren van xtables-addons maakt een server niet alleen veiliger en ontzegt toegang aan gesanctioneerde landen, het vermindert ook de serverbelasting aanzienlijk, wat resulteert in een duurzamere situatie met een lager stroomverbruik.

Zie ook https://inai.de/projects/xtables-addons/geoip.php en https://codeberg.org/jengelh/xtables-addons voor meer technische informatie. Indien jouw organisatie netwerkhardware van Cisco Systems, Juniper, etc. gebruikt, is het ook mogelijk om blokkering te configureren op IP-gebaseerde geografische locaties.

## 2 Landen

Landen kunnen worden geblokkeerd op basis van landcode. De lijst met codes die door xtables-addons worden ondersteund, is te vinden op https://db-ip.com/faq.php. Let op: er zijn ook enkele aanvullende codes naast die van [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).

Zo is er bijvoorbeeld een lijst met landen samengesteld op basis van [sancties van de EU en/of de Verenigde Naties](https://www.sanctionsmap.eu/). Dit is niet alleen bedoeld om sancties af te dwingen, maar het is ook bekend of zeer waarschijnlijk dat deze landen kwaadaardig verkeer naar EU-landen niet voorkomen. In verschillende gevallen creëren zelfs de overheden van deze landen actief kwaadaardig verkeer.

Landen met alleen persoonlijke sancties zijn niet opgenomen. Sommige landen die sancties zouden moeten hebben, maar die door een minderheidsveto zijn verhinderd, zijn wel opgenomen. Nogmaals, dit is slechts een voorbeeld dat wordt geïllustreerd door de onderstaande kaart en tabel.

[![Example map](example_map.png)](example_map.png)

| Code | Vlag | Land                                              |
|------|------|---------------------------------------------------|
| `AF` | 🇦🇫   | Afghanistan, Islamitisch Emiraat                  |
| `BY` | 🇧🇾   | Wit-Rusland (Republiek Belarus)                   |
| `CF` | 🇨🇫   | Centraal-Afrikaanse Republiek                     |
| `CN` | 🇨🇳   | China, Volksrepubliek                             |
| `CD` | 🇨🇩   | Democratische Republiek Congo                     |
| `HT` | 🇭🇹   | Haïti, Republiek                                  |
| `HK` | 🇭🇰   | Hong Kong (speciale bestuurlijke regio van China) |
| `IL` | 🇮🇱   | Israël, Staat                                     |
| `IR` | 🇮🇷   | Iran, Islamitische Republiek                      |
| `MM` | 🇲🇲   | Myanmar, Republiek van de Unie van                |
| `MO` | 🇲🇴   | Macao (speciale bestuurlijke regio van China)     |
| `KP` | 🇰🇵   | Noord-Korea (Democratische Volksrepubliek Korea)  |
| `LY` | 🇱🇾   | Libië, Staat                                      |
| `RU` | 🇷🇺   | Rusland (Russische Federatie)                     |
| `SD` | 🇸🇩   | Soedan, Republiek                                 |
| `SO` | 🇸🇴   | Somalië, Federale Republiek                       |
| `SS` | 🇸🇸   | Zuid-Soedan, Republiek                            |
| `SY` | 🇸🇾   | Syrië, Arabische Republiek                        |
| `VE` | 🇻🇪   | Venezuela, Bolivariaanse Republiek                |
| `YE` | 🇾🇪   | Jemen, Republiek                                  |
| `ZW` | 🇿🇼   | Zimbabwe, Republiek                               |

Om verkeer uit deze landen te blokkeren, gebruik je de onderstaande codes, waar `XX, YY, ZZ` staat:

    AF, BY, CF, CN, CD, HT, HK, IL, IR, MM, MO, KP, LY, RU, SD, SO, SS, SY, VE, YE, ZW

Om een goed inzicht te krijgen in de landen die jouw infrastructuur gebruiken, kun je web analytics gebruiken zoals [GoAccess](https://en.wikipedia.org/wiki/GoAccess). Stel dat jouw infrastructuur alleen gericht is op zeer lokaal gebruik, dan kun je de toegang tot jouw infrastructuur blokkeren voor landen aan de andere kant van de wereld. Dit heeft geen invloed op jouw doelgroep en leidt tot minder verspilling van resources.

Zie bijvoorbeeld de volgende kaart voor een website in een Europees land waar 67% van de 7,78 GB aan verkeer niet eens uit Europa afkomstig is.

[![GoAccess map](goaccess-map.png)](goaccess-map.png)

Natuurlijk is het mogelijk om deze blokkade te omzeilen met behulp van een VPN. Het resterende schadelijke verkeer, dat veel minder is, kan bijvoorbeeld worden geblokkeerd met [Fail2Ban](https://en.wikipedia.org/wiki/Fail2ban).

## 3 Ubuntu

### 24.04 LTS Noble Numbat

Deze distributie biedt xtables-addons 3.25. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 23.10 Mantic Minotaur

Deze distributie biedt xtables-addons 3.24. Installeer softwarepakketten volgens de vorige instructies hieronder.

Deze distributie biedt xtables-addons 3.23. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 22.10 Kinetic Kudu

Deze distributie biedt xtables-addons 3.21. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 22.04 LTS Jammy Jellyfish

Deze distributie biedt xtables-addons 3.19. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 21.10 Impish Indri

Deze distributie biedt xtables-addons 3.18. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 21.04 Hirsute Hippo

Deze distributie biedt xtables-addons 3.13. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir -p /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s > /dev/null
    cd && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

### 20.04 LTS Focal Fossa

Deze distributie biedt xtables-addons 3.9. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo chmod a+x /usr/lib/xtables-addons/xt_geoip_build
    sudo mkdir -p /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/lib/xtables-addons/xt_geoip_dl
    /usr/lib/xtables-addons/xt_geoip_build -D /usr/share/xt_geoip/ > /dev/null
    cd && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

### 18.04 LTS Bionic Beaver

Deze distributie biedt xtables-addons 3.0. xtables-addons gebruikt hier alleen de maxmind geo IP database. Echter, die database is nu beschikbaar via een andere URL dan xtables-addons verwachtneeds it to be. Verder is deze versie van xtables-addons nogal oud.

Deze handleiding heeft nog geen oplossing voor het issue met de database, maar
het bijdragen van een oplossing is welkom.

## 4 Debian

### 13 Trixie

Deze distributie biedt xtables-addons 3.25. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 12 Bookworm

Deze distributie biedt xtables-addons 3.23. Installeer softwarepakketten volgens de vorige instructies hieronder.

### 11 Bullseye

Deze distributie biedt xtables-addons 3.13. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir -p /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s > /dev/null
    cd && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## 5 Testen

Test de installatie met

    sudo modprobe xt_geoip
    lsmod | grep ^xt_geoip
    sudo /etc/cron.daily/xt_geoip
    ls /usr/share/xt_geoip/

WAARSCHUWING: De volgende commando's kunnen jou en alle anderen van je systeem buitensluiten!

Zoek de landcodes op van de te blokkeren landen op https://db-ip.com/faq.php en let op dat er ook een aantal extra codes beschikbaar zijn. Gebruik de codes in plaats van `XX,YY,ZZ` hieronder. Een voorbeeld is `BY,CH,HK,IR,KP,RU`.

Blokkeer inkomende netwerkpakketten door deze regels (rules) toe te voegen

    iptables -I INPUT -m geoip --src-cc XX,YY,ZZ -j DROP
    ip6tables -I INPUT -m geoip --src-cc XX,YY,ZZ -j DROP

Blokkeer ook uitgaande netwerkpakketten door deze regels (rules) toe te voegen

    iptables -A OUTPUT -m geoip --dst-cc XX,YY,ZZ -j DROP
    ip6tables -A OUTPUT -m geoip --dst-cc XX,YY,ZZ -j DROP

Tot en met versie 3.23 is het maximum aan te blokkeren landen vijftien. Het maximaal aantal landen is 31 vanaf versie 3.24. Alle regels (rules) kunnen worden getoond met

    sudo iptables -L --line-numbers
    sudo ip6tables -L --line-numbers

Er kan bijvoorbeeld getest worden op een mobiel apparaat met een gratis VPN van Android-appstores zoals [Google Play](https://play.google.com/store/apps/details?id=ch.protonvpn.android) en [F-Droid](https://f-droid.org/en/packages/ch.protonvpn.android/) of de [App Store](https://apps.apple.com/us/app/protonvpn-fast-secure-vpn/id1437005085) voor iOS. Het kan zijn dat ze niet de specifieke landen die je wil blokkeren aanbieden, maar voor testdoeleinden via de gratis beschikbare landen is dit nutig.

Regels (rules) kunnen worden verwijderd met

    sudo iptables -D INPUT 1
    sudo iptables -D OUTPUT 1
    sudo ip6tables -D INPUT 1
    sudo ip6tables -D OUTPUT 1

waar het nummer het regelnummer is van de regel (rule) die verwijderd moet worden.

## 6 Configuratie

Maak het iptables-commando blijvend (persistent) door eerst de huidige configuratie op te slaan met

    iptables-save > rules
    ip6tables-save > rules6

Alleen als de regels met `-I INPUT -m geoip ... -j DROP` of `-A OUTPUT -m geoip ... -j DROP` ontbreken, volg de volgende editinstructie. Dit kan resulteren in een leeg bestand of iets dat eruitziet als

    # Generated by iptables-save ...
    *filter
    :INPUT ACCEPT [0:0]
    :FORWARD ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    ...
    COMMIT
    # Completed on ...

Wijzig beide bestanden door alleen de volgende twee regels toe te voegen

    *filter
    :INPUT ACCEPT [0:0]
    :FORWARD ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    -I INPUT -m geoip --src-cc XX,YY,ZZ -j DROP
    ...
    -A OUTPUT -m geoip --dst-cc XX,YY,ZZ -j DROP
    COMMIT

Sla op en activeer de nieuwe configuratie met

    iptables-restore < rules
    ip6tables-restore < rules6

Controleer de resulterende wijzigingen met

    sudo iptables -L -v
    sudo ip6tables -L -v

## 7 Probleemoplossen

Effect van een test of blijvende configuratie kan worden gemonitord met

    tail -f /var/log/kern.log

## 8 De-installatie

De-installatie kan worden gedaan met

    sudo apt-get purge xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo apt-get -y autoremove
    sudo rm -rf /etc/cron.daily/xt_geoip /usr/share/xt_geoip/

## 9 Zie ook

Zie ook:
- https://packages.ubuntu.com/search?keywords=xtables-addons
- https://packages.debian.org/search?keywords=xtables-addons
- https://software.opensuse.org/package/xtables-addons
- https://wiki.ubuntu.com/Releases
- https://wiki.debian.org/DebianReleases

