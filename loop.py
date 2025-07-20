# for i in range(3):
#     print(i,"kiran wants to grow a tree")
#     for j in range(2):
#         print("tree",j)
#     print(i,"Exited")


# s = ["one problem a day", "hi this is kiran kumar", "hello welcome"]
# max=0
# for sentence in s:
#     c=len(sentence.split())
#     if max<c:
#         max=c
# print(max)

li = ["one problem a day", "hi this is kiran", "hello welcome"]
for j in range(len(li)):
    s = li[j]          # Get the j-th sentence
    temp = 1          # Start with 1 word
    for i in range(len(s)):  
        ch=s[i]    # Loop through each character in the sentence
        if ch == " ":
            temp += 1
    print(temp)








