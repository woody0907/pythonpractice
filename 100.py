def find_dif_num():
    for i in range(1,5): #1,2,,3,4
        for j in range(1,5):
            for k in range(1,5):
                if(i!=j and j!=k):
                    print(i,j,k)

find_dif_num()
