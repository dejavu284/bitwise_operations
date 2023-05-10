def BitConverter(value: int) -> int:
    strBit = ''
    i = 0
    while value > 0:
        strBit = str(value & 1) + strBit
        # print('log {BitConverter}: ', strBit)
        value >>= 1
        i += 1
    if strBit == '':
        return 0
    return int(strBit)


def countBits(value: int) -> int:
    counter = 0
    while value > 0:
        value >>= 1
        counter += 1
    return counter


def xor(first_value: int, second_value: int) -> int:
    strXor = ''
    # print(BitConverter(first_value))
    # print(BitConverter(second_value))

    while first_value > 0:
        bit_fv = first_value & 1
        bit_sv = second_value & 1

        strXor = str(bit_fv ^ bit_sv) + strXor
        
        first_value >>= 1
        second_value >>= 1
    # print(strXor)
    return fromBin(strXor)


def fromBin(value:str) -> int:
    decimal = 0
    for digit in value:
        decimal <<= 1
        if digit =='1':
            decimal |= 1
    return decimal


def divide_polynomial_on_polynomial(first_polynomial: int, second_polynomial: int) -> int:
    """
    first_polinomial: int - первый полином, формата: 10111; что означает: x^4 + x^2 + x + 1
    second_polinomial: int - второй полином, формата: 1011; что означает: x^3 + x + 1

    Метод принимает на вход 2 числа, работает с ними и на выходе выдаёт одно число - остаток от деления первого числа на второе.

    Берётся первый полином, например, 10110, и второй - 101. Для начала добьём нулями недостоющее количество битов во втором полиноме.

    Было: 101; стало: 00101. Всегда нужно сдвигать второй полином в старший бит первого полинома: если в первом полиноме старший бит - 4,
    а во втором - 2, то все биты второго полинома нужно сдвинуть на 2 бита влево: 00101 -> 10100.

    Теперь деление полиномов будет выглядить так:
    >>> 10110  /
    ... 10100 

    Само деление осуществляется при помощи операции xor ( ^ ), чья таблица истинности выглядит так:
    >>> 0 ^ 1 - 1
    ... 0 ^ 0 - 0
    ... 1 ^ 0 - 1
    ... 1 ^ 1 - 0

    В нашем примере, деление полиномов будет выглядеть следующим образом: 
    >>> 10110 ^
    ... 10100
    ... -----
    ... 00010

    Для того, чтобы понять, когда стоит завершить алгоритм деления полиномов, нужно следить за степенью первого полинома: как только 
    она станет меньше степени второго полинома, нужно будет остановить алгоритм и вывести число получившееся из первого полинома.

    Еще пример деления полинома на полином:
    >>> first_polynomial = 11010111 # x^7 + x^6 + x^4 + x^2 + x + 1
    >>> second_polynomial = 10011 # x^4 + x + 1
    >>> divide_polynomial_on_polynomial(first_polynomial, second_polynomial)
    ... 11010111 ^
    ... 10011000
    ... --------
    ... 01001111 ^
    ... 01001100
    ... --------
    ... 00000011 - x + 1 - степень первого полинома стала меньше степени второго, следовательно это остаток от деления
    """
    # Сначала рандомные значения
    bit_in_fp = 1
    bit_in_sp = 0

    while bit_in_fp >= bit_in_sp:
        second_polynomial_pad = second_polynomial
        bin_fp = BitConverter(first_polynomial)
        bin_sp = BitConverter(second_polynomial)

        # Считаем количество бит в полиномах
        bit_in_fp = countBits(first_polynomial)
        bit_in_sp = countBits(second_polynomial)

        # print('log {divide_polynomial_on_polynomial}: ', bin_fp, '\nlog {divide_polynomial_on_polynomial}: ', bin_sp)
        # print()

        if bit_in_fp > bit_in_sp:
            shift = bit_in_fp - bit_in_sp
            second_polynomial_pad <<= shift
            bin_sp = BitConverter(second_polynomial_pad)
            # print('log {divide_polynomial_on_polynomial}: ', bin_fp, '\nlog {divide_polynomial_on_polynomial}: ', bin_sp)

        first_polynomial = xor(first_polynomial, second_polynomial_pad)
        bin_fp = BitConverter(first_polynomial)
        # print(f'{first_polynomial} == {bin_fp}')
        bit_in_fp = countBits(first_polynomial)
        bit_in_sp = countBits(second_polynomial)
    return BitConverter(first_polynomial)


def first_test(first_value: str, second_value: str, must_be_result: str):
    # print(f"first value is: {first_value}\nsecond value is: {second_value}")
    output = divide_polynomial_on_polynomial(fromBin(first_value), fromBin(second_value))
    # print(f'must_be_result: {must_be_result}')
    # print(f'output: {output}')
    print(f"{must_be_result} == {output} is {must_be_result == str(output)} ")

if __name__ == '__main__':

    # f = input()
    # s = input()
    # print('f: ', bin(int(f))[2:], '\ns: ', bin(int(s))[2:])

    # divide_polynomial_on_polynomial(fromBin(f), fromBin(s))
    first_test('10110', '101', '10')
    first_test('11010111', '10011', '11')
    first_test('10111', '11', '0')
    first_test('10', '11', '1')
    first_test('1100100', '1011', '110')
    first_test('1000111', '1011', '10')




