#match case   edno uslovie 6te se izpulni, ako ima dublira6ti 6te grumne
#igrae rolqta na elif...elsifove
#ako e 1, 6te se printe Data is 1 
#trqbva da e constanta, edno 4islo, duma, nemoje da e list, clas, masiv(masiv moje no ot edno 4islo[1])
#obekt {1, 2, 3}
data = 5          
match data:
    case 1:
        print("Data is 1")
    case 2:
         print("Data is 2")
    case 3:
         print("Data is 3")
    case _:
        print("Data is not 1, 2, or 3")

