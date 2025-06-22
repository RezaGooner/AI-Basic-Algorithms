# X is sample set and a is num of attribute
def Find_S(X,a):
    #most specific hypothensis
    msh = a * ['None']
    for x in X :
        # Last index is Tag
        if x[-1] == '+' :
            for j in range(a) :
                if msh[j] != x[j] :
                    if msh[j] == 'None' :
                        msh[j] = x[j]
                    else :
                        msh[j] = '?'
    return msh


X = [ # sample attribute and tag 
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm',   'Same', '+'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm',   'Same', '+'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', '-'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change', '+']
]

print("Most-Specific Hypothensis = ", Find_S(X,6))
# Output should be ['Sunny', 'Warm', '?', 'Strong', '?', '?']
                    
            
