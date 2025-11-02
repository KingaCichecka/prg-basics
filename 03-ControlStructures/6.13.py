###
# Good influencer if at least two accounts are True
#
facebook  = True
twitter   = False
instagram = True

has_accounts = sum([facebook, twitter, instagram])  # True==1, False==0

if has_accounts >= 2:
    print("You are a good influencer!")
else:
    print("You need more social presence.")
