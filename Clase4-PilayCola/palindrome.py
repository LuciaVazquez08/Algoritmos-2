def palindrome(xs: list[str]) -> bool:
    if not xs:
        return True
    if len(xs) == 1:
        return True
    else: 
        return xs[0] == xs[-1] and palindrome(xs[1:-1])
    
l = [1, 2, 2]
print(palindrome(l))