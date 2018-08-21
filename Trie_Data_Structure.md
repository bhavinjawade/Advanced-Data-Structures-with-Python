# Trie Data Structure
Trie is an efficient information reTrieval data structure. Using Trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements.
<br>

## Advantages of Tries
<br>
With Trie, we can insert and find strings in O(L) time where L represent the length of a single word. This is obviously faster that BST. This is also faster than Hashing because of the ways it is implemented. We do not need to compute any hash function. No collision handling is required (like we do in open addressing and separate chaining)
Another advantage of Trie is, we can easily print all words in alphabetical order which is not easily possible with hashing.
We can efficiently do prefix search (or auto-complete) with Trie.
<br>

<div style="text-align:center"><img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Patricia_trie.svg/350px-Patricia_trie.svg.png
"/></div>

## Advanced Learning Resources
1)https://www.cs.cmu.edu/~fp/courses/15122-f10/lectures/18-tries.pdf
2)http://ellard.org/dan/www/libsq/cb_1998/c06.pdf
3) [Harvard CS50: Tries](https://www.youtube.com/watch?v=TRg9DQFu0kU)