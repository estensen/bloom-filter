import pyhash


# Init storage and hash functions
bit_vector = [0] * 20
print(bit_vector)
fnv_hasher = pyhash.fnv1_32()
murmur_hasher = pyhash.murmur3_32()


def add_item(item):
    fnv_hash = fnv_hasher(item) % 20
    print(f'FNV hash of {item}: {fnv_hash}')
    bit_vector[fnv_hash] = 1

    murmur_hash = murmur_hasher(item) % 20
    print(f'Murmur hash of {item}: {murmur_hash}')
    bit_vector[murmur_hash] = 1

    print(f'Bit vector after adding {item}: {bit_vector}')


# Add cat, dog and goat
add_item('cat')
add_item('dog')
add_item('goat')
