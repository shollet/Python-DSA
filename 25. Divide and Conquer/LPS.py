def findLPS(s, start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    if s[start] == s[end]:
        return 2 + findLPS(s, start+1, end-1)
    else:
        op1 = findLPS(s, start, end-1)
        op2 = findLPS(s, start+1, end)
        return max(op1,op2)

string = "ELRMENMET"
print(findLPS(string, 0, len(string) - 1))