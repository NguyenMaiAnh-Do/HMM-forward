def alphaPass(A, B, pi, O):
    #pi is the initial distribution
    #A is the transitional matrix
    #B is the emission matrix
    # O is the observation sequence
   
    #T is the number of observations
    T = len(B[0])

    # N is the number of states 
    N = len(A)
    
    o_observation = len(O)

    # matrix row_idx: observations col_idx = states
    # each entry is the probability of each state given the observation
    matrix = [[0]*N for _ in range(o_observation)]

    for i in range(N):
        alpha =  pi[i]*B[i][O[0]]
        matrix[0][i] = alpha
    
    for t in range(1,T):
        for i in range(N):
            alpha_i = 0
            for j in range(N):
                alpha_i += (B[i][t])*(matrix[t-1][j])*(A[j][i])
            matrix[t][i] = alpha_i
    
    print(matrix)
    
    
    

    

    




    