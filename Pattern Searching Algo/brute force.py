#brute force for pattern searching .Time complexity O(m*(n-m+1))
def search(pat, str): 
    m = len(pat) 
    n = len(str) 

    for i in range(n-m+1):
        j=0

        for j in range(0, m):
            if (str[i + j] != pat[j]):
                break

        if (j == m-1):
            print("Pattern found at", i)

if __name__ == '__main__':
    str = "abcdabdadadcabdacabdac"
    pat = "abda"
    search(pat, str)

