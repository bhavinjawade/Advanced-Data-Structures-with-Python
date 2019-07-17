#effective approach for pattern searching KMP(Knuth Morris Pratt) algorithm.Time complexity O(n)
def search(out, pat):
    n=len(out)
    m=len(pat)
    #array for longest prefix suffix
    p=[0]*m
    compute(pat,m,p)
    q = 0
    i = 0
    while i < n:
        if pat[q]==out[i]:
            q=q+1
            i = i + 1
        else:
            if q != 0:
                q = p[q-1]
            else:
                i = i + 1
        if q == m:
            print ("pattern occurs at "+str(i-q))
            q = p[q-1]
#function definition for preproscessing longest prefix suffix
def compute(pat,m,p):
   
    k=1
    l = 0
    while k < m:
        if pat[k] <= pat[l]:
            l = l + 1
            p[k] = l
            k = k + 1
        else:
            if l != 0:
                l = p[l-1]
            else:
                p[k] = 0
                k = k + 1
    
#to find pattern from string out
out = 'abcacdbacdabdacaabcdba'
pat = 'dba'
search(out,pat)