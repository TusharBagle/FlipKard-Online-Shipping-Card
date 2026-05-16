'''                             Online Shopping Card System                                   ''' 




class call :

    def __init__ (Self) :
        Self.User_Information() 
        Self.menu()



    def User_Information (self) :
        User_name = str(input("Enter your name : "))
        User_mobile_number = int(input("Enter your mobile number : "))
        User_password = int(input("Enter your password : "))


        print("\nHi !" , User_name , "hope you well !...")
        print("Your mobile number is added successfully !...")
        print("Your password is added successfully !...")
        print("Now , You are log in !...")



    def menu (self) :
        user_input = int(input("""\n
    Hi ! how can i help you ?
    1. Fashion
    2. Mobile
    3. Laptop
    4. Vehicle
    5. Food
    6. Book         
    7. exit
    \nEnter your choice which item do you want : """))
        



        if (user_input == 1) :
            Fashion()
            self.menu()
        elif (user_input == 2) :
            Mobile()
            self.menu()
        elif (user_input == 3) :
            Laptop()
            self.menu()
        elif (user_input == 4) :
            Vehicle()
            self.menu()
        elif (user_input == 5) :
            Food()
            self.menu()
        elif (user_input == 6) :
            Book()
            self.menu()
        elif (user_input == 7) :
            exit
        else :
            print("Please , enter the valid Input !...")











class Fashion(call) :


    def __init__ (self) :
        self.Fashion_Brand()
        self.Fashion_Type()



