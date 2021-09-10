import pickle

imelda=("More Mayhem",
        "Imelda May",
        "2011",
        ((1,"pulling the rug"),
         (2,"Psycho"),
         (4,"Kentish Town Walts")))
even=list(range(0,10,2))
odd=list(range(1,10,2))

with open("imelda.pickle2","wb") as pickle_file2:
    pickle.dump(imelda,pickle_file2,protocol=0)

with open("imelda.pickle2","rb") as imdelda_pickled2:
    imelda2=pickle.load(imdelda_pickled2)


print(imelda2)

