wavelength = int(input("Enter wavelength in nanometers: "))

if wavelength >= 380 and wavelength <= 449:
    print("Violet")
elif wavelength >= 450 and wavelength <= 484:
    print("Blue")
elif wavelength >= 485 and wavelength <= 499:
    print("Cyan")
elif wavelength >= 500 and wavelength <= 564:
    print("Green")
elif wavelength >= 565 and wavelength <= 589:
    print("Yellow")
elif wavelength >= 590 and wavelength <= 624:
    print("Orange")
elif wavelength >= 625 and wavelength <= 720:
    print("Red")
else:
    print("Wavelength is outside the visible spectrum")
