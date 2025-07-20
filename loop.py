for i in range(3):
    print(i,"kiran wants to grow a tree")
    for j in range(2):
        print("tree",j)
    print(i,"Exited")


# highest length of sentence
l=["hi this kiran, hello welcome all this is me,hello kiran"]  
max=0
for i in l:
    if len(i)>max:
        max=len(i)
print(max  )

# Maximum Number of Words Found in Sentences

l=["hi this kiran, hello welcome all this is me,hello kiran"]  
max=0
for i in l:
    if len(i.split())>max:
        max=len(i.split())
print(max)