print("Dette programmet treng hjelp!")
print("Kødda prank, du treng dette programmet treng ikkje hjelp")
print("Velkommen til hello world kalkulator")

try:
    Tall1 = float(input("Skriv ditt første tall: "))
    Tegn = input("Kva vil du gjere? +,  -,  *,  /: ")
    Tall2 = float(input("Skriv ditt andre tall: "))

except ValueError:
    print("Du må skrive gyldige verdier")

print(f"{Tall1} {Tegn} {Tall2} = Hellow World")
