
methods = ['GET', 'POST', 'PUT', 'DELETE']

def sort_dict(dicto):
    items = dicto.items()
    sorted_items = sorted(items , key =lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict