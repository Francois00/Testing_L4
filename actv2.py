import math

def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):  # ERROR: debería ser +1
        if (number % check) == 0:
            return False
    return True


def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def test():
    # Pruebas originales
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False

    # ✅ Caso que falla en isPrime pero pasa en isPrime2
    assert isPrime(25) == True    # Incorrecto
    assert isPrime2(25) == False  # Correcto

if __name__ == "__main__":
    test()