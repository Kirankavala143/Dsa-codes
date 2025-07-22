# o(1)  fast (best )
# o(logn)
# o(n)
# o(nlogn)
# o(n2)
# o(n3)

l=[7,1,5,3,6,4]
mina=l[0]
ans=0
for i in l:
    if i<mina:
        mina=i
    else:
         profit=i-mina
         ans=max(ans,profit)
print(ans)


#         else:
#             profit = price - min_price  # Sell today
#             max_profit = max(max_profit, profit)  # Keep max profit

#     return max_profit