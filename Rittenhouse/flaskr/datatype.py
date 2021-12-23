def __init__(self, type, books):
    """

    :param self:
    :type self:
    :param type: toggles data type returned
    :type type:
    :param books: data that is manipulated
    :type books:
    """
    if type == "d":
        result = {}
        for title, author, descrip in cursor:
            result[author] = [title, descrip]
    elif type == "c":
        pass
        # result = ?
    elif type == "l":
        result = []
        for title, author, descrip in cursor:
            result.append(title)
            result.append(author)
            result.append(descrip)
    elif type == "s":
        result = set()
        for title, author, descrip in cursor:
            result.add(title)
            result.add(author)
            result.add(descrip)
    elif type == "tp":
        pass
        # ask how this should be returned

    elif type == "tb":
        pass
        # ask how this should be returned

    else:
        print("Please enter valid input: d, c, l, tp, tb")