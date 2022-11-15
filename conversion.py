def convertBinToOct(num):
    # print the steps to convert bin to oct
    # Convert every 3 binary digits (from bit0) to octal digit (see conversion table below):
    dict = {'000': '0', '001': '1', '010': '2', '011': '3',
            '100': '4', '101': '5', '110': '6', '111': '7'}
    num = str(num)
    if len(num) % 3 == 1:
        num = '00' + num
    elif len(num) % 3 == 2:
        num = '0' + num
    num = num[::-1]
    group = []
    for i in range(0, len(num), 3):
        group.append(num[i:i+3])
    group = group[::-1]
    # reverse each string in group
    for i in range(len(group)):
        group[i] = group[i][::-1]

    explain = []
    res = ''
    for i in group:
        res += dict[i]
        explain.append(f'{i} = {dict[i]}')
    return ' | '.join(explain)


def convertBinToDec(num):
    # print the steps to convert bin to dec
    # The decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n):
    num = str(num)
    length = len(num)
    res = 0
    explain = []
    for i in range(length):
        explain.append(f'{num[i]}*2^{length-i-1}')
        res += int(num[i]) * 2**(length-i-1)

    return (' + '.join(explain))


def convertBinToHex(num):
    # print the steps to convert bin to hex
    # Convert every 4 binary digits (from bit0) to hexadecimal digit (see conversion table below):
    dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
            '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
            '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    num = str(num)
    if len(num) % 4 == 1:
        num = '000' + num
    elif len(num) % 4 == 2:
        num = '00' + num
    elif len(num) % 4 == 3:
        num = '0' + num
    num = num[::-1]
    group = []
    for i in range(0, len(num), 4):
        group.append(num[i:i+4])
    group = group[::-1]
    # reverse each string in group
    for i in range(len(group)):
        group[i] = group[i][::-1]

    explain = []
    res = ''
    for i in group:
        res += dict[i]
        explain.append(f'{i} = {dict[i]}')

    return ' | '.join(explain)


def convertOctToBin(num):
    # print the steps to convert oct to bin
    # Convert every octal digit to binary (see conversion table below):
    dict = {'0': '000', '1': '001', '2': '010', '3': '011',
            '4': '100', '5': '101', '6': '110', '7': '111'}
    num = str(num)
    res = ''
    explain = []
    for i in num:
        res += dict[i]
        explain.append(f'{i} = {dict[i]}')
    return ' | '.join(explain)


def convertOctToDec(num):
    # print the steps to convert oct to dec
    # The decimal number is equal to the sum of octal digits (dn) times their power of 8 (8n):
    num = str(num)
    length = len(num)
    res = 0
    explain = []
    for i in range(length):
        explain.append(f'{num[i]}*8^{length-i-1}')
        res += int(num[i]) * 8**(length-i-1)
    return ' + '.join(explain)


def convertOctToHex(num):
    # print the steps to convert oct to hex
    # Convert octal to binary, then binary to hexadecimal:
    explain, res = convertOctToBin(num)

    explain2, res = convertBinToHex(res)
    return explain, explain2, res


def convertDecToBin(num):
    num = int(num)
    res = ''
    explain = []

    bit = 0
    while num != 0:
        res += str(num % 2)
        explain.append(
            f'{num:8} / 2       {(num//2):8}        {(num % 2):6}            {bit:3}')
        num = num // 2
        bit += 1
    return "Division by 2       Quotient   Remainder  Bit #\n" + '\n'.join(explain), res[::-1]


def convertDecToOct(num):
    # print the steps to convert dec to oct
    # Divide the number by 8 until you get a quotient of 0.
    # The remainders are the octal digits in reverse order.
    num = int(num)
    res = ''
    explain = []

    bit = 0
    while num != 0:
        res += str(num % 8)
        explain.append(
            f'{num:8} / 8       {(num//8):8}        {(num % 8):6}            {bit:3}')
        num = num // 8
        bit += 1
    return "Division by 8       Quotient   Remainder  Bit #\n" + '\n'.join(explain)


def convertDecToHex(num):
    num = int(num)
    res = ''
    explain = []
    dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    bit = 0
    while num != 0:
        if num % 16 >= 10:
            res += dict[num % 16]
        else:
            res += str(num % 16)
        explain.append(
            f'{num:8} / 16       {(num//16):8}        {(num % 16):6}            {bit:3}')
        num = num // 16
        bit += 1
    return "Division by 16       Quotient   Remainder  Bit #\n" + '\n'.join(explain)



def convertHexToBin(num):
    # print the steps to convert hex to bin
    # Convert every hexadecimal digit to binary (see conversion table below):
    dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
            '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    num = str(num)
    temp = ''
    explain = []
    for i in num:
        temp += dict[i]
        explain.append(f'{i} = {dict[i]}')
    res = []
    for i in range(0, len(temp), 4):
        res.append(temp[i:i+4])

    return ' | '.join(explain)



def convertHexToOct(num):
    # print the steps to convert hex to oct
    # Convert hexadecimal to binary, then binary to octal:
    # print("Convert hexadecimal to binary, then binary to octal:")
    explain, res = convertHexToBin(num)
    res = ''.join(res.split(' '))
    explain2, res = convertBinToOct(res)
    return explain, explain2



def convertHexToDec(num):
    # print the steps to convert hex to dec
    # The decimal number is equal to the sum of hexadecimal digits (dn) times their power of 16 (16n):
    num = str(num)
    length = len(num)
    res = 0
    explain = []
    dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(length):
        if num[i] in dict:
            res += dict[num[i]] * 16**(length-i-1)
            explain.append(f'{dict[num[i]]}*16^{length-i-1}')
        else:
            res += int(num[i]) * 16**(length-i-1)
            explain.append(f'{num[i]}*16^{length-i-1}')

    return ' + '.join(explain)