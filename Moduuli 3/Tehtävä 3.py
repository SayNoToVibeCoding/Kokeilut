sukupuoli = str(input("Sukupuoli: ").lower())
hemog = float(input("Hemoglobiini g/l: "))

if (sukupuoli == "mies" and 134<=hemog<=190):
    print("Hemoglobiinisi on normaali")
elif (sukupuoli == "mies" and hemog >=190):
    print("Hemoglobiinisi on korkea")
elif (sukupuoli == "mies" and hemog <=134):
    print("Hemoglobiinisi on matala")

if (sukupuoli == "nainen" and 117 <= hemog <= 175):
        print("Hemoglobiinisi on normaali")
elif (sukupuoli == "nainen" and hemog >= 175):
        print("Hemoglobiinisi on korkea")
elif (sukupuoli == "nainen" and hemog <= 117):
        print("Hemoglobiinisi on matala")
