def non_mersenne_prime(multi, exp, mod):
    return (multi * pow(2, exp, mod) + 1) % mod

print(non_mersenne_prime(28433, 7830457, 10**10))