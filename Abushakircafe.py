import random
print("welcome to Abushakir cafe")
milk_bill = 0
coffee_bill = 0
tea_bill = 0
bill = 0
coca_bill = 0
fanta_bill = 0
meta_bill = 0
walia_bill = 0
pizza_bill = 0
half_ice = 0
full_ice = 0
ice = 0
chocolate_p = 0
bedelle_bill = 0
def cafe_assistant():
    coffee = '''
     (
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
jgs \""--..__                              __..--""/
     '._     """----.....______.....----"""     _.'
        `""--..,,_____            _____,,..--""`
                      `"""----"""`
    '''
    tea = '''
             (  )   (   )  )
             ) (   )  (  (
             ( )  (    ) )
             _____________
            <_____________> ___
            |             |/ _ \/
            |             | | |
            |             |_| |
         ___|             |\___/
        /    \___________/    /
    '''
    milk = '''
     _________
  | _______ |
 / \        \\
/___\_________\\
|   | \       |
|   |  \      |
|   |   \     |
|   | M  \    |
|   |     \   |
|   |\  I  \  |
|   | \     \ |
|   |  \  L  \|
|   |   \     |
|   |    \  K |
|   |     \   |
|   |      \  |
|___|_______\_|
    '''
    beer = '''
    .~~~~.
    i====i_
    |cccc|_)
    |cccc|   
    `-==-'
    '''
    chocolate = '''
     ___  ___  ___  ___  ___.---------------.
    .'\__\\'\__\\'\__\\'\__\'\__,`   .  ____ ___ \\
    |\/ __\/ __\/ __\/ __\/ _:\   |`.  \  \___ \\
     \\'\__\\'\__\\'\__\\'\__\\'\_`.__|""`. \  \___ \\
      \\/ __\/ __\/ __\/ __\/ __:                \\
       \\'\__\\'\__\\'\__\ \__\\'\_;-----------------`
        \\/   \/   \/   \/   \/ :               hh|
         \|______________________;________________|
    '''
    icecream = '''
                ..oo.
              oGGGGGGo
             GGGGGGGGGG
      .mMMMMMMGGGGGGEEEE=
     MMMMMMMMMMMGGEEEEEEEE
    MMMMMMMMMMMNICKEEEEEEEE
    MMMMMMMMMMMMMEEEEEEEEEE
    !MMMMMMMMMMMOOEEEEEEEE
     MMM!MMMMMMOOOOOOE!=
      MM!!!!!!!!!!!!!!!
       MM!!!!!!!!!!!!!'
       !M!!!!!!!!!!!!!
        MM!!!!!!!!!!!'
        MM!!!!!!!!!!!
        ! `!!!!!!!!!'
        .  !!!!!!!!!
           `!!!!!!!'
            !!!!!!!
            `!!!!!'
             !!!!!
             `!!!'
              !!!
              `!'
               !
    '''
    birth_day_half = '''
    (        (
                 ( )      ( )          (
          (       Y        Y          ( )
         ( )     |"|      |"|          Y
          Y      | |      | |         |"|
         |"|     | |.-----| |---.___  | |
         | |  .--| |,~~~~~| |~~~,,,,'-| |
         | |-,,~~'-'___   '-'       ~~| |._
        .| |~       // ___            '-',,'.
       /,'-'     <_// // _  __             ~,\
      / ;     ,-,     \\_> <<_______________;_)
      | ;    {(_)} _,      . |================|
      | '-._ ~~,,,           | ,,             |
      |     '-.__ ~~~~~~~~~~~|________________|   
      |\         `'----------|
      | '=._                 |
      :     '=.__            |
       \         `'==========|
    snd '-._                 |
            '-.__            |
                 `'----------|
    '''
    birth_day_full = '''
    * 
                                      * 
         *                                             * 
                                              * 
                   * 
                                 * 
                                                           * 
        * 
                                                 * 
            * 
                          *             * 
                                                    * 
     *                                                               * 
              * 
                              (             ) 
                      )      (*)           (*)      ( 
             *       (*)      |             |      (*) 
                      |      |~|           |~|      |          * 
                     |~|     | |           | |     |~| 
                     | |     | |           | |     | | 
                    ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |. 
               .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,. 
             ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a, 
            a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a 
            ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@'; 
            ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@; 
            ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@; 
            ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@; 
            ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;; 
            ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;; 
            ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@a; 
        ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%, 
     .%%%%%%;;;;;;;a@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%, 
    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%, 
    %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%% 
    %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%% 
    `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%' 
      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%' 
          `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%' 
                 """"""""""""""`,,,,,,,,,'""""""""""""""""" 
                                `%%%%%%%' 
                                 `%%%%%' 
                                   %%% 
                                  %%%%% 
                               .,%%%%%%%,. 
                          ,%%%%%%%%%%%%%%%%%%%, 
              ---------------------------------------------
    '''
    soft_drink = '''
    _
     {_}
     |(|
     |=|
    /   \
    |.--|
    ||  |
    ||  |    .    ' .
    |'--|  '     \~~~/
    '-=-' \~~~/   \_/
           \_/     Y
            Y     _|_
           _|_
    '''
    hot_drinks = "hot drinks:\n \t1 for coffee (ETB 10)\n \t2 for milk (ETB 15)\n \t3 for tea (ETB 8)\n"
    soft_drinks = 'soft drinks:\n \t4 for coca-cola (ETB 30)\n \t5 for fanta(ETB 25)\n'
    alcoholic_drinks = "alcoholic drinks:\n \t6 for meta-beer(ETB 50)\n \t7 for walia beer (ETB 60)\n \t8 for bedelle-beer (ETB 70)\n"
    for_icecream = "icecreams:\n \t- for birthday icecream:\n \t \t9 for full birthday icecreams(ETB 800)\n \t \t10 for half birthday icecream (ETB 400)\n"
    for_chocolate = "11 for chocolate (ETB 140)\n"
    normal_ice = "12 for normal ice-cream (ETB 120)\n"

    global milk_bill
    global coffee_bill
    global tea_bill
    global bill
    global meta_bill
    global walia_bill
    global half_ice
    global full_ice
    global ice
    global pizza_bill
    global fanta_bill
    global coca_bill
    global chocolate_p
    global bedelle_bill
    first_input = input(f"please choose from the menu:\n {hot_drinks} {soft_drinks} {alcoholic_drinks} {for_icecream} {for_chocolate} {normal_ice}")
    if first_input == "2":
        second_input = int(input("please how many bottles of milk do you want, enter the number(eg. 3)\n"))
        print("enjoy your milk!")
        print(milk * second_input)
        milk_bill += 12 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no \n").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "1":
        bill = 20
        second_input = int(input("please how many cups of coffee do you want, enter the number(eg. 3)\n"))
        print("enjoy your coffee!")
        print(coffee * second_input)
        coffee_bill += 20 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "3":
        second_input = int(input("please how many cup of tea do you want, enter the number(eg. 3)\n"))
        print("enjoy your tea!")
        print(tea * second_input)
        tea_bill += 6 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "4":
        second_input = int(input("please how many bottles coca-cola do you want, enter the number(eg. 3) \n"))
        print("enjoy your coca!")
        print(soft_drink * second_input)
        coca_bill += 30 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "5":
        second_input = int(input("please how many bottle of fanta do you want, enter the number(eg. 3) \n"))
        print("enjoy your fanta!")
        print(soft_drink * second_input)
        fanta_bill += 25 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "6":
        second_input = int(input("please how many bottles do you want, enter the number(eg. 3) \n"))
        print("enjoy your beer!")
        print(beer * second_input)
        meta_bill += 50 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "7":
        second_input = int(input("please how many bottles do you want, enter the number(eg. 3) \n"))
        print("enjoy your beer!")
        print(beer * second_input)
        walia_bill += 60 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "8":
        second_input = int(input("please how many bottles do you want, enter the number(eg. 3) \n"))
        print("enjoy your beer!")
        print(beer * second_input)
        bedelle_bill += 70 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "9":
        second_input = int(input("please how many full birthday ice-creams do you want, enter the number(eg. 3) \n"))
        print("enjoy your icecream!")
        print(birth_day_full * second_input)
        full_ice += 800 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "10":
        second_input = int(input("please how many half birthday ice-creams do you want, enter the number(eg. 3) \n"))
        print("enjoy your icecream!")
        print(birth_day_half * second_input)
        half_ice += 400 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "11":
        second_input = int(input("please how many do you want, enter the number(eg. 3) \n"))
        print("enjoy your chocolate!")
        print(chocolate*second_input)
        chocolate_p += 140 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    elif first_input == "12":
        second_input = int(input("please how many ice-cream do you want, enter the number(eg. 3) \n"))
        print("enjoy your icecream!")
        print(icecream * second_input)
        ice += 120 * second_input
        def other_input():
            other_inputs = input("do you want other services? y for yes n for no ").lower()
            if other_inputs == "y":
                cafe_assistant()
            elif other_inputs == "n":
                pass
            else:
                other_input()
        other_input()
    else:
        cafe_assistant()
    bill += milk_bill + coffee_bill + tea_bill + coffee_bill + fanta_bill + meta_bill + walia_bill + bedelle_bill + half_ice + full_ice + ice + chocolate_p
