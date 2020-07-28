def check_email(string):
    if " " in string:
        print("False")
    elif "@" not in string:
        print("False")
    elif "@" in string:
        index_at = int(string.find("@"))
        print(index_at)
        if string[index_at - 1] == ".":
            print("False")
        elif string[index_at + 1] == ".":
            print("False")
        elif "." in string[index_at:]:
            print("True")
        else:
            print("True")

check_email("anna.tt..@gmail.com")            