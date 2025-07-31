#!/usr/bin/python3
def split_32bit_to_4bit_segments(num_32bit):
    """
    Splits a 32-bit integer into eight 4-bit segments.
    """
    segments = []
    for i in range(8):  # There are 8 segments of 4 bits in a 32-bit number
        # Shift the number right to bring the desired 4 bits to the least significant position
        # Then, apply a mask (0xF or 0b1111) to isolate those 4 bits
        segment = (num_32bit >> (i * 4)) & 0xF
        segments.append(segment)
    
    # The segments are extracted from least significant to most significant.
    # Reverse the list to get them in the conventional order (most significant first).
    return segments[::-1]



def binary_list_to_hex(binary_list):
    """
    Converts a list of 4-bit binary strings to a hexadecimal string.

    Args:
        binary_list: A list of strings, where each string represents a 4-bit binary number.
                     Example: ["0001", "1101", "1010"]

    Returns:
        A string representing the hexadecimal equivalent of the combined binary numbers.
    """
    hex_string = ""
    for four_bit_binary in binary_list:
        if len(four_bit_binary) != 4 or not all(bit in '01' for bit in four_bit_binary):
            raise ValueError("Each item in the list must be a 4-bit binary string.")
        
        # Convert the 4-bit binary string to an integer
        decimal_value = int(four_bit_binary, 2)
        
        # Convert the integer to its hexadecimal character representation
        hex_char = format(decimal_value, 'X').lower()
        
        hex_string += hex_char
    return hex_string

def hex_to_little_endian(hex_string):
    """Converts a hex string to little-endian format.

    Args:
        hex_string: The hex string to convert (e.g., "1234").

    Returns:
        The little-endian representation as a string.
    """
    # Ensure the hex string is of even length
    if len(hex_string) % 2 != 0:
        hex_string = "0" + hex_string

    # Convert hex string to bytes
    byte_array = bytes.fromhex(hex_string)

    # Reverse the byte order
    little_endian_bytes = byte_array[::-1]

    # Convert back to hex string
    return little_endian_bytes.hex()

with open('Input.asm', 'r') as file:
    lines = file.readlines()
    # Each element in 'lines' is a string ending with '\n' (unless it's the last line without one)
    # To remove the newline character, you can use strip()
    clean_lines = [line.strip() for line in lines]