# -------------------------------------------------------  Gucci   ----------------------------------------------------------



    def Gucci_T_Shirts (self) :
        user_input_for_T_Shirt = int(input("""\n
        Choose T-shirt :
            1. Men Cartoon Round Neck Cotton T-shirts
            2. Pack of 2 Printed Polyester T-shirts
            3. Men Checkered Polo T-shirts
            4. Exit
        \nEnter your choice which T-Shirt do you like : """))

        print("\nNice Dude !...")


        if user_input_for_T_Shirt == 1 :
            print("You choose : Men Cartoon Round Neck Cotton T-Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 2 :
            print("You choose : Pack of 2 Printed Polyester T-Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 3 :
            print("You choose : Men Checkered Polo T-Shirt !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Gucci_Shirts (self) :
        user_input_for_Shirt = int(input("""\n
        Choose Shirt :
            1. Men Regular Fit Self Design Spread Collar Casual Shirt
            2. Men Regular Fit Solid Design Spread Collar Casual Shirt
            3. Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt
            4. Men Slim Fit Self Checkeared Spread Collar Casual Shirt
            5. Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt
            6. Men Regular Fit Striped Casual Shirt
            7. Exit
        \nEnter your choice which Shirt do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shirt == 1 :
            print("You choose : Men Regular Fit Self Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 2 :
            print("You choose : Men Regular Fit Solid Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 3 :
            print("You choose : Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 4 :
            print("You choose : Men Slim Fit Self Checkeared Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 5 :
            print("You choose : Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt !... ")
            print("The price of this Shirts is : $610 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 6 :
            print("You choose : Men Regular Fit Striped Casual Shirt !... ")
            print("The price of this Shirts is : $450 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Gucci_Pant (self) :
        user_input_for_Pant = int(input("""\n
        Choose Pant :
            1. Men Striped Black Track Pants 
            2. Men Colorblock Brown Track Pants
            3. Men Printed Black Track Pants
            4. Men Self Desgn Black Track Pants
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Pant do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Pant == 1 :
            print("You choose : Men Striped Black Track Pants !... ")
            print("The price of this Shirts is : $364 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 2 :
            print("You choose : Men Colorblock Brown Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 3 :
            print("You choose : Men Printed Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 4 :
            print("You choose : Men Self Desgn Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Gucci_Hoddie (self) :
        user_input_for_Hoddie = int(input("""\n
        Choose Hoddie :
            1. Men Full Sleeve Printed Hooded Sweatshirts 
            2. Men & Women Full Sleeve Solid Hooded Sweatshirts
            3. Men Full Sleeve zip-up Sweatshirts
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue Hoddie
            6. Exit
        \nEnter your choice which Hoddie do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Hoddie == 1 :
            print("You choose : Men Full Sleeve Printed Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 2 :
            print("You choose : Men & Women Full Sleeve Solid Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 3 :
            print("You choose : Men Full Sleeve zip-up Sweatshirts!... ")
            print("The price of this Shirts is : $499 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $333 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 5 :
            print("You choose : Men Solid Dark Blue Hoddie !... ")
            print("The price of this Shirts is : $555 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Gucci_Shorts (self) :
        user_input_for_Shorts = int(input("""\n
        Choose Shorts :
            1. Solid Men Grey Cargo Shorts 
            2. Self Design Men Black Regular Shorts
            3. Self Design Men Black Sports Shorts 
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue Shorts
            6. Exit
        \nEnter your choice which Shorts do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shorts == 1 :
            print("You choose : Solid Men Grey Cargo Shorts !... ")
            print("The price of this Shirts is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 2 :
            print("You choose : Self Design Men Black Regular Shorts !... ")
            print("The price of this Shirts is : $490 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 3 :
            print("You choose : Self Design Men Black Sports Shorts Shorts !... ")
            print("The price of this Shirts is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 5 :
            print("You choose : Men Solid Dark Blue Shorts !... ")
            print("The price of this Shirts is : $850 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Gucci_Jacket (self) :
        user_input_for_Jacket = int(input("""\n
        Choose Jacket :
            1. Men Printed Biker / Riding Jacket
            2. Men Printed Quilted Jacket
            3. Men colorblock Casual Jacket
            4. Men Printed Casal Jacket
            5. Full Sleeve Colorblock Men Casual Jacket
            6. Exit
        \nEnter your choice which Jacket do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Jacket == 1 :
            print("You choose : Men Printed Biker / Riding Jacket !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 2 :
            print("You choose : Men Printed Quilted Jacket !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 3 :
            print("You choose a : Men colorblock Casual Jacket !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 4 :
            print("You choose : Men Printed Casal Jacket !... ")
            print("The price of this Shirts is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 5 :
            print("You choose : Full Sleeve Colorblock Men Casual Jacket !... ")
            print("The price of this Shirts is : $885 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  H_&_M   ----------------------------------------------------------



    def H_M_T_Shirts (self) :
        user_input_for_T_Shirt = int(input("""\n
        Choose T-shirt :
            1. Men Cartoon Round Neck Cotton T-shirts
            2. Pack of 2 Printed Polyester T-shirts
            3. Men Checkered Polo T-shirts
            4. Exit
        \nEnter your choice which T-Shirt do you like : """))

        print("\nNice Dude !...")


        if user_input_for_T_Shirt == 1 :
            print("You choose : Men Cartoon Round Neck Cotton T-Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 2 :
            print("You choose : Pack of 2 Printed Polyester T-shirts !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 3 :
            print("You choose : Men Checkered Polo T-shirts !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def H_M_Shirts (self) :
        user_input_for_Shirt = int(input("""\n
        Choose Shirt :
            1. Men Regular Fit Self Design Spread Collar Casual Shirt
            2. Men Regular Fit Solid Design Spread Collar Casual Shirt
            3. Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt
            4. Men Slim Fit Self Checkeared Spread Collar Casual Shirt
            5. Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt
            6. Men Regular Fit Striped Casual Shirt
            7. Exit
        \nEnter your choice which Shirt do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shirt == 1 :
            print("You choose : Men Regular Fit Self Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 2 :
            print("You choose : Men Regular Fit Solid Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 3 :
            print("You choose : Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 4 :
            print("You choose : Men Slim Fit Self Checkeared Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 5 :
            print("You choose : Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt !... ")
            print("The price of this Shirts is : $610 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 6 :
            print("You choose : Men Regular Fit Striped Casual Shirt !... ")
            print("The price of this Shirts is : $450 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def H_M_Pant (self) :
        user_input_for_Pant = int(input("""\n
        Choose Pant :
            1. Men Striped Black Track Pants 
            2. Men Colorblock Brown Track Pants
            3. Men Printed Black Track Pants
            4. Men Self Desgn Black Track Pants
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Pant do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Pant == 1 :
            print("You choose : Men Striped Black Track Pants !... ")
            print("The price of this Shirts is : $364 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 2 :
            print("You choose : Men Colorblock Brown Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 3 :
            print("You choose : Men Printed Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 4 :
            print("You choose : Men Self Desgn Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def H_M_Hoddie (self) :
        user_input_for_Hoddie = int(input("""\n
        Choose Hoddie :
            1. Men Full Sleeve Printed Hooded Sweatshirts 
            2. Men & Women Full Sleeve Solid Hooded Sweatshirts
            3. Men Full Sleeve zip-up Sweatshirts
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Hoddie do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Hoddie == 1 :
            print("You choose : Men Full Sleeve Printed Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 2 :
            print("You choose : Men & Women Full Sleeve Solid Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 3 :
            print("You choose : Men Full Sleeve zip-up Sweatshirts !... ")
            print("The price of this Shirts is : $499 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $333 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $555 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def H_M_Shorts (self) :
        user_input_for_Shorts = int(input("""\n
        Choose Shorts :
            1. Solid Men Grey Cargo Shorts 
            2. Self Design Men Black Regular Shorts
            3. Self Design Men Black Sports Shorts 
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Shorts do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shorts == 1 :
            print("You choose : Solid Men Grey Cargo Shorts !... ")
            print("The price of this Shirts is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 2 :
            print("You choose : Self Design Men Black Regular Shorts !... ")
            print("The price of this Shirts is : $490 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 3 :
            print("You choose : Self Design Men Black Sports Shorts !... ")
            print("The price of this Shirts is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $850 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def H_M_Jacket (self) :
        user_input_for_Jacket = int(input("""\n
        Choose Jacket :
            1. Men Printed Biker / Riding Jacket
            2. Men Printed Quilted Jacket
            3. Men colorblock Casual Jacket
            4. Men Printed Casal Jacket
            5. Full Sleeve Colorblock Men Casual Jacket
            6. Exit
        \nEnter your choice which Jacket do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Jacket == 1 :
            print("You choose : Men Printed Biker / Riding Jacket !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 2 :
            print("You choose : Men Printed Quilted Jacket !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 3 :
            print("You choose : Men colorblock Casual Jacket !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 4 :
            print("You choose : Men Printed Casal Jacket !... ")
            print("The price of this Shirts is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 5 :
            print("You choose : Full Sleeve Colorblock Men Casual Jacket !... ")
            print("The price of this Shirts is : $885 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Gucci   ----------------------------------------------------------



    def Nike_T_Shirts (self) :
        user_input_for_T_Shirt = int(input("""\n
        Choose T-shirt :
            1. Men Cartoon Round Neck Cotton T-shirts
            2. Pack of 2 Printed Polyester T-shirts
            3. Men Checkered Polo T-shirts
            4. Exit
        \nEnter your choice which T-Shirt do you like : """))

        print("\nNice Dude !...")


        if user_input_for_T_Shirt == 1 :
            print("You choose : Men Cartoon Round Neck Cotton T-shirts !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 2 :
            print("You choose : Pack of 2 Printed Polyester T-shirts !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 3 :
            print("You choose : Men Checkered Polo T-shirts !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Nike_Shirts (self) :
        user_input_for_Shirt = int(input("""\n
        Choose Shirt :
            1. Men Regular Fit Self Design Spread Collar Casual Shirt
            2. Men Regular Fit Solid Design Spread Collar Casual Shirt
            3. Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt
            4. Men Slim Fit Self Checkeared Spread Collar Casual Shirt
            5. Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt
            6. Men Regular Fit Striped Casual Shirt
            7. Exit
        \nEnter your choice which Shirt do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shirt == 1 :
            print("You choose : Men Regular Fit Self Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 2 :
            print("You choose : Men Regular Fit Solid Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 3 :
            print("You choose : Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 4 :
            print("You choose : Men Slim Fit Self Checkeared Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 5 :
            print("You choose : Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt !... ")
            print("The price of this Shirts is : $610 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 6 :
            print("You choose : Men Regular Fit Striped Casual Shirt !... ")
            print("The price of this Shirts is : $450 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Nike_Pant (self) :
        user_input_for_Pant = int(input("""\n
        Choose Pant :
            1. Men Striped Black Track Pants 
            2. Men Colorblock Brown Track Pants
            3. Men Printed Black Track Pants
            4. Men Self Desgn Black Track Pants
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Pant do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Pant == 1 :
            print("You choose : Men Striped Black Track Pants !... ")
            print("The price of this Shirts is : $364 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 2 :
            print("You choose : Men Colorblock Brown Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 3 :
            print("You choose : Men Printed Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 4 :
            print("You choose : Men Self Desgn Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Nike_Hoddie (self) :
        user_input_for_Hoddie = int(input("""\n
        Choose Hoddie :
            1. Men Full Sleeve Printed Hooded Sweatshirts 
            2. Men & Women Full Sleeve Solid Hooded Sweatshirts
            3. Men Full Sleeve zip-up Sweatshirts
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Hoddie do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Hoddie == 1 :
            print("You choose : Men Full Sleeve Printed Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 2 :
            print("You choose : Men & Women Full Sleeve Solid Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 3 :
            print("You choose : Men Full Sleeve zip-up Sweatshirts !... ")
            print("The price of this Shirts is : $499 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $333 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $555 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Nike_Shorts (self) :
        user_input_for_Shorts = int(input("""\n
        Choose Shorts :
            1. Solid Men Grey Cargo Shorts 
            2. Self Design Men Black Regular Shorts
            3. Self Design Men Black Sports Shorts 
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Shorts do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shorts == 1 :
            print("You choose : Solid Men Grey Cargo Shorts !... ")
            print("The price of this Shirts is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 2 :
            print("You choose : Self Design Men Black Regular Shorts !... ")
            print("The price of this Shirts is : $490 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 3 :
            print("You choose : Self Design Men Black Sports Shorts !... ")
            print("The price of this Shirts is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $850 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Nike_Jacket (self) :
        user_input_for_Jacket = int(input("""\n
        Choose Jacket :
            1. Men Printed Biker / Riding Jacket
            2. Men Printed Quilted Jacket
            3. Men colorblock Casual Jacket
            4. Men Printed Casal Jacket
            5. Full Sleeve Colorblock Men Casual Jacket
            6. Exit
        \nEnter your choice which Jacket do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Jacket == 1 :
            print("You choose : Men Printed Biker / Riding Jacket !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 2 :
            print("You choose  : Men Printed Quilted Jacket !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 3 :
            print("You choose : Men colorblock Casual Jacket !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 4 :
            print("You choose : Men Printed Casal Jacket !... ")
            print("The price of this Shirts is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 5 :
            print("You choose : Full Sleeve Colorblock Men Casual Jacket !... ")
            print("The price of this Shirts is : $885 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Zara   ----------------------------------------------------------



    def Zara_T_Shirts (self) :
        user_input_for_T_Shirt = int(input("""\n
        Choose T-shirt :
            1. Men Cartoon Round Neck Cotton T-shirts
            2. Pack of 2 Printed Polyester T-shirts
            3. Men Checkered Polo T-shirts
            4. Exit
        \nEnter your choice which T-Shirt do you like : """))

        print("\nNice Dude !...")


        if user_input_for_T_Shirt == 1 :
            print("You choose : Men Cartoon Round Neck Cotton T-shirts !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 2 :
            print("You choose : Pack of 2 Printed Polyester T-shirts !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 3 :
            print("You choose : Men Checkered Polo T-shirts !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Zara_Shirts (self) :
        user_input_for_Shirt = int(input("""\n
        Choose Shirt :
            1. Men Regular Fit Self Design Spread Collar Casual Shirt
            2. Men Regular Fit Solid Design Spread Collar Casual Shirt
            3. Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt
            4. Men Slim Fit Self Checkeared Spread Collar Casual Shirt
            5. Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt
            6. Men Regular Fit Striped Casual Shirt
            7. Exit
        \nEnter your choice which Shirt do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shirt == 1 :
            print("You choose : Men Regular Fit Self Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 2 :
            print("You choose : Men Regular Fit Solid Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 3 :
            print("You choose : Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 4 :
            print("You choose : Men Slim Fit Self Checkeared Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 5 :
            print("You choose : Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt !... ")
            print("The price of this Shirts is : $610 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 6 :
            print("You choose : Men Regular Fit Striped Casual Shirt !... ")
            print("The price of this Shirts is : $450 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Zara_Pant (self) :
        user_input_for_Pant = int(input("""\n
        Choose Pant :
            1. Men Striped Black Track Pants 
            2. Men Colorblock Brown Track Pants
            3. Men Printed Black Track Pants
            4. Men Self Desgn Black Track Pants
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Pant do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Pant == 1 :
            print("You choose : Men Striped Black Track Pants !... ")
            print("The price of this Shirts is : $364 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 2 :
            print("You choose : Men Colorblock Brown Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 3 :
            print("You choose : Men Printed Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 4 :
            print("You choose : Men Self Desgn Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Zara_Hoddie (self) :
        user_input_for_Hoddie = int(input("""\n
        Choose Hoddie :
            1. Men Full Sleeve Printed Hooded Sweatshirts 
            2. Men & Women Full Sleeve Solid Hooded Sweatshirts
            3. Men Full Sleeve zip-up Sweatshirts
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Hoddie do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Hoddie == 1 :
            print("You choose : Men Full Sleeve Printed Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 2 :
            print("You choose : Men & Women Full Sleeve Solid Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 3 :
            print("You choose : Men Full Sleeve zip-up Sweatshirts !... ")
            print("The price of this Shirts is : $499 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $333 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $555 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Zara_Shorts (self) :
        user_input_for_Shorts = int(input("""\n
        Choose Shorts :
            1. Solid Men Grey Cargo Shorts 
            2. Self Design Men Black Regular Shorts
            3. Self Design Men Black Sports Shorts 
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Shorts do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shorts == 1 :
            print("You choose : Solid Men Grey Cargo Shorts  !... ")
            print("The price of this Shirts is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 2 :
            print("You choose : Self Design Men Black Regular Shortss !... ")
            print("The price of this Shirts is : $490 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 3 :
            print("You choose : Self Design Men Black Sports Shorts !... ")
            print("The price of this Shirts is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $850 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Zara_Jacket (self) :
        user_input_for_Jacket = int(input("""\n
        Choose Jacket :
            1. Men Printed Biker / Riding Jacket
            2. Men Printed Quilted Jacket
            3. Men colorblock Casual Jacket
            4. Men Printed Casal Jacket
            5. Full Sleeve Colorblock Men Casual Jacket
            6. Exit
        \nEnter your choice which Jacket do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Jacket == 1 :
            print("You choose : Men Printed Biker / Riding Jacket !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 2 :
            print("You choose : Men Printed Quilted Jacket !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 3 :
            print("You choose : Men colorblock Casual Jacket !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 4 :
            print("You choose : Men Printed Casal Jacket !... ")
            print("The price of this Shirts is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 5 :
            print("You choose : Full Sleeve Colorblock Men Casual Jacket !... ")
            print("The price of this Shirts is : $885 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Levi's   ----------------------------------------------------------



    def Levis_T_Shirts (self) :
        user_input_for_T_Shirt = int(input("""\n
        Choose T-shirt :
            1. Men Cartoon Round Neck Cotton T-shirts
            2. Pack of 2 Printed Polyester T-shirts
            3. Men Checkered Polo T-shirts
            4. Exit
        \nEnter your choice which T-Shirt do you like : """))

        print("\nNice Dude !...")


        if user_input_for_T_Shirt == 1 :
            print("You choose : Men Cartoon Round Neck Cotton T-shirts !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 2 :
            print("You choose : Pack of 2 Printed Polyester T-shirts !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 3 :
            print("You choose : Men Checkered Polo T-shirts !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Levis_Shirts (self) :
        user_input_for_Shirt = int(input("""\n
        Choose Shirt :
            1. Men Regular Fit Self Design Spread Collar Casual Shirt
            2. Men Regular Fit Solid Design Spread Collar Casual Shirt
            3. Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt
            4. Men Slim Fit Self Checkeared Spread Collar Casual Shirt
            5. Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt
            6. Men Regular Fit Striped Casual Shirt
            7. Exit
        \nEnter your choice which Shirt do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shirt == 1 :
            print("You choose : Men Regular Fit Self Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 2 :
            print("You choose : Men Regular Fit Solid Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 3 :
            print("You choose : Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 4 :
            print("You choose : Men Slim Fit Self Checkeared Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 5 :
            print("You choose : Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt !... ")
            print("The price of this Shirts is : $610 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 6 :
            print("You choose : Men Regular Fit Striped Casual Shirt !... ")
            print("The price of this Shirts is : $450 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Levis_Pant (self) :
        user_input_for_Pant = int(input("""\n
        Choose Pant :
            1. Men Striped Black Track Pants 
            2. Men Colorblock Brown Track Pants
            3. Men Printed Black Track Pants
            4. Men Self Desgn Black Track Pants
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Pant do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Pant == 1 :
            print("You choose : Men Striped Black Track Pants !... ")
            print("The price of this Shirts is : $364 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 2 :
            print("You choose : Men Colorblock Brown Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 3 :
            print("You choose : Men Printed Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 4 :
            print("You choose : Men Self Desgn Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Levis_Hoddie (self) :
        user_input_for_Hoddie = int(input("""\n
        Choose Hoddie :
            1. Men Full Sleeve Printed Hooded Sweatshirts 
            2. Men & Women Full Sleeve Solid Hooded Sweatshirts
            3. Men Full Sleeve zip-up Sweatshirts
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Hoddie do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Hoddie == 1 :
            print("You choose : Men Full Sleeve Printed Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 2 :
            print("You choose : Men & Women Full Sleeve Solid Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 3 :
            print("You choose : Men Full Sleeve zip-up Sweatshirts !... ")
            print("The price of this Shirts is : $499 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $333 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $555 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Levis_Shorts (self) :
        user_input_for_Shorts = int(input("""\n
        Choose Shorts :
            1. Solid Men Grey Cargo Shorts 
            2. Self Design Men Black Regular Shorts
            3. Self Design Men Black Sports Shorts 
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Shorts do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shorts == 1 :
            print("You choose : Solid Men Grey Cargo Shorts !... ")
            print("The price of this Shirts is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 2 :
            print("You choose : Self Design Men Black Regular Shorts !... ")
            print("The price of this Shirts is : $490 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 3 :
            print("You choose : Self Design Men Black Sports Shorts !... ")
            print("The price of this Shirts is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 5 :
            print("You choose : Men Solid Dark Blue  !... ")
            print("The price of this Shirts is : $850 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Levis_Jacket (self) :
        user_input_for_Jacket = int(input("""\n
        Choose Jacket :
            1. Men Printed Biker / Riding Jacket
            2. Men Printed Quilted Jacket
            3. Men colorblock Casual Jacket
            4. Men Printed Casal Jacket
            5. Full Sleeve Colorblock Men Casual Jacket
            6. Exit
        \nEnter your choice which Jacket do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Jacket == 1 :
            print("You choose : Men Printed Biker / Riding Jacket !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 2 :
            print("You choose : Men Printed Quilted Jacket !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 3 :
            print("You choose : Men colorblock Casual Jacket !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 4 :
            print("You choose : Men Printed Casal Jacket !... ")
            print("The price of this Shirts is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 5 :
            print("You choose : Full Sleeve Colorblock Men Casual Jacket !... ")
            print("The price of this Shirts is : $885 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Calvin_Klein   -------------------------------------------------------



    def Calvin_Klein_T_Shirts (self) :
        user_input_for_T_Shirt = int(input("""\n
        Choose T-shirt :
            1. Men Cartoon Round Neck Cotton T-shirts
            2. Pack of 2 Printed Polyester T-shirts
            3. Men Checkered Polo T-shirts
            4. Exit
        \nEnter your choice which T-Shirt do you like : """))

        print("\nNice Dude !...")


        if user_input_for_T_Shirt == 1 :
            print("You choose : Men Cartoon Round Neck Cotton T-shirts !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 2 :
            print("You choose : Pack of 2 Printed Polyester T-shirts !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_T_Shirt == 3 :
            print("You choose : Men Checkered Polo T-shirts !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Calvin_Klein_Shirts (self) :
        user_input_for_Shirt = int(input("""\n
        Choose Shirt :
            1. Men Regular Fit Self Design Spread Collar Casual Shirt
            2. Men Regular Fit Solid Design Spread Collar Casual Shirt
            3. Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt
            4. Men Slim Fit Self Checkeared Spread Collar Casual Shirt
            5. Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt
            6. Men Regular Fit Striped Casual Shirt
            7. Exit
        \nEnter your choice which Shirt do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shirt == 1 :
            print("You choose : Men Regular Fit Self Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 2 :
            print("You choose : Men Regular Fit Solid Design Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $390 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 3 :
            print("You choose : Men Regular , Super Slim Fit Self Design Ribbed Collar Casual Shirt !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 4 :
            print("You choose : Men Slim Fit Self Checkeared Spread Collar Casual Shirt !... ")
            print("The price of this Shirts is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 5 :
            print("You choose : Men Slim Fit Self Checkeared Botton Down Collar Casual Shirt !... ")
            print("The price of this Shirts is : $610 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shirt == 6 :
            print("You choose : Men Regular Fit Striped Casual Shirt !... ")
            print("The price of this Shirts is : $450 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Calvin_Klein_Pant (self) :
        user_input_for_Pant = int(input("""\n
        Choose Pant :
            1. Men Striped Black Track Pants 
            2. Men Colorblock Brown Track Pants
            3. Men Printed Black Track Pants
            4. Men Self Desgn Black Track Pants
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Pant do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Pant == 1 :
            print("You choose : Men Striped Black Track Pants !... ")
            print("The price of this Shirts is : $364 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 2 :
            print("You choose : Men Colorblock Brown Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 3 :
            print("You choose : Men Printed Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 4 :
            print("You choose : Men Self Desgn Black Track Pants !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Pant == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Calvin_Klein_Hoddie (self) :
        user_input_for_Hoddie = int(input("""\n
        Choose Hoddie :
            1. Men Full Sleeve Printed Hooded Sweatshirts 
            2. Men & Women Full Sleeve Solid Hooded Sweatshirts
            3. Men Full Sleeve zip-up Sweatshirts
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Hoddie do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Hoddie == 1 :
            print("You choose : Men Full Sleeve Printed Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 2 :
            print("You choose : Men & Women Full Sleeve Solid Hooded Sweatshirts !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 3 :
            print("You choose : Men Full Sleeve zip-up Sweatshirts !... ")
            print("The price of this Shirts is : $499 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $333 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Hoddie == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $555 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Calvin_Klein_Shorts (self) :
        user_input_for_Shorts = int(input("""\n
        Choose Shorts :
            1. Solid Men Grey Cargo Shorts 
            2. Self Design Men Black Regular Shorts
            3. Self Design Men Black Sports Shorts 
            4. Men Full sleeve oversized Hoddie
            5. Men Solid Dark Blue
            6. Exit
        \nEnter your choice which Shorts do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Shorts == 1 :
            print("You choose : Solid Men Grey Cargo Shorts !... ")
            print("The price of this Shirts is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 2 :
            print("You choose : Self Design Men Black Regular Shorts !... ")
            print("The price of this Shirts is : $490 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 3 :
            print("You choose : Self Design Men Black Sports Shorts !... ")
            print("The price of this Shirts is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 4 :
            print("You choose : Men Full sleeve oversized Hoddie !... ")
            print("The price of this Shirts is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Shorts == 5 :
            print("You choose : Men Solid Dark Blue !... ")
            print("The price of this Shirts is : $850 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")




    def Calvin_Klein_Jacket (self) :
        user_input_for_Jacket = int(input("""\n
        Choose Jacket :
            1. Men Printed Biker / Riding Jacket
            2. Men Printed Quilted Jacket
            3. Men colorblock Casual Jacket
            4. Men Printed Casal Jacket
            5. Full Sleeve Colorblock Men Casual Jacket
            6. Exit
        \nEnter your choice which Jacket do you like : """))

        print("\nNice Buddy !...")


        if user_input_for_Jacket == 1 :
            print("You choose : Men Printed Biker / Riding Jacket !... ")
            print("The price of this Shirts is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 2 :
            print("You choose : Men Printed Quilted Jacket !... ")
            print("The price of this Shirts is : $350 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 3 :
            print("You choose : Men colorblock Casual Jacket !... ")
            print("The price of this Shirts is : $400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 4 :
            print("You choose : Men Printed Casal Jacket !... ")
            print("The price of this Shirts is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jacket == 5 :
            print("You choose : Full Sleeve Colorblock Men Casual Jacket !... ")
            print("The price of this Shirts is : $885 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")







    def Fashion_Brand (self) :
        user_input_Fashion_Brand = int(input("""\n
        Choose a Fashion brand:
            1. Gucci
            2. H&M
            3. Nike
            4. Zara
            5. Levi's
            6. Calvin Klein
            7. Exit
        \nEnter your choice which brand do you like : """))

        print("\nNice Dude !...")


        if  user_input_Fashion_Brand == 1 :
            self.Fashion_Type()

        elif  user_input_Fashion_Brand == 2 :
            self.Fashion_Type()

        elif  user_input_Fashion_Brand == 3 :
            self.Fashion_Type()

        elif  user_input_Fashion_Brand == 4 :
            self.Fashion_Type()

        elif  user_input_Fashion_Brand == 5 :
            self.Fashion_Type()

        elif  user_input_Fashion_Brand == 6 :
            self.Fashion_Type()

        elif  user_input_Fashion_Brand == 7 :
            self.menu()

        else :
            print("Please , enter the valid Input !...")




    def Fashion_Type (self) :
        user_input_Fashion_Type = int(input("""\n
        Choose a Fashion brand:
            1. T-Shirts
            2. Shirts
            3. Pant
            4. Hoddie
            5. Shorts
            6. Jackets
            7. Exit
        \nEnter your choice which brand type do you like : """))

        print("\nNice Buddy !...")



        if  user_input_Fashion_Type == 1 :
            self.Gucci_T_Shirts()
            self.Fashion_Type()

        elif user_input_Fashion_Type == 2 :
            self.Gucci_Shirts()
            self.Fashion_Type()

        elif  user_input_Fashion_Type == 3 :
            self.Gucci_Pant()
            self.Fashion_Type()

        elif  user_input_Fashion_Type == 4 :
            self.Gucci_Hoddie()
            self.Fashion_Type()

        elif  user_input_Fashion_Type == 5 :
            self.Gucci_Shorts()
            self.Fashion_Type()

        elif  user_input_Fashion_Type == 6 :
            self.Gucci_Jacket()
            self.Fashion_Type()

        elif  user_input_Fashion_Type == 7 :
            self.Fashion_Brand()

        else :
            print("Please , enter the valid Input !...")




#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#                                                     New Class




class Mobile(Fashion) :


    def __init__ (self) :
        self.Mobile_Brand()



# -------------------------------------------------------  Oppo   ----------------------------------------------------------



    def Oppo_Mobile (self) :
        user_input_Oppo_Mobile = int(input("""\n
        Choose Mobile :
            1. Oppo K13 5G 6000mAh abd 45W SUPERVOOC Charge & AI  
                features :  ( 4 GB | 128 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50MP + 2MP Real Camera )
                            ( 8 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 6000 mAh Battery ) \n
            2. Oppo A5x (Laser White , 64 GB )  
                features :  ( 4 GB | 64 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 32MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.67 inch )
                            ( 6000 mAh Battery ) \n
            3. Oppo F29 PRO ( marval White , 256 GB ) ( 8 GB RAM )  
                features :  ( 4 GB | 64 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 32MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.67 inch )
                            ( 6000 mAh Battery ) \n
            4. Oppo A17 ( Lake Blue , 64 GB ) ( 4 GB RAM )  
                features :  ( 4 GB | 64 GB ROM ) -> ( Store up to 2000 photos )
                            ( Mediatek Helio G35 | Octa Core Lag-Free Performance )
                            ( 50 MP + 0.3 MP + 0.3 MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Oppo_Mobile == 1 :
            print("You choose : K13 5G 6000mAh aNd 45W SUPERVOOC Charge & AI Mobile !... ")
            print("Which prich has : $12,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Oppo_Mobile == 2 :
            print("You choose : Oppo A5x ( Laser White , 64 GB ) Mobile !... ")
            print("The price of this Shirts is : $10,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Oppo_Mobile == 3 :
            print("You choose : Oppo F29 PRO ( marval White , 256 GB ) ( 8 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $29,800 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Oppo_Mobile == 4 :
            print("You choose : Oppo A17 ( Lake Blue , 64 GB ) ( 4 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $9,500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Vivo   ----------------------------------------------------------



    def Vivo_Mobile (self) :
        user_input_Vivo_Mobile = int(input("""\n
        Choose Mobile :
            1. Vivo T4 Lite 5G Charger in the Box ( Titanium Gold , 128 GB ) ( 4 GB RAM )  
                features :  ( 4 GB | 128 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock Speed )
                            ( 50MP + 2MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.74 inch HD + LCD Display )
                            ( 6000 mAh Battery ) \n
            2. Vivo Y31 5G  ( Rose Red , 128 GB ) ( 4 GB RAM ) 
                features :  ( 4 GB | 128 GB ROM )
                            ( 4 Gen 2 | Octa Core Processor | 2.2 GHz Clock Speed )
                            ( 50 MP + 0.08 MP Real Camera )
                            ( 8 MP Front Camera )
                            ( 6.68 inch )
                            ( 6500 mAh Battery ) \n
            3. Vivo Y31 5G ( Glacier Blue , 128 GB ) ( 4 GB RAM )  
                features :  ( 4 GB | 128 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock , Powerful Performance )
                            ( 50 MP + 0.08 MP Real Camera )
                            ( 8 MP Front Camera )
                            ( 6.68 inch )
                            ( 5500 mAh Battery ) \n
            4. Vivo V25 5G  ( Sunrise Gold , 128 GB ) ( 8 GB RAM )  
                features :  ( 8 GB | 128 GB ROM ) -> ( Store up to 2000 photos )
                            ( Mediatek Helio G35 | Octa Core Lag-Free Performance )
                            ( 64 MP + 8 MP + 2 MP Real Camera )
                            ( 50 MP Front Camera )
                            ( 6.44 inch HD + LCD Display )
                            ( 4500 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Vivo_Mobile == 1 :
            print("You choose : Vivo T4 Lite 5G Charger in the Box ( Titanium Gold , 128 GB ) ( 4 GB RAM )  Mobile !... ")
            print("Which prich has : $21,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Vivo_Mobile == 2 :
            print("You choose : Vivo Y31 5G  ( Rose Red , 128 GB ) ( 4 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $15,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Vivo_Mobile == 3 :
            print("You choose : Vivo Y31 5G ( Glacier Blue , 128 GB ) ( 4 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $19,800 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Vivo_Mobile == 4 :
            print("You choose : Vivo V25 5G  ( Sunrise Gold , 128 GB ) ( 8 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $19,500 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Apple   ----------------------------------------------------------



    def Apple_Mobile (self) :
        user_input_Apple_Mobile = int(input("""\n
        Choose Mobile :
            1. Iphone 17 Pro Max ( Deep Blue , 256 GB )
                features :  ( 8 GB | 256 GB ROM )
                            ( Superfast Multitasking  )
                            ( 50MP + 2MP Real Camera )
                            ( 8 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 6000 mAh Battery ) \n
            2. Iphone 16 Pro Max ( Desert Titanium , 256 GB ) 
                features :  ( 16 GB | 256 GB ROM )
                            ( A18 Pro Chip | 6 Core Processor | 2.4 GHz Clock )
                            ( 48 MP + 48 MP + 12 MP Real Camera )
                            ( 12 MP Front Camera )
                            ( 6.9 inch )
                            ( 6000 mAh Battery ) \n
            3. Iphone 15 Pro Max ( Natural Titanium , 256 GB ) 
                features :  ( 8 GB | 256 GB ROM ) -> ( Store up to 6000 photos )
                            ( A17 Pro Chip | 6 Core Processor | 2.4 GHz Clock )
                            ( 48 MP + 12 MP + 12 MP Real Camera )
                            ( 12 MP Front Camera )
                            ( 6.7 inch )
                            ( 6000 mAh Battery ) \n
            4. Iphone 14 Pro Max ( Natural Titanium , 256 GB )  
                features :  ( 4 GB | 64 GB ROM ) -> ( Store up to 2000 photos )
                            ( Mediatek Helio G35 | Octa Core Lag-Free Performance )
                            ( 48 MP + 12 MP + 12 MP Real Camera )
                            ( 12 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Apple_Mobile == 1 :
            print("You choose : Iphone 17 Pro Max ( Deep Blue , 256 GB ) Mobile !... ")
            print("Which prich has : $1,49,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Apple_Mobile == 2 :
            print("You choose : Oppo A5x ( Laser White , 64 GB ) Mobile !... ")
            print("The price of this Shirts is : $1,00,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Apple_Mobile == 3 :
            print("You choose : Oppo F29 PRO ( marval White , 256 GB ) ( 8 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $1,58,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Apple_Mobile == 4 :
            print("You choose : Oppo A17 ( Lake Blue , 64 GB ) ( 4 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $95,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Samsung   ----------------------------------------------------------



    def Samsung_Mobile (self) :
        user_input_Samsung_Mobile = int(input("""\n
        Choose Mobile :
            1. Samsung Galaxy F06 5G ( Bahama Blue , 128 GB ) ( 4 GB RAM )  
                features :  ( 4 GB | 128 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP + 2MP Real Camera )
                            ( 8 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
            2. Samsung Galaxy A16 5G ( Light Green , 128 GB ) ( 6 GB RAM ) 
                features :  ( 4 GB | 64 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP + 5 MP + 2 MP Real Camera )
                            ( 13 MP Front Camera )
                            ( 6.7 inch )
                            ( 5000 mAh Battery ) \n
            3. Samsung Galaxy S24 Ultra 5G ( Titanium Violet , 256 GB ) ( 12 GB RAM )   
                features :  ( 12 GB | 256 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 200 MP + 50 MP + 12 MP + 10 MP Real Camera )
                            ( 12 MP Front Camera )
                            ( 6.8 inch )
                            ( 5000 mAh Battery ) \n
            4. Samsung Galaxy Note 20 Ultra 5G ( Mystic Black , 256 GB ) ( 12 GB RAM )   
                features :  ( 12 GB | 256 GB ROM ) -> ( Store up 6000 photos )
                            ( Mediatek Helio G35 | Octa Core Lag-Free Performance )
                            ( 108 MP + 12 MP + 12 MP Real Camera )
                            ( 10 MP Front Camera )
                            ( 6.9 inch HD + LCD Display )
                            ( 4500 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Samsung_Mobile == 1 :
            print("You choose : Samsung Galaxy F06 5G ( Bahama Blue , 128 GB ) ( 4 GB RAM ) Mobile !... ")
            print("Which prich has : $9,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Samsung_Mobile == 2 :
            print("You choose : Samsung Galaxy A16 5G ( Light Green , 128 GB ) ( 6 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $14,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Samsung_Mobile == 3 :
            print("You choose : Samsung Galaxy S24 Ultra 5G ( Titanium Violet , 256 GB ) ( 12 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $88,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Samsung_Mobile == 4 :
            print("You choose : Samsung Galaxy Note 20 Ultra 5G ( Mystic Black , 256 GB ) ( 12 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $1,00,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Xiaomi   ----------------------------------------------------------



    def Xiaomi_Mobile (self) :
        user_input_Xiaomi_Mobile = int(input("""\n
        Choose Mobile :
            1. Mi 14 CIVI ( Aqua Blue , 512 GB ) ( 12 GB RAM ) 
                features :  ( 12 GB | 512 GB ROM ) -> ( Store up to 10000 photos )
                            ( 8s Gen 3 Mobile Platform | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP Real Camera )
                            ( 32 MP + 32 MP Front Camera )
                            ( 6.55 inch HD + LCD Display )
                            ( 4700 mAh Battery ) \n
            2. Mi 15 5G ( Midnight Black , 128 GB ) ( 6 GB RAM )  
                features :  ( 6 GB | 128 GB ROM )
                            ( 2.3 GHz Clock Speed )
                            ( 50 MP Real Camera )
                            ( 6.9 inch )
                            ( 7000 mAh Battery ) \n
            3. Mi 13 5G ( Black Diamond , 128 GB ) ( 6 GB RAM )
                features :  ( 4 GB | 64 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 32MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.67 inch )
                            ( 6000 mAh Battery ) \n
            4. Mi Note-14 Pro 5G ( Titan Black , 256 GB ) ( 8 GB RAM ) 
                features :  ( 8 GB | 256 GB ROM ) -> ( Store up to 6000 photos )
                            ( Mediatek Helio G35 | Octa Core Lag-Free Performance )
                            ( 50 MP + 8 MP + 2 MP Real Camera )
                            ( 20 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 5500 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Xiaomi_Mobile == 1 :
            print("You choose : K13 5G 6000mAh aNd 45W SUPERVOOC Charge & AI Mobile !... ")
            print("Which prich has : $36,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Xiaomi_Mobile == 2 :
            print("You choose : Mi 15 5G ( Midnight Black , 128 GB ) ( 6 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $14,500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Xiaomi_Mobile == 3 :
            print("You choose : Mi 13 5G ( Black Diamond , 128 GB ) ( 6 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $14,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Xiaomi_Mobile == 4 :
            print("You choose : Mi Note-14 Pro 5G ( Titan Black , 256 GB ) ( 8 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $23,300 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# -------------------------------------------------------  Poco   ----------------------------------------------------------



    def Poco_Mobile (self) :
        user_input_Poco_Mobile = int(input("""\n
        Choose Mobile :
            1. Poco M7 5G ( Mint Green , 128 GB )  
                features :  ( 6 GB | 128 GB ROM )
                            ( 4 Gen 2 5G | Octa Core Processor | 2.4 GHz Clock )
                            ( 50MP Real Camera )
                            ( 8 MP Front Camera )
                            ( 6.88 inch HD + 120Hz Display )
                            ( 1560 mAh Battery ) \n
            2. Poco C75 5G ( Aqua Bliss , 64 GB )  ->  ( Store up to 2000 photos )
                features :  ( 4 GB | 164 GB ROM )
                            ( 4s Gen 2 5G | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.88 inch )
                            ( 5160 mAh Battery ) \n
            3. Poco X7 5G ( Yellow , 128 GB )  
                features :  ( 8 GB | 128 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP + 8 MP + 2 MP Real Camera )
                            ( 20 MP Front Camera )
                            ( 6.67 inch )
                            ( 5500 mAh Battery ) \n
            4. Poco 5G ( Orion Blue , 128 GB ) ( 6 GB RAM )  
                features :  ( 6 GB | 128 GB ROM )
                            ( Mediatek Helio 6100 + | Octa Core Lag-Free Performance )
                            ( 50 MP MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.74 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Poco_Mobile == 1 :
            print("You choose : Poco M7 5G ( Mint Green , 128 GB ) Mobile !... ")
            print("Which prich has : $9,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Poco_Mobile == 2 :
            print("You choose : Poco C75 5G ( Aqua Bliss , 64 GB ) Mobile !... ")
            print("The price of this Shirts is : $8,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Poco_Mobile == 3 :
            print("You choose : Poco X7 5G ( Yellow , 128 GB ) Mobile !... ")
            print("The price of this Shirts is : $15,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Poco_Mobile == 4 :
            print("You choose : Oppo A17 ( Lake Blue , 64 GB ) ( 4 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $12,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ------------------------------------------------------  Motorola   ---------------------------------------------------------



    def Motorola_Mobile (self) :
        user_input_Motorola_Mobile = int(input("""\n
        Choose Mobile :
            1. MOTOROLA g35 5G ( Leaf Green , 128 GB ) 
                features :  ( 4 GB | 128 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP + 8 MP Real Camera )
                            ( 16 MP Front Camera )
                            ( 6.72 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
            2. MOTOROLA G85 5G ( Olive Green , 128 GB )  
                features :  ( 8 GB | 128 GB ROM )  ->  ( Store up to 3000 photos )
                            ( 6s Gen 3 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP + 8 MP Real Camera )
                            ( 32 MP Front Camera )
                            ( 6.67 inch )
                            ( 5000 mAh Battery ) \n
            3. MOTOROLA Edge 60 Fusion 5G ( PANTONE Mykonos Blue , 256 GB ) ( 8 GB ) 
                features :  ( 8 GB | 256 GB ROM )
                            ( Dimensity 7400 | Octa Core Processor | 2.4 GHz Clock )
                            ( 50 MP + 13 MP Real Camera )
                            ( 32 MP Front Camera )
                            ( 6.67 inch )
                            ( 5500 mAh Battery ) \n
            4. MOTOROLA G34 5G ( Ice Blue , 128 GB ) ( 8 GB RAM )
                features :  ( 8 GB | 128 GB ROM ) -> ( Store up to 3000 photos )
                            ( Snapdragon 695 5G | Octa Core Lag-Free Performance )
                            ( 50 MP + 2 MP Real Camera )
                            ( 16 MP Front Camera )
                            ( 6.5 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_Motorola_Mobile == 1 :
            print("You choose : MOTOROLA g35 5G ( Leaf Green , 128 GB ) !... ")
            print("Which prich has : $9,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Motorola_Mobile == 2 :
            print("You choose : MOTOROLA G85 5G ( Olive Green , 128 GB ) Mobile !... ")
            print("The price of this Shirts is : $15,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Motorola_Mobile == 3 :
            print("You choose : MOTOROLA Edge 60 Fusion 5G ( PANTONE Mykonos Blue , 256 GB ) ( 8 GB ) Mobile !... ")
            print("The price of this Shirts is : $11,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_Motorola_Mobile == 4 :
            print("You choose : MOTOROLA G34 5G ( Ice Blue , 128 GB ) ( 8 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $15,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ------------------------------------------------------  OnePlus   ---------------------------------------------------------



    def One_Plus_Mobile (self) :
        user_input_One_Plus_Mobile = int(input("""\n
        Choose Mobile :
            1. OnePlus Nord CE4 lite 5G ( SUPER SLIVER , 128 GB ) ( 8 GB RAM )  
                features :  ( 8 GB | 128 GB ROM )
                            ( 2.2 GHz Clock Speed )
                            ( 50MP Real Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 5500 mAh Battery ) \n
            2.OnePlus 13R 5G ( Astral Trail , 256 GB ) ( 12 GB RAM )  
                features :  ( 4 GB | 64 GB ROM )
                            ( Dimensity 6300 | Octa Core Processor | 2.4 GHz Clock )
                            ( 32MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.67 inch )
                            ( 6000 mAh Battery ) \n
            3. OnePlus 13s 5G ( Pink Satin , 256 GB ) ( 12 GB RAM )  
                features :  ( 12 GB | 256 GB ROM )
                            ( 4.32 GHz Clock Speed )
                            ( 50 MP Real Camera )
                            ( 6.37 inch )
                            ( 5850 mAh Battery ) \n
            4. OnePlus 12r 5G ( Iron Grey , 256 GB ) ( 16 GB RAM )  
                features :  ( 4 GB | 64 GB ROM ) -> ( Store up to 2000 photos )
                            ( Mediatek Helio G35 | Octa Core Lag-Free Performance )
                            ( 50 MP + 0.3 MP + 0.3 MP Real Camera )
                            ( 5 MP Front Camera )
                            ( 6.67 inch HD + LCD Display )
                            ( 5000 mAh Battery ) \n
        \nEnter your choice which Mobile do you like : """))

        print("\nNice Dude !...")


        if user_input_One_Plus_Mobile == 1 :
            print("You choose : OnePlus Nord CE4 lite 5G ( SUPER SLIVER , 128 GB ) ( 8 GB RAM ) Mobile !... ")
            print("Which prich has : $17,900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_One_Plus_Mobile == 2 :
            print("You choose : OnePlus 13R 5G ( Astral Trail , 256 GB ) ( 12 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $38,899 !...")
            print("That item is successfully added in the card !...")

        elif user_input_One_Plus_Mobile == 3 :
            print("You choose : OnePlus 13s 5G ( Pink Satin , 256 GB ) ( 12 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $51,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_One_Plus_Mobile == 4 :
            print("You choose : OnePlus 12r 5G ( Iron Grey , 256 GB ) ( 16 GB RAM ) Mobile !... ")
            print("The price of this Shirts is : $39,899 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")





    def Mobile_Brand (self) :
        user_input = int(input("""\n
        Choose a Fashion brand:
            1. Oppo
            2. Vivo
            3. Apple
            4. Samsung 
            5. Xiaomi
            6. Poco
            7. Motorola 
            8. OnePlus
            9. Exit
        \nEnter your choice which brand do you like : """))

        print("\nNice Dude !...")


        if user_input == 1 :
            self.Oppo_Mobile()
            self.Mobile_Brand()
        elif user_input == 2 :
            self.Vivo_Mobile()
            self.Mobile_Brand()
        elif user_input == 3 :
            self.Apple_Mobile()
            self.Mobile_Brand()
        elif user_input == 4 :
            self.Samsung_Mobile()
            self.Mobile_Brand()
        elif user_input == 5 :
            self.Xiaomi_Mobile()
            self.Mobile_Brand()
        elif user_input == 6 :
            self.Poco_Mobile()
            self.Mobile_Brand()
        elif user_input == 7 :
            self.Motorola_Mobile()
            self.Mobile_Brand()
        elif user_input == 8 :
            self.One_Plus_Mobile()
            self.Mobile_Brand()
        elif user_input == 9 :
            self.menu()
        else :
            print("Please eter the valid input !...")




#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#                                                     New Class




class Laptop(Mobile) :



    def __init__ (self) :
        self.Laptop_Brand()



# ------------------------------------------------------  Dell   ---------------------------------------------------------



    def Dell_Laptop (self) :
        user_input_for_Dell_Laptop = int(input("""\n
        Choose Laptop :
            1. Dell 15 Intel Core i5  13th Gen 1334U
                features :  ( 8 GB RAM | 512 GB SSD / Window 11 Home --> Smooth Gaming and Video Editing )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.62 Kg --> Light Weight And Easy to Carry ) \n

            2. Dell Inspiron 15 MSO'24 with Blacklit Intel Core i7  11th Gen 1334U
                features :  ( 16 GB RAM | 512 GB SSD / Window 11 Home --> Smooth Gaming and Video Editing )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.62 Kg --> Light Weight And Easy to Carry ) \n
            
            3. Dell G7 Intel Core i9 10th Gen 10885H 
                features :  ( 16 GB RAM | 1 TB SSD / Window 10 Home --> Smooth Gaming and Video Editing )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( NVIDIA GeForce RTX )
                            ( 2.56 Kg --> Light Weight And Easy to Carry ) \n

            4. Dell Inspiron AMD Ryzen 3 Quad Core 5th Gen 3535
                features :  ( 8 GB RAM | 512 G  B SSD / Window 11 Home )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated )
                            ( 2.56 Kg --> Light Weight And Easy to Carry ) \n

            5. Dell Core i5 ( 7th Gen ) 
                features :  ( 8 GB RAM | 256 GB SSD / Window 10 Home )
                            ( 15.8 inch | Full HD Display | 120 Hz )
                            ( 1.6 Kg --> Light Weight And Easy to Carry ) \n
    
        \nEnter your choice which Laptop do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Dell_Laptop == 1 :
            print("You choose : Dell 15 Intel Core i5 13th Gen 1334U Laptop !... ")
            print("The price of this Shirts is : $46,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Dell_Laptop == 2 :
            print("You choose : Dell Inspiron 15 MSO'24 with Blacklit Intel Core i7  11th Gen 1334U Laptop !... ")
            print("The price of this Shirts is : $67,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Dell_Laptop == 3 :
            print("You choose : Dell G7 Intel Core i9 10th Gen 10885H Laptop !... ")
            print("The price of this Shirts is : $2,08,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Dell_Laptop == 4 :
            print("You choose : Dell Inspiron AMD Ryzen 3 Quad Core 5th Gen 3535 Laptop !... ")
            print("The price of this Shirts is : $37,999 !...")
            print("That item is successfully added in the card !...")
        elif user_input_for_Dell_Laptop == 5 :
            print("You choose : Dell Corei5 ( 7th Gen ) Laptop !... ")
            print("The price of this Shirts is : $24,999 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ------------------------------------------------------  HP   ---------------------------------------------------------



    def HP_Laptop (self) :
        user_input_for_HP_Laptop = int(input("""\n
        Choose Laptop :
            1. HP Intel Core i7  13th Gen 13620H
                features :  ( 16 GB RAM | 512 GB SSD / Window 11 Home --> Smooth Gaming and Video Editing )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.65 Kg --> Light Weight And Easy to Carry ) \n

            2. HP OMEN Intel Core i7 14th Gen 14650HX
                features :  ( 24 GB RAM | 1 TB SSD / Window 11 Home --> Smooth Gaming and Video Editing )
                            ( 16 inch | 2K Display | 120 Hz )
                            ( NVIDIA GeForce RTX )
                            ( 2.43 Kg ) \n
            
            3. HP G7 Intel Core i5 10th Gen 10885H 
                features :  ( 16 GB RAM | 1 TB SSD / Window 10 Home --> Smooth Gaming and Video Editing )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( NVIDIA GeForce RTX )
                            ( 2.56 Kg --> Light Weight And Easy to Carry ) \n

            4. HP Pavilion Eyesafe Intel Core i9 12th Gen 1260P
                features :  ( 16 GB RAM | 1 TB SSD / Window 11 Home )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.75 Kg --> Light Weight And Easy to Carry ) \n

            5. HP Intel Core i5 11th Gen 1155G7  
                features :  ( 8 GB RAM | 512 GB SSD / Window 11 Home )
                            ( 15.9 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.69 Kg --> Light Weight And Easy to Carry ) \n
    
        \nEnter your choice which Laptop do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_HP_Laptop == 1 :
            print("You choose : HP Intel Core i7  13th Gen 13620H Laptop !... ")
            print("The price of this Shirts is : $66,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_HP_Laptop == 2 :
            print("You choose : HP OMEN Intel Core i7 14th Gen 14650HX Laptop !... ")
            print("The price of this Shirts is : $1,29,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_HP_Laptop == 3 :
            print("You choose : HP G7 Intel Core i9 10th Gen 10885H Laptop !... ")
            print("The price of this Shirts is : $2,08,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_HP_Laptop == 4 :
            print("You choose : HP Pavilion Eyesafe Intel Core i7 12th Gen 1260P Laptop !... ")
            print("The price of this Shirts is : $37,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_HP_Laptop == 5 :
            print("You choose : HP Intel Core i5 11th Gen 1155G7 Laptop !... ")
            print("The price of this Shirts is : $29,999 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ------------------------------------------------------  Lenovo   ---------------------------------------------------------



    def Lenovo_Laptop (self) :
        user_input_for_Lenovo_Laptop = int(input("""\n
        Choose Laptop :
            1. Lenovo V 14 (2025) Intel Core i3 13th Gen 1315U 
                features :  ( 16 GB RAM | 512 GB SSD / Window 11 Home --> Smooth Gaming and Video Editing )
                            ( 14 inch | Full HD Display )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.4 Kg --> Light Weight And Easy to Carry ) \n

            2. Lenovo IdeaPad Slim 3 Backlit Intel Core i5 12th Gen 12450H
                features :  ( 16 GB RAM | 512 GB SSD / Window 11 Home --> Smooth Gaming and Video Editing )
                            ( 15.6 inch | Full HD Display )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.4 Kg --> Light Weight And Easy to Carry ) \n
            
            3. Lenovo V 14 (2025) Intel Core i7 11th Gen 1255U
                features :  ( 24 GB RAM | 512 GB SSD / Window 11 Home )
                            ( 14 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.5 Kg --> Light Weight And Easy to Carry ) \n

            4. Lenovo Legion 9 Intel Core i9 14th Gen 14900
                features :  ( 24 GB RAM | 512 GB SSD / Window 11 Home )
                            ( 14 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.5 Kg --> Light Weight And Easy to Carry ) \n

            5. Lenovo IdeaPad Slim 3 Backlit Intel Core i5 12th Gen 12450H   
                features :  ( 16 GB RAM | 512 GB SSD / Window 11 Home )
                            ( 15.6 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.62 Kg --> Light Weight And Easy to Carry ) \n
    
        \nEnter your choice which Laptop do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Lenovo_Laptop == 1 :
            print("You choose : Lenovo V 14 (2025) Intel Core i3 13th Gen 1315U  Laptop !... ")
            print("The price of this Shirts is : $35,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lenovo_Laptop == 2 :
            print("You choose : Lenovo IdeaPad Slim 3 Backlit Intel Core i5 12th Gen 12450H Laptop !... ")
            print("The price of this Shirts is : $47,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lenovo_Laptop == 3 :
            print("You choose : Lenovo V 14 (2025) Intel Core i7 11th Gen 1255U Laptop !... ")
            print("The price of this Shirts is : $60,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lenovo_Laptop == 4 :
            print("You choose : Lenovo Legion 9 Intel Core i9 14th Gen 14900 Laptop !... ")
            print("The price of this Shirts is : $4,88,999 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lenovo_Laptop == 5 :
            print("You choose : Lenovo IdeaPad Slim 3 Backlit Intel Core i5 12th Gen 12450H Laptop !... ")
            print("The price of this Shirts is : $50,999 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ------------------------------------------------------  Apple   ---------------------------------------------------------



    def Apple_Laptop (self) :
        user_input_for_Apple_Laptop = int(input("""\n
        Choose Laptop :
            1. Apple MacBook AIR M2 MC7X4HN/A 
                features :  ( 16 GB RAM | 256 GB SSD )
                            ( 13.6 inch | Full HD Display )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.24 Kg --> Light Weight And Easy to Carry ) \n

            2. Apple Macook Air M4  MW0Y3HN / AmacOS Sequoia
                features :  ( 16 GB RAM | 256 GB SSD )
                            ( 15.6 inch | Liquid Retina Display | 60 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.24 Kg --> Light Weight And Easy to Carry ) \n
            
            3. Apple MacBook Pro M3 MTL83HN/A
                features :  ( 8 GB RAM | 1 TB SSD )
                            ( 14 inch | Liquid Retina XDR Display | 60 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.55 Kg --> Light Weight And Easy to Carry ) \n

            4. Apple M5 MDE34HN/A 
                features :  ( 24 GB RAM | 1 TB SSD )
                            ( 14 inch | Full HD Display | 120 Hz , Space Black )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.55 Kg --> Light Weight And Easy to Carry ) \n

            5. Apple MacBook Air Intel Core i5 5th Gen MQD32HN/A   
                features :  ( 8 GB RAM | 128 GB SSD ) 
                            ( 13.3 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.35 Kg --> Light Weight And Easy to Carry ) \n
    
        \nEnter your choice which Laptop do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Apple_Laptop == 1 :
            print("You choose : Apple MacBook AIR M2 MC7X4HN/A Laptop !... ")
            print("The price of this Shirts is : $82,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Apple_Laptop == 2 :
            print("You choose : Apple Macook Air M4 MW0Y3HN / AmacOS Sequoia Laptop !... ")
            print("The price of this Shirts is : $94,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Apple_Laptop == 3 :
            print("You choose : Apple MacBook Pro M3 MTL83HN/A Laptop !... ")
            print("The price of this Shirts is : $1,58,799 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Apple_Laptop == 4 :
            print("You choose : Apple M5 MDE34HN/A  Laptop !... ")
            print("The price of this Shirts is : $2,09,900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Apple_Laptop == 5 :
            print("You choose : Apple MacBook Air Intel Core i5 5th Gen MQD32HN/A Laptop !... ")
            print("The price of this Shirts is : $72,199 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ------------------------------------------------------  Asus   ---------------------------------------------------------



    def Asus_Laptop (self) :
        user_input_for_Asus_Laptop = int(input("""\n
        Choose Laptop :
            1. ASUS Vivobook 15 , with Backlit Keyboard , Intel Core i3 Gen 1315U X1504VA-NJ2325WS 
                features :  ( 16 GB RAM | 512 GB SSD / Window 11 Home )
                            ( 13.6 inch | Full HD Display )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.24 Kg --> Light Weight And Easy to Carry ) \n

            2. ASUS Vivobook 14 Intel Core i5 11th Gen 1135G7 X1400EA-EK543WS
                features :  ( 16 GB RAM | 512 GB SSD , Window 11 Home )
                            ( 14 inch | Liquid Retina Display | 60 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.60 Kg --> Light Weight And Easy to Carry ) \n
            
            3. ASUS Vivobook S14 (2025) with Office 2024 + M365 Intel Core i7 13th Gen 13620H 
                features :  ( 16 GB RAM | 512 GB SSD , Window 11 Home )
                            ( 14 inch | Liquid Retina XDR Display | 60 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.39 Kg --> Light Weight And Easy to Carry ) \n

            4. ASUS Zenbook 14X OLED Space Edition Touchscreen Intel H-Series Intel Core i9 12th Gen 12900H UX5401ZAS-KN901WS
                features :  ( 32 GB RAM | 1 TB SSD , Window 11 Home )
                            ( 14 inch | Full HD Display | 120 Hz , Space Black )
                            ( Intel Integrated --> Efficient grafics )
                            ( 1.55 Kg --> Light Weight And Easy to Carry ) \n

            5. ASUS ROG Strix G16 Intel Core i9 14th Gen 14900HX G614JIR-N4062WS Gaming Laptop   
                features :  ( 16 GB RAM | 1 GTB SSD , Window 11 Home ) 
                            ( Graphics / NVIDIA GetForce RTX 4070 )
                            ( 16 inch | Full HD Display | 120 Hz )
                            ( Intel Integrated --> Efficient grafics )
                            ( 2.5 Kg ) \n
    
        \nEnter your choice which Laptop do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Asus_Laptop == 1 :
            print("You choose : ASUS Vivobook 15 , with Backlit Keyboard , Intel Core i3 Gen 1315U X1504VA-NJ2325WS Laptop !... ")
            print("The price of this Shirts is : $38,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Asus_Laptop == 2 :
            print("You choose : ASUS Vivobook 14 Intel Core i5 11th Gen 1135G7 X1400EA-EK543WS Laptop !... ")
            print("The price of this Shirts is : $39,890 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Asus_Laptop == 3 :
            print("You choose : ASUS Vivobook S14 (2025) with Office 2024 + M365 Intel Core i7 13th Gen 13620H  Laptop !... ")
            print("The price of this Shirts is : $68,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Asus_Laptop == 4 :
            print("You choose : ASUSZenbook 14X OLED Space Edition Touchscreen Intel H-Series Intel Core 19 12th Gen 12900H UX5401ZAS-KN901WS Laptop !... ")
            print("The price of this Shirts is : $1,39,990 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Asus_Laptop == 5 :
            print("You choose : ASUS ROG Strix G16 Intel Core i9 14th Gen 14900HX G614JIR-N4062WS Gaming Laptop Laptop !... ")
            print("The price of this Shirts is : $2,00,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")


#    --------------------------------------------------------------------------------------------------------------------------
#                                                       Call of Laptop

    def Laptop_Brand (self) :
        user_input = int(input("""\n
        Choose a Fashion brand:
            1. Dell
            2. HP
            3. Lenovo
            4. Apple
            5. Asus
            6. Exit 
        \nEnter your choice which brand do you like : """))

        print("\nNice Dude !...")


        if user_input == 1 :
            self.Dell_Laptop()
            self.Laptop_Brand()
        elif user_input == 2 :
            self.HP_Laptop()
            self.Laptop_Brand()
        elif user_input == 3 :
            self.Lenovo_Laptop()
            self.Laptop_Brand()
        elif user_input == 4 :
            self.Apple_Laptop()
            self.Laptop_Brand()
        elif user_input == 5 :
            self.Asus_Laptop()
            self.Laptop_Brand()
        elif user_input == 5 :
            self.menu()
        else :
            print("Please , enter the valid input !...")




#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#                                                     New Class




class Vehicle(Laptop) :

    def __init__ (self) :
        self.Vehicle_Type()



# ----------------------------------------------------  Royal Enfield   -------------------------------------------------------



    def Royal_Enfield (self) :
        user_input_for_Royal_Enfeld = int(input("""\n
        Choose model :
            1. Classic 350
                features :  Engine : 349 cc single-cylinder , air/oil-cooled (RE J-platform) 
                            Power / Torque : 20.2 bhp , 27 Nm (manufacturer/market variants may differ) 
                            Weight / Tank :  195 kg kerb ; fuel tank = 13L
                            Brakes / Safety : Forn disc , rear drum (some variants) , Single-channel ABS / variant-dependent 
                            Positioning :  Classic/cruiser styling with retro looks , spoked wheels (depending on variants) and relaxed ergonomics !...  \n

            2. Meteor 350
                features :  Engine : 349 cc single-cylinder , air/oil-cooled (RE 350 platform)
                            Power / Torque : 20-21 bhp and Torque in the high - 20s Nm (varies slightly by tune/variant)
                            Weight / Tank : 191-195 kg; tank -15L (model/variant dependent)
                            Key features : Cruiser ergonomics , Tripper / navigation mount (on some trims) , updated 2025 colour/options and accessory kits !... \n
            
            3. Interceptor 650 
                features :  Engine : 648 cc parallel-twin , air/oil cooked 
                            Power / Torque : 47 bhp and 52 Nm 
                            Weight / Tank : 211 kg ; fuel tank = 13.7L
                            Brakes / Safety : Dual disc with ABS ; Classic raodster ergonomics , twin-exhaudst , retro styling !...  \n

            4. Continental GT 650
                features :  Engine : 648 cc parallel-twin , air/oil cooked 
                            Power / Torque : 47 bhp and 52 Nm (factory quoted for the 650 twins)  
                            Weight / Tank : 211 kg ; fuel tank = 12.5L 
                            Positioning : Cafe - racer styling (clip-on bars , rear-set footpegs) , tuned for spporty mid-range feel \n

            5. Himalayan 450
                features :  Engine : 452 cc , liquid-cooled single (approx. 451.6 cc)
                            Power / Torque : 39-40 PS and 40Nm torque (manufacturer-quoted figures)
                            Weight / Tank : 196 kg kerb ; fuel tank = 17L  
                            Key features : Adventure-touring focus-longer travel suspension , higher ground clearance , rider-oriented ergonomics and off-road capability !... \n
    
        \nEnter your choice which model do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Royal_Enfeld == 1 :
            print("You choose : Classic 350 !... ")
            print("The price of this model is : $1,81,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Royal_Enfeld == 2 :
            print("You choose : Meteor 350 !... ")
            print("The price of this Shirts is : $1,91,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Royal_Enfeld == 3 :
            print("You choose : Interceptor 650 !... ")
            print("The price of this Shirts is : $3,32,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Royal_Enfeld == 4 :
            print("You choose : Himalayan 450 !... ")
            print("The price of this Shirts is : $3,50,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Royal_Enfeld == 5 :
            print("You choose : Continental GT 650 !... ")
            print("The price of this Shirts is : $3,05,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  TVS  ---------------------------------------------------------



    def TVS_motor (self) :
        user_input_for_TVS_motor = int(input("""\n
        Choose model :
            1. TVS Sport BS6
                features :  Engine : 109.7 cc single-cylinder , 4-stroke , fuel-injection , air/oil-cooled displacement
                            Power / Torque : 8.7 Nm , 110 kg kerb
                            Brakes / Safety : Drum front (130 mm) and Drum rear (110 mm) on that model 
                            Positioning :  Entry - level commuter bike aimed at very economical transport !...  \n

            2. TVS Ntorq 150
                features :  Engine : 149 cc Drived from the 125 cc unit 
                            Power / Torque : 12.7 bhp , 14.2 Nm
                            Weight / Tank : While full weight info is not shown that article 
                            Positioning : A Performance-orented scooter (rather than basic commuting) aimed at the buyers wanting more zip !... \n
            
            3. TVS RT-XD4 300
                features :  Engine : 299.1 cc single-cylinder , liquid - cooled 
                            Power / Torque : 35 PS , 28.5 Nm 
                            Brakes / Safety : A "premium" performance plateforme aimed at bigger bikes advance featuress , higher segment !...  \n

            4. TVS Raider 125
                features :  Engine : 124.8 cc , Air + Oil cooled , single - cylinder , 3 valves 
                            Power / Torque : 8.37 kW , 11.2 Nm  
                            Weight / Tank : 211 kg ; fuel tank = 12.5L
                            Brakes / Safety : 240 mm Disc Front , Rear Drum 130 mm or Disc 200 mm 
                            Positioning : This is a very spoty co commuter motorcycle - aimed at rider wanting higher performance than basic commuter bike , but still manageable and economical !... \n

            5. TVS Aparche RTR 160
                features :  Engine : 159.7 cc single - cylinder , SI , 4-stroke , fuel inject Oil cooked with "Ram Air Assist"
                            Power / Torque : 17.55 PS , 14.73 Nm
                            Brakes / Safety : 270 mm Disc Front , Rear Drum 130 mm or Disc 200 mm
                            Weight / Tank : 178 kg ; fuel tank = 12.5L  
                            Key features : A Performance-orented sport bike in the 160 cc class . It target to the riders !... \n
    
        \nEnter your choice which model do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_TVS_motor == 1 :
            print("You choose : TVS Sport BS6 !... ")
            print("The price of this model is : $81,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_TVS_motor == 2 :
            print("You choose : TVS Ntorq 150 !... ")
            print("The price of this Shirts is : $59,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_TVS_motor == 3 :
            print("You choose : TVS RT-XD4 300 !... ")
            print("The price of this Shirts is : $78,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_TVS_motor == 4 :
            print("You choose : TVS Raider 125 !... ")
            print("The price of this Shirts is : $77,500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_TVS_motor == 5 :
            print("You choose : TVS Aparche RTR 160 !... ")
            print("The price of this Shirts is : $1,34,320 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Bajaj  ---------------------------------------------------------



    def Bajaj_motor (self) :
        user_input_for_Bajaj_motor = int(input("""\n
        Choose model :
            1. Bajaj Pulsar NS125
                features :  Engine : 124.4 cc , air - cooled , single - cylinder
                            Power / Torque : 12 PS , 11 Nm 
                            Weight / Tank : 144 kg ; Fuel tank 12 L
                            Brakes / Safety : Front : 240 mm disc ; Rear : 130 mm drum , Single - channel ABS 
                            Positioning :  Entry - level sport - commuter in the Pulsar "NS" !...  \n

            2. Bajaj Pulsar 150
                features :  Engine : 149 cc , air - cooled , single - cylinder 
                            Power / Torque : 12.7 bhp , 14.2 Nm
                            Weight / Tank : 144 kg ; Fuel tank 12 L
                            Brakes / Safety : Front : 260 mm disc ; Rear : 130 mm drum , Single - channel ABS 
                            Positioning : Popular everyday sport - commuter bike for riders wanting more than basic commuter !... \n
            
            3. Bajaj Avenger Street 160
                features :  Engine : 160 cc , air - cooled , single - cylinder , twin - sprak DTS-i 
                            Power / Torque : 15 bhp , 13.7 Nm
                            Weight / Tank : 156 kg ; Fuel tank 13 L
                            Brakes / Safety : Front : 280 mm disc ; Rear : 130 mm drum , Single - channel ABS 
                            Positioning : Cruiser - style bike -- comfortable , long - leg ride , designed for urban + highway ease !...  \n

            4. Bajaj Pulsar N160
                features :  Engine : 164.82 cc , oil - cooled , single - cylinder 
                            Power / Torque : 16 bhp , 14.65 Nm
                            Weight / Tank : Fuel tank 14 L
                            Brakes / Safety : Front : 300 mm disc ; Rear : 230 mm drum , Single - channel ABS 
                            Positioning : uprated sporty commuter with better features ( ABS , disc , brakes ) !... \n

            5. Bajaj Dominar 400
                features :  Engine : 373.3 cc , liquid - cooled , single - cylinder 
                            Power / Torque : 39.4 bhp , 35 Nm
                            Weight / Tank : 193 kg ; Fuel tank 13 L
                            Brakes / Safety : Front : 300 mm disc ; Rear : 230 mm drum , Single - channel ABS 
                            Positioning : Premium sports / touring bike in bajaj lineup , for riders wanting more power & highway capability !... \n
    
        \nEnter your choice which model do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Bajaj_motor == 1 :
            print("You choose : Bajaj Pulsar NS125 !... ")
            print("The price of this model is : $92,182 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Bajaj_motor == 2 :
            print("You choose : Bajaj Pulsar 150 !... ")
            print("The price of this Shirts is : $95,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Bajaj_motor == 3 :
            print("You choose : Bajaj Avenger Street 160 !... ")
            print("The price of this Shirts is : $1,30,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Bajaj_motor == 4 :
            print("You choose : Bajaj Pulsar N160 !... ")
            print("The price of this Shirts is : $1,20,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Bajaj_motor == 5 :
            print("You choose : Bajaj Dominar 400 !... ")
            print("The price of this Shirts is : $2,30,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Suzuki  ---------------------------------------------------------



    def Suzuki_motor (self) :
        user_input_for_Suzuki_motor = int(input("""\n
        Choose model :
            1. Suzuki Gixxer (155 cc)
                features :  Engine : 155 cc , single - cylinder , fuel injected
                            Power / Torque : 13.4 PS , 13.8 Nm 
                            Weight / Tank : 141 kg ; Fuel tank 12 L
                            Brakes / Safety : Disc Front & Rear Single - channel ABS 
                            Positioning :  Entry sport - commuter in the Pulsar "NS" !...  \n

            2. Suzuki Gixxer SF (155 cc)
                features :  Engine : 155 cc , air - cooled , single - cylinder 
                            Power / Torque : 13.4 bhp , 13.8 Nm
                            Weight / Tank : 148 kg ; Fuel tank 12 L
                            Brakes / Safety : Disc Front & Rear ABS 
                            Positioning : sport - faired version of the commuter !... \n
            
            3. Suzuki Gixxer 250 (249 cc)
                features :  Engine : 249 cc , oil - cooled , single - cylinder
                            Power / Torque : 26.1 bhp , 22.2 Nm
                            Weight / Tank : 156 kg ; Fuel tank 12 L
                            Brakes / Safety : Disc brakes ; Dual - channel ABS 
                            Positioning : Mid - quater liter segment , more performance than commuter !...  \n

            4. Suzuki V-strom SX
                features :  Engine : 249 cc , oil - cooled , single - cylinder 
                            Power / Torque : 26.1 bhp , 22.2 Nm
                            Weight / Tank : 167 kg ; Fuel tank 12 L
                            Brakes / Safety : Disc Front & Rear Dual - channel ABS 
                            Positioning : Entry adventure - tourer segment  !... \n

            5. Suzuki Hayabusa (1340 cc superbike)
                features :  Engine : 1340 cc , liquid - cooled , inline - 4 
                            Power / Torque : 190 bhp , 150 Nm
                            Weight / Tank : 266 kg ; Fuel tank 20 L
                            Brakes / Safety : Dual disc front disc rear ; dual - channel ABS + advanced rider ads  
                            Positioning : Iconic super bike !... \n
    
        \nEnter your choice which model do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Suzuki_motor == 1 :
            print("You choose : Suzuki Gixxer (155 cc) !... ")
            print("The price of this model is : $1,31,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Suzuki_motor == 2 :
            print("You choose : Suzuki Gixxer SF (155 cc) !... ")
            print("The price of this Shirts is : $1,40,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Suzuki_motor == 3 :
            print("You choose : Suzuki Gixxer 250 (249 cc) !... ")
            print("The price of this Shirts is : $1,83,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Suzuki_motor == 4 :
            print("You choose : Suzuki V-strom SX !... ")
            print("The price of this Shirts is : $2,40,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Suzuki_motor == 5 :
            print("You choose : Suzuki Hayabusa (1340 cc superbike) !... ")
            print("The price of this Shirts is : $18,00,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Yamaha  ---------------------------------------------------------



    def Yamaha_motor (self) :
        user_input_for_Yamaha_motor = int(input("""\n
        Choose model :
            1. Yamaha R15 V4
                features :  Engine : 155 cc , liquid - cooled , single - cylinder with VVA
                            Power / Torque : 18.1 PS , 14.2 Nm 
                            Weight / Tank : 141 kg ; Fuel tank 11 L
                            Brakes / Safety : Front & Rear Disc ; Dual - channel ABS ; traction control & quick shifter in variant 
                            Positioning : Premium 155 cc sport bike !...  \n

            2. Yamaha MT - 15 V2
                features :  Engine : 155 cc , liquid - cooled , single - cylinder 
                            Power / Torque : 18.4 bhp , 14.1 Nm
                            Weight / Tank : 164 kg ; Fuel tank 10 L
                            Brakes / Safety : Disc brakes ; ABS (Single/dual depending on varient) 
                            Positioning : Street - naked sporty segment !... \n
            
            3. Yamaha FZ-X
                features :  Engine : 149 cc , air - cooled , single - cylinder , twin - sprak DTS-i 
                            Power / Torque : 12.2 bhp , 13.3 Nm
                            Weight / Tank : 139 kg ; Fuel tank 10 L
                            Brakes / Safety : Disc brakes (front) with ABS ; upright neo - retro styling 
                            Positioning : Premium commuter / neo - retro nike in 150 cc class !...  \n

            4. Yamaha FZ S Hybrid
                features :  Engine : 149 cc , oil - cooled , single - cylinder plus hybrid assist  (Smart Motor Generator & Stop - start) in Hybrid variant
                            Power / Torque : 12.4 bhp , 13.3 Nm
                            Weight / Tank : Fuel tank 13 L
                            Brakes / Safety : Disc front brake + Single - channel ABS ; hybrid tech adds smoother start/stop
                            Positioning : Premium commuter 150 cc class with hybrid tech !... \n

            5. Yamaha Aerox 155 (Scooter)
                features :  Engine : 1555 cc , liquid - cooled , single - cylinder , 4 - valve , VVA
                            Power / Torque : 14.75 bhp , 13.9 Nm
                            Weight / Tank : 126 kg ; Fuel tank 5.5 L
                            Brakes / Safety : Front Disc : 230 mm Single - channel ABS ; drum rear ; big under - seat storage 
                            Positioning : Maxi - scooter segment (sporty scooter) with 155 cc power !... \n
    
        \nEnter your choice which model do you like : """)) 

        print("\nNice Dude !...")


        if user_input_for_Yamaha_motor == 1 :
            print("You choose : Yamaha R15 V4 !... ")
            print("The price of this model is : $2,00,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Yamaha_motor == 2 :
            print("You choose : Yamaha MT - 15 V2 !... ")
            print("The price of this Shirts is : $1,80,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Yamaha_motor == 3 :
            print("You choose : Yamaha FZ-X !... ")
            print("The price of this Shirts is : $1,40,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Yamaha_motor == 4 :
            print("You choose : Yamaha FZ S Hybrid !... ")
            print("The price of this Shirts is : $1,55,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Yamaha_motor == 5 :
            print("You choose : Yamaha Aerox 155 (Scooter) !... ")
            print("The price of this Shirts is : $1,34,320 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  KTM  ---------------------------------------------------------



    def KTM (self) :
        user_input_for_KTM = int(input("""\n
        Choose model :
            1. KTM 250 Duke
                features :  Engine : 249.07 cc , liquid - cooled , single - cylinder
                            Power / Torque : 31 PS , 25 Nm 
                            Weight / Tank : 162.8 kg ; Fuel tank 15 L
                            Brakes / Safety : Front : 320 mm disc ; Rear : 240 mm disc , features like Supermoto ABS , ride - by - wire , quickshifter + 
                            Positioning : Naked sport bike in -520 cc class !...  \n

            2. KTM 250 Adventures
                features :  Engine : 249 cc , liquid DOHC - cooled , single - cylinder 
                            Power / Torque : 31 bhp , 25 Nm
                            Weight / Tank : 160 kg ; Fuel tank 14 L
                            Brakes / Safety : BYBRE 320 mm / 230 mm discs ; dual - channel ABS with off - road mode 
                            Positioning : Entry - level Advanture / touring bike !... \n
            
            3. KTM 200 Duke
                features :  Engine : 199.5 cc , air - cooled , single - cylinder , twin - sprak DTS-i 
                            Power / Torque : 26 bhp , 20 Nm
                            Weight / Tank : 156 kg ; Fuel tank 13.5 L
                            Brakes / Safety : Disc 300 mm front / 230 mm rear ; ABS 
                            Positioning : Street Naked spoty 200 cc class !...  \n

            4. KTM RC 390
                features :  Engine : 373.27 cc , oil - cooled , single - cylinder 
                            Power / Torque : 43 bhp , 37 Nm
                            Weight / Tank : Fuel tank 13.7 L
                            Brakes / Safety :LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : Fully - faired sports bike !... \n

            5. KTM 390 Duke
                features :  Engine : 398.63 cc , liquid - cooled , single - cylinder 
                            Power / Torque : 37.34 bhp , 39 Nm
                            Weight / Tank : 168.3 kg ; Fuel tank 15 L
                            Brakes / Safety : Digital cluster , traction control (MTC) , ABS (cornering ABS/supermoto ABS in newer ones)
                            Positioning : Premium naked sports in 400 cc class !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_KTM == 1 :
            print("You choose : KTM 250 Duke !... ")
            print("The price of this model is : $2,50,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_KTM == 2 :
            print("You choose : KTM 250 Adventures !... ")
            print("The price of this Shirts is : $2,60,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_KTM == 3 :
            print("You choose : KTM 200 Duke !... ")
            print("The price of this Shirts is : $2,00,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_KTM == 4 :
            print("You choose : KTM RC 390 !... ")
            print("The price of this Shirts is : $3,25,000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_KTM == 5 :
            print("You choose : KTM 390 Duke !... ")
            print("The price of this Shirts is : $3,00,000 !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------  BMW  -----------------------------------------------------------------



    def BMW (self) :
        user_input_for_BMW = int(input("""\n
        Choose model :
            1. BMW X1
                features :  Engine : 1499 cc , three - cylinder
                            Power / Torque : 134 PS , 230 Nm 
                            Weight / Tank : 1560 kg ; Fuel tank 51 L
                            Brakes / Safety : Front & rear ventilated disc brakes. Safety features : multiple airbags , traction control , ABS , etc.
                            Positioning : Entry Luxury SUV in BMW line-up premium compact SUV !...  \n

            2. BMW 2 Series Gran Coupe
                features :  Engine : 1493 cc , Three - cylinder 
                            Power / Torque : 156 bhp , 230 Nm
                            Weight / Tank : 1505 kg ; Fuel tank 49 L
                            Brakes / Safety : Brakes : Ventilated discs front & rear , Safety : Six airbags , ABS + EBD , DSC , tyre - pressure monitoring
                            Positioning : premium compact sedan / coupe alternative , sportier shape !... \n
            
            3. BMW 3 Series (Sedan)
                features :  Engine : 2998 cc , six - cylinder  
                            Power / Torque : 368.78 bhp , 500 Nm
                            Weight / Tank : 1536 kg ; Fuel tank 59 L
                            Brakes / Safety : Standard premium safety tech for the segment
                            Positioning : Mid luxury sedan , BMW's traditional performance - sedan core !...  \n

            4. BMW 5 Series (Sedan)
                features :  Engine : 373.27 cc , oil - cooled , single - cylinder 
                            Power / Torque : 43 bhp , 37 Nm
                            Weight / Tank : Fuel tank 13.7 L
                            Brakes / Safety : LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : Exclusive luxury sedan one step above 3 Series !... \n

            5. BMW X5
                features :  Engine : 2998 cc , six - cylinder  
                            Power / Torque : 368.78 bhp , 500 Nm
                            Weight / Tank : 1536 kg ; Fuel tank 59 L
                            Brakes / Safety : Standard premium safety tech for the segment
                            Positioning : Mid luxury sedan , BMW's traditional performance - sedan core !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_BMW == 1 :
            print("You choose : BMW X1 !... ")
            print("The price of this model is : $49.5 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_BMW == 2 :
            print("You choose : BMW 2 Series Gran Coupe !... ")
            print("The price of this Shirts is : $46.90 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_BMW == 3 :
            print("You choose : BMW 3 Series (Sedan) !... ")
            print("The price of this Shirts is : $72.85 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_BMW == 4 :
            print("You choose : BMW 5 Series (Sedan) !... ")
            print("The price of this Shirts is : $72.35 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_BMW == 5 :
            print("You choose : BMW X5 !... ")
            print("The price of this Shirts is : $1.3 Crore !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Mercedes  ---------------------------------------------------------



    def Mercedes (self) :
        user_input_for_Mercedes = int(input("""\n
        Choose model :
            1. Mercedes - Benz A - Class Limousine ( A200 / A200d )
                features :  Engine : 2998 cc , liquid - cooled , single - cylinder
                            Power / Torque : 163 bhp , 250 Nm 
                            Weight / Tank : 1655 kg ; Fuel tank 66 L
                            Brakes / Safety : Front & rear ventilated disc brakes. Safety features : multiple airbags , traction control , ABS , etc. 
                            Positioning : Entry - level luxury sedan !...  \n

            2. Mercedes - Benz C - Class C 200 Progressive
                features :  Engine : 2998 cc , liquid DOHC - cooled , single - cylinder 
                            Power / Torque : 201 bhp , 280 Nm
                            Weight / Tank : 1605 kg ; Fuel tank 66 L
                            Brakes / Safety : Brakes : Ventilated discs front & rear , Safety : Six airbags , ABS + EBD , DSC , tyre - pressure monitoring
                            Positioning : Mid - luxury sedan !... \n
            
            3. Mercedes - Benz GLC 200 Progressive
                features :  Engine : 2998 cc , air - cooled , single - cylinder , twin - sprak DTS-i 
                            Power / Torque : 26 bhp , 320 Nm
                            Weight / Tank : 1835 kg ; Fuel tank 66 L
                            Brakes / Safety : Standard premium safety tech for the segment 
                            Positioning : Compact luxury SUV !...  \n

            4. Mercedes - Benz E - Class LWB ( E200 / E200 d / E450 )
                features :  Engine : 2998 cc , oil - cooled , single - cylinder 
                            Power / Torque : 43 bhp , 400 Nm
                            Weight / Tank : Fuel tank 66 L
                            Brakes / Safety : LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : Premium executive luxury sedan (long-weelbase version) !... \n

            5. Mercedes - Benz S - Class 400d
                features :  Engine : 2998 cc , liquid - cooled , single - cylinder 
                            Power / Torque : 37.34 bhp , 500 Nm
                            Weight / Tank : 1655 kg ; Fuel tank 66 L
                            Brakes / Safety : Standard premium safety tech for the segment
                            Positioning : Flagship luxury sedan !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_Mercedes == 1 :
            print("You choose : Mercedes - Benz A - Class Limousine ( A200 / A200d ) !... ")
            print("The price of this model is : $40 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Mercedes == 2 :
            print("You choose : Mercedes - Benz C - Class C 200 Progressive !... ")
            print("The price of this Shirts is : $45 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Mercedes == 3 :
            print("You choose : Mercedes - Benz GLC 200 Progressive !... ")
            print("The price of this Shirts is : $62 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Mercedes == 4 :
            print("You choose : Mercedes - Benz E - Class LWB ( E200 / E200 d / E450 ) !... ")
            print("The price of this Shirts is : $78 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Mercedes == 5 :
            print("You choose : Mercedes - Benz S - Class 400d !... ")
            print("The price of this Shirts is : $2.17 Crore !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Rolls-Royce  ---------------------------------------------------------



    def Rolls_Royce (self) :
        user_input_for_Rolls_Royce = int(input("""\n
        Choose model :
            1. Rolls - Royce Phantom
                features :  Engine : 3000 cc , Three - cylinder
                            Power / Torque : 563 bhp , 63 Nm 
                            Weight / Tank : 162.8 kg ; Fuel tank 15 L
                            Brakes / Safety : Front : 320 mm disc ; Rear : 240 mm disc , features like Supermoto ABS , ride - by - wire , quickshifter + 
                            Positioning : Flagship Ultra - luxury sedan (the highest tier) !...  \n

            2. Rolls - Royce Ghost ( Series II )
                features :  Engine : 3420 cc , Three - cylinder 
                            Power / Torque : 563 bhp , 900 Nm
                            Weight / Tank : 160 kg ; Fuel tank 14 L
                            Brakes / Safety : BYBRE 320 mm / 230 mm discs ; dual - channel ABS with off - road mode 
                            Positioning : High luxury sedan , just below Phontom !... \n
            
            3. Rolls - Royce Cullinan ( Series II )
                features :  Engine : 3246 cc , Three - cylinder 
                            Power / Torque : 571 bhp , 900 Nm
                            Weight / Tank : 156 kg ; Fuel tank 13.5 L
                            Brakes / Safety : Disc 300 mm front / 230 mm rear ; ABS 
                            Positioning : Luxury SUV - the SUV offering fro Rolls - Royce !...  \n

            4. Rolls - Royce Spectre (Couple/Electric)
                features :  Engine : 3298 cc , Three - cylinder 
                            Power / Torque : 577 bhp , 900 Nm
                            Weight / Tank : Fuel tank 13.7 L
                            Brakes / Safety :LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : First full electric Rolls - Royce , Ultra - luxury grand tourer !... \n

            5. Rolls - Royce Wraith
                features :  Engine : 4390 cc , Three - cylinder 
                            Power / Torque : 591 bhp , 900 Nm
                            Weight / Tank : 168.3 kg ; Fuel tank 15 L
                            Brakes / Safety : Digital cluster , traction control (MTC) , ABS (cornering ABS/supermoto ABS in newer ones)
                            Positioning : Luxury two door coupe (less mainstream in india now) !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_Rolls_Royce == 1 :
            print("You choose : Rolls - Royce Phantom !... ")
            print("The price of this model is : $8.99 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Rolls_Royce == 2 :
            print("You choose : Rolls - Royce Ghost ( Series II ) !... ")
            print("The price of this Shirts is : $8.95 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Rolls_Royce == 3 :
            print("You choose : Rolls - Royce Cullinan ( Series II ) !... ")
            print("The price of this Shirts is : $10.50 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Rolls_Royce == 4 :
            print("You choose : Rolls - Royce Spectre (Couple/Electric) !... ")
            print("The price of this Shirts is : $7.5 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Rolls_Royce == 5 :
            print("You choose : Rolls - Royce Wraith !... ")
            print("The price of this Shirts is : $7 Crore !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Jaguar  ---------------------------------------------------------



    def Jaguar (self) :
        user_input_for_Jaguar = int(input("""\n
        Choose model :
            1. Jaguar XE
                features :  Engine : 1499 cc , three - cylinder
                            Power / Torque : 134 PS , 230 Nm 
                            Weight / Tank : 1560 kg ; Fuel tank 51 L
                            Brakes / Safety : Front & rear ventilated disc brakes. Safety features : multiple airbags , traction control , ABS , etc.
                            Positioning : Entry Luxury SUV in BMW line-up premium compact SUV !...  \n

            2. Jaguar XF
                features :  Engine : 1493 cc , Three - cylinder 
                            Power / Torque : 156 bhp , 230 Nm
                            Weight / Tank : 1505 kg ; Fuel tank 49 L
                            Brakes / Safety : Brakes : Ventilated discs front & rear , Safety : Six airbags , ABS + EBD , DSC , tyre - pressure monitoring
                            Positioning : premium compact sedan / coupe alternative , sportier shape !... \n
            
            3. Jaguar F - Pace
                features :  Engine : 2998 cc , six - cylinder  
                            Power / Torque : 368.78 bhp , 500 Nm
                            Weight / Tank : 1536 kg ; Fuel tank 59 L
                            Brakes / Safety : Standard premium safety tech for the segment
                            Positioning : Mid luxury sedan , BMW's traditional performance - sedan core !...  \n

            4. Jaguar F - Type
                features :  Engine : 373.27 cc , oil - cooled , single - cylinder 
                            Power / Torque : 43 bhp , 37 Nm
                            Weight / Tank : Fuel tank 13.7 L
                            Brakes / Safety : LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : Exclusive luxury sedan one step above 3 Series !... \n

            5. Jaguar I - Pace
                features :  Engine : 2998 cc , six - cylinder  
                            Power / Torque : 368.78 bhp , 500 Nm
                            Weight / Tank : 1536 kg ; Fuel tank 59 L
                            Brakes / Safety : Standard premium safety tech for the segment
                            Positioning : Mid luxury sedan , BMW's traditional performance - sedan core !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_Jaguar == 1 :
            print("You choose : Jaguar XE !... ")
            print("The price of this model is : $1.8 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jaguar == 2 :
            print("You choose : Jaguar XF !... ")
            print("The price of this Shirts is : $2 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jaguar == 3 :
            print("You choose : Jaguar F - Pace !... ")
            print("The price of this Shirts is : $2.3 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jaguar == 4 :
            print("You choose : Jaguar F - Type !... ")
            print("The price of this Shirts is : $2.9 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Jaguar == 5 :
            print("You choose : Jaguar I - Pace !... ")
            print("The price of this Shirts is : $3 Crore !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Lamborgini  ---------------------------------------------------------



    def Lamborgini (self) :
        user_input_for_Lamborgini = int(input("""\n
        Choose model :
            1. Lamborgini Aventador
                features :  Engine : 2998 cc , liquid - cooled , single - cylinder
                            Power / Torque : 163 bhp , 250 Nm 
                            Weight / Tank : 1655 kg ; Fuel tank 66 L
                            Brakes / Safety : Front & rear ventilated disc brakes. Safety features : multiple airbags , traction control , ABS , etc. 
                            Positioning : Entry - level luxury sedan !...  \n

            2. Lamborgini Huracan
                features :  Engine : 2998 cc , liquid DOHC - cooled , single - cylinder 
                            Power / Torque : 201 bhp , 280 Nm
                            Weight / Tank : 1605 kg ; Fuel tank 66 L
                            Brakes / Safety : Brakes : Ventilated discs front & rear , Safety : Six airbags , ABS + EBD , DSC , tyre - pressure monitoring
                            Positioning : Mid - luxury sedan !... \n
            
            3. Lamborgini Urus
                features :  Engine : 2998 cc , air - cooled , single - cylinder , twin - sprak DTS-i 
                            Power / Torque : 26 bhp , 320 Nm
                            Weight / Tank : 1835 kg ; Fuel tank 66 L
                            Brakes / Safety : Standard premium safety tech for the segment 
                            Positioning : Compact luxury SUV !...  \n

            4. Lamborgini Revuelto
                features :  Engine : 2998 cc , oil - cooled , single - cylinder 
                            Power / Torque : 43 bhp , 400 Nm
                            Weight / Tank : Fuel tank 66 L
                            Brakes / Safety : LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : Premium executive luxury sedan (long-weelbase version) !... \n

            5. Lamborgini Sian FKP 37
                features :  Engine : 2998 cc , liquid - cooled , single - cylinder 
                            Power / Torque : 37.34 bhp , 500 Nm
                            Weight / Tank : 1655 kg ; Fuel tank 66 L
                            Brakes / Safety : Standard premium safety tech for the segment
                            Positioning : Flagship luxury sedan !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_Lamborgini == 1 :
            print("You choose : Lamborgini Aventador !... ")
            print("The price of this model is : $1.17 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lamborgini == 2 :
            print("You choose : Lamborgini Huracan !... ")
            print("The price of this Shirts is : $1.37 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lamborgini == 3 :
            print("You choose : Lamborgini Urus !... ")
            print("The price of this Shirts is : $2.87 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lamborgini == 4 :
            print("You choose : Lamborgini Revuelto !... ")
            print("The price of this Shirts is : $2.45 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Lamborgini == 5 :
            print("You choose : Lamborgini Sian FKP 37 !... ")
            print("The price of this Shirts is : $2.17 Crore !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ----------------------------------------------------  Toyota  ---------------------------------------------------------



    def Toyota (self) :
        user_input_for_Toyota = int(input("""\n
        Choose model :
            1. Toyota Fortuner
                features :  Engine : 3000 cc , Three - cylinder
                            Power / Torque : 563 bhp , 63 Nm 
                            Weight / Tank : 162.8 kg ; Fuel tank 15 L
                            Brakes / Safety : Front : 320 mm disc ; Rear : 240 mm disc , features like Supermoto ABS , ride - by - wire , quickshifter + 
                            Positioning : Flagship Ultra - luxury sedan (the highest tier) !...  \n

            2. Toyota Innova Hycross
                features :  Engine : 3420 cc , Three - cylinder 
                            Power / Torque : 563 bhp , 900 Nm
                            Weight / Tank : 160 kg ; Fuel tank 14 L
                            Brakes / Safety : BYBRE 320 mm / 230 mm discs ; dual - channel ABS with off - road mode 
                            Positioning : High luxury sedan , just below Phontom !... \n
            
            3. Toyota Camry Hybrid
                features :  Engine : 3246 cc , Three - cylinder 
                            Power / Torque : 571 bhp , 900 Nm
                            Weight / Tank : 156 kg ; Fuel tank 13.5 L
                            Brakes / Safety : Disc 300 mm front / 230 mm rear ; ABS 
                            Positioning : Luxury SUV - the SUV offering fro Rolls - Royce !...  \n

            4. Toyota Glanza
                features :  Engine : 3298 cc , Three - cylinder 
                            Power / Torque : 577 bhp , 900 Nm
                            Weight / Tank : Fuel tank 13.7 L
                            Brakes / Safety :LED headlamps , traction control , dual - channeln ABS , digital instrumentation 
                            Positioning : First full electric Rolls - Royce , Ultra - luxury grand tourer !... \n

            5. Toyota Hilux
                features :  Engine : 4390 cc , Three - cylinder 
                            Power / Torque : 591 bhp , 900 Nm
                            Weight / Tank : 168.3 kg ; Fuel tank 15 L
                            Brakes / Safety : Digital cluster , traction control (MTC) , ABS (cornering ABS/supermoto ABS in newer ones)
                            Positioning : Luxury two door coupe (less mainstream in india now) !... \n
    
        \nEnter your choice which model do you like : """)) 



        if user_input_for_Toyota == 1 :
            print("You choose : Toyota Fortuner !... ")
            print("The price of this model is : $98 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Toyota == 2 :
            print("You choose : Toyota Innova Hycross !... ")
            print("The price of this Shirts is : $88.95 Lakh !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Toyota == 3 :
            print("You choose : Toyota Camry Hybrid !... ")
            print("The price of this Shirts is : $3.5 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Toyota == 4 :
            print("You choose : Toyota Glanza !... ")
            print("The price of this Shirts is : $1.5 Crore !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Toyota == 5 :
            print("You choose : Toyota Hilux !... ")
            print("The price of this Shirts is : $70 Lakh !...")
            print("That item is successfully added in the card !...")

        else :
            print("You enter the wrong input , \nPlease enter the correct input !...")



# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------



    def Vehicle_Type (self) :
        user_input = int(input("""\n
        Choose a Fashion brand:
            1. Two-Wheeler
            2. Four-Wheeler
            3. Exit
        \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")


        if user_input == 1 :
            self.Two_Wheeler_Brand()

        elif user_input == 2 :
            self.Four_Wheeler_Brand()

        elif user_input == 3 :
            self.menu()

        else :
            print("Please , enter the valid input !...")




    def Two_Wheeler_Brand (self) :
        user_input_for_Two_Wheeler_Brand = int(input("""\n
        Choose a Fashion brand:
            1. Royal Enfield
            2. TVS Motor Company
            3. Bajaj 
            4. Suzuki
            5. Yamaha
            6. KTM
            7. Exit 
        \nEnter your choice which brand do you like : """))

        print("\nNice Dude !...")


        if  user_input_for_Two_Wheeler_Brand == 1 :
            self.Royal_Enfield()
            self.Two_Wheeler_Brand()

        elif  user_input_for_Two_Wheeler_Brand == 2 :
            self.TVS_motor()
            self.Two_Wheeler_Brand()

        elif  user_input_for_Two_Wheeler_Brand == 3 :
            self.Bajaj_motor()
            self.Two_Wheeler_Brand()

        elif  user_input_for_Two_Wheeler_Brand == 4 :
            self.Suzuki_motor()
            self.Two_Wheeler_Brand()

        elif  user_input_for_Two_Wheeler_Brand == 5 :
            self.Yamaha_motor()
            self.Two_Wheeler_Brand()

        elif  user_input_for_Two_Wheeler_Brand == 6 :
            self.KTM()
            self.Two_Wheeler_Brand()

        elif  user_input_for_Two_Wheeler_Brand == 7 :
            self.Vehicle_Type()

        else :
            print("Please , enter the valid input !...")




    def Four_Wheeler_Brand (self) :
        user_input_for_Four_Wheeler_Brand = int(input("""\n
        Choose a Fashion brand:
            1. BMW
            2. Mercedes
            3. Rolls-Royce
            4. Jaguar
            5. Lamborgini
            6. Toyota
            7. Exit 
        \nEnter your choice which brand do you like : """))

        print("\nNice Dude !...")


        if user_input_for_Four_Wheeler_Brand == 1 :
            self.BMW()
            self.Four_Wheeler_Brand()

        elif user_input_for_Four_Wheeler_Brand == 2 :
            self.Mercedes()
            self.Four_Wheeler_Brand()

        elif user_input_for_Four_Wheeler_Brand == 3 :
            self.Rolls_Royce()
            self.Four_Wheeler_Brand()

        elif user_input_for_Four_Wheeler_Brand == 4 :
            self.Jaguar()
            self.Four_Wheeler_Brand()

        elif user_input_for_Four_Wheeler_Brand == 5 :
            self.Lamborgini()
            self.Four_Wheeler_Brand()

        elif user_input_for_Four_Wheeler_Brand == 6 :
            self.Toyota()
            self.Four_Wheeler_Brand()

        elif user_input_for_Four_Wheeler_Brand == 7 :
            self.Vehicle_Type()

        else :
            print("Please , enter the valid input !...")




#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#                                                     New Class




class Food(Vehicle) :

    def __init__ (self) :
        self.Food_Brand()
        self.Food_Type()



# ----------------------------------------------------  Royal Enfield   -------------------------------------------------------



    def Namkeen (self) :
        user_input_for_Namkeen = int(input("""\n
        Choose a Namkeen :
            1. Ratlam Sev
            2. Khatta Meetha Mix
            3. Chiwda
            4. Chana Dal
            5. Exit 
        \nEnter your choice which Namkeen do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Namkeen == 1 :
            print("You choose : Ratlam Sev !...")
            print("The price of this item is : $7 !...")
            print("That item is successfully added in the card !...")
            self.Namkeen()

        elif user_input_for_Namkeen == 2 :
            print("You choose : Ratlam Sev !...")
            print("The price of this item is : $7 !...")
            print("That item is successfully added in the card !...")
            self.Namkeen()

        elif user_input_for_Namkeen == 3 :
            print("You choose : Ratlam Sev !...")
            print("The price of this item is : $7 !...")
            print("That item is successfully added in the card !...")
            self.Namkeen()

        elif user_input_for_Namkeen == 4 :
            print("You choose : Ratlam Sev !...")
            print("The price of this item is : $7 !...")
            print("That item is successfully added in the card !...")
            self.Namkeen()

        elif user_input_for_Namkeen == 5 :
            self.Food_Type()

        else :
            print("Please enter the valid number !...")




    def Bhujia (self) :
        user_input_for_Bhujia = int(input("""\n
        Choose a Bhujia :
            1. Aloo Bhujia
            2. Masala Bhujia
            3. Chatapata Bhujia
            4. Bikneri Bhujai
            5. Exit 
        \nEnter your choice which Bhujia do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Bhujia == 1 :
            print("You choose : Aloo Bhujia !...")
            print("The price of this item is : $10 !...")
            print("That item is successfully added in the card !...")
            self.Bhujia()

        elif user_input_for_Bhujia == 2 :
            print("You choose : Ratlam Sev !...")
            print("The price of this item is : $20 !...")
            print("That item is successfully added in the card !...")
            self.Bhujia()

        elif user_input_for_Bhujia == 3 :
            print("You choose : Chatapata Bhujia !...")
            print("The price of this item is : $15 !...")
            print("That item is successfully added in the card !...")
            self.Bhujia()

        elif user_input_for_Bhujia == 4 :
            print("You choose : Bikneri Bhujai !...")
            print("The price of this item is : $5 !...")
            print("That item is successfully added in the card !...")
            self.Bhujia()

        elif user_input_for_Bhujia == 5 :
            self.Food_Type()

        else :
            print("Please enter the valid number !...")




    def Soan_papdi (self) :
        user_input_for_Soan_papdi = int(input("""\n
        Choose a Soan_papdi :
            1. Maida Soan_papdi
            2. Sooji Soan_papdi
            3. Salt Soan_papdi
            4.Salt Soan_papdi
            5. Exit 
        \nEnter your choice which Soan_papdi do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Soan_papdi == 1 :
            print("You choose : Maida Soan_papdi !...")
            print("The price of this item is : $60 !...")
            print("That item is successfully added in the card !...")
            self.Soan_papdi()

        elif user_input_for_Soan_papdi == 2 :
            print("You choose : Sooji Soan_papdi !...")
            print("The price of this item is : $30 !...")
            print("That item is successfully added in the card !...")
            self.Soan_papdi()

        elif user_input_for_Soan_papdi == 3 :
            print("You choose : Salt Soan_papdi !...")
            print("The price of this item is : $50 !...")
            print("That item is successfully added in the card !...")
            self.Soan_papdi()

        elif user_input_for_Soan_papdi == 4 :
            print("You choose : Salt Soan_papdi !...")
            print("The price of this item is : $70 !...")
            print("That item is successfully added in the card !...")
            self.Soan_papdi()

        elif user_input_for_Soan_papdi == 5 :
            self.Food_Type()

        else :
            print("Please enter the valid number !...")




    def Sweets (self) :
        user_input_for_Sweets = int(input("""\n
        Choose a Sweets :
            1. Rasagulla
            2. Gulab Jamun
            3. Peda
            4. Chikki
            5. Exit 
        \nEnter your choice which Sweets do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Sweets == 1 :
            print("You choose : Rasagulla !...")
            print("The price of this item is : $100 !...")
            print("That item is successfully added in the card !...")
            self.Sweets()

        elif user_input_for_Sweets == 2 :
            print("You choose : Gulab Jamun !...")
            print("The price of this item is : $80 !...")
            print("That item is successfully added in the card !...")
            self.Sweets()

        elif user_input_for_Sweets == 3 :
            print("You choose : Peda !...")
            print("The price of this item is : $30 !...")
            print("That item is successfully added in the card !...")
            self.Sweets()

        elif user_input_for_Sweets == 4 :
            print("You choose : Chikki !...")
            print("The price of this item is : $10 !...")
            print("That item is successfully added in the card !...")
            self.Sweets()

        elif user_input_for_Sweets == 5 :
            self.Food_Type()

        else :
            print("Please enter the valid number !...")




    def Biscuits (self) :
        user_input_for_Biscuits = int(input("""\n
        Choose a Namkeen :
            1. Parle Biscuits
            2. Marigold Biscuits
            3. KrackJack Biscuits
            4. Moneco Biscuits
            5. Exit 
        \nEnter your choice which Biscuits do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Biscuits == 1 :
            print("You choose : Parle Biscuits !...")
            print("The price of this item is : $10 !...")
            print("That item is successfully added in the card !...")
            self.Biscuits()

        elif user_input_for_Biscuits == 2 :
            print("You choose : Marigold Biscuits !...")
            print("The price of this item is : $10 !...")
            print("That item is successfully added in the card !...")
            self.Biscuits()

        elif user_input_for_Biscuits == 3 :
            print("You choose : KrackJack Biscuits !...")
            print("The price of this item is : $10 !...")
            print("That item is successfully added in the card !...")
            self.Biscuits()

        elif user_input_for_Biscuits == 4 :
            print("You choose : Moneco Biscuits !...")
            print("The price of this item is : $10 !...")
            print("That item is successfully added in the card !...")
            self.Biscuits()

        elif user_input_for_Biscuits == 5 :
            self.Food_Type()

        else :
            print("Please enter the valid number !...")




    def Chips (self) :
        user_input_for_Chip = int(input("""\n
        Choose a Namkeen :
            1. Classic Salted Chips
            2. Masala Chips 
            3. Tomato Chips
            4. Chilli Chips
            5. Exit 
        \nEnter your choice which Chips do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Chip == 1 :
            print("You choose : Classic Salted Chips !...")
            print("The price of this item is : $20 !...")
            print("That item is successfully added in the card !...")
            self.Chips()

        elif user_input_for_Chip == 2 :
            print("You choose : Masala Chip !...")
            print("The price of this item is : $20 !...")
            print("That item is successfully added in the card !...")
            self.Chips()

        elif user_input_for_Chip == 3 :
            print("You choose : Tomato Chips !...")
            print("The price of this item is : $20 !...")
            print("That item is successfully added in the card !...")
            self.Chips()

        elif user_input_for_Chip == 4 :
            print("You choose : Chilli Chips !...")
            print("The price of this item is : $20 !...")
            print("That item is successfully added in the card !...")
            self.Chips()

        elif user_input_for_Chip == 5 :
            self.Food_Type()

        else :
            print("Please enter the valid number !...")













    def Food_Brand (self) :
        user_input_for_Food_Brand = int(input("""\n
        Choose a Food brand :
            1. Haldiram's
            2. Patanjali
            3. Balaji 
            4. Bikai
            5. Exit
        \nEnter your choice which brand do you like : """))

        print("\nNice Dude !...")


        if  user_input_for_Food_Brand == 1 :
            self.Food_Type()

        elif  user_input_for_Food_Brand == 2 :
            self.Food_Type()

        elif  user_input_for_Food_Brand == 3 :
            self.Food_Type()

        elif  user_input_for_Food_Brand == 4 :
            self.Food_Type()

        elif  user_input_for_Food_Brand == 5 :
            self.menu()

        else :
            print("Please , enter the valid input !...")



    def Food_Type (self) :
        user_input = int(input("""\n
        Choose a Food Type :
            1. Namkeen
            2. Bhujia
            3. Soan papdi
            4. Sweets
            5. Biscuits
            6. Chips
            7. Exit
        \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")


        if user_input == 1 :
            self.Namkeen()
            self.Food_Type()

        elif user_input == 2 :
            self.Bhujia()
            self.Food_Type()

        elif user_input == 3 :
            self.Soan_papdi()
            self.Food_Type()

        elif user_input == 4 :
            self.Sweets()
            self.Food_Type()

        elif user_input == 5 :
            self.Biscuits()
            self.Food_Type()

        elif user_input == 6 :
            self.Chips()
            self.Food_Type()

        elif user_input == 7 :
            self.Food_Brand()

        else :
            print("Please , enter the valid input !...")




#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#                                                     New Class




class Book(Food) :


    def __init__ (self) :
        self.Books_Type()



# -------------------------------------------------------  Horror_books   ----------------------------------------------------------



    def Horror_books (self) :

        user_input_for_Horror_Books = int(input("""\n  
            1. Dracula Book
            2. Frankenstein Book
            3. The Exorcist Book
            4. The Shining Book
            5. Bird Box Book
            6. The Silent Patient Book
            7. The Haunting of Hill House Book
            8. Maxican Gothic Book
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Horror_Books == 1 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 2 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 3 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 4 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 5 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $890 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 6 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $170 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 7 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $3500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 8 :
            print("You choose : Dracula book !...")
            print("The price of this item is : $1000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horror_Books == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -----------------------------------------------------  Romance_book   --------------------------------------------------------



    def Romance_book (self) :

        user_input_for_Horro_Books = int(input("""\n
            1. Pride and Prejudice Book
            2. Wuthering Heights Book
            3. Jane Eyre Book
            4. Romeo and Juliet Book
            5. Anna Karenuina Book
            6. The Fault in our Star Book
            7. Me Before You Book 
            8. It Ends With Us Book 
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Horro_Books == 1 :
            print("You choose : Pride and Prejudice book !...")
            print("The price of this item is : $100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 2 :
            print("You choose : Wuthering Heights book !...")
            print("The price of this item is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 3 :
            print("You choose : Jane Eyre book !...")
            print("The price of this item is : $250 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 4 :
            print("You choose : Romeo and Juliet book !...")
            print("The price of this item is : $150 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 5 :
            print("You choose : Anna Karenuina book !...")
            print("The price of this item is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 6 :
            print("You choose : The Fault in our Star book !...")
            print("The price of this item is : $500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 7 :
            print("You choose : Me Before You book !...")
            print("The price of this item is : $1000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 8 :
            print("You choose : It Ends With Us book !...")
            print("The price of this item is : $450 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -------------------------------------------------------  Childrens_book   ----------------------------------------------------------



    def Childrens_book (self) :

        user_input_for_Childrens_Books = int(input("""
        \n  1. Picture Books
            2. Board Books
            3. Early Reader Books
            4. Chapter Books
            5. Middle Grade Books
            6. Fairly Tales & Folk Tales Books
            7. Bed Time Story Books
            8. Advantures & Fantasy Books
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Childrens_Books == 1 :
            print("You choose : Picture book !...")
            print("The price of this item is : $1000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 2 :
            print("You choose : Board book !...")
            print("The price of this item is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 3 :
            print("You choose : Early Reader book !...")
            print("The price of this item is : $450 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 4 :
            print("You choose : Chapter book !...")
            print("The price of this item is : $550 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 5 :
            print("You choose : Middle Grade book !...")
            print("The price of this item is : $680 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 6 :
            print("You choose : Fairly Tales & Folk Tales book !...")
            print("The price of this item is : $440 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 7 :
            print("You choose : Bed Time Story book !...")
            print("The price of this item is : $280 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 8 :
            print("You choose : Advantures & Fantasy book !...")
            print("The price of this item is : $780 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Childrens_Books == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -------------------------------------------------------  Young_Adult_book   ----------------------------------------------------------



    def Young_Adult_book (self) :

        user_input_for_Young_Adult_book = int(input("""
        \n  1. The Hunger Game by Suzannne Coilins Books
            2. Harry potter Series by J.K.Rowling Books
            3. The Fault in our star by John Green Books
            4. Twilight Series by Stephenie Meyer Books
            5. Devirgent Serie by Veronica Roth Books
            6. The Maze Runner by James Dashner Books
            7. Six of Crows by Leigh Bardugo Books
            8. Elanor & Park by Rainbow Rowell Books            
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Young_Adult_book == 1 :
            print("You choose : The Hunger Game by Suzannne Coilins book !...")
            print("The price of this item is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 2 :
            print("You choose : Harry potter Series by J.K.Rowling book !...")
            print("The price of this item is : $1000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 3 :
            print("You choose : The Fault in our star by John Green book !...")
            print("The price of this item is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 4 :
            print("You choose : Twilight Series by Stephenie Meyer Books book !...")
            print("The price of this item is : $2000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 5 :
            print("You choose : Devirgent Serie by Veronica Roth book !...")
            print("The price of this item is : $5050 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 6 :
            print("You choose : The Maze Runner by James Dashner book !...")
            print("The price of this item is : $450 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 7 :
            print("You choose : Six of Crows by Leigh Bardugo book !...")
            print("The price of this item is : $80 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 8 :
            print("You choose : Elanor & Park by Rainbow Rowell book !...")
            print("The price of this item is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Young_Adult_book == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -------------------------------------------------------  Textbooks   ----------------------------------------------------------



    def Textbooks (self) :
        user_input_for_Textbooks = int(input("""
        \n  1. The Out Sider Books
            2. To kill a Mockingbird Books 
            3. The diary of Young Girl Books 
            4. Animal Farm Books
            5. Lord of the Files Books 
            6. The catcher in the Rye Books
            7. A Wrinlle Time Books
            8. The Book of Thief  
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Textbooks == 1 :
            print("You choose : The Out Sider book !...")
            print("The price of this item is : $3000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 2 :
            print("You choose : To kill a Mockingbird book !...")
            print("The price of this item is : $2700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 3 :
            print("You choose : The diary of Young Girl book !...")
            print("The price of this item is : $9000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 4 :
            print("You choose : Animal Farm book !...")
            print("The price of this item is : $4300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 5 :
            print("You choose : Lord of the Files book !...")
            print("The price of this item is : $100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 6 :
            print("You choose : The catcher in the Rye book !...")
            print("The price of this item is : $1650 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 7 :
            print("You choose : A Wrinlle Time book !...")
            print("The price of this item is : $5400 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 8 :
            print("You choose : The Book of Thief !...")
            print("The price of this item is : $3100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Textbooks == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -------------------------------------------------------  Poetry   ----------------------------------------------------------



    def Poetry_books (self) :

        user_input_for_Poetry_Books = int(input("""
        \n  1. Milk and Honey Books 
            2. The Sun and Her Flowers Books
            3. Leaves of Grass Books
            4. The complete Poems of Emily Dickinson Books
            5. Ariel Books
            6. the Waste Land and Other Poems Books
            7. Love her Wild Books
            8. The Esseential Rumi translated Books
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Poetry_Books == 1 :
            print("You choose : Milk and Honey book !...")
            print("The price of this item is : $1340 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 2 :
            print("You choose : The Sun and Her Flowers book !...")
            print("The price of this item is : $1200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 3 :
            print("You choose : Leaves of Grass book !...")
            print("The price of this item is : $1900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 4 :
            print("You choose : The complete Poems of Emily Dickinson book !...")
            print("The price of this item is : $2000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 5 :
            print("You choose : Ariel book !...")
            print("The price of this item is : $3000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 6 :
            print("You choose : the Waste Land and Other Poems book !...")
            print("The price of this item is : $100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 7 :
            print("You choose : Love her Wild book !...")
            print("The price of this item is : $10000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 8 :
            print("You choose : The Esseential Rumi translated book !...")
            print("The price of this item is : $6700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Poetry_Books == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -------------------------------------------------------  Drama_books   ----------------------------------------------------------



    def Drama_books (self) :
        user_input_for_Drama_books = int(input("""
        \n  1. Romeo and Juliet Books
            2. Hamlet Books
            3. Oedipus Rex Books
            4. Death of Salesman Books
            5. A street car named Desire Books
            6. Macbeth Books
            7. The Crucible Books
            8. Pygmalion Books
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Drama_books == 1 :
            print("You choose : Romeo and Juliet book !...")
            print("The price of this item is : $6700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 2 :
            print("You choose : Hamlet book !...")
            print("The price of this item is : $5600 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 3 :
            print("You choose : Oedipus Rex book !...")
            print("The price of this item is : $4200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 4 :
            print("You choose : Death of Salesman book !...")
            print("The price of this item is : $200 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 5 :
            print("You choose : A street car named Desire book !...")
            print("The price of this item is : $300 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 6 :
            print("You choose : Macbeth book !...")
            print("The price of this item is : $700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 7 :
            print("You choose : The Crucible book !...")
            print("The price of this item is : $100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 8 :
            print("You choose : Pygmalion book !...")
            print("The price of this item is : $1000 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Drama_books == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")



# -------------------------------------------------------  Comic_books   ----------------------------------------------------------



    def Comic_books (self) :

        user_input_for_Horro_Books = int(input("""
        \n  1. Spider-Man Books
            2. Batman Books
            3. Wonder Woman Books
            4. Captain America Books
            5. Iron Man Books
            6. X-Man Books
            7. Superman Books
            8. Deadpool Books
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Horro_Books == 1 :
            print("You choose : Spider-Man book !...")
            print("The price of this item is : $4500 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 2 :
            print("You choose : Batman book !...")
            print("The price of this item is : $2100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 3 :
            print("You choose : Wonder Woman book !...")
            print("The price of this item is : $2100 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 4 :
            print("You choose : Captain America book !...")
            print("The price of this item is : $8700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 5 :
            print("You choose : Iron Man book !...")
            print("The price of this item is : $900 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 6 :
            print("You choose : X-Man book !...")
            print("The price of this item is : $8700 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 7 :
            print("You choose : Superman book !...")
            print("The price of this item is : $650 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 8 :
            print("You choose : Deadpool book !...")
            print("The price of this item is : $430 !...")
            print("That item is successfully added in the card !...")

        elif user_input_for_Horro_Books == 9 :
            self.Books_Type()

        else :
            print("Please enter the valid input !...")


#  ---------------------------------------------------------------------------------------------------------------------------
#  ---------------------------------------------------------------------------------------------------------------------------



    def Books_Type (self) :
        user_input_for_Books_Type = int(input("""\n  
            1. Horror
            2. Romance
            3. Children's Book
            4. Young Adult (YA)
            5. Textbooks
            6. Poetry
            7. Drama
            8. Comics
            9. Exit
            \nEnter your choice which Type do you like : """))

        print("\nNice Dude !...")



        if user_input_for_Books_Type == 1 :
            self.Horror_books()
            self.Books_Type()

        elif user_input_for_Books_Type == 2 :
            self.Romance_book()
            self.Books_Type()

        elif user_input_for_Books_Type == 3 :
            self.Childrens_book()
            self.Books_Type()

        elif user_input_for_Books_Type == 4 :
            self.Young_Adult_book()
            self.Books_Type()

        elif user_input_for_Books_Type == 5 :
            self.Textbooks()
            self.Books_Type()

        elif user_input_for_Books_Type == 6 :
            self.Poetry_books()
            self.Books_Type()

        elif user_input_for_Books_Type == 7 :
            self.Drama_books()
            self.Books_Type()

        elif user_input_for_Books_Type == 8 :
            self.Comic_books()
            self.Books_Type()

        elif user_input_for_Books_Type == 9 :
            self.menu()

        else :
            print("Please enetr the valid input !...")




#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------
#       -------------------------------------------------------------------------------------------------------------------








a = call()