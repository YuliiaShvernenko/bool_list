middle = len(main_list) // 2

if len(main_list) % 2 != 0:
        middle += 1
        first_list = main_list[:middle]
        second_list = main_list[middle:]
elif not main_list:
        first_list = second_list = []
else:
        first_list = main_list[:middle]
        second_list = main_list[middle:]

main_list = [first_list] + [second_list]
