prenume=['mihai','george','ana','dan','ion','geta','vio']
virsta=[14, 23, 15, 14, 12, 41, 39]
for i in range(0, len(prenume)):
    print(f'{prenume[i]} are virsta de {virsta[i]} ani')
prenume.extend(['andreea','ioan'])
virsta.extend([34,23])
print(prenume)
print(virsta)
prenume.remove('ana')
virsta.pop(2)
print(prenume)
print(virsta)
print(prenume[-8:-5])
print(prenume[::-1])
print(prenume[2], prenume[4])
print(virsta[0:6])