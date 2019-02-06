def matrice(mot,gen):
    
    tab=[""]*(len(gen))
    i=0
    j=0
    temp=0
    if(len(mot)==len(gen)):
        while(j<len(gen[0])):
            while(i<len(mot)):

                if(mot[i]==1 and gen[i][j]==1):
                    temp=temp+1
                i=i+1

            if(temp%2==0):
                tab[j]=0

            else:
                tab[j]=1

            temp=0
            j=j+1
            i=0
        print tab
    else:
        print"matrices non conformes"

M=[1,0,1]
G=[[1,0,1],[1,1,0],[0,1,1]]
matrice(M,G)