
# Exception Handling

# We can raise exception in two ways

# Here if some condition is not matched then we are intentionally throwing an exception
ItemInCart = 0
# 2 items are added to the cart, so now 2 items were there in the cart
if ItemInCart != 2:
    pass
    # raise Exception("Item Mismatch")
# By providing an assertion

assert (ItemInCart == 2)
# Assert will check for the True if it fails then it will through an exception
