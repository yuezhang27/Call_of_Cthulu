def parent():
    print("Printing from the parent() function")
    def first_child():
        print("Printing from the inner first_child() function")
    def second_child():
        print("Printing from the inner second_child() function")

    first_child()
    second_child()

parent()