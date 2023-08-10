

# Einführung

In unserer heutigen Gesellschaft ist Zeitersparnis oftmals ein wichtiges Thema. Bevor wir rausgehen, überprüfen wir meist mithilfe einer unserer Apps auf dem Handy, wie sich das Wetter entwickeln wird. Doch wie wäre es mit einer Alternative für Zuhause? Eine welche uns wieder etwas vom Smartphone weg bringt?

# Problemstellung

- Heutzutage gibt es sogut wie für alles eine App, doch ist dies wirklich so gut? Viele Menschen verbringen schon einen großen Teil ihrer Zeit mit iherem Smartphone. Besonders bei den jüngeren Generationen ist gelegentlich zu beobachten, wie manch einer fast vergisst sein normales Leben zu leben, weil er zu tief versunken ist. Doch gibt es eine Möglichkeit diesem Problem entgegenzuwirken? Es wäre schön, wenn Lösungen für Probleme wieder mehr werden als eine App auf dem Handy.
- Um das Problem auf einen kleineren Bereich zu beschränken, soll der Fokus hier auf Wetter Apps liegen. Eine bisherige Alternative zu diesen sind der Wetterbericht in Zeitung, Radio oder Fernsehen, als auch physische Displays für die Anzeige der lokalen Wetterdaten. Interssant ist die Frage, wie man diese physischen Wetteranzeigen etwas spannender machen kann oder möglicherweise dafür sorgt, dass diese nicht nur wieder einen weiteren Platz im Regal wegnehmen?


# Lösungsansatz

Eine prominente Idee für die Lösung des Problems war, das Anzeigen von Wetterdaten intuitiv in andere Alltagsgegenstände zu integrieren, ohne diese mit Informationen zu überladen.

## Kombination: Uhr

Diese Kombination hat die Vorteile, dass für einen großteil Nutzer Wetterdaten, wie Temperatur, Bewölkungsgrad, Regenwahrscheinlichkeit meist in Zusammenhang mit der gegebenen Uhrzeit gebraucht werden.
Außerdem ist ein Blick auf die Uhr an der Wand durchaus intuitiver, häufiger und etwas leichter, als das Handy zu entsperren und die jeweilge App oder das jeweilge Widget zu suchen.

# Idee und Skizzen

![image](https://i.imgur.com/MMtGajV.jpg)


# Planung

## Im Bereich Software

- WiFi connect (WPS?)
- Standort durch IP?
- Wetter API pull
- Wetterdaten zu Signalen gemapt
- Signale an Leds gesendet
- Spracherkennung sorgt für Wechsel der Led-Anzeige (Wetter, Temperatur, Sonnenauf- und Untergang)

## Im Bereich Hardware

- Led-Leuchtbogen
- standard Wanduhr
- Arduino Nano 2040rp connect
- 5V Batterie / Netzteil

# Umsetzung

Als erstes war es wichtig, überhaupt an Wetterdaten zu gelangen und festzustellen, in welchem Format diese erhalten werden. Diese Funktion übernahm zunächst ein alleinstehendes Python-Skript, welches kostenfrei stündlich die lokalen Wetterdaten von der API der Website open-meteo.com bezog.
Um diesen Service auf dem Arduino auszuführen, musste zunächst eine Internetverbindung hergestellt werden. Genutzt wurde dafür eine Abwandlung eines Beispielskriptes für WifiNINA.
Als nächsten Schritt folgte ein Versuch beide Skripte zu kombinieren, indem das Python-Skript in C++ abgewandelt werden sollte.Allerdings gab es einige Probleme, auf diese Weise eine vernünftig gesicherte Verbindung zu der Website aufzubauen. Außerdem stellte es sich als deutlich aufwendiger heraus, die Wetterdaten geordnet zwischenzuspeichern um diese verarbeiten zu können.
Um dieses Problem zu lösen spielt die Verwendung von MikroPython in der Entwicklungsumgebung "Thonny" eine Rolle. MikroPython läuft auf dem Arduino ebenso wie C++, nur halt in Python. Ein kurzes Skript zum Test befindet sich im Verzeichnis.


# Zukunft



# Fazit

# Quellen

