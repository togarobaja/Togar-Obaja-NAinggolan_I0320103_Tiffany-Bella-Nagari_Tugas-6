for i in range(10,25):
    hasil = False
    for j in range(2,i):
        if i % j == 0:
            hasil = True
            break
    if hasil == False:
        print(str(i)+ " adalah bilangan prima")
    else :
        print(str(i)+ " adalah bilangan bukan prima")
print()
