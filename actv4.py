# ERROR MANUAL
def stats(lst):
    min = 999  # Esto es un error
    # resto igual...

# TEST que detecta error
def test():
    stats([1])  # Aquí esperaría min=1 pero da min=999 → detectado

if __name__ == "__main__":
    test()