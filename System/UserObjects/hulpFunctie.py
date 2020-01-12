def stringToIntVal(s):
    """
    zet elke char in een string om naar zijn intval en plakt deze aan elkaar om zo een key te bekomen
    :param s:
    :return:
    """
    intValString = ""

    for char in s:
        intval = ord(char)

        intValString += str(intval)

    return int(intValString)
