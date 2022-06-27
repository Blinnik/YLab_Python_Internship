def dec(bin):
    bin = int(bin, 2)
    # We need a number in string format
    bin = str(bin)
    return bin


def int32_to_ip(int32):
    ipv4 = format(int32, 'b')
    bit_diff = 32 - len(ipv4)
    ipv4 = str(ipv4)
    if bit_diff:
        for i in range(bit_diff):
            ipv4 = '0' + ipv4
    ipv4 = (
        dec(ipv4[:8]) + '.' +
        dec(ipv4[8:16]) + '.' +
        dec(ipv4[16:24]) + '.' +
        dec(ipv4[24:32])
        )
    return ipv4
