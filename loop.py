for i in range(3):
    print(i,"kiran wants to grow a tree")
    for j in range(2):
        print("tree",j)
    print(i,"Exited")

s=["one problem a day", "hi this is kiran","hello,welcome"]
for j in range(len(s)):
    a=s[j]
    print(a)
# temp=1
# for i in range(len(s)):
#     ch=s[i]
#     if ch==" ":
#         temp=temp+1
# print(temp)








# # highest length of sentence
# l=["hi this kiran, hello welcome all this is me,hello kiran"]  
# max=0
# for i in l:
#     if len(i)>max:
#         max=len(i)
# print(max  )

# # Maximum Number of Words Found in Sentences

# l=["hi this kiran, hello welcome all this is me,hello kiran"]  
# max=0
# for i in l:
#     if len(i.split())>max:
#         max=len(i.split())
# print(max)

# # Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# # Output: 6
# # Explanation: 
# # - The first sentence, "alice and bob love leetcode", has 5 words in total.
# # - The second sentence, "i think so too", has 4 words in total.
# # - The third sentence, "this is great thanks very much", has 6 words in total.
# # Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

# l=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# max=0
# for i in l:
#     if len(i.split())>max:
#         max=len(i.split())
# print(max)