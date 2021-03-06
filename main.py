'''problema 8'''


def isPrime(x):
    '''
    functia verifica daca numarul dat prin parametrul x este prim
    '''
    d = 2
    s = 0
    if x < 2:
        return False
    else:
        while d * d <= x:
            if int(x % d) == 0:
                return False
            d = d + 1
    return True


def Sum(l):
    '''
    calculeaza suma listei
    '''
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    return s


def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    '''
    functia returneaza cu ajutorul a doua for-uri cea mai lunga subsecventa care are ca suma un numar prim
    '''
    max_length = 0
    ret_l = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            cl = lst[i: j + 1]
            if len(cl) > max_length and isPrime(Sum(cl)):
                max_length = len(cl)
                ret_l = cl
    return ret_l


def test_get_longest_sum_is_prim():
    assert get_longest_sum_is_prime([2, 3, 5, 4, 7, 2]) == [2, 3, 5, 4, 7, 2]
    assert get_longest_sum_is_prime([2, 3, 5, 4, 7, 2, 1]) == [2, 3, 5, 4, 7, 2]
    assert get_longest_sum_is_prime([2, 3, 5, 4, 7, 2, 1, 2]) == [2, 3, 5, 4, 7, 2]


'''problema 14'''


def int_equal_to_fractional(n: float) -> bool:
    '''
    verifica daca partea intreaga a unui numar este egala cu partea fractionara
    '''
    x = str(n).split('.')
    if x[0] == x[1]:
        return 1
    else: return 0


def test_int_equal_to_fractional():
    assert int_equal_to_fractional(47.83) == False
    assert int_equal_to_fractional(0.0) == True
    assert int_equal_to_fractional(893.893) == True
    assert int_equal_to_fractional(98.23) == False


def are_int_equal_to_fractional(lst: list[float]) -> bool:
    for x in lst:
        if int_equal_to_fractional(x)== 0:
            return False
    return True


def test_are_int_equal_to_fractional():
    assert are_int_equal_to_fractional([1.1, 2.2, 0.0]) == True
    assert are_int_equal_to_fractional([]) == True
    assert are_int_equal_to_fractional([1.2, 2.3, 3.4, 4.4, 5.5]) == False
    assert are_int_equal_to_fractional([1.1]) == True


def get_longest_equal_int_real(lst: list[float]) -> list[float]:
    '''
    functia verifica cu ajutorul a doua for-uri daca subsecventa curenta are lungimea mai mare decat lmax
    si daca toate elementele din cureent_subs au partea fractionara egala cu partea intreaga
    '''
    subs_max = []
    lmax = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            cureent_subs = lst[i:j + 1]
            if len(cureent_subs) > lmax and are_int_equal_to_fractional(cureent_subs):
                lmax = len(cureent_subs)
                subs_max = cureent_subs
    return subs_max


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([]) == []
    assert get_longest_equal_int_real([2.2, 1.1, 3.3, 14.2, 54.54, 13.3]) == [2.2, 1.1, 3.3]
    assert get_longest_equal_int_real([1.1, 5.5, 23.2, 51.2, 16.0]) == [1.1, 5.5]
    assert get_longest_equal_int_real([28.3, 51.9, 63.4]) == []


'''problema 9'''


def produs(l):
    s = 1
    for i in range(len(l)):
        s = s * l[i]
    return s


def get_longest_product_is_odd(lst: list[int]) -> list[int]:
    '''
    functia trece cu ajutorul a doua for uri prin lista
    verificand daca subsecventa curenta are ca produs al elementelor un numar impar
    si daca lungimea listei curente(cl) este mai mare decat lungimea maxima
    apoi daca indeplineste conditiile este salvata in ret_cl care este returnata
    '''
    max_length = 0
    ret_l = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            cl = lst[i: j + 1]
            if len(cl) > max_length and int(produs(cl) % 2) == 1:
                max_length = len(cl)
                ret_l = cl
    return ret_l


def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([1, 3, 5]) == [1, 3, 5]
    assert get_longest_product_is_odd([1, 3, 5, 6]) == [1, 3, 5]
    assert get_longest_product_is_odd([1, 3, 4, 5, 6, 7]) == [1, 3]


def printMenu():
    print("1. Citire lista int ")
    print("2.Citire lista float")
    print("3. Afisare subsecventa care are partea intreaga egala cu partea fractionara")
    print("4.Afisare subsecventa maxima care are suma un numar prim ")
    print("5. Afisare subsecventa maxima care are produsul un numar impar ")
    print("6. Iesire")


def citireListaint():
    l = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input()))
    return l
def citireListafloat():
    l = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append((input()))
    return l


def main():
    test_get_longest_product_is_odd()
    test_get_longest_sum_is_prim()
    test_get_longest_equal_int_real()
    test_int_equal_to_fractional()
    test_are_int_equal_to_fractional()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireListaint()
        elif optiune == "2":
            l = citireListafloat()
        elif optiune == "3":
            print(get_longest_equal_int_real(l))
        elif optiune == "4":
            print(get_longest_sum_is_prime(l))
        elif optiune == "5":
            print(get_longest_product_is_odd(l))
        elif optiune == "6":
            break
        else:
            print("Optiune gresita! Reincercati!")
main()
