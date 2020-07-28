def whattodo(instructions):
    if "Simon says" in instructions:
        print("I " + instructions.replace("Simon says", ""))
    else:
        return True
    return False

whattodo("make a wish Simon says")