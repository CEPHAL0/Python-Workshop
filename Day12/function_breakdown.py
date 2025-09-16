from functions import print_menu, take_option, main

option = ""
while option != "4":
    print_menu()
    option = take_option()
    main(option=option)