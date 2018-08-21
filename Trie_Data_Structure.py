class TrieNode:
  children = {}
  endofword = False
  def __init__(self):
    self.children = {}
    self.endofword = False

root = TrieNode() 
def insert(word):
  current = root
  for i in range(len(word)):
    if word[i] not in current.children:
      node = TrieNode()
      current.children[word[i]] = node
    else:
      node = current.children[word[i]]
    current = node
  current.endofword = True

lis = []
def printTrie(current):  
  for char, node in current.children.items():
    print(char,end='')
    lis.append(node)
  print("")
  if lis:
    nextnode = lis.pop()
    printTrie(nextnode)

def search(word,root):
  current  = root
  for i in range(len(word)):
    if word[i] not in current.children:
      return False
    else:
      node = current.children[word[i]]
    current = node
  return current.endofword

insert("HelloBhavin")
insert("Hell")
insert("Hello")
insert("Hat")
insert("Cases")
insert("Cast")
insert("Cause")
insert("Chastise")
insert("Date")
print(search("Bhavin",root))
print(search("Hello",root))
print(search("Hell",root))
print(search("Cast",root))
print(search("Dat",root))
print(search("Date",root))
# printTrie(root)