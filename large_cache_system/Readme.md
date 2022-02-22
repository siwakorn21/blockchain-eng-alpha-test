## How to run the program.
1. open your terminal
2. go into blockchain-eng-alpha-test directory (cmd: cd /path/to/blockchain-eng-alpha-test)
3. go into algo directory (cmd: cd ./large_cache_system)
4. if you don't have python3 in your computer, please install it for running the program.
5. run command: python3
6. currently, you are in python3 console.
7. import function run command: from large_cache import LargeValueCache
8. now you can run your test case here.

## example.

cd /path/to/

cd ./large_cache_system

python3

...>>> from large_cache import LargeValueCache

...>>> cache = LargeValueCache(3)

...>>> cache.insert(3, 4)

...>>> cache.insert(1, -1)

...>>> print(cache.lookup(1))

...>>> -1

## Time complexity analysis

1. There are four methods in LargeCacheValue class.
2. First, get_capacity() method
    - Returning Value from Class -> O(1)
3. Second, lookup(key) method
    - Reading Value in Dictionary -> O(1), --- In python, the time complexity of reading value in dictionary is O(1).
4. Third, update_capacity(N) method
   1. Case: N >= current capacity
      - set new capacity = N -> O(1)
   2. Case: N < current capacity
      - Removing the minimum value data in dict, for each removing the program will take the time for O(n).
      - The number of removing data is current_capacity - N (new capacity) = k
      - So that, The time complexity of this method is O(k * N) ~ O(n)
5. Last, insert(key, value) method
   1. Case: we don't have the "key" in dict
      - Insert new key and value to dictionary - O(1)
      - So that, the time complexity of this case is O(1)
   2. Case: we have "key" in dict
      - Remove the minimum one in dictionary - O(n)
      - Insert new key and value to dictionary - O(1)
      - So that, the time complexity of this case is O(n)
   
## What can be improved ?

In my opinion, If the program will be used for more reading than writing, the current program is suitable for using in this situation.

But if we need to write and update (add new value) the data more than read the value,
we can create new data that store the sorted data by value as "Tree" for removing.
Because the current program, when we remove the data, it will take the time for O(n).
If we sorted the data before using, the removing and updating the tree will take the time for O(1).
But the insertion will take the time for O(h) (Binary Tree insertion, h is height of the tree).
And the new program will use space for than current one.
