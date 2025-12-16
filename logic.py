def percent_change(old,new):
       

    if old is None or new is None:
        return None
    if old == 0:
        return None

    try:
        change = ((float(new) - float(old)) / float(old)) * 100
        return change
    except TypeError:
        return None
