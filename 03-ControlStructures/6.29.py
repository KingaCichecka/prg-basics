for i in range(1, 50, 7):      
    for j in range(i, i + 7):  
        if j <= 49:
            print(f"{j:2}", end=" ")
    print()