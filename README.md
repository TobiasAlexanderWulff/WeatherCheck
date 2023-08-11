

# Einführung

In unserer heutigen Gesellschaft ist Zeitersparnis oft ein wichtiges Thema. Bevor wir vor die Tür gehen, checken wir mit einer unserer Apps auf dem Handy, wie das Wetter wird. 
<br>
Aber wie wäre es mit einer Alternative für zu Hause? Eine, die uns wieder etwas weg vom Smartphone führt?

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

Zunächst war es wichtig, überhaupt an Wetterdaten zu gelangen und herauszufinden, in welchem Format diese zur Verfügung stehen. Diese Aufgabe übernahm zunächst ein eigenständiges Python-Skript, das stündlich die lokalen Wetterdaten kostenlos von der API der Webseite open-meteo.com bezog.
<br>
Um diesen Dienst auf dem Arduino auszuführen, musste zunächst eine Verbindung zum Internet hergestellt werden. Dazu wurde eine Modifikation eines Beispielskripts für WifiNINA verwendet.
<br>
Im nächsten Schritt wurde versucht, die beiden Skripte zu kombinieren, indem das Python-Skript in C++ umgewandelt wurde. Es gab jedoch einige Probleme, auf diese Weise eine vernünftige sichere Verbindung zur Website herzustellen. Außerdem erwies es sich sich als wesentlich aufwendiger, auf diese Weise die Wetterdaten geordnet zwischenzuspeichern und sie zu verarbeiten.
<br>
Um dieses Problem zu lösen, spielte die Verwendung von MicroPython in der Entwicklungsumgebung "Thonny" eine Rolle. MikroPython läuft auf dem Arduino genauso wie C++, nur eben in Python. Ein kurzes Skript zum Testen befindet sich im Verzeichnis.


# Zukunft



# Fazit

# Quellen

