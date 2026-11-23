# Importiert das eingebaute JSON-Modul, um JSON-Dateien verarbeiten zu können.
import json

# Definiert den relativen Pfad zur JSON-Datei im Unterordner.
dateipfad = 'daten.json'

# Try-Except-Block fängt potenzielle Fehler ab, falls die Datei fehlt.
try:
    # Öffnet die Datei im Lesemodus ('r') mit UTF-8 Kodierung für Umlaute.
    with open(dateipfad, 'r', encoding='utf-8') as datei:
        # Konvertiert den JSON-Inhalt in eine Python-Liste aus Dictionaries.
        daten = json.load(datei)

    # Gibt eine einfache Trennlinie auf der Konsole aus.
    print("--- Aus der JSON-Datei gelesene Daten ---")

    # Iteriert durch jede Person (Dictionary) in der geladenen Liste.
    for person in daten:
        # Gibt den Wert des Schlüssels 'name' aus.
        print(f"Name: {person['name']}")

        # Gibt den Wert des Schlüssels 'alter' aus.
        print(f"Alter: {person['alter']}")

        # Gibt den Wert des Schlüssels 'beruf' aus.
        print(f"Beruf: {person['beruf']}")

        # Verbindet die Listenelemente der Interessen mit Komma und Leerzeichen.
        interessen_str = ", ".join(person['interessen'])

        # Gibt die formatierten Interessen als einen Textstring aus.
        print(f"Interessen: {interessen_str}")

        # Erzeugt eine visuelle Trennlinie (40 Bindestriche) nach jeder Person.
        print("-" * 40)

# Wird ausgeführt, wenn der angegebene Pfad oder die Datei nicht existiert.
except FileNotFoundError:
    # Gibt eine Fehlermeldung mit dem falschen Pfad aus.
    print(f"Fehler: Datei '{dateipfad}' wurde nicht gefunden!")
