'''You can print your name on a billboard ad. Find out how much it will cost you.
Each letter has a default price of £30, but that can be different if you are given
2 parameters instead of 1.
You can not use multiplier "*" operator.
If your name would be Jeong-Ho Aristotelis, ad would cost £600.
20 leters * 30 = 600 (Space counts as a letter).
'''

def billboard(name, price=30):
    result = 0
    for i in name:
        result += price
    return result

print(billboard("Jeong-Ho Aristotelis"))
print(billboard("Abishai Charalampos"))
print(billboard("Idwal Augustin"))
print(billboard("Hadufuns John",20))
print(billboard("Zoroaster Donnchadh"))
print(billboard("Claude Miljenko"))
print(billboard("Werner Vigi",15))
print(billboard("Anani Fridumar"))
print(billboard("Paolo Oli"))
print(billboard("Hjalmar Liupold",40))
print(billboard("Simon Eadwulf"))