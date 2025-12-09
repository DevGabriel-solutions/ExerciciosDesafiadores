import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase

    lines = []

    for i in range(size):
        left = alphabet[size - 1: size - 1 - i: -1]  # sequencia decrescente
        right = alphabet[size - 1 - i: size]  # sequencia crescente
        row = "-".join(left + right)
        width = 4 * size - 3  # largura fixa
        lines.append(row.center(width, "-"))

        # parte superior + parte inferior espelhada
    print("\n".join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)