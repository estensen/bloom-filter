import pyhash

fnv_hasher = pyhash.fnv1_32()
murmur_hasher = pyhash.murmur3_32()


class BloomFilter:
    def __init__(self):
        self.bit_vector = [0] * 20

    def add_item(self, item):
        fnv_hash = fnv_hasher(item) % 20
        print(f'FNV hash of {item}: {fnv_hash}')
        self.bit_vector[fnv_hash] = 1

        murmur_hash = murmur_hasher(item) % 20
        print(f'Murmur hash of {item}: {murmur_hash}')
        self.bit_vector[murmur_hash] = 1

        print(f'Bit vector after adding {item}: {self.bit_vector}')


if __name__ == '__main__':
    bloom_filter = BloomFilter()

    # Add cat, dog and goat
    bloom_filter.add_item('cat')
    bloom_filter.add_item('dog')
    bloom_filter.add_item('goat')
