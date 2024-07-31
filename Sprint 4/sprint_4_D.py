def get_polynomial_hash(line, q, m):
    n = len(line)
    q_power = 1
    hash_value = 0
    for i in range(n):
        num_char = ord(line[n - 1 - i]) % m
        hash_value = (hash_value + num_char * q_power) % m
        q_power = (q_power * q) % m
    print(hash_value)

def read_input():
    q = int(input().strip())
    m = int(input().strip())
    line = input().strip()
    return line, q, m


# line, q, m = read_input()
line1 = 'GOSHA'
# line2 = 'kokobozhpmlokzovbiqfqikihexmwumiyjfjtcklrzfxcvxmtpizrpxrjrusnynogvvioucqjontledwdmfwpawt'
q = 251
m = 2**8
get_polynomial_hash(line1, q, m)
# get_polynomial_hash(line2, q, m)


# pdzfgnmyclndipxwcfrorfsdqdmssvfdpjnmfxfurnarvuspomkuiisdwckdbaktkiixgzeetuorwilzkbkcygpwopnbyhgahjz
# 828421
# ========================================================================================================================================================================================================
# pdzfgnmyclndipxwcfrorfsdqdmssvfdpjnmfxfurnarvuspomkuiisdwckdbaktkiixgzeetuorwilzkbkcygpwopnbyhgahjz
# kokobozhpmlokzovbiqfqikihexmwumiyjfjtcklrzfxcvxmtpizrpxrjrusnynogvvioucqjontledwdmfwpawt