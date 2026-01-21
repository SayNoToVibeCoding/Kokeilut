while True:
    tuumat = float(input("Anna tuumat: "))
    tuumat = tuumat * 2.54
    if tuumat >= 0.01:
        print("Tuumat senttimetreinä: " + str(tuumat) + "cm")
    elif tuumat <= 0:
        break
