data List = Cons String List | Empty 
emptyList, oneList, twoList :: List 
emptyList = Empty 
oneList = Cons "Primero" emptyList 
twoList = Cons "Segundo" oneList 
hasOneOnly :: List -> Bool 
hasOneOnly (Cons _ Empty) = True 
hasOneOnly _ = False 
main = do 
print $ hasOneOnly emptyList