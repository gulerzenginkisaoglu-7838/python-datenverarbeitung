"""Objektorientierte Programmierung (OOP) mit Python.

Das Beispiel zeigt vier Grundprinzipien der OOP:
- Abstraktion:    abstrakte Basisklasse mit Pflichtmethode
- Vererbung:      konkrete Klassen erben von der Basisklasse
- Kapselung:      Attribut ist privat und nur über eine Methode lesbar
- Polymorphie:    gleiche Methode, je nach Klasse anderes Verhalten
"""

from abc import ABC, abstractmethod


class Telefon(ABC):
    """Abstrakte Basisklasse: legt fest, was jedes Telefon können muss."""

    @abstractmethod
    def entsperren(self):
        """Pflichtmethode. Jede Unterklasse muss sie selbst umsetzen."""


class IPhone(Telefon):
    def __init__(self, modell, akkuzustand):
        self.modell = modell                  # öffentliches Attribut
        self.__akkuzustand = akkuzustand      # privates Attribut (Kapselung)

    def get_akkuzustand(self):
        """Getter: einziger Zugriff auf das private Attribut."""
        return f"Akkuzustand: {self.__akkuzustand} %"

    def entsperren(self):
        return f"{self.modell}: Entsperrt per Gesichtserkennung"


class Samsung(Telefon):
    def __init__(self, modell):
        self.modell = modell

    def entsperren(self):
        return f"{self.modell}: Entsperrt per Fingerabdruck"


class Konto:
    """Einfaches Beispiel für Zustand und Methoden eines Objekts."""

    def __init__(self, kontostand):
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def auszahlen(self, betrag):
        self.kontostand -= betrag


if __name__ == "__main__":
    mein_iphone = IPhone("iPhone 15", 98)
    mein_samsung = Samsung("Galaxy S24")

    print("[1] Kapselung")
    print(mein_iphone.get_akkuzustand())

    print("\n[2] Polymorphie")
    for telefon in (mein_iphone, mein_samsung):
        print(telefon.entsperren())

    print("\n[3] Konto")
    konto = Konto(100)
    konto.einzahlen(50)
    konto.auszahlen(30)
    print(f"Kontostand: {konto.kontostand}")
