import time
import math

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.
    """
    cislo = int(cislo)
    
    if cislo <= 1:
        return False
    
    for delitel in range(2, int(cislo**0.5) + 1):
        if cislo % delitel == 0:
            return False
            
    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    maximum = int(maximum)
    results = []
    
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
            
    return results


if __name__ == "__main__":
    print("Тесты je_prvocislo:")
    print(f"1 -> {je_prvocislo(1)}")
    print(f"2 -> {je_prvocislo(2)}")
    print(f"3 -> {je_prvocislo(3)}")
    print(f"100 -> {je_prvocislo(100)}")
    print(f"101 -> {je_prvocislo(101)}")

    print("\nТесты vrat_prvocisla:")
    print(f"1 -> {vrat_prvocisla(1)}")
    print(f"2 -> {vrat_prvocisla(2)}")
    print(f"3 -> {vrat_prvocisla(3)}")
    print(f"10 -> {vrat_prvocisla(10)}")

