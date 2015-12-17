prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
def compute_bill(food):
#    slist=[]
#    slist==slist.append(food)
    total=0
    for item in food:
	total+=prices[item]
    return total

print compute_bill(['apple'])
print stock.values()

