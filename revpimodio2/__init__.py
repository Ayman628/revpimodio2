# -*- coding: utf-8 -*-
#
# python3-RevPiModIO
#
# Webpage: https://revpimodio.org/
# (c) Sven Sager, License: LGPLv3
#
"""Stellt alle Klassen fuer den RevolutionPi zur Verfuegung.

Stellt Klassen fuer die einfache Verwendung des Revolution Pis der
Kunbus GmbH (https://revolution.kunbus.de/) zur Verfuegung. Alle I/Os werden
aus der piCtory Konfiguration eingelesen und mit deren Namen direkt zugreifbar
gemacht. Fuer Gateways sind eigene IOs ueber mehrere Bytes konfigurierbar
Mit den definierten Namen greift man direkt auf die gewuenschten Daten zu.
Auf alle IOs kann der Benutzer Funktionen als Events registrieren. Diese
fuehrt das Modul bei Datenaenderung aus.

"""
import warnings

from .modio import *

__all__ = ["RevPiModIO", "RevPiModIOSelected", "RevPiModIODriver"]
__author__ = "Sven Sager <akira@revpimodio.org>"
__name__ = "revpimodio2"
__package__ = "revpimodio2"
__version__ = "2.0.1"

# Global package values
OFF = 0
GREEN = 1
RED = 2
RISING = 31
FALLING = 32
BOTH = 33

warnings.simplefilter(action="always")


def consttostr(value):
    """Gibt <class 'str'> fuer Konstanten zurueck.

    Diese Funktion ist erforderlich, da enum in Python 3.2 nicht existiert.

    @param value Konstantenwert
    @return <class 'str'> Name der Konstanten

    """
    if value == 0:
        return "OFF"
    elif value == 1:
        return "GREEN"
    elif value == 2:
        return "RED"
    elif value == 31:
        return "RISING"
    elif value == 32:
        return "FALLING"
    elif value == 33:
        return "BOTH"
    else:
        return ""
