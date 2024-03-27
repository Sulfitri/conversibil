def bilangan_ke_biner(n):
    return bin(n)[2:]

def bilangan_ke_oktal(n):
    return oct(n)[2:]

def bilangan_ke_desimal(n):
    return n

def bilangan_ke_heksadesimal(n):
    return hex(n)[2:]

# input bilangan
bilangan = int(input("Masukan bilangan bulat: "))

# konversi dan tampilkan hasil
print("Konversi ke biner:", bilangan_ke_biner(bilangan))
print("Konversi ke oktal:", bilangan_ke_oktal(bilangan))
print("Konversi ke desimal:", bilangan_ke_desimal(bilangan))
print("Konversi ke heksadesimal:", bilangan_ke_heksadesimal(bilangan))