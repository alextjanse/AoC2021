from math import prod

f = open('./input/16.txt')

hexadecimal = f.readline()

packet = ''.join(map(lambda c: format(int(c, 16), '04b'), hexadecimal))

operators = [
    sum,
    prod,
    min,
    max,
    None,
    lambda x: 1 if x[0] > x[1] else 0,
    lambda x: 1 if x[0] < x[1] else 0,
    lambda x: 1 if x[0] == x[1] else 0,
]

def packet_parser(packet, offset=0):
    version_total = int(packet[offset: offset + 3], 2)
    type_id = int(packet[offset + 3: offset + 6], 2)

    if type_id == 4:
        literal = 0

        for i in range(offset + 6, len(packet), 5):
            literal = (literal << 4) + int(packet[i + 1: i + 5], 2)

            if packet[i] == '0':
                return i + 5, version_total, literal
    
    results = []
    end = -1

    len_type_id = int(packet[offset + 6], 2)

    if len_type_id == 0:
        length = int(packet[offset + 7: offset + 7 + 15], 2)
        offset += 7 + 15

        while length > 0:
            end, version, expr_res = packet_parser(packet, offset)
            results.append(expr_res)
            version_total += version
            length -= end - offset
            offset = end

    else:
        count = int(packet[offset + 7: offset + 7 + 11], 2)
        offset += 7 + 11

        for _ in range(count):
            end, version, expr_res = packet_parser(packet, offset)
            results.append(expr_res)
            version_total += version
            offset = end

    return end, version_total, operators[type_id](results)

_, version_sum, result = packet_parser(packet)

###############
print('part 1')
###############

print(version_sum)

###############
print('part 2')
###############

print(result)