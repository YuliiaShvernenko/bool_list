if not main_list:
    main_list = []
else:
    last = main_list.pop()
    main_list.insert(0, last)

