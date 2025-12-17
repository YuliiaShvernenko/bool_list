if main_list == []:
    main_list = []
else:
    last = main_list[-1]
    main_list.insert(0, last)
    main_list.pop()
