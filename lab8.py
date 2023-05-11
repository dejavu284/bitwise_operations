import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from ui import Ui_MainWindow


class Lab8(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lab8, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    
    def init_ui(self):
        print('Done')
        
        self.ui.custom_btn.clicked.connect(self.custom_test)

        # first_test('10', '0', '0')
        # first_test('10110', '101', '10')
        # first_test('11010111', '10011', '11')
        # first_test('10111', '11', '0')
        # first_test('10', '11', '1')
        # first_test('1100100', '1011', '110')
        # first_test('1000111', '1011', '10')


    # def Custom(self):

    #     self.custom_test()


    def custom_test(self):
        f = self.ui.first_value_line.text()
        s = self.ui.second_value_line.text()
        # print('f: ', bin(int(f))[2:], '\ns: ', bin(int(s))[2:])
        
        f = self.fromBin(f)
        s = self.fromBin(s)

        self.ui.some_output_1.setText(f'First value in decimal is: {f}\nSecond value in decimal is: {s}')
        # self.ui.some_output_2.setText(f'Second value in decimal is: {s}')

        result = self.divide_polynomial_on_polynomial(f, s)
        self.ui.some_output_3.setText(f'Count of iteration is: {self.counter}')
        self.ui.some_output_4.setText(f'Remainder of the division is: {result}')
        strLine = 'divide_polynomial_on_polynomial:\n'
        for i in self.arrTemps:
            temp = self.arrTemps[i]
            for j in temp:
                strLine += f'{j}\n'
                counterBit = len(str(j))
            strLine += '-' * counterBit * 2 + '\n'
        # strLine += f'{self.arrTemps[str(len(self.arrTemps))][0]}\n'
        strLine += f'{result}\n'
        self.ui.some_output_2.setText(strLine)
        print(self.arrTemps)


    def BitConverter(self, value: int) -> int:
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


    def countBits(self, value: int) -> int:
        counter = 0
        while value > 0:
            value >>= 1
            counter += 1
        return counter


    def xor(self, first_value: int, second_value: int) -> int:
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
        return self.fromBin(strXor)


    def fromBin(self, value:str) -> int:
        decimal = 0
        for digit in value:
            decimal <<= 1
            if digit =='1':
                decimal |= 1
        return decimal


    def divide_polynomial_on_polynomial(self, first_polynomial: int, second_polynomial: int) -> int:
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
        bit_in_fp = self.countBits(first_polynomial)
        bit_in_sp = self.countBits(second_polynomial)
        self.counter = 0
        self.arrTemps = dict()
        flag = bit_in_sp != 0
        while (bit_in_fp >= bit_in_sp) & flag:
            self.counter += 1
            second_polynomial_pad = second_polynomial

            bin_fp = self.BitConverter(first_polynomial)
            bin_sp = self.BitConverter(second_polynomial)
            

            # Считаем количество бит в полиномах
            bit_in_fp = self.countBits(first_polynomial)
            bit_in_sp = self.countBits(second_polynomial)

            # print('log {divide_polynomial_on_polynomial}: ', bin_fp, '\nlog {divide_polynomial_on_polynomial}: ', bin_sp)
            # print()

            if bit_in_fp > bit_in_sp:
                shift = bit_in_fp - bit_in_sp
                second_polynomial_pad <<= shift
                bin_sp = self.BitConverter(second_polynomial_pad)
                # print('log {divide_polynomial_on_polynomial}: ', bin_fp, '\nlog {divide_polynomial_on_polynomial}: ', bin_sp)
            
            self.arrTemps[f'{self.counter}'] = [bin_fp, bin_sp]
            
            first_polynomial = self.xor(first_polynomial, second_polynomial_pad)
            bin_fp = self.BitConverter(first_polynomial)
            # print(f'{first_polynomial} == {bin_fp}')
            bit_in_fp = self.countBits(first_polynomial)
            bit_in_sp = self.countBits(second_polynomial)
        return self.BitConverter(first_polynomial)


    def test_maket(self, first_value: str, second_value: str, must_be_result: str):
        # print(f"first value is: {first_value}\nsecond value is: {second_value}")
        output = self.divide_polynomial_on_polynomial(self.fromBin(first_value), self.fromBin(second_value))
        # print(f'must_be_result: {must_be_result}')
        # print(f'output: {output}')
        print(f"{must_be_result} == {output} is {must_be_result == str(output)} ")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Lab8()
    application.show()
    sys.exit(app.exec())



