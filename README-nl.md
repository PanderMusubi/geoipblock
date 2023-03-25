_For English, see [README.md](README.md)_

# geoipblock

Blokkeer netwerkverkeer op IP-adres voor bepaalde landen.

> <em>Het enige goed is kennis en het enige kwaad is onwetendheid.</em> —
Socrates (469 – 399 v.Chr.) Griekse filosoof in Athene

Deze handleiding beschrijft hoe xtables-addons te gebruiken om inkomende en
uitgaande netwerkpakketten tegen te houden voor alle poorten voor bepaalde
landen. Zie ook https://inai.de/projects/xtables-addons/geoip.php voor meer
documentatie.

(Voor Debian, zie verder onderaan.)

## Ubuntu 23.04 Lunar Lobster

Deze distributie biedt xtables-addons 3.23.  Deze distributie is nog niet
uitgebracht.

## Ubuntu 22.10 Kinetic Kudu

Deze distributie biedt xtables-addons 3.21. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 22.04 LTS Jammy Jellyfish

Deze distributie biedt xtables-addons 3.19. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 21.04 Hirsute Hippo

Deze distributie biedt xtables-addons 3.13. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 21.10 Impish Indri

Deze distributie biedt xtables-addons 3.18. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 21.04 Hirsute Hippo

Deze distributie biedt xtables-addons 3.13. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 20.04 LTS Focal Fossa

Deze distributie biedt xtables-addons 3.9. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo chmod a+x /usr/lib/xtables-addons/xt_geoip_build
    sudo mkdir /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/lib/xtables-addons/xt_geoip_dl
    /usr/lib/xtables-addons/xt_geoip_build -D /usr/share/xt_geoip/
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 18.04 LTS Bionic Beaver

Deze distributie biedt xtables-addons 3.0. xtables-addons gebruikt hier alleen
de maxmind geo IP database. Echter, die database is nu beschikbaar via een
andere URL dan xtables-addons verwachtneeds it to be. Verder is deze versie van
xtables-addons nogal oud.

Deze handleiding heeft geen oplossing voor het issue met de database, maar het
bijdragen van een oplossing is welkom.

## Debian 12 Bookworm

Deze distributie biedt xtables-addons 3.23. Deze distributie is nog niet
uitgebracht.

## Debian 11 Bullseye

Deze distributie biedt xtables-addons 3.13. Installeer softwarepakketten met

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Maak het bestand `/etc/cron.daily/xt_geoip` met daarin

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

en geef dat bestand uitvoeringsrechten met

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Testen

Test de installatie met

    sudo modprobe xt_geoip
    lsmod | grep ^xt_geoip
    sudo iptables -m geoip -h
    sudo /etc/cron.daily/xt_geoip
    ls /usr/share/xt_geoip/

WAARSCHUWING: De volgende commando's kunnen jou en alle anderen van je systeem
buitensluiten!

Zoekde landcodes op van de te blokkeren landen op https://db-ip.com/faq.php
en let op dat er ook een aantal extra codes beschikbaar zijn. Gebruik de codes
in plaats van `XX,YY` hieronder. Up to and including version 3.23, the maximum
number of countries to block is fifteen. The maximum number of countries for
newer versions is 31.

Blokkeer inkomende netwerkpakketten door deze regels (rules) toe te voegen

    iptables -I INPUT -m geoip --src-cc XX,YY -j DROP
    ip6tables -I INPUT -m geoip --src-cc XX,YY -j DROP

Blokkeer ook uitgaande netwerkpakketten door deze regels (rules) toe te voegen

    iptables -A OUTPUT -m geoip --dst-cc XX,YY -j DROP
    ip6tables -A OUTPUT -m geoip --dst-cc XX,YY -j DROP

Alle regels (rules) kunnen worden getoond met

    sudo iptables -L --line-numbers
    sudo ip6tables -L --line-numbers

Er kan bijvoorbeeld getest worden op een mobiel apparaat met een gratis VPN van
Android-appstores zoals
[Google Play](https://play.google.com/store/apps/details?id=ch.protonvpn.android)
en
[F-Droid](https://f-droid.org/en/packages/ch.protonvpn.android/) of de
[App Store](https://apps.apple.com/us/app/protonvpn-fast-secure-vpn/id1437005085)
voor iOS. This might not offer the specific countries to block, but for testing
temporarily via the freely available countries, this is useful.

Regels (rules) kunnen worden verwijderd met

    sudo iptables -D INPUT 1
    sudo iptables -D OUTPUT 1
    sudo ip6tables -D INPUT 1
    sudo ip6tables -D OUTPUT 1

waar het nummer het regelnummer is van de regel (rule) die verwijderd moet worden.

## Configuratie

Maak het iptables-commando blijvend door eerst de huidige configuratie op te
slaan met

    iptables-save > rules
    ip6tables-save > rules6

Dit kan resulteren in een leeg bestand of iets dat eruitziet als

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
    -I INPUT -m geoip --src-cc XX,YY -j DROP
    ...
    -A OUTPUT -m geoip --dst-cc XX,YY -j DROP
    COMMIT

Sla op en activeer de nieuwe configuratie met

    iptables-restore < rules
    ip6tables-restore < rules6

Controleer de resulterende wijzigingen met

    sudo iptables -L -v
    sudo ip6tables -L -v

## Optimalisatie

Vervang de laatste regen in het bestand `/etc/cron.daily/xt_geoip` met

    cd /usr/share/xt_geoip/ && rm $(ls|grep -v XX|grep -v YY) && rm -rf ${workdir}

die bestanden verwijderd voor de landen die niet geblokkeerd moeten worden.

VRAAG: Gebruiken van `rm !(XX.iv?|YY.iv?)` in dit cron-bestand resulteert in de
fout `Syntax error: "(" unexpected`, vandaar het gebruik van `grep`. Bijdragen
om dit te fiksen zijn welkom.

## Probleemoplossen

Effect van een test of blijvende configuratie kan worden gemonitord met

    tail -f /var/log/kern.log

## Zie ook

Zie ook:
- https://packages.ubuntu.com/search?keywords=xtables-addons
- https://packages.debian.org/search?keywords=xtables-addons
- https://software.opensuse.org/package/xtables-addons

