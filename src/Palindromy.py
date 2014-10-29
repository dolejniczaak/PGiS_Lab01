def is_palindrome(s):
    i = 0 
    j= len(s)-1
    while i:
        i -= 1 ##zmniejszamy co przejscie o 1
        if s[i]==' ': i+1
        elif s[j]==' ':j-1
    if s[i] != s[j]: return False
    return True
palindrom="dkdkdkff"
sprawdz = is_palindrome(palindrom)
print sprawdz