for i in range(len(clean_lines)):
 
    inst = clean_lines[i]
    result = 0

    if inst.split(" ")[0] == "ABS": # Green
    #   ABS <Xd>, <Xn>
    #
    #   ABS
    #   print(448001 << 13)
    #   <Xd>
    #   print(int(inst.split(" ")[1][1:-1]))
    #   <Xn>
    #   print(int(inst.split(" ")[2][1:]) << 5)
        result = ((448001 << 13) + int(inst.split(" ")[1][1:-1]) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "ADC": # Green
        # ADC <Xd>, <Xn>, <Xm>
        #
        # ADC
        # print(77 << 25)
        # <Xd>
        # print(int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # print(int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # print(int(inst.split(" ")[3][1:]) << 16)
        result = ((77 << 25) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "ADCS": # Green
        # ADCS <Xd>, <Xn>, <Xm>
        # ADCS
        # print(93 << 25)
        # <Xd>
        # int(inst.split(" ")[1][1:-1])
        # <Xn>
        # int(inst.split(" ")[2][1:-1]) << 5
        # <Xm>
        # int(inst.split(" ")[3][1:]) << 16
        result = ((93 << 25) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))                                                                                                   
    elif inst.split(" ")[0] == "ADD" and (inst.split(" ")[1][1:-1]).isdigit() and (inst.split(" ")[2][1:-1]).isdigit() and (inst.split(" ")[3][3:]
    ).isdigit(): # Green
        # ADD <Xd|SP>, <Xn|SP>, #<imm12>
        # ADD - Immediate
        # print(580 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm12>
        # (int(inst.split(" ")[3][3:]) << 10)
        result = ((580 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 10))
    elif inst.split(" ")[0] == "ADDS" and (inst.split(" ")[1][1:-1]).isdigit() and (inst.split(" ")[2][1:-1]).isdigit() and (inst.split(" ")[3][3:]
    ).isdigit(): # Green
        # ADDS <Xd>, <Xn|SP>, #<imm12>
        # ADDS - Immediate with CPSR Turned On
        # print(708 << 22)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm12>
        # (int(inst.split(" ")[3][3:]) << 10)
        result = ((708 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 10))
    elif inst.split(" ")[0] == "ADDG": # Green
        # ADDG <Xd|SP>, <Xn|SP>, #<uimm6>, #<uimm4>
        # ADDG
        # print(582 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP> 
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <uimm6>
        # (int(inst.split(" ")[3][3:-1], 16) << 16)
        # <uimm4>
        # (int(inst.split(" ")[4][3:], 16) << 10)
        result = ((582 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:-1], 16) << 16) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "ADDPT": # Green
        # ADDPT <Xd|SP>, <Xn|SP>, <Xm>{, #<amount>}
        # ADDPT
        # print(315393 << 13)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <amount> / <imm3>
        # (int(inst.split(" ")[4][3:], 16) << 10)
        result = ((315393 << 13) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "ADD":
        choice = input("ADD <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}} or ADD <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}?: ")
        if choice == "ADD <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}}": 
            # ADD <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}}
            # ADD (extended register)
            # print(1113 << 21)
            # <Xd|SP>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # (int(inst.split(" ")[2][1:-1]))
            # <Rm>
            # (int(inst.split(" ")[3][1:-1]))
            # <extend> / option
            # int(inst.split(" ")[4][3:-1], 16)
            # <amount> / imm3
            # int(inst.split(" ")[5][3:], 16)
            result = ((1113 << 21) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 13) + (int(inst.split(" ")[5][3:], 16) << 10) + ((int(inst.split(" ")[2][1:-1])) << 5) + (int(inst.split(" ")[1][1:-1])))
            pass
        elif choice == "ADD <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}":
            # ADD <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}
            # ADD (shifted register)
            # print(1112 << 21)
            # <Xd>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <shift> / 2 bit
            # (int(inst.split(" ")[4][3:-1], 16) << 22)
            # <amount> / imm6
            # (int(inst.split(" ")[5][3:], 16) << 10)
            result = (((1112 << 21)) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + ((int(inst.split(" ")[4][3:-1], 16)) << 22) + ((int(inst.split(" ")[5][3:], 16)) << 10))
            pass
        else:
            result = 0
    elif inst.split(" ")[0] == "ADDS":
        choice = input("ADDS <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}} or ADDS <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}?: ")
        if choice == "ADDS <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}}": 
            # ADDS <Xd|SP>, <Xn|SP>, <Xm>{, <extend>, {#<amount>}}
            # ADDS (extended register)
            # print(1369 << 21)
            # <Xd|SP>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # (int(inst.split(" ")[2][1:-1]))
            # <Rm>
            # (int(inst.split(" ")[3][1:-1]))
            # <extend> / option
            # int(inst.split(" ")[4][3:-1], 16)
            # <amount> / imm3
            # int(inst.split(" ")[5][3:], 16)
            result = ((1369 << 21) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 13) + (int(inst.split(" ")[5][3:], 16) << 10) + ((int(inst.split(" ")[2][1:-1])) << 5) + (int(inst.split(" ")[1][1:-1])))
            pass
        elif choice == "ADDS <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}":
            # ADDS <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}
            # ADDS (shifted register)
            # print(1368 << 21)
            # <Xd>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <shift> / 2 bit
            # (int(inst.split(" ")[4][3:-1], 16) << 22)
            # <amount> / imm6
            # (int(inst.split(" ")[5][3:], 16) << 10)
            result = (((1368 << 21)) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 22) + (int(inst.split(" ")[5][3:], 16) << 10))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "ADR":
        # ADR <Xd>, <label>
        # ADR
        num = int(inst.split(" ")[2][3:],16)
        # Calculate shift to bring the first two bits to the rightmost position    
        shift_amount = num.bit_length() - 2 
        # Right-shift to move the desired bits to the least significant positions
        shifted_num = num >> shift_amount
        # Mask to isolate the first two bits
        immlo = shifted_num & 0b11
        immhi = num >> 2
        result = ((immlo << 29) + (1 << 28) + (immhi << 5) + (int(inst.split(" ")[1][1:-1])))
    elif inst.split(" ")[0] == "ADRP":
        # ADRP <Xd>, <label>
        # ADRP
        num = int(inst.split(" ")[2][3:],16)
        # Calculate shift to bring the first two bits to the rightmost position    
        shift_amount = num.bit_length() - 2 
        # Right-shift to move the desired bits to the least significant positions
        shifted_num = num >> shift_amount
        # Mask to isolate the first two bits
        immlo = shifted_num & 0b11
        immhi = num >> 2
        result = ((1 << 31) + (immlo << 29) + (1 << 28) + (immhi << 5) + (int(inst.split(" ")[1][1:-1])))
    elif inst.split(" ")[0] == "APAS":
        # APAS <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(6 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(0 << 8)
        # <op2>
        # print(0 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (6 << 16) + (7 << 12) + (0 << 8) + (0 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "CFP":
        # CFP <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(3 << 8)
        # <op2>
        # print(4 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (3 << 8) + (4 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "COSP":
        # COSP <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(3 << 8)
        # <op2>
        # print(6 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (3 << 8) + (6 << 5) + (int(inst.split(" ")[1][1:])))    
    elif inst.split(" ")[0] == "CPP":
        # CPP <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(3 << 8)
        # <op2>
        # print(7 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (3 << 8) + (7 << 5) + (int(inst.split(" ")[1][1:])))   
    elif inst.split(" ")[0] == "DVP":
        # DVP <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(3 << 8)
        # <op2>
        # print(5 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (3 << 8) + (5 << 5) + (int(inst.split(" ")[1][1:])))   
    elif inst.split(" ")[0] == "GCSPOPCX":
        # GCSPOPCX <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(0 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(7 << 8)
        # <op2>
        # print(5 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (0 << 16) + (7 << 12) + (7 << 8) + (5 << 5) + (int(inst.split(" ")[1][1:])))   
    elif inst.split(" ")[0] == "GCSPOPX":
        # GCSPOPX <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(0 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(7 << 8)
        # <op2>
        # print(6 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (0 << 16) + (7 << 12) + (7 << 8) + (6 << 5) + (int(inst.split(" ")[1][1:])))   
    elif inst.split(" ")[0] == "GCSPUSHM":
        # GCSPUSHM <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(7 << 8)
        # <op2>
        # print(0 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (7 << 8) + (0 << 5) + (int(inst.split(" ")[1][1:])))    
    elif inst.split(" ")[0] == "GCSPUSHX":
        # GCSPUSHX <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(0 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(7 << 8)
        # <op2>
        # print(4 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (0 << 16) + (7 << 12) + (7 << 8) + (4 << 5) + (int(inst.split(" ")[1][1:])))    
    elif inst.split(" ")[0] == "GCSSS1":
        # GCSSS1 <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(7 << 8)
        # <op2>
        # print(2 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (7 << 8) + (2 << 5) + (int(inst.split(" ")[1][1:])))        
    elif inst.split(" ")[0] == "TRCIT":
        # TRCIT <Xt>
        #
        # SYS #<op1>, <CRn>, <CRm>, #<op2>{, <Xt>}
        # SYS
        # print(6817 << 19)
        # <op1>
        # print(3 << 16)
        # <CRn>
        # print(7 << 12)
        # <CRm> 
        # print(2 << 8)
        # <op2>
        # print(7 << 5)
        # <Xt>
        # (int(inst.split(" ")[1][1:]))
        result = ((6817 << 19) + (3 << 16) + (7 << 12) + (2 << 8) + (7 << 5) + (int(inst.split(" ")[1][1:])))            
    elif inst.split(" ")[0] == "ASRV":
        # ASRV <Xd>, <Xn>, <Xm>
        # ASRV 
        # print(1267717 << 22)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((1267717 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "ASR":
        # ASR <Xd>, <Xn>, #<shift>
        # ASR 
        # print(2470509568)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <shift>
        # ((int(inst.split(" ")[3][3:], 16)) << 16)    
        result = ((2470509568) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + ((int(inst.split(" ")[3][3:], 16)) << 16))
    elif inst.split(" ")[0] == "AUTDA":
        # AUTDA <Xd>, <Xn|SP>
        # AUTDA
        # print(1792035 << 11)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # (int(inst.split(" ")[2][1:]) << 5)
        result = ((1792035 << 11) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "AUTDZA":
        # AUTDZA <Xd>
        # AUTDZA
        # print(114690527 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:]))
        result = ((114690527 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "AUTDB":
        # AUTDB <Xd>, <Xn|SP>
        # AUTDB
        # print(3584071 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # (int(inst.split(" ")[2][1:]) << 5)
        result = ((3584071 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "AUTDZB":
        # AUTDZB <Xd>
        # AUTDZB
        # print(114690303 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:]))
        result = ((114690303 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "AUTIA":
        # AUTDA <Xd>, <Xn|SP>
        # AUTDA
        # print(896017 << 12)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # (int(inst.split(" ")[2][1:]) << 5)
        result = ((896017 << 12) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "AUTIZA":
        # AUTDZA <Xd>
        # AUTDZA
        # print(28672639 << 5) 
        # <Xd>
        # (int(inst.split(" ")[1][1:]))
        result = ((28672639 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst == "AUTIA1716":
        result = (3573752223)
    elif inst == "AUTIASP":
        result = (3573752767)
    elif inst == "AUTIAZ":
        result = (3573752735)
    elif inst == "AUTIA171615":
        result = (3670129662)
    elif inst.split(" ")[0] == "AUTIASPPC": 
        # AUTIASPPC <label>
        # AUTIASPPC
        # print(4085252127)
        # <label> / imm16
        # int(inst.split(" ")[1][3:],16)
        result = ((4085252127) + (int(inst.split(" ")[1][3:],16)))
    elif inst.split(" ")[0] == "AUTIASPPCR":
        # AUTIASPPCR <Xn>
        # AUTIASPPCR 
        # print(3670118430)
        # <Xn>
        # (int(inst.split(" ")[1][1:]) << 5)
        result = ((3670118430) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "AUTIB":
        # AUTDB <Xd>, <Xn|SP>
        # AUTDB
        # result = (3584069 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # (int(inst.split(" ")[2][1:]) << 5)
        result = ((3584069 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "AUTIZB":
        # AUTDZB <Xd>
        # AUTDZB
        # print(114690495 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:]))
        result = ((114690495 << 5) + (int(inst.split(" ")[1][1:])))    
    elif inst. split(" ")[0] == "AUTIB1716":
        result = ("3573752287")
    elif inst.split(" ")[0] == "AUTIBSP":
        result = (3573752831)
    elif inst.split(" ")[0] == "AUTIBZ":
        result = (3573752799)

    elif inst.split(" ")[0] == "AXFLAG":
        result = (3573563487)
    elif inst.split(" ")[0] == "AND" and (inst.split(" ")[3][3:]).isdigit():
        # AND <Xd|SP>, <Xn>, #<imm>
        # AND - Immediate
        # print(585 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm>
        # (int(inst.split(" ")[3][3:]))
        num = (int(inst.split(" ")[3][3:]))
        # Calculate shift to bring the first six bits to the rightmost position    
        shift_amount = num.bit_length() - 6 
        # Right-shift to move the desired bits to the least significant positions
        shifted_num = num >> shift_amount
        # Mask to isolate the first six bits
        imms = shifted_num & 0b111111
        immr = num >> 6
        result = ((585 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + imms + immr)
    elif inst.split(" ")[0] == "EOR" and (inst.split(" ")[3][3:]).isdigit():
        # EOR <Xd|SP>, <Xn>, #<imm>
        # EOR - Immediate
        # print(841 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm>
        # (int(inst.split(" ")[3][3:]))
        num = (int(inst.split(" ")[3][3:]))
        # Calculate shift to bring the first six bits to the rightmost position    
        shift_amount = num.bit_length() - 6 
        # Right-shift to move the desired bits to the least significant positions
        shifted_num = num >> shift_amount
        # Mask to isolate the first six bits
        imms = shifted_num & 0b111111
        immr = num >> 6
        result = ((841 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + imms + immr)
    elif inst.split(" ")[0] == "ORR" and (inst.split(" ")[3][3:]).isdigit():
        # ORR <Xd|SP>, <Xn>, #<imm>
        # ORR - Immediate
        # print(713 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm>
        # (int(inst.split(" ")[3][3:]))
        num = (int(inst.split(" ")[3][3:]))
        # Calculate shift to bring the first six bits to the rightmost position    
        shift_amount = num.bit_length() - 6 
        # Right-shift to move the desired bits to the least significant positions
        shifted_num = num >> shift_amount
        # Mask to isolate the first six bits
        imms = shifted_num & 0b111111
        immr = num >> 6
        result = ((713 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + imms + immr)
    elif inst.split(" ")[0] == "AND" and (inst.split(" ")[3][1:-1]).isdigit():
        # AND <Xd>, <Xn>, <Xm>{, <shift> #<amount>}
        # AND
        # print(1104 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[4][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[5][3:], 16) << 10)  
        result = ((1104 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 22) + (int(inst.split(" ")[5][3:], 16) << 10))
    elif inst.split(" ")[0] == "EOR" and (inst.split(" ")[3][1:-1]).isdigit():
        # EOR <Xd>, <Xn>, <Xm>{, <shift> #<amount>}
        # EOR
        # print(1616 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[4][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[5][3:], 16) << 10)  
        result = ((1616 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 22) + (int(inst.split(" ")[5][3:], 16) << 10))
    elif inst.split(" ")[0] == "ORR" and (inst.split(" ")[3][1:-1]).isdigit():
        # ORR <Xd>, <Xn>, <Xm>{, <shift> #<amount>}
        # ORR
        # print(1360 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[4][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[5][3:], 16) << 10)  
        result = ((1360 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 22) + (int(inst.split(" ")[5][3:], 16) << 10))        
    elif inst.split(" ")[0] == "B": 
        # B <label>
        # B
        # print(5 << 26)
        # <label> / imm26
        # int(inst.split(" ")[1][3:],16)
        result = ((5 << 26) + (int(inst.split(" ")[1][3:],16)))
    elif inst.split(" ")[0] == "B.":
        # B.<cond> <label>
        # B.
        # print(21 << 26)
        # <cond> / 4 bit
        # (int(inst.split(" ")[1][3:-1],16))
        # <label> / imm19
        # (int(inst.split(" ")[2][3:],16) << 5)
        result = ((21 << 26) + (int(inst.split(" ")[1][3:-1],16)) + (int(inst.split(" ")[2][3:],16) << 5))
    elif inst.split(" ")[0] == "BC.":
        # BC.<cond> <label>
        # BC.
        # print((21 << 26) + (1 << 4))
        # <cond> / 4 bit
        # (int(inst.split(" ")[1][3:-1],16))
        # <label> / imm19
        # (int(inst.split(" ")[2][3:],16) << 5)
        result = (((21 << 26) + (1 << 4)) + (int(inst.split(" ")[1][3:-1],16)) + (int(inst.split(" ")[2][3:],16) << 5))
    elif inst.split(" ")[0] == "BLR": # Green
        # BLR <Xn>
        # BLR
        # print(54847 << 16)  
        # <Xn>
        # int(inst.split(" ")[1][1:]) << 5
        result = ((54847 << 16) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "BL": # Green
        # BL <label>
        # BL
        # print(37 << 26)
        # <label>
        # int(inst.split(" ")[1][3:],16)
        result = ((37 << 26) + (int(inst.split(" ")[1][3:],16)))
    elif inst.split(" ")[0] == "BR": # Green
        # BR <Xn>
        # BR
        # print(54815 << 16)  
        # <Xn>
        # int(inst.split(" ")[1][1:]) << 5
        result = ((54815 << 16) + (int(inst.split(" ")[1][1:]) << 5)) 
    elif inst.split(" ")[0] == "BRK":
        # BRK #<imm16>
        # BRK
        # print(1697 << 21)
        # <imm16>
        # int(inst.split(" ")[1][3:],16)
        result = ((1697 << 21) + (int(inst.split(" ")[1][3:],16) << 5))
    elif inst.split(" ")[0] == "BLRAA":
        # BLRAA <Xn>, <Xm|SP>
        # 1101011	Z	0011111100001	M	00000	00000
        # BLRAA 
        # print(3611232256)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm|SP>
        # (int(inst.split(" ")[2][1:]))
        result = ((3611232256) + (int(inst.split(" ")[1][1:-1]) << 5) + (int(inst.split(" ")[2][1:])))
    elif inst.split(" ")[0] == "BLRAAZ":
        # BLRAAZ <Xn>
        # BLRAAZ 
        # print(3594455071)
        # <Xn>
        # (int(inst.split(" ")[1][1:]) << 5)
        result = ((3594455071) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "BLRAB":
        # BLRAB <Xn>, <Xm|SP>
        # BLRAB 
        # print(3611233280)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm|SP>
        # (int(inst.split(" ")[2][1:]))
        result = ((3611233280) + (int(inst.split(" ")[1][1:-1]) << 5) + (int(inst.split(" ")[2][1:])))
    elif inst.split(" ")[0] == "BLRABZ":
        # BLRABZ <Xn>
        # BLRABZ 
        # print(3594456095)
        # <Xn>
        # (int(inst.split(" ")[1][1:]) << 5)
        result = ((3594456095) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "BRAA":
        # BRAA <Xn>, <Xm|SP>
        # 1101011	Z	0001111100001	M	00000	00000
        # BRAA 
        # print(3609135104)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm|SP>
        # (int(inst.split(" ")[2][1:]))
        result = ((3609135104) + (int(inst.split(" ")[1][1:-1]) << 5) + (int(inst.split(" ")[2][1:])))
    elif inst.split(" ")[0] == "BRAAZ":
        # BRAAZ <Xn>
        # BRAAZ 
        # print(3592357919)
        # <Xn>
        # (int(inst.split(" ")[1][1:]) << 5)
        result = ((3592357919) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "BRAB":
        # BRAB <Xn>, <Xm|SP>
        # BRAB 
        # print(3609136128)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm|SP>
        # (int(inst.split(" ")[2][1:]))
        result = ((3609136128) + (int(inst.split(" ")[1][1:-1]) << 5) + (int(inst.split(" ")[2][1:])))
    elif inst.split(" ")[0] == "BRABZ":
        # BRABZ <Xn>
        # BRABZ 
        # print(3592358943)
        # <Xn>
        # (int(inst.split(" ")[1][1:]) << 5)
        result = ((3592358943) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "GCSPOPM":
        # GCSPOPM {<Xt>}
        # GCSPOPM
        # print(111762361 << 5)
        # {<Xt>}
        # (int(inst.split(" ")[1][1:]))
        result = ((111762361 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "GCSSS2":
        # GCSSS2 {<Xt>}
        # GCSSS2
        # print(111762363 << 5)
        # {<Xt>}
        # (int(inst.split(" ")[1][1:]))
        result = ((111762363 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "CBNZ":
        # CBNZ <Xt>, <label>
        # CBNZ
        # print(181 << 24)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <label> / imm19
        # ((int(inst.split(" ")[2][3:]), 16) << 5)
        result = ((181 << 24) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:]), 16) << 5))
    elif inst.split(" ")[0] == "CBZ":
        # CBZ <Xt>, <label>
        # CBZ
        # print(180 << 24)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <label> / imm19
        # ((int(inst.split(" ")[2][3:]), 16) << 5)
        result = ((180 << 24) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:]), 16) << 5))
    elif inst.split(" ")[0] == "CBGT" and (int(inst.split(" ")[2][3:-1]), 16).isdigit():
        # CBGT <Xt>, #<imm6>, <label>
        # CBGT
        # print(1960 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm6>
        # ((int(inst.split(" ")[2][3:-1]), 16) << 15)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1960 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1]), 16) << 15) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBLT" and (inst.split(" ")[2][3:-1]).isdigit():
        # CBLT <Xt>, #<imm6>, <label>
        # CBLT
        # print(1961 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm6>
        # ((int(inst.split(" ")[2][3:-1]), 16) << 15)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1961 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1]), 16) << 15) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBHI" and (inst.split(" ")[2][3:-1]).isdigit():
        # CBHI <Xt>, #<imm6>, <label>
        # CBHI
        # print(1962 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm6>
        # ((int(inst.split(" ")[2][3:-1]), 16) << 15)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1962 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1]), 16) << 15) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBLO" and (inst.split(" ")[2][3:-1]).isdigit():
        # CBLO <Xt>, #<imm6>, <label>
        # CBLO
        # print(1963 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm6>
        # ((int(inst.split(" ")[2][3:-1]), 16) << 15)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1963 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1]), 16) << 15) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBEQ" and (inst.split(" ")[2][3:-1]).isdigit():
        # CBEQ <Xt>, #<imm6>, <label>
        # CBEQ
        # print(1964 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm6>
        # ((int(inst.split(" ")[2][3:-1]), 16) << 15)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1964 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1]), 16) << 15) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBNE" and (inst.split(" ")[2][3:-1]).isdigit():
        # CBNE <Xt>, #<imm6>, <label>
        # CBNE
        # print(1965 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm6>
        # ((int(inst.split(" ")[2][3:-1]), 16) << 15)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1965 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1]), 16) << 15) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBGT" and (inst.split(" ")[2][1:-1]).isdigit():
        # CBGT <Xt>, <Xm>, <label>
        # CBGT
        # print(1952 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # (int(inst.split(" ")[2][1:-1]) << 16)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1952 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 16) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBGE" and (inst.split(" ")[2][1:-1]).isdigit():
        # CBGE <Xt>, <Xm>, <label>
        # CBGE
        # print(1953 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # (int(inst.split(" ")[2][1:-1]) << 16)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1953 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 16) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBHI" and (inst.split(" ")[2][1:-1]).isdigit():
        # CBHI <Xt>, <Xm>, <label>
        # CBHI
        # print(1954 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # (int(inst.split(" ")[2][1:-1]) << 16)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1954 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 16) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBHS" and (inst.split(" ")[2][1:-1]).isdigit():
        # CBHS <Xt>, <Xm>, <label>
        # CBHS
        # print(1955 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # (int(inst.split(" ")[2][1:-1]) << 16)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1955 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 16) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBEQ" and (inst.split(" ")[2][1:-1]).isdigit():
        # CBEQ <Xt>, <Xm>, <label>
        # CBEQ
        # print(1958 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # (int(inst.split(" ")[2][1:-1]) << 16)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1958 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 16) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CBNE" and (inst.split(" ")[2][1:-1]).isdigit():
        # CBNE <Xt>, <Xm>, <label>
        # CBNE
        # print(1959 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # (int(inst.split(" ")[2][1:-1]) << 16)
        # <label> / <imm9>
        # (int(inst.split(" ")[3][3:],16) << 5)
        result = ((1959 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 16) + (int(inst.split(" ")[3][3:],16) << 5))
    elif inst.split(" ")[0] == "CSEL":
        # CSEL <Xd>, <Xn>, <Xm>, <cond>
        # CSEL
        # print(309 << 23)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <cond> / 4 bit
        # (int(inst.split(" ")[3][3:], 16) << 12)
        result = ((309 << 23) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[3][3:], 16) << 12))
    elif inst.split(" ")[0] == "CSINC":
        # CSINC <Xd>, <Xn>, <Xm>, <cond>
        # CSINC
        # print(2531329 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <cond> / 4 bit
        # (int(inst.split(" ")[3][3:], 16) << 12)
        result = ((2531329 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[3][3:], 16) << 12))    
    elif inst.split(" ")[0] == "CSINV":
        # CSINV <Xd>, <Xn>, <Xm>, <cond>
        # CSINV
        # print(437 << 23)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <cond> / 4 bit
        # (int(inst.split(" ")[3][3:], 16) << 12)
        result = ((437 << 23) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[3][3:], 16) << 12))    
    elif inst.split(" ")[0] == "CSNEG":
        # CSNEG <Xd>, <Xn>, <Xm>, <cond>
        # CSNEG
        # print(3579905 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <cond> / 4 bit
        # (int(inst.split(" ")[3][3:], 16) << 12)
        result = ((3579905 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[3][3:], 16) << 12))            
    elif inst.split(" ")[0] == "CMPP":
        # CMPP <Xn|SP>, <Xm|SP>
        # CMPP 
        # print(3133145119)
        # <Xn|SP>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm|SP>
        # (int(inst.split(" ")[2][1:]) << 16)
        result = ((3133145119) + ((int(inst.split(" ")[1][1:-1])) << 5) + ((int(inst.split(" ")[2][1:])) << 16))
    elif inst.split(" ")[0] == "CMP":
        choice = input("CMP <Xn|SP>, <R><m>{, <extend> {#<amount>}} or CMP <Xn|SP>, #<imm>{, <shift>} or CMP <Xn>, <Xm>{, <shift> #<amount>}?: ")
        if choice == "CMP <Xn|SP>, <R><m>{, <extend> {#<amount>}}":
            # CMP <Xn|SP>, <Rm>{, <extend> {#<amount>}}
            # CMP - extended register
            # print(3944742943)
            # <Xn|SP>
            # (int(inst.split(" ")[1][1:-1] << 5)
            # <Rm>
            # (int(inst.split(" ")[2][1:-1] << 16)
            # <extend> / option
            # (int(inst.split(" ")[3][3:-1], 16) << 13)
            # <amount> / imm3
            # (int(inst.split(" ")[4][3:], 16) << 10) 
            result == ((3944742943) + ((int(inst.split(" ")[1][1:-1])) << 5) + ((int(inst.split(" ")[2][1:-1])) << 16) + ((int(inst.split(" ")[3][3:-1], 16)) << 13) + ((int(inst.split(" ")[4][3:], 16)) << 10))
            pass
        elif choice == "CMP <Xn>, <Xm>{, <shift> #<amount>}": 
            # CMP <Xn>, <Xm>{, <shift> #<amount>}
            # CMP - shifted register
            # print(3942645791)
            # <Xn>
            # (int(inst.split(" ")[1][1:-1] << 5)
            # <Xm>
            # (int(inst.split(" ")[2][1:-1] << 16)
            # <shift> / 2 bit
            # (int(inst.split(" ")[3][3:-1], 16) << 22)
            # <amount> / imm6
            # (int(inst.split(" ")[4][3:], 16) << 10) 
            result = ((3942645791) + ((int(inst.split(" ")[1][1:-1])) << 5) + ((int(inst.split(" ")[2][1:-1])) << 16) + ((int(inst.split(" ")[3][3:-1], 16)) << 22) + ((int(inst.split(" ")[4][3:], 16)) << 10)) 
            pass      
        elif choice == "CMP <Xn|SP>, #<imm>{, <shift>}":
            # CMP <Xn|SP>, #<imm12>{, <shift>}
            # CMP - immediate
            # print(4043309087)
            # <Xn|SP>
            # (int(inst.split(" ")[1][1:-1] << 5)
            # <imm12>
            # (int(inst.split(" ")[2][3:-1], 16) << 10)
            # <shift> / sh
            # (int(inst.split(" ")[3][3:], 16) << 22) 
            result = ((4043309087) + ((int(inst.split(" ")[1][1:-1]) << 5)) + ((int(inst.split(" ")[2][3:-1], 16) << 10)) + ((int(inst.split(" ")[3][3:], 16)) << 22))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "CMN":
        choice = input("CMN <Xn|SP>, <R><m>{, <extend> {#<amount>}} or CMN <Xn|SP>, #<imm>{, <shift>} or CMN <Xn>, <Xm>{, <shift> #<amount>}?: ")
        if choice == "CMN <Xn|SP>, #<imm>{, <shift>}": 
            # CMN <Xn|SP>, <Rm>{, <extend> {#<amount>}}
            # CMN - extended register
            # print(2871001119)
            # <Xn|SP>
            # (int(inst.split(" ")[1][1:-1] << 5)
            # <Rm>
            # (int(inst.split(" ")[2][1:-1] << 16)
            # <extend> / option
            # (int(inst.split(" ")[3][3:-1], 16) << 13)
            # <amount> / imm3
            # (int(inst.split(" ")[4][3:], 16) << 10) 
            result == ((2871001119) + (int(inst.split(" ")[1][1:-1] << 5)) + (int(inst.split(" ")[2][1:-1] << 16)) + (int(inst.split(" ")[3][3:-1], 16) << 13) + (int(inst.split(" ")[4][3:], 16) << 10))
            pass
        elif choice == "CMN <Xn>, <Xm>{, <shift> #<amount>}": 
            # CMN <Xn>, <Xm>{, <shift> #<amount>}
            # CMN - shifted register
            # print(2868903967)
            # <Xn>
            # (int(inst.split(" ")[1][1:-1] << 5)
            # <Xm>
            # (int(inst.split(" ")[2][1:-1] << 16)
            # <shift> / 2 bit
            # (int(inst.split(" ")[3][3:-1], 16) << 22)
            # <amount> / imm6
            # (int(inst.split(" ")[4][3:], 16) << 10) 
            result = ((2868903967) + (int(inst.split(" ")[1][1:-1] << 5)) + (int(inst.split(" ")[2][1:-1] << 16)) + (int(inst.split(" ")[3][3:-1], 16) << 22) + (int(inst.split(" ")[4][3:], 16) << 10))       
            pass
        elif choice == "CMN <Xn|SP>, #<imm>{, <shift>}":
            # CMN <Xn|SP>, #<imm12>{, <shift>}
            # CMN - immediate
            # print(2969567263)
            # <Xn|SP>
            # (int(inst.split(" ")[1][1:-1] << 5)
            # <imm12>
            # (int(inst.split(" ")[2][3:-1], 16) < 10)
            # <shift> / sh
            # (int(inst.split(" ")[3][3:], 16) << 22) 
            result = ((2969567263) + (int(inst.split(" ")[1][1:-1] << 5)) + (int(inst.split(" ")[2][3:-1], 16) < 10) + (int(inst.split(" ")[3][3:], 16) << 22))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "CCMP" and (inst.split(" ")[2][1:-1]).isdigit():
        # CCMP <Xn>, <Xm>, #<nzcv>, <cond>
        # CCMP
        # print(1001 << 22)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm>
        # ((int(inst.split(" ")[2][1:-1])) << 16)
        # <nzcv> / 4 bit
        # (int(inst.split(" ")[3][3:-1], 16))
        # <cond> / 4 bit
        # (int(inst.split(" ")[4][3:], 16) << 12)  
        result = ((1001 << 22) + (int(inst.split(" ")[1][1:-1]) << 5) + ((int(inst.split(" ")[2][1:-1])) << 16) + (int(inst.split(" ")[3][3:-1], 16)) + (int(inst.split(" ")[4][3:], 16) << 12))
    elif inst.split(" ")[0] == "CCMP" and (inst.split(" ")[2][3:-1]).isdigit():
        # CCMP <Xn>, #<imm5>, #<nzcv>, <cond>
        # CCMP
        # print(2050049 << 11)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <imm5>
        # (int(inst.split(" ")[1][3:-1], 16) << 16)
        # <nzcv> / 4 bit
        # (int(inst.split(" ")[3][3:-1], 16))
        # <cond> / 4 bit
        # (int(inst.split(" ")[4][3:], 16) << 12)  
        result = ((2050049 << 11) + (int(inst.split(" ")[1][1:-1]) << 5) + (int(inst.split(" ")[1][3:-1], 16) << 16) + (int(inst.split(" ")[3][3:-1], 16)) + (int(inst.split(" ")[4][3:], 16) << 12))
    elif inst.split(" ")[0] == "CCMN" and (inst.split(" ")[2][1:-1]).isdigit():
        # CCMN <Xn>, <Xm>, #<nzcv>, <cond>
        # CCMN
        # print(745 << 22)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <Xm>
        # ((int(inst.split(" ")[2][1:-1])) << 16)
        # <nzcv> / 4 bit
        # (int(inst.split(" ")[3][3:-1], 16))
        # <cond> / 4 bit
        # (int(inst.split(" ")[4][3:], 16) << 12)  
        result = ((745 << 22) + (int(inst.split(" ")[1][1:-1]) << 5) + ((int(inst.split(" ")[2][1:-1])) << 16) + (int(inst.split(" ")[3][3:-1], 16)) + (int(inst.split(" ")[4][3:], 16) << 12))
    elif inst.split(" ")[0] == "CCMN" and (inst.split(" ")[2][3:-1]).isdigit():
        # CCMN <Xn>, #<imm5>, #<nzcv>, <cond>
        # CCMN
        # print(1525761 << 11)
        # <Xn>
        # (int(inst.split(" ")[1][1:-1]) << 5)
        # <imm5>
        # (int(inst.split(" ")[1][3:-1], 16) << 16)
        # <nzcv> / 4 bit
        # (int(inst.split(" ")[3][3:-1], 16))
        # <cond> / 4 bit
        # (int(inst.split(" ")[4][3:], 16) << 12)  
        result = ((1525761 << 11) + (int(inst.split(" ")[1][1:-1]) << 5) + (int(inst.split(" ")[1][3:-1], 16) << 16) + (int(inst.split(" ")[3][3:-1], 16)) + (int(inst.split(" ")[4][3:], 16) << 12))
    elif inst.split(" ")[0] == "DCPS1":
        # DCPS1 {#<imm16>}
        # DCPS1
        # print(3567255553)
        # <imm16>
        # (int(inst.split(" ")[1][3:],16) << 5)
        result = ((3567255553) + (int(inst.split(" ")[1][3:],16) << 5))
    elif inst.split(" ")[0] == "DCPS2":
        # DCPS2 {#<imm16>}
        # DCPS2
        # print(3567255554)
        # <imm16>
        # (int(inst.split(" ")[1][3:],16) << 5)
        result = ((3567255554) + (int(inst.split(" ")[1][3:],16) << 5))
    elif inst.split(" ")[0] == "DCPS3":
        # DCPS3 {#<imm16>}
        # DCPS3
        # print(3567255555)
        # <imm16>
        # (int(inst.split(" ")[1][3:],16) << 5)
        result = ((3567255555) + (int(inst.split(" ")[1][3:],16) << 5))
    elif inst == "DRPS":
        result = (3602842592)
    elif inst.split(" ")[0] == "EON":
        # EON <Xd>, <Xn>, <Xm>{, <shift> #<amount>}
        # EON
        # print(1617 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[4][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[5][3:], 16) << 10)  
        result = ((1617 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 22) + (int(inst.split(" ")[5][3:], 16) << 10))
    elif inst == "ERETAA":
        result = (3600747519)
    elif inst == "ERETAB":
        result = (3600748543)
    elif inst == "ERET":
        result = (3600745440)
    elif inst == "ESB":
        result = (3573752351)
    elif inst.split(" ")[0] == "EXTR":
        # EXTR <Xd>, <Xn>, <Xm>, #<lsb>
        # print(1182 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <lsb>
        # (int(inst.split(" ")[4][3:], 16) << 10)    
        result = ((1182 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "STZ2G":
        # STZ2G <Xt|SP>, [<Xn|SP>], #<simm>
        # STZ2G
        # print(3569665 << 10)
        # <Xt|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <simm> / imm9
        # (int(inst.split(" ")[3][3:], 16) << 12)
        result = ((3569665 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 12))
    elif inst.split(" ")[0] == "STZG":
        # STZG <Xt|SP>, [<Xn|SP>], #<simm>
        # STZG
        # print(3561473 << 10)
        # <Xt|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <simm> / imm9
        # (int(inst.split(" ")[3][3:], 16) << 12)
        result = ((3561473 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 12))
    elif inst.split(" ")[0] == "STZGM":
        # STZGM <Xt>, [<Xn|SP>]
        # STZGM
        # print(1737 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[2][1:]) << 5)
        result = ((1737 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "SVC":
        # SVC #<imm16>
        # SVC
        # print((53 << 26) + 1)
        # <imm16>
        # (int(inst.split(" ")[1][3:],16) << 5)
        result = (((53 << 26) + 1) + (int(inst.split(" ")[1][3:],16) << 5))
    elif inst.split(" ")[0] == "SXTB":
        # SXTB <Xd>, <Wn>
        # SXTB
        # result = (2412551 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:]) << 5)   
        result = ((2412551 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "SXTH":
        # SXTH <Xd>, <Wn>
        # SXTH
        # print(2412559 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:]) << 5)   
        result = ((2412559 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "SXTW":
        # SXTW <Xd>, <Wn>
        # SXTW
        # print(2412575 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:]) << 5)   
        result = ((2412575 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:]) << 5))
    elif inst.split(" ")[0] == "MUL":
        # MUL <Xd>, <Xn>, <Xm>
        # MUL 
        # print(2539551 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((2539551 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "LSLV":
        # LSLV <Xd>, <Xn>, <Xm>
        # LSLV
        # print(316929 << 13)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        result = ((316929 << 13) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16))
    elif inst.split(" ")[0] == "LSL":
        # LSL<Xd>, <Xn>, #<shift>
        # print(845 << 22)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <shift> / immr
        # (int(inst.split(" ")[3][3:], 16) << 16)
        result = ((845 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 16))
    elif inst.split(" ")[0] == "LSRV":
        # LSRV <Xd>, <Xn>, <Xm>
        # LSRV
        # print(2535433 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        result = ((2535433 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16))
    elif inst.split(" ")[0] == "LSR":
        # LSR <Xd>, <Xn>, #<shift>
        # print(3461183 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <shift> / immr
        # (int(inst.split(" ")[3][3:], 16) << 16)
        result = ((3461183 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 16))
    elif inst.split(" ")[0] == "SWPT":
        # 0	sz	011001	A	R	1	Rs	100001	Rn	Rt
        # SWPT <Xs>, <Xt>, [<Xn|SP>]
        # SWPT
        # print(1495303168)
        # <Xs>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((1495303168) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPTA":
        # 0	sz	011001	A	R	1	Rs	100001	Rn	Rt
        # SWPTA <Xs>, <Xt>, [<Xn|SP>]
        # SWPTA
        # print(1503691776)
        # <Xs>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((1503691776) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPTAL":
        # 0	sz	011001	A	R	1	Rs	100001	Rn	Rt
        # SWPTAL <Xs>, <Xt>, [<Xn|SP>]
        # SWPTAL
        # print(1507886080)
        # <Xs>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((1507886080) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPTL":
        # 0	sz	011001	A	R	1	Rs	100001	Rn	Rt
        # SWPTL <Xs>, <Xt>, [<Xn|SP>]
        # SWPTL
        # print(1499497472)
        # <Xs>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((1499497472) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPP":
        # 00011001	A	R	1	Rt2	100000	Rn	Rt1
        # 00011001001000001000000000000000
        # SWPP <Xt1>, <Xt2>, [<Xn|SP>]
        # SWPP 
        # print(421560320)
        # <Xt1>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt2>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((421560320) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPPA":
        # SWPPA <Xt1>, <Xt2>, [<Xn|SP>]
        # SWPPA 
        # print(429948928)
        # <Xt1>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt2>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((429948928) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPPAL":
        # SWPPAL <Xt1>, <Xt2>, [<Xn|SP>]
        # SWPPAL 
        # print(434143232)
        # <Xt1>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt2>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((434143232) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPPL":
        # SWPPL <Xt1>, <Xt2>, [<Xn|SP>]
        # SWPPL 
        # print(425754624)
        # <Xt1>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Xt2>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((425754624) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPH":
        # 01111000	A	R	1	Rs	100000	Rn	Rt
        # 01111000	0	0	1	00000	100000	00000	00000
        # SWPH <Ws>, <Wt>, [<Xn|SP>]
        # SWPH
        # print(2015395840)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((2015395840) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPAH":
        # 01111000	A	R	1	Rs	100000	Rn	Rt
        # 01111000	1	0	1	00000	100000	00000	00000
        # SWPAH <Ws>, <Wt>, [<Xn|SP>]
        # SWPAH
        # print(2023784448)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((2023784448) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPALH":
        # 01111000	A	R	1	Rs	100000	Rn	Rt
        # 01111000	1	1	1	00000	100000	00000	00000
        # SWPALH <Ws>, <Wt>, [<Xn|SP>]
        # SWPALH
        # print(2027978752)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((2027978752) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPLH":
        # 01111000	A	R	1	Rs	100000	Rn	Rt
        # 01111000	0	1	1	00000	100000	00000	00000
        # SWPLH <Ws>, <Wt>, [<Xn|SP>]
        # SWPLH
        # print(2019590144)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((2019590144) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPB":
        # 00111000	A	R	1	Rs	100000	Rn	Rt
        # 00111000	0	0	1	00000	100000	00000	00000
        # SWPB <Ws>, <Wt>, [<Xn|SP>]
        # SWPB
        # print(941654016)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((941654016) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPAB":
        # 00111000	A	R	1	Rs	100000	Rn	Rt
        # 00111000	1	0	1	00000	100000	00000	00000
        # SWPAB <Ws>, <Wt>, [<Xn|SP>]
        # SWPAB
        # print(950042624)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((950042624) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPALB":
        # 00111000	A	R	1	Rs	100000	Rn	Rt
        # 00111000	1	1	1	00000	100000	00000	00000
        # SWPALB <Ws>, <Wt>, [<Xn|SP>]
        # SWPALB
        # print(954236928)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((954236928) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SWPLB":
        # 00111000	A	R	1	Rs	100000	Rn	Rt
        # 00111000	0	1	1	00000	100000	00000	00000
        # SWPLB <Ws>, <Wt>, [<Xn|SP>]
        # SWPLB
        # print(945848320)
        # <Ws>
        # (int(inst.split(" ")[1][1:-1]) << 16)
        # <Wt>
        # (int(inst.split(" ")[2][1:-1]))
        # [<Xn|SP>]
        # (int(inst.split(" ")[3][1:]) << 5)
        result = ((945848320) + (int(inst.split(" ")[1][1:-1]) << 16) + (int(inst.split(" ")[2][1:-1])) + (int(inst.split(" ")[3][1:]) << 5))
    elif inst.split(" ")[0] == "SUB" and (inst.split(" ")[1][1:-1]).isdigit() and (inst.split(" ")[2][1:-1]).isdigit() and (inst.split(" ")[3][3:]
    ).isdigit(): # Green
        # SUB <Xd|SP>, <Xn|SP>, #<imm12>
        # SUB - Immediate
        # print(836 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm12>
        # (int(inst.split(" ")[3][3:]) << 10)
        result = ((836 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 10))
    elif inst.split(" ")[0] == "SUBS" and (inst.split(" ")[1][1:-1]).isdigit() and (inst.split(" ")[2][1:-1]).isdigit() and (inst.split(" ")[3][3:]
    ).isdigit(): # Green
        # SUBS <Xd>, <Xn|SP>, #<imm12>
        # SUBS - Immediate with CPSR Turned On
        # print(964 << 22)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>    
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <imm12>
        # (int(inst.split(" ")[3][3:]) << 10)
        result = ((964 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 10))
    elif inst.split(" ")[0] == "SUBG": # Green
        # SUBG <Xd|SP>, <Xn|SP>, #<uimm6>, #<uimm4>
        # SUBG
        # print(838 << 22)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP> 
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <uimm6>
        # (int(inst.split(" ")[3][3:-1], 16) << 16)
        # <uimm4>
        # (int(inst.split(" ")[4][3:], 16) << 10)
        result = ((838 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:-1], 16) << 16) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "SUBPT": # Green
        # SUBPT <Xd|SP>, <Xn|SP>, <Xm>{, #<amount>}
        # SUBPT
        # print(446465 << 13)
        # <Xd|SP>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <amount> / <imm3>
        # (int(inst.split(" ")[4][3:], 16) << 10)
        result = ((446465 << 13) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "SUB":
        choice = input("SUB <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}} or SUB <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}?: ")
        if choice == "SUB <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}}": 
            # SUB <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}}
            # SUB (extended register)
            # print(1625 << 21)
            # <Xd|SP>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # (int(inst.split(" ")[2][1:-1]))
            # <Rm>
            # (int(inst.split(" ")[3][1:-1]))
            # <extend> / option
            # int(inst.split(" ")[4][3:-1], 16)
            # <amount> / imm3
            # int(inst.split(" ")[5][3:], 16)
            result = ((1625 << 21) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 13) + (int(inst.split(" ")[5][3:], 16) << 10) + ((int(inst.split(" ")[2][1:-1])) << 5) + (int(inst.split(" ")[1][1:-1])))
            pass
        elif choice == "SUB <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}":
            # SUB <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}
            # SUB (shifted register)
            # print(1624 << 21)
            # <Xd>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <shift> / 2 bit
            # (int(inst.split(" ")[4][3:-1], 16) << 22)
            # <amount> / imm6
            # (int(inst.split(" ")[5][3:], 16) << 10)
            result = ((1624 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + ((int(inst.split(" ")[4][3:-1], 16)) << 22) + ((int(inst.split(" ")[5][3:], 16)) << 10))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "SUBS":
        choice = input("SUBS <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}} or SUBS <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}?: ")
        if choice == "SUBS <Xd|SP>, <Xn|SP>, <Rm>{, <extend>, {#<amount>}}": 
            # SUBS <Xd|SP>, <Xn|SP>, <Xm>{, <extend>, {#<amount>}}
            # SUBS (extended register)
            # print(1881 << 21)
            # <Xd|SP>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # (int(inst.split(" ")[2][1:-1]))
            # <Rm>
            # (int(inst.split(" ")[3][1:-1]))
            # <extend> / option
            # int(inst.split(" ")[4][3:-1], 16)
            # <amount> / imm3
            # int(inst.split(" ")[5][3:], 16)
            result = ((1881 << 21) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 13) + (int(inst.split(" ")[5][3:], 16) << 10) + ((int(inst.split(" ")[2][1:-1])) << 5) + (int(inst.split(" ")[1][1:-1])))
            pass
        elif choice == "SUBS <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}":
            # SUBS <Xd>, <Xn>, <Xm>{, <shift>, {#<amount>}}
            # SUBS (shifted register)
            # print(1880 << 21)
            # <Xd>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <shift> / 2 bit
            # (int(inst.split(" ")[4][3:-1], 16) << 22)
            # <amount> / imm6
            # (int(inst.split(" ")[5][3:], 16) << 10)
            result = (((1880 << 21)) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:-1], 16) << 22) + (int(inst.split(" ")[5][3:], 16) << 10))
        else: 
            result = 0    
            pass
    elif inst.split(" ")[0] == "LDAPR":
        choice = input("Post-index or No offset?: ")
        if choice == "Post-index":
            # LDAPR <Xt>, [<Xn|SP>]
            # LDAPR
            # print(3567618 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            result = ((3567618 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "No offset":
            # LDAPR <Xt>, [<Xn|SP>]
            # LDAPR
            # print(4075504 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            result = ((4075504 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDAPRB":
        # LDAPRB <Wt>, [<Xn|SP>]
        # LDAPRB
        # print(929776 << 10)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((929776 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5)) 
    elif inst.split(" ")[0] == "LDAPRH":
        # LDAPRH <Wt>, [<Xn|SP>]
        # LDAPRH
        # print(1978352 << 10)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1978352 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))       
    elif inst.split(" ")[0] == "LDAPUR":
        # LDAPUR <Xt>, [<Xn|SP>{, #<simm>}]
        # LDAPUR
        # print(869 << 22)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        # <simm> / imm9
        # ((int(inst.split(" ")[3][3:]), 16) << 12)
        result = ((869 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAPURB":
        # LDAPURB <Xt>, [<Xn|SP>{, #<simm>}]
        # LDAPURB
        # print(101 << 22)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        # <simm> / imm9
        # ((int(inst.split(" ")[3][3:]), 16) << 12)
        result = ((101 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAPURH":
        # LDAPURH <Xt>, [<Xn|SP>{, #<simm>}]
        # LDAPURH
        # print(357 << 22)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        # <simm> / imm9
        # ((int(inst.split(" ")[3][3:]), 16) << 12)
        result = ((357 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAPURSB":
        # LDAPURSB <Xt>, [<Xn|SP>{, #<simm>}]
        # LDAPURSB
        # print(102 << 22)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        # <simm> / imm9
        # ((int(inst.split(" ")[3][3:]), 16) << 12)
        result = ((102 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAR":
        # LDAR <Xt>, [<Xn|SP>]
        # LDAR
        # print(3291135 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((3291135 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDARB":
        # LDARB <Xt>, [<Xn|SP>]
        # LDARB
        # print(145407 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((145407 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDARH":
        # LDARH <Xt>, [<Xn|SP>]
        # LDARH
        # print(1193983 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1193983 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDARXR":
        # LDARXR <Xt>, [<Xn|SP>]
        # LDARXR
        # print(3299327 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((3299327 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAXR":
        # LDAXR <Xt>, [<Xn|SP>]
        # LDAXR
        # print(3282943 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((3282943 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAXRB":
        # LDAXRB <Xt>, [<Xn|SP>]
        # LDAXRB
        # print(137215 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((137215 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDAXRH":
        # LDAXRH <Xt>, [<Xn|SP>]
        # LDAXRH
        # print(1185791 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1185791 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDG":
        # LDG <Xt>, [<Xn|SP>{, #<simm>}]
        # LDG
        # print(1739 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        # <simm> / imm9
        # ((int(inst.split(" ")[3][3:]), 16) << 12)
        result = ((1739 << 21) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDGM":
        # LDGM <Xt>, [<Xn|SP>]
        # LDGM
        # print(1743 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1743 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDLAR":
        # LDLAR <Xt>, [<Xn|SP>]
        # LDLAR
        # print(3291103 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((3291103 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDLARB":
        # LDLARB <Xt>, [<Xn|SP>]
        # LDLARB
        # print(145375 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((145375 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDLARH":
        # LDLARH <Xt>, [<Xn|SP>]
        # LDLARH
        # print(1193951 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1193951 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "LDNP": 
        # LDNP <Xt1>, <Xt2>, [<Xn|SP>{, #<imm7>}]
        # LDNP
        # print(673 << 22)
        # <Xt1>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xt2>
        # (int(inst.split(" ")[2][1:-1]) << 10)
        # <Xn|SP>
        # (int(inst.split(" ")[3][1:-1]) << 5)
        # <imm7>
        # (int(inst.split(" ")[4][3:], 16) << 15)
        result = ((673 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
    elif inst.split(" ")[0] == "LDP" and ((inst.split(" ")[4][3:])).isdigit():
        choice = input("Post-index or Pre-index or Signed offset?: ")
        if choice == "Post-index":
            # LDP <Xt1>, <Xt2>, [<Xn|SP>], #<imm7>
            # LDP - Post-index
            # print(675 << 22)
            # <Xt1>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xt2>
            # (int(inst.split(" ")[2][1:-1]) << 10)
            # <Xn|SP>
            # (int(inst.split(" ")[3][1:-1]) << 5)
            # <imm7>
            # (int(inst.split(" ")[4][3:], 16) << 15)
            result = ((675 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
            pass
        elif choice == "Pre-index":
            # LDP <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
            # LDP - Pre-index
            # print(679 << 22)
            # <Xt1>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xt2>
            # (int(inst.split(" ")[2][1:-1]) << 10)
            # <Xn|SP>
            # (int(inst.split(" ")[3][1:-1]) << 5)
            # <imm7>
            # (int(inst.split(" ")[4][3:], 16) << 15)
            result = ((679 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
            pass
        elif choice == "Signed offset":
            # LDP <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
            # LDP - Signed offset
            # print(677 << 22)
            # <Xt1>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xt2>
            # (int(inst.split(" ")[2][1:-1]) << 10)
            # <Xn|SP>
            # (int(inst.split(" ")[3][1:-1]) << 5)
            # <imm7>
            # (int(inst.split(" ")[4][3:], 16) << 15)
            result = ((677 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDPSW" and ((inst.split(" ")[4][3:])).isdigit():
        choice = input("Post-index or Pre-index or Signed offset?: ")
        if choice == "Post-index":
            # LDPSW <Xt1>, <Xt2>, [<Xn|SP>], #<imm7>
            # LDPSW - Post-index
            # print(419 << 22)
            # <Xt1>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xt2>
            # (int(inst.split(" ")[2][1:-1]) << 10)
            # <Xn|SP>
            # (int(inst.split(" ")[3][1:-1]) << 5)
            # <imm7>
            # (int(inst.split(" ")[4][3:], 16) << 15)
            result = ((419 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
            pass
        elif choice == "Pre-index":
            # LDPSW <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
            # LDPSW - Pre-index
            # print(423 << 22)
            # <Xt1>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xt2>
            # (int(inst.split(" ")[2][1:-1]) << 10)
            # <Xn|SP>
            # (int(inst.split(" ")[3][1:-1]) << 5)
            # <imm7>
            # (int(inst.split(" ")[4][3:], 16) << 15)
            result = ((423 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
            pass
        elif choice == "Signed offset":
            # LDPSW <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
            # LDPSW - Signed offset
            # print(421 << 22)
            # <Xt1>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xt2>
            # (int(inst.split(" ")[2][1:-1]) << 10)
            # <Xn|SP>
            # (int(inst.split(" ")[3][1:-1]) << 5)
            # <imm7>
            # (int(inst.split(" ")[4][3:], 16) << 15)
            result = ((421 << 22) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 10) + (int(inst.split(" ")[3][1:-1]) << 5) + (int(inst.split(" ")[4][3:], 16) << 15))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRSW" and ((inst.split(" ")[2][3:])).isdigit():
        # LDRSW <Xt>, <label>
        # LDRSW - literal
        # print(19 << 27)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <label> / imm19
        # ((int(inst.split(" ")[2][3:]), 16) << 5)
        result = ((19 << 27) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:]), 16) << 5))
    elif inst.split(" ")[0] == "LDRSW" and ((inst.split(" ")[2][1:-1])).isdigit():
        # LDRSW <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
        # LDRSW - register
        # print(1512449 << 11)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Wm>|<Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <extend>
        # (int(inst.split(" ")[4][3:], 16) << 13)
        result = ((1512449 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
    elif inst.split(" ")[0] == "LDRSW" and ((inst.split(" ")[3][3:])).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # LDRSW <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSW - Post-index
            # print(3022849 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((3022849 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # LDRSW <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSW - Pre-index
            # print(3022851 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((3022851 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # LDRSW <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSW - Unsigned offset
            # print(371 << 23)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((371 << 23) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRSH" and ((inst.split(" ")[2][1:-1])).isdigit():
        # LDRSH <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
        # LDRSH - register
        # print(988161 << 11)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Wm>|<Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <extend> / option
        # (int(inst.split(" ")[4][3:], 16) << 13)
        result = ((988161 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
    elif inst.split(" ")[0] == "LDRSH" and ((inst.split(" ")[3][3:])).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # LDRSH <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSH - Post-index
            # print(1974273 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((1974273 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # LDRSH <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSH - Pre-index
            # print(1974275 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((1974275 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # LDRSH <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSH - Unsigned offset
            # print(243 << 23)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((243 << 23) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRH" and ((inst.split(" ")[2][1:-1])).isdigit():
        # LDRH <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
        # LDRH - register
        # print(986113 << 11)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Wm>|<Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <extend> / option
        # (int(inst.split(" ")[4][3:], 16) << 13)
        result = ((986113 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
    elif inst.split(" ")[0] == "LDRH" and ((inst.split(" ")[3][3:])).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # LDRH <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRH - Post-index
            # print(1970177 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((1970177 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # LDRH <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRH - Pre-index
            # print(1970179 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((1970179 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # LDRH <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRH - Unsigned offset
            # print(485 << 22)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((485 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDR" and ((inst.split(" ")[2][1:-1])).isdigit():
        # LDR <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
        # LDR - register
        # print(2034689 << 11)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Wm>|<Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <extend> / option
        # (int(inst.split(" ")[4][3:], 16) << 13)
        result = ((2034689 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
    elif inst.split(" ")[0] == "LDR" and ((inst.split(" ")[2][3:])).isdigit():
        # LDR <Xt>, <label>
        # LDR - literal
        # print(11 << 27)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <label> / imm19
        # ((int(inst.split(" ")[2][3:]), 16) << 5)
        result = ((11 << 27) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:], 16)) << 5))
    elif inst.split(" ")[0] == "LDR" and ((inst.split(" ")[3][3:])).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # LDR <Xt>, [<Xn|SP>{, #<simm>}]
            # LDR - Post-index
            # print(4067329 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((4067329 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # LDR <Xt>, [<Xn|SP>{, #<simm>}]
            # LDR - Pre-index
            # print(4067331 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((4067331 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # LDR <Xt>, [<Xn|SP>{, #<simm>}]
            # LDR - Unsigned offset
            # print(997 << 22)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((997 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRSB" and ((inst.split(" ")[3][3:])).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # LDRSB <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSB - Post-index
            # print(925697 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((925697 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # LDRSB <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSB - Pre-index
            # print(925699 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((925699 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # LDRSB <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRSB - Unsigned offset
            # print(230 << 22)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((230 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRB" and ((inst.split(" ")[3][3:])).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # LDRB <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRB - Post-index
            # print(921601 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((921601 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # LDRB <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRB - Pre-index
            # print(921603 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((921603 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # LDRB <Xt>, [<Xn|SP>{, #<simm>}]
            # LDRB - Unsigned offset
            # print(229 << 22)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((229 << 22) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRSB" and ((inst.split(" ")[3][1:-1])).isdigit():
        choice = input("LDRSB <Xt>, [<Xn|SP>, (<Wm>|<Xm>), <extend> {<amount>}] or LDRSB <Xt>, [<Xn|SP>, <Xm>{, LSL <amount>}]?: ")
        if choice == "LDRSB <Xt>, [<Xn|SP>, (<Wm>|<Xm>), <extend> {<amount>}]":
            # LDRSB <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
            # LDRSB - Extended register
            # print(463873 << 11)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Wm>|<Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <extend> / option
            # (int(inst.split(" ")[4][3:], 16) << 13)
            result = ((463873 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
            pass
        elif choice == "LDRSB <Xt>, [<Xn|SP>, <Xm>{, LSL <amount>}]":
            # LDRSB <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, LSL}]
            # LDRSB - Shifted register
            # print(463873 << 11)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Wm>|<Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # LSL
            # (3 << 13)
            result = ((463873 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (3 << 13))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "LDRB" and ((inst.split(" ")[3][1:-1])).isdigit():
        choice = input("LDRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>), <extend> {<amount>}] or LDRB <Wt>, [<Xn|SP>, <Xm>{, LSL <amount>}]?: ")
        if choice == "LDRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>), <extend> {<amount>}]":
            # LDRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
            # LDRB - Extended register
            # print(461825 << 11)
            # <Wt>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Wm>|<Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <extend> / option
            # (int(inst.split(" ")[4][3:], 16) << 13)
            result = ((461825 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
            pass
        elif choice == "LDRB <Wt>, [<Xn|SP>, <Xm>{, LSL <amount>}]":
            # LDRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>){, LSL}]
            # LDRB - Shifted register
            # print(461825 << 11)
            # <Wt>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Wm>|<Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # LSL
            # (3 << 13)
            result = ((461825 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (3 << 13))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "STG":
        choice = input("Post-index or Pre-index or Signed offset?: ")
        if choice == "Post-index":
            # STG <Xt>, [<Xn|SP>{, #<simm>}]
            # STG - Post-index
            # print(3557377 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((3557377 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # STG <Xt>, [<Xn|SP>{, #<simm>}]
            # STG - Pre-index
            # print(3557379 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((3557379 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Signed offset":
            # STG <Xt>, [<Xn|SP>{, #<simm>}]
            # STG - Signed offset
            # print(3557378 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((3557378 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "STGM":
        # STGM <Xt>, [<Xn|SP>]
        # STGM
        # print(1741 << 21)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1741 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "STLR":
        # STLR <Xt>, [<Xn|SP>]
        # STLR
        # print(3287039 << 10)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((3287039 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "STLRB":
        # STLRB <Wt>, [<Xn|SP>]
        # STLRB
        # print(141311 << 10)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((141311 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "STLRH":
        # STLRH <Wt>, [<Xn|SP>]
        # STLRH
        # print(1189887 << 10)
        # <Wt>
        # (int(inst.split(" ")[1][1:-1]))
        # [<Xn|SP>]
        # ((int(inst.split(" ")[2][1:-1])) << 5) 
        result = ((1189887 << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
    elif inst.split(" ")[0] == "STR" and (inst.split(" ")[3][3:]).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # STR <Xt>, [<Xn|SP>{, #<simm>}]
            # STR - Post-index
            # print(4063233 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((4063233 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # STR <Xt>, [<Xn|SP>{, #<simm>}]
            # STR - Pre-index
            # print(4063235 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((4063235 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # STR <Xt>, [<Xn|SP>{, #<simm>}]
            # STR - Unsigned offset
            # print(249 << 24)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 10)
            result = ((249 << 24) + ((int(inst.split(" ")[3][3:]), 16) << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "STRB" and (inst.split(" ")[3][3:]).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # STRB <Xt>, [<Xn|SP>{, #<simm>}]
            # STRB - Post-index
            # print(917505 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((917505 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # STRB <Xt>, [<Xn|SP>{, #<simm>}]
            # STRB - Pre-index
            # print(917507 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((917507 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # STRB <Xt>, [<Xn|SP>{, #<simm>}]
            # STRB - Unsigned offset
            # print(57 << 24)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 10)
            result = ((57 << 24) + ((int(inst.split(" ")[3][3:]), 16) << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "STRH" and (inst.split(" ")[3][3:]).isdigit():
        choice = input("Post-index or Pre-index or Unsigned offset?: ")
        if choice == "Post-index":
            # STRH <Xt>, [<Xn|SP>{, #<simm>}]
            # STRH - Post-index
            # print(1966081 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((1966081 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Pre-index":
            # STRH <Xt>, [<Xn|SP>{, #<simm>}]
            # STRH - Pre-index
            # print(1966083 << 10)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm9
            # ((int(inst.split(" ")[3][3:]), 16) << 12)
            result = ((1966083 << 10) + ((int(inst.split(" ")[3][3:]), 16) << 12) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        elif choice == "Unsigned offset":
            # STRH <Xt>, [<Xn|SP>{, #<simm>}]
            # STRH - Unsigned offset
            # print(121 << 24)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # [<Xn|SP>]
            # ((int(inst.split(" ")[2][1:-1])) << 5) 
            # <simm> / imm12
            # ((int(inst.split(" ")[3][3:]), 16) << 10)
            result = ((121 << 24) + ((int(inst.split(" ")[3][3:]), 16) << 10) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "STR" and ((inst.split(" ")[3][1:-1])).isdigit():
        # STR <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
        # STR - register
        # print(2032641 << 11)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Wm>|<Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <extend> / option
        # (int(inst.split(" ")[4][3:], 16) << 13)
        result = ((2032641 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
    elif inst.split(" ")[0] == "STRB" and ((inst.split(" ")[3][1:-1])).isdigit():
        choice = input("STRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>), <extend> {<amount>}] or STRB <Wt>, [<Xn|SP>, <Xm>{, LSL <amount>}]?: ")
        if choice == "STRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>), <extend> {<amount>}]":
            # STRB <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
            # STRB - Extended register
            # print(459777 << 11)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Wm>|<Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # <extend> / option
            # (int(inst.split(" ")[4][3:], 16) << 13)
            result = ((459777 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))
            pass
        elif choice == "STRB <Wt>, [<Xn|SP>, <Xm>{, LSL <amount>}]":
            # STRB <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, LSL}]
            # STRB - Shifted register
            # print(459777 << 11)
            # <Xt>
            # (int(inst.split(" ")[1][1:-1]))
            # <Xn|SP>
            # ((int(inst.split(" ")[2][1:-1])) << 5)
            # <Wm>|<Xm>
            # ((int(inst.split(" ")[3][1:-1])) << 16)
            # LSL
            # (3 << 13)
            result = ((459777 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (3 << 13))
            pass
        else:
            result = 0
            pass
    elif inst.split(" ")[0] == "STRH" and ((inst.split(" ")[3][1:-1])).isdigit():
        # STRH <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> }]
        # STRH - register
        # print(984065 << 11)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn|SP>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Wm>|<Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <extend> / option
        # (int(inst.split(" ")[4][3:], 16) << 13)
        result = ((984065 << 11) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[4][3:], 16) << 13))    
    elif inst == "HLT": 
        result = ((849 << 22) + (int(inst.split(" ")[1][3:], 16)) << 5)
    elif inst == "HVC": 
        result = (((53 << 26) + 2) + (int(inst.split(" ")[1][3:], 16)) << 5)
    elif inst.split(" ")[0] == "TBNZ":
        # TBNZ <Xt>, #<imm5, <label>
        # TBNZ
        # print(183 << 24)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm5> / b40
        # ((int(inst.split(" ")[2][3:-1]), 16) << 19)
        # <label> / imm14
        # ((int(inst.split(" ")[3][3:]), 16) << 5)
        result = ((183 << 24) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1], 16)) << 19) + ((int(inst.split(" ")[3][3:], 16)) << 5))
    elif inst.split(" ")[0] == "TBZ":
        # TBZ <Xt>, #<imm5, <label>
        # TBZ
        # print(182 << 24)
        # <Xt>
        # (int(inst.split(" ")[1][1:-1]))
        # <imm5> / b40
        # ((int(inst.split(" ")[2][3:-1]), 16) << 19)
        # <label> / imm14
        # ((int(inst.split(" ")[3][3:]), 16) << 5)
        result = ((182 << 24) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][3:-1], 16)) << 19) + ((int(inst.split(" ")[3][3:], 16)) << 5))
    elif inst.split(" ")[0] == "TCANCEL":
        # TCANCEL #<imm16>
        # TCANCEL
        # print(1699 << 21)
        # <imm16>
        # (int(inst.split(" ")[1][3:], 16) << 5)
        result = ((1699 << 21) + (int(inst.split(" ")[1][3:], 16) << 5))
    elif inst == "TCOMMIT":
        result = (3573756031)
    elif inst == "TSB":
        result = (3573752415)
    elif inst.split(" ")[0] == "TSTART":
        # TSTART <Xt>
        # TSTART
        # print(111745411 << 5)
        # <Xt>
        # int(inst.split(" ")[1][1:])
        result = ((111745411 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "TTEST":
        # TTEST <Xt>
        # TTEST
        # print(111745419 << 5)
        # <Xt>
        # int(inst.split(" ")[1][1:])
        result = ((111745419 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "UDIV": 
        # UDIV <Xd>, <Xn>, <Xm>
        # UDIV
        # print(1267713 << 11)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)    
        result = ((1267713 << 11) + (int(inst.split(" ")[3][1:]) << 16) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[1][1:-1])))

    elif inst.split(" ")[0] == "UMADDL":
        # UMADDL <Xd>, <Wn>, <Wm>, <Xa>
        # UMADDL
        # print(1245 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Wn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Wm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <Xa>
        # (int(inst.split(" ")[4][1:]) << 10)
        result = ((1245 << 21) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][1:]) << 10) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[1][1:-1])))
    elif inst.split(" ")[0] == "UMAX" and ((inst.split(" ")[1][1:-1]).isdigit()) and ((inst.split(" ")[2][1:-1]).isdigit()) and ((inst.split(" ")[3][3:]).isdigit()):
        # UMAX <Xd>, <Xn>, #<uimm8>
        # UMAX
        # print(9329 << 18)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)    
        # <uimm8>
        # (int(inst.split(" ")[3][3:], 16) << 10)
        result = ((9329 << 18) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 10))
    elif inst.split(" ")[0] == "UMAX" and ((inst.split(" ")[1][1:-1]).isdigit()) and ((inst.split(" ")[2][1:-1]).isdigit()) and ((inst.split(" ")[3][1:]).isdigit()):
        # UMAX <Xd>, <Xn>, <Xm>
        # UMAX
        # print(2535449 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)    
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((2535449 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "UMIN" and ((inst.split(" ")[1][1:-1]).isdigit()) and ((inst.split(" ")[2][1:-1]).isdigit()) and ((inst.split(" ")[3][3:]).isdigit()):
        # UMIN <Xd>, <Xn>, #<uimm8>
        # UMIN
        # print(9331 << 18)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)    
        # <uimm8>
        # (int(inst.split(" ")[3][3:], 16) << 10)
        result = ((9331 << 18) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][3:], 16) << 10))
    elif inst.split(" ")[0] == "UMIN" and ((inst.split(" ")[1][1:-1]).isdigit()) and ((inst.split(" ")[2][1:-1]).isdigit()) and ((inst.split(" ")[3][1:]).isdigit()):
        # UMIN <Xd>, <Xn>, <Xm>
        # UMIN
        # print(2535451 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)    
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((2535451 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "UMNEGL":
        # UMNEGL <Xd>, <Wn>, <Wm>
        # UMNEGL
        # print(2549823 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Wn>
        # (int(inst.split(" ")[2][1:-1]) << 5)    
        # <Wm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((2549823 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "UMSUBL":
        # UMSUBL <Xd>, <Wn>, <Wm>, <Xa>
        # UMSUBL
        # print(79681 << 15)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Wn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xa>
        # (int(inst.split(" ")[4][1:]) << 10)    
        # <Wm>
        # (int(inst.split(" ")[3][1:-1]) << 16)   
        result = ((79681 << 15) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[4][1:]) << 10) + (int(inst.split(" ")[3][1:-1]) << 16))   
    elif inst.split(" ")[0] == "MOVZ":
        # MOVZ
        result = ((293 << 23) + (2 << 29) + (int(inst.split(" ")[2][1:],16) << 5) + (int(inst.split(" ")[1][1: -1])))

    elif inst.split(" ")[0] == "MOVK":
        # MOVK
        result = ((293 << 23) + (3 << 29) + (int(inst.split(" ")[2][1:],16) << 5) + (int(inst.split(" ")[1][1: -1])))

    elif inst.split(" ")[0] == "MOVN":
        # MOVN
        result = ((293 << 23) + (int(inst.split(" ")[2][1:],16) << 5) + (int(inst.split(" ")[1][1: -1]))) 
    elif inst.split(" ")[0] == "MADD":
        # MADD <Xd>, <Xn>, <Xm>, <Xa>
        # MADD
        # print(155 << 24)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <Xa>
        # (int(inst.split(" ")[4][1:]) << 10)
        result = ((155 << 24) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][1:]) << 10))
    elif inst.split(" ")[0] == "MADDPT":
        # MADDPT <Xd>, <Xn>, <Xm>, <Xa>
        # MADDPT
        # print(1243 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <Xa>
        # (int(inst.split(" ")[4][1:]) << 10)
        result = ((1243 << 21) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][1:]) << 10))
    elif inst.split(" ")[0] == "MNEG":
        # MNEG <Xd>, <Xn>, <Xm>
        # MNEG
        # print(2539583 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((2539583 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "MSUB":
        # MSUB <Xd>, <Xn>, <Xm>, <Xa>
        # MSUB
        # print(79361 << 15)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <Xa>
        # (int(inst.split(" ")[4][1:]) << 10)
        result = ((79361 << 15) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][1:]) << 10))
    elif inst.split(" ")[0] == "MSUBPT":
        # MSUBPT <Xd>, <Xn>, <Xm>, <Xa>
        # MSUBPT
        # print(79553 << 15)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:-1]) << 16)
        # <Xa>
        # (int(inst.split(" ")[4][1:]) << 10)
        result = ((79553 << 15) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:-1]) << 16) + (int(inst.split(" ")[4][1:]) << 10))
    elif inst.split(" ")[0] == "NOP":
        # NOP
        result = (3573751839)
    elif inst.split(" ")[0] == "ORN":
        # ORN <Xd>, <Xn>, <Xm>{, <shift> #<amount>}
        # ORN
        # print(1361 << 21)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:-1])) << 5)
        # <Xm>
        # ((int(inst.split(" ")[3][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[4][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[5][3:], 16) << 10)  
        result = ((1361 << 21) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 5) + ((int(inst.split(" ")[3][1:-1])) << 16) + (int(inst.split(" ")[5][3:], 16) << 10))
    elif inst.split(" ")[0] == "NEG":
        # NEG <Xd>, <Xm>{, <shift> #<amount>}
        # NEG
        # print(106430495 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # ((int(inst.split(" ")[2][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[3][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[4][3:], 16) << 10) 
        result = ((106430495 << 5) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 16) + (int(inst.split(" ")[3][3:-1], 16) << 22) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "NEGS":
        # NEGS <Xd>, <Xm>{, <shift> #<amount>}
        # NEGS
        # print(123207711 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # ((int(inst.split(" ")[2][1:-1])) << 16)
        # <shift> / 2 bit
        # (int(inst.split(" ")[3][3:-1], 16) << 22)
        # <amount> / imm6
        # (int(inst.split(" ")[4][3:], 16) << 10) 
        result = ((123207711 << 5) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:-1])) << 16) + (int(inst.split(" ")[3][3:-1], 16) << 22) + (int(inst.split(" ")[4][3:], 16) << 10))
    elif inst.split(" ")[0] == "NGC":
        # NGC <Xd>, <Xm>
        # NGC
        # print(114294815 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # ((int(inst.split(" ")[2][1:])) << 16)
        result = ((114294815 << 5) +(int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:])) << 16))
    elif inst.split(" ")[0] == "NGCS":
        # NGCS <Xd>, <Xm>
        # NGCS
        # print(131072031 << 5)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xm>
        # ((int(inst.split(" ")[2][1:])) << 16)
        result = ((131072031 << 5) +(int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:])) << 16))
    elif inst.split(" ")[0] == "RBIT":
        # RBIT <Xd>, <Xn>
        # RBIT
        # print(875 << 22)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # ((int(inst.split(" ")[2][1:])) << 5)
        result = ((875 << 22) + (int(inst.split(" ")[1][1:-1])) + ((int(inst.split(" ")[2][1:])) << 5))
    elif inst.split(" ")[0] == "RET":
        # RET {<Xn>}
        # RET
        # print(875 << 22)
        # <Xn>
        # (int(inst.split(" ")[1][1:]) << 5)
        result = ((875 << 22) + (int(inst.split(" ")[1][1:]) << 5))
    elif inst.split(" ")[0] == "ROR":
        # ROR <Xd>, <Xn>, <Xm>
        # ROR
        # print(2596285440)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)       
        result = ((2596285440) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16)) 
    elif inst.split(" ")[0] == "SBC": # Green
        # SBC <Xd>, <Xn>, <Xm>
        #
        # SBC
        # print(109 << 25)
        # <Xd>
        # print(int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # print(int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # print(int(inst.split(" ")[3][1:]) << 16)
        result = ((109 << 25) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "SBCS": # Green
        # SBCS <Xd>, <Xn>, <Xm>
        #
        # SBCS
        # print(125 << 25)
        # <Xd>
        # print(int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # print(int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # print(int(inst.split(" ")[3][1:]) << 16)
        result = ((125 << 25) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))    
    elif inst.split(" ")[0] == "SDIV": 
        # SDIV <Xd>, <Xn>, <Xm>
        # SDIV
        # print(2535427 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)  
        result = ((2535427 << 10) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))  
    elif inst.split(" ")[0] == "SMC":
        # SMC #<imm16>
        # SMC
        # print(3556769795)
        # <imm16>
        # (int(inst.split(" ")[1][3:],16) << 5)
        result = ((3556769795) + (int(inst.split(" ")[1][3:],16) << 5))  
        
    elif inst.split(" ")[0] == "UMULH":
        # UMULH <Xd>, <Xn>, <Xm>
        # UMULH
        # print(2613083136)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Xn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Xm>
        # (int(inst.split(" ")[3][1:]) << 16)    
        result = ((2613083136) + (int(inst.split(" ")[1][1:-1])) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[3][1:]) << 16))
    elif inst.split(" ")[0] == "UMULL":
        # UMULL <Xd>, <Wn>, <Wm>
        # UMULL
        # print(2549791 << 10)
        # <Xd>
        # (int(inst.split(" ")[1][1:-1]))
        # <Wn>
        # (int(inst.split(" ")[2][1:-1]) << 5)
        # <Wm>
        # (int(inst.split(" ")[3][1:]) << 16)
        result = ((2549791 << 10) + (int(inst.split(" ")[3][1:]) << 16) + (int(inst.split(" ")[2][1:-1]) << 5) + (int(inst.split(" ")[1][1:-1])))
    elif inst.split(" ")[0] == "WFET":
        # WFET <Xt>
        # WFET 
        # print(111679616 << 5)
        # <Xt>
        # int(inst.split(" ")[1][1:])    
        result = ((111679616 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst == "WFE":
        result = (3573751903)
    elif inst == "WFI": 
        result = (3573751935)
    elif inst.split(" ")[0] == "WFIT":
        # WFIT <Xt>
        # WFIT 
        # print(111679617 << 5)
        # <Xt>
        # int(inst.split(" ")[1][1:])    
        result = ((111679617 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst == "XAFLAG":
        result = (3573563455)
    elif inst.split(" ")[0] == "XPACI":
    # XPACI <Xd>
    # XPACI
    # print(114690591 << 5)
    # <Xd>
    # int(inst.split(" ")[1][1:])
        result = ((114690591 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst.split(" ")[0] == "XPACD":
    # XPACD <Xd>
    # XPACD
    # print(114690623 << 5)
    # <Xd>
    # int(inst.split(" ")[1][1:])
        result = ((114690623 << 5) + (int(inst.split(" ")[1][1:])))
    elif inst == "XPACLRI":
        result = (3573752063)
    elif inst == "Yield":
        result = (3573751871)     
    else: 
        result = 0



    # 32-bit binary number:
    segments_list = split_32bit_to_4bit_segments(result)
    # To view them in binary:
    binary_segments = [bin(s)[2:].zfill(4) for s in segments_list]
    # 4-bit segments (binary): {binary_segments}


    hex_result = binary_list_to_hex(binary_segments)
    # Binary list: {binary_segments}
    # Hexadecimal equivalent: {hex_result}

    little_endian_value = hex_to_little_endian(hex_result)
    with open("Output.xxd", "a") as file:
        file.write(f"{little_endian_value}\n")
