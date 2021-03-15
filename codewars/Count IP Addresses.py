def to_byte(x):
    s = str(bin(int(x))[2:])
    return "0" * (8 - len(s)) + s


def ip_to_byte(ip):
    answer = ""
    for s in ip.split('.'):
        answer += to_byte(s)
    return answer


def ips_between(start, end):
    return int(ip_to_byte(end), 2) - int(ip_to_byte(start), 2)


ips_between("20.0.0.10", "20.0.1.0")
