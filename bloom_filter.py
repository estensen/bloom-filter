import pyhash

fnv_hasher = pyhash.fnv1_32()
murmur_hasher = pyhash.murmur3_32()


class BloomFilter:
    def __init__(self):
        self.bit_vector = [0] * 20

    def add(self, item):
        fnv_hash, murmur_hash = self.hash(item)
        print(f'FNV hash of {item}: {fnv_hash}')
        print(f'Murmur hash of {item}: {murmur_hash}')

        self.bit_vector[fnv_hash] = 1
        self.bit_vector[murmur_hash] = 1

        print(f'Bit vector after adding {item}: {self.bit_vector}')

    def contains(self, item):
        fnv_hash, murmur_hash = self.hash(item)
        return self.bit_vector[fnv_hash] and self.bit_vector[murmur_hash]

    @staticmethod
    def hash(item):
        fnv_hash = fnv_hasher(item) % 20
        murmur_hash = murmur_hasher(item) % 20

        return fnv_hash, murmur_hash


if __name__ == '__main__':
    bloom_filter = BloomFilter()

    # Add cat, dog and goat
    bloom_filter.add('cat')
    bloom_filter.add('dog')
    bloom_filter.add('goat')

    print(f"Contains 'cat'? {bloom_filter.contains('cat')}")
    print(f"Contains 'lion'? {bloom_filter.contains('lion')}")
