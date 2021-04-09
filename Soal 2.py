print("Berapa total bilangan yang ingin dimasukkan :")
input_saya = input()
counter = 1
total = 0
while counter < int(input_saya) :
    print("Masukkan bilangan ke "+ str(counter)+": ")
    inputAngka = input()
    total += int(inputAngka)
    counter += 1
print("Rata-ratanya adalah: "+str(total/int(input_saya)))