print(input("enter name : "))
print(" 1.regular 2.admin")
choice=(input(">"))
if choice == "1":
    print(input("1.view books 2.search books 3.borrow books "))
if choice =="1":
    print("2 books in store")
    view = (input("> A.after  M.Malory towers"))
    view =(input(">"))
    if view == "A":
      A ={"title :" "After" , "author :" "anna todd",
            "genre :" "romance" , "category :" "A", 
            "copies available :" "12" , "description:" "they love each other",
            "price:" "$20" , "date added:" "20/1/09"}
    print(A)
    if view == "M":
            M ={"title:" "Malory towers" , "author:" "enid blyton",
               "genre:" "adventure",   "category:" "M",
               "copies available:" "23" , "description:" "girls boarding school",
                "price:" "$11", "date added:" "20/1/08"}
    print(M)



    