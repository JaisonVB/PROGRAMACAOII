for i in [1, 2, 3, 4, 5]: 
    print(i)                  # primeira linha do bloco "for i"  
    for j in [1, 2, 3, 4, 5]: 
        print(j)              # primeira linha do bloco "for j" 
        print(i + j)          # ultima linha do bloco  "for j"  
    print(i)                  # ultima linha do bloco  "for i"  
print("Fim") 