#input
N = int(input())
string = input()
books = list(string)

#bubble sort
def sort(books, N):
    reads = 0
    for i in range(N-1):
        for j in range(N-i-1):
            if books[j] > books[j+1]:
                temp = books[j]
                books[j] = books[j+1]
                books[j+1] = temp
                reads += 1
    return reads

x = sort(books, N)
if(x > 5):
    print("A Database Systems student read a book.\n")

else:
    print(x)


