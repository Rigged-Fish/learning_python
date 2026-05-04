# My fourth python Project.
# Still there is nothing special about this one in particular, just progressing and documenting my journey.
# This one is a simple if, elif and else practice for me.
# Of course! there are a lot! of improvements to the code that need to be taken into consideration, however this was the code I came up with to that point, and I'm honest about it.
# Learning from my mistakes!
# If you have advice for me, I am absolute more than open for every bit I can learn!

# Code Intro: Variable Sets and Definitions

distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

# Conditional Operators in multiplity, testing and learning the logic

if distance_mi == 0:
    result = False
elif distance_mi <= 1 and not is_raining:
    result = True
elif distance_mi <= 1 and is_raining:
    result = False
elif (distance_mi > 1 and distance_mi <= 6) and is_raining and not has_bike:
    result = False
elif (distance_mi > 1 and distance_mi <= 6) and not is_raining and not has_bike :
    result = False
elif (distance_mi > 1 and distance_mi <= 6) and not is_raining and has_bike:
    result = True
elif distance_mi >= 6 and has_ride_share_app:
    result = True
elif distance_mi >= 6 and has_car:
    result = True
elif distance_mi >= 6 and not has_car and not has_ride_share_app :
    result = False
else:
    result = False
# Not sure wether this 'else' operator is necessary, but I will figure it out later!

print(result)

# Finished!





# Further infos regarding cases like that, just for myself: (With my current, very, very limited knowledge!)

# In Zeilen wie dieser hier:
# elif distance_mi > 1 or distance_mi <= 6 and is_raining and not has_bike:
# Python wertet and immer vor or aus (genau wie Punktrechnung vor Strichrechnung).
# Das bedeutet für Python:
# Entweder ist die Distanz größer als 1 (distance_mi > 1)
# Oder die Distanz ist <= 6 UND es regnet UND man hat kein Fahrrad.
# Die Folge: Sobald Ihre Distanz einfach nur größer als 1 ist (z. B. distance_mi = 10), ist der erste Teil (distance_mi > 1) bereits wahr. 
# Python bricht die Prüfung ab und setzt result = False – völlig egal, wie das Wetter ist oder ob Sie ein Auto haben!
# 💡 So lösen Sie das Problem mit Klammern
# Sie müssen Python durch Klammern zwingen, die Distanz-Prüfung zuerst als einen gemeinsamen Block auszuwerten:
# ❌ Aktuell: distance_mi > 1 or distance_mi <= 6 and ...
# Richtig: (distance_mi > 1 and distance_mi <= 6) and ...
# Hinweis: Beachten Sie, dass Sie hier auch das or durch ein and ersetzen müssen, da die Distanz ja gleichzeitig größer als 1 UND kleiner/gleich 6 sein soll.
# Wenn Sie innerhalb der if- und elif-Zweige bereits "True" und "False" mit print() ausgeben lassen, benötigen Sie am Ende kein zusätzliches print() mehr. 
# Das Programm gibt das Ergebnis automatisch aus, sobald es in den passenden Zweig springt. Das print(distance_mi) am Ende können Sie einfach löschen.
# 2. Das Arbeiten mit einer Variable (Empfohlener Weg)
# Oft ist es in Übungen gewollt, das Ergebnis erst in einer Variable zu speichern und diese ganz am Ende einmal auszugeben:
# Erstellen Sie in jedem Zweig eine Variable (z. B. ergebnis = True statt print("True")).
# Schreiben Sie ganz am Ende der Datei: print(ergebnis).
# ⚠️ Zusatz-Tipp zu Ihren Bedingungen (ohne Code-Korrektur):
# Achten Sie bei Ihren elif-Zeilen mit or (z. B. distance_mi > 1 or distance_mi <= 6) auf die Logik. In Python bindet der and-Operator stärker als der or-Operator. 
# Das kann dazu führen, dass Bedingungen anders wahr werden, als Sie es beabsichtigen.
