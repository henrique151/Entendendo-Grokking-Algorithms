import mmh3
from bitarray import bitarray
import math
import hashlib

# --- Filtro de Bloom ---


class BloomFilter:
    def __init__(self, tamanho, n_hashes):
        self.tamanho = tamanho
        self.n_hashes = n_hashes
        self.bit_array = bitarray(tamanho)
        self.bit_array.setall(0)

    def adicionar(self, item):
        for i in range(self.n_hashes):
            index = mmh3.hash(item, i) % self.tamanho
            self.bit_array[index] = 1

    def verificar(self, item):
        for i in range(self.n_hashes):
            index = mmh3.hash(item, i) % self.tamanho
            if self.bit_array[index] == 0:
                return False
        return True

# --- HyperLogLog (Simples Aproximação) ---


class HyperLogLog:
    def __init__(self, b=4):
        self.b = b  # número de bits para os registradores
        self.m = 2 ** b
        self.registradores = [0] * self.m

    def adicionar(self, item):
        hash_value = int(hashlib.sha1(item.encode('utf-8')).hexdigest(), 16)
        index = hash_value & (self.m - 1)
        w = hash_value >> self.b
        self.registradores[index] = max(
            self.registradores[index], self._rho(w))

    def _rho(self, x):
        # posição do primeiro 1
        rho = 1
        while x & 1 == 0 and x != 0:
            rho += 1
            x >>= 1
        return rho

    def contar(self):
        alpha = 0.673  # Constante para m == 16
        E = alpha * self.m * self.m / sum(2 ** -r for r in self.registradores)
        return int(E)


if __name__ == "__main__":
    # Exemplo de Filtro de Bloom
    bf = BloomFilter(tamanho=500, n_hashes=5)
    itens = ["gato", "cachorro", "papagaio"]
    for item in itens:
        bf.adicionar(item)

    print("Filtro de Bloom:")
    for teste in ["gato", "leão"]:
        print(f"{teste}: {bf.verificar(teste)}")

    # Exemplo de HyperLogLog
    hll = HyperLogLog(b=4)
    for i in range(1000):
        hll.adicionar(f"item_{i}")
    print(f"\nEstimativa de cardinalidade (HyperLogLog): {hll.contar()}")
