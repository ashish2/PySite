
# Print the day and prices where the seller can sell oil and make MAX profit
# eg, in the following case

# output:
# 1 70
# 6 79


prices = [ 70, 72, 73, 78, 74, 79, 77 ]
def  calculateProfit(prices):
    di = {}
    for i in prices:
        for j in prices[prices.index(i):]:
            try:
                ii = prices.index(i)
                i_1 = prices.index(j)
                i_1_val = j
                subt = i - j
                di.update({subt: (ii,i_1)})
            except:
                pass
    de = di.copy()
    for i in di.iteritems():
        mn = min(de)
        tu = de[mn]
        if tu[0] < tu[1]:
            break
        else:
            de.pop(mn)
    print tu[0]+1, prices[tu[0]]
    print tu[1]+1, prices[tu[1]]


calculateProfit(prices)


