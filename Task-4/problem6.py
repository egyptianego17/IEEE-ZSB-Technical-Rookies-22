import math
pages_num = int(input(""))
wanted_page = int(input(""))
book_pages = ""
book_ar = []
c = 0
r = 0
l = 0
n = math.ceil(pages_num/2)
for lista in range(0,n+1):
    book_pages = str(c) + " " + str(c+1)
    book_ar.append(book_pages.split())
    c = c + 2
for lista1 in range(0,n):
    if wanted_page == int(book_ar[lista1][0]) or wanted_page == int(book_ar[lista1][1]):
        r = lista1
    if wanted_page == int(book_ar[n-lista1-1][0]) or wanted_page == int(book_ar[n-lista1-1][1]):
        l = lista1 
print(min(l,r))