cafe_assistant()
ask_bill = input("do you want me to calculate your bills? Y for yes or N for no\n").lower()
def bill_calculator():
    global bill
    global ask_bill
    if ask_bill == "y":
        print("your bill is: ", bill, "and you will pay: ", bill + 0.15 * bill, "with 15% of taxation.\n")
        ask_to = input("shall I calculate the amount that each one of you will pay?(enter 1) or,\nshall i choose someone from you to pay(enter 2)\n")
        if ask_to == "1":
            number = int(input("please enter your numbers, enter a figure(eg. 3) \n"))
            assert type(number) == int , "you can only enter a number in a figural form"
            print("each one of you will contribute: ", (bill + 0.15*bill)/number)
            another = input("thank you for choosing us🙂, come back again. if you want to order again enter 1, to exit enter any key other than 1\n").lower()
            if another == "1":
                cafe_assistant()
            else:
                pass
        elif ask_to == "2":
            taker = input("enter your names separated by space: ").split(" ")
            selector = random.randint(0,len(taker) -1)
            print(f"{taker[selector]} will pay the bill!")
            another = input("thank you for choosing us🙂, come back again. if you want to order again enter 1, to exit enter any key other than 1\n").lower()
            if another == "1":
                cafe_assistant()
            else:
                pass
    elif ask_bill == "n":
        alternative = input("Ok, enter 1 to order another , and 2 to recalculate your bill:\n ").lower()
        if alternative == "1":
            cafe_assistant()
            bill_calculator()
        elif alternative == "2":
            ask_bill = "y"
            bill_calculator()
bill_calculator()



