# First Non-Repeating Character
# Input: "loveleetcode" → Output: 2 (character 'v')

# 🔹 Hard Level

# Longest Substring Without Repeating Characters
# Input: "abcabcbb" → Output: 3 ("abc")

# Minimum Window Substring
# Input: s="ADOBECODEBANC", t="ABC" → Output: "BANC"

# Regular Expression Matching
# Input: s="mississippi", p="mis*is*p*." → Output: False



# Longest Common Prefix
# a = ["flower", "flow", "flight"]
# a.sort()
# l,r=a[0],a[-1]
# res=""
# for i in range(min(len(l),len(r))):
#     if l[i]==r[i]:
#         res+=l[i]
#     else:
#         break
# print(res)


# First Non-Repeating Character
# Input: "loveleetcode" → Output: 2 (character 'v')
a="loveleetcode"  
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in range(len(a)):
    if d[a[i]]==1:
        print(i)
        break
# Longest Substring Without Repeating Characters
# Input: "abcabcbb" → Output: 3 ("abc")
a="abcabcbb"
s=set()
l=0
res=0
for r in range(len(a)):
    while a[r] in s:
        s.remove(a[l])
        l+=1
    s.add(a[r])
    res=max(res,r-l+1)
print(res)


