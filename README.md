# bloom-filter
A bloom filter is a probabilistic data structure with no false negatives. Use bloom filters when you want something more space efficient than a hash table and can tolerate false positives. This especially useful when you might have to do expensive task like disk access or network calls. To remove an item from a bloom filter you have to make a new one without that item.

<img src="https://user-images.githubusercontent.com/9142800/48547733-99bb6380-e8cb-11e8-9450-4d2b6efee2da.png" width="600">

### False Positive Rate vs. Space
Imagine we have a bloom filter in memory keeping track of which items are stored in the database. If someone wants to check if an item is in the database the bloom filter can immediately return false if it the item is not there. We only have to do a certain percentage of unecessary expensive calls and this can be tweeked by allocating more space to the bit vector.

The false positive rate is approximately `(1 - e^(-kn/m))^k`

`k` is the number of hash functions used

`n` is the number of inserted elements

`m` is the total number of bits in the bit vector
