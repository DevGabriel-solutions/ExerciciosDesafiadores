import argparse
import secrets
import string
import random
from pathlib import Path

AMBIGUOUS = set("O0oIl|`'\"~^,.;:[](){}<>")

def build_charset(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous):
    pools = []
    if use_upper: pools.append(set(string.ascii_uppercase))
    if use_lower: pools.append(set(string.ascii_lowercase))
    if use_digits: pools.append(set(string.digits))
    if use_symbols: pools.append(set("!@#$%^&*_-+=/?"))
    if not pools:
        raise ValueError("Selecione pelo menos um tipo de caractere.")
    charset = set().union(*pools)
    if exclude_ambiguous:
        charset -= AMBIGUOUS
        pools = [pool - AMBIGUOUS for pool in pools]
    # remove pools vazios após exclusões
    pools = [pool for pool in pools if len(pool) > 0]
    if not pools:
        raise ValueError("Exclusões removeram todos os caracteres. Ajuste as opções.")
    return pools, list(charset)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous):
    pools, charset = build_charset(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous)
    if length < len(pools):
        raise ValueError(f"Comprimento mínimo é {len(pools)} para garantir diversidade.")
    pwd = [secrets.choice(list(pool)) for pool in pools]
    for _ in range(length - len(pwd)):
        pwd.append(secrets.choice(charset))
    random.SystemRandom().shuffle(pwd)
    return "".join(pwd)

def estimate_entropy(length, charset_size):
    # Entropia aproximada: H ≈ length * log2(charset_size)
    import math
    return length * math.log2(charset_size)

def main():
    parser = argparse.ArgumentParser(description="Gerador de senhas seguras")
    parser.add_argument("-l", "--length", type=int, default=16, help="Comprimento da senha (padrão: 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Quantidade de senhas (padrão: 1)")
    parser.add_argument("--no-upper", action="store_true", help="Não usar maiúsculas")
    parser.add_argument("--no-lower", action="store_true", help="Não usar minúsculas")
    parser.add_argument("--no-digits", action="store_true", help="Não usar dígitos")
    parser.add_argument("--no-symbols", action="store_true", help="Não usar símbolos")
    parser.add_argument("--allow-ambiguous", action="store_true", help="Permitir caracteres ambíguos (O,0,l,I,|, etc.)")
    parser.add_argument("-o", "--output", type=Path, help="Salvar senhas em arquivo")
    args = parser.parse_args()

    use_upper = not args.no_upper
    use_lower = not args.no_lower
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols
    exclude_ambiguous = not args.allow_ambiguous

    pools, charset = build_charset(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous)
    entropy = estimate_entropy(args.length, len(charset))

    print(f"Conjunto de caracteres: {len(charset)} | Entropia estimada: {entropy:.1f} bits")
    passwords = []
    for _ in range(args.count):
        passwords.append(generate_password(args.length, use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous))
    for p in passwords:
        print(p)

    if args.output:
        args.output.write_text("\n".join(passwords), encoding="utf-8")
        print(f"Salvo em: {args.output}")

if __name__ == "__main__":
    main()