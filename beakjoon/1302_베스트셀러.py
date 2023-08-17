import sys

n = int(sys.stdin.readline())
books = dict()
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    
    if name not in books:
        books[name] = 1
    else:
        books[name] += 1
        
books = sorted(books.items(), key=lambda item: (-item[1], item[0]))

print(books[0][0])