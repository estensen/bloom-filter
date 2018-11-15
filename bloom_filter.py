import pyhash


# Init storage and hash functions
bit_vector = [0] * 20
print(bit_vector)
fnv_hasher = pyhash.fnv1_32()
murmur_hasher = pyhash.murmur3_32()

# Add cat
fnv_hash_cat = fnv_hasher('cat') % 20
print(f'FNV hash of cat: {fnv_hash_cat}')
bit_vector[fnv_hash_cat] = 1

murmur_hash_cat = murmur_hasher('cat') % 20
print(f'Murmur hash of cat: {murmur_hash_cat}')
bit_vector[murmur_hash_cat] = 1

print(f'Bit vector after adding cat: {bit_vector}')

# Add dog
fnv_hash_dog = fnv_hasher('dog') % 20
bit_vector[fnv_hash_dog] = 1
print(f'FNV hash of dog: {fnv_hash_dog}')

murmur_hash_dog = fnv_hasher('dog') % 20
bit_vector[murmur_hash_dog] = 1
print(f'Murmur hash of dog: {murmur_hash_dog}')

print(f'Bit vector after adding dog: {bit_vector}')
