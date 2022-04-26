# geoipblock

Block network traffic for IP addresses of specific countries. This manual
describes how to use xtables-addons to drop incoming and outgoing packages for
all or certain ports. See also
https://inai.de/projects/xtables-addons/geoip.php for more documentation.

## Ubuntu 22.04 LTS Jammy Jellyfish

This distribution offers xtables-addons 3.19. Install packages with

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Create the file `/etc/cron.daily/xt_geoip` containing

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

and give that file execution rights with

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 21.04 Hirsute Hippo

This distribution offers xtables-addons 3.13. Install packages with

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Create the file `/etc/cron.daily/xt_geoip` containing

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

and give that file execution rights with

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 21.10 Impish Indri

This distribution offers xtables-addons 3.18. Install packages with

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl

Create the file `/etc/cron.daily/xt_geoip` containing

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

and give that file execution rights with

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 21.04 Hirsute Hippo

This distribution offers xtables-addons 3.13. Install packages with

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Create the file `/etc/cron.daily/xt_geoip` containing

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

and give that file execution rights with

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 20.04 LTS Focal Fossa

This distribution offers xtables-addons 3.9. Install packages with

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo chmod a+x /usr/lib/xtables-addons/xt_geoip_build
    sudo mkdir /usr/share/xt_geoip/

Create the file `/etc/cron.daily/xt_geoip` containing

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/lib/xtables-addons/xt_geoip_dl
    /usr/lib/xtables-addons/xt_geoip_build -D /usr/share/xt_geoip/
    cd ${HOME} && rm -rf ${workdir}

and give that file execution rights with

    sudo chmod a+x /etc/cron.daily/xt_geoip

## Ubuntu 18.04 LTS Bionic Beaver

This distribution offers xtables-addons 3.0. Here xtables-addons uses only the
maxmind geo IP database. However, that database is now available under another
URL than xtables-addons needs it to be. Additionally, this version of
xtables-addons is rather old to what is available.

This manual has not have a workaround for the database issue, but contributing
a workaround is welcome.

## Debian 11 Bullseye

This distribution offers xtables-addons 3.13. Install packages with

    sudo apt-get install -y xtables-addons-common libtext-csv-xs-perl libnet-cidr-lite-perl
    sudo mkdir /usr/share/xt_geoip/

Create the file `/etc/cron.daily/xt_geoip` containing

    #!/bin/sh -e
    workdir=$(mktemp -d)
    cd ${workdir}
    /usr/libexec/xtables-addons/xt_geoip_dl
    /usr/libexec/xtables-addons/xt_geoip_build -s
    cd ${HOME} && rm -rf ${workdir}

and give that file execution rights with

    sudo chmod a+x /etc/cron.daily/xt_geoip
## Testing

Test the installation with

    sudo modprobe xt_geoip
    lsmod | grep ^xt_geoip
    sudo iptables -m geoip -h
    sudo /etc/cron.daily/xt_geoip
    ls /usr/share/xt_geoip/

WARNING: The following commands can lock you and all others out of your machine!

Look up the country codes of the countries to block at https://db-ip.com/faq.php
and note there are also some additional codes available. Use the codes instead
of `XX,YY` below.

Block incoming packages by adding these rules

    iptables -I INPUT -m geoip --src-cc XX,YY -j DROP
    ip6tables -I INPUT -m geoip --src-cc XX,YY -j DROP

Also block outgoing packages by adding these rules

    iptables -A OUTPUT -m geoip --dst-cc XX,YY -j DROP
    ip6tables -A OUTPUT -m geoip --dst-cc XX,YY -j DROP

All rules can be listed with

    sudo iptables -L --line-numbers
    sudo ip6tables -L --line-numbers

Testing can be done on a mobile device by using a free VPN from
Android app stores such as
[Google Play](https://play.google.com/store/apps/details?id=ch.protonvpn.android)
and
[F-Droid](https://f-droid.org/en/packages/ch.protonvpn.android/) or the
[App Store](https://apps.apple.com/us/app/protonvpn-fast-secure-vpn/id1437005085)
for iOS. This might not offer the specific countries to block, but for testing
temporarily via the freely available countries, this is useful.

Rules can be deleted with

    sudo iptables -D INPUT 1
    sudo iptables -D OUTPUT 1
    sudo ip6tables -D INPUT 1
    sudo ip6tables -D OUTPUT 1

where the number is the line number of the rule to delete.    

## Configuration

Make the iptables command persistent by first saving the current configuration
with

    iptables-save > rules
    ip6tables-save > rules6

This can result in an empty file or something that looks like

    # Generated by iptables-save ...
    *filter
    :INPUT ACCEPT [0:0]
    :FORWARD ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    ...
    COMMIT
    # Completed on ...

Change both files by only adding these two lines

    *filter
    :INPUT ACCEPT [0:0]
    :FORWARD ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    -I INPUT -m geoip --src-cc XX,YY -j DROP
    ...
    -A OUTPUT -m geoip --dst-cc XX,YY -j DROP
    COMMIT

Store and activate the new configuration with

    iptables-restore < rules
    ip6tables-restore < rules6

Check the resulting changes with

    sudo iptables -L -v
    sudo ip6tables -L -v

## Optimization

Replace the last line of the file `/etc/cron.daily/xt_geoip` with

    cd /usr/share/xt_geoip/ && rm $(ls|grep -v XX|grep -v YY) && rm -rf ${workdir}

which removes files for countries that are not to be blocked.

QUESTION: Using `rm !(XX.iv?|YY.iv?)` in this cron file results in the error
`Syntax error: "(" unexpected`, hence the use of `grep`. Contribution how to fix
this is welcome.

## Troubleshooting

Effect of the test or persistent configuration can be monitored with

    tail -f /var/log/kern.log

## See also

See also and preferably give a thumbs up for the following issues:
- https://gitlab.nic.cz/turris/reforis/reforis/-/issues/379
- https://github.com/openwrt/luci/issues/5722
