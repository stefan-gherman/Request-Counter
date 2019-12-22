
methods = ['GET', 'POST', 'PUT', 'DELETE']


def create_dict_from_file(filename):
    with open(filename) as counts:
        counts_list = counts.readlines()
        for elem in range(len(counts_list)):
            counts_list[elem] = counts_list[elem].replace('\n', '')
            counts_list[elem] = counts_list[elem].split()
        counts_list = dict(counts_list)
        for key in counts_list.keys():
            counts_list[key] = int(counts_list[key])
        return counts_list

def write_dict_to_file(dicto, filename):
    with open(filename,'w') as writer:
        for key in dicto.keys():
            writer.writelines(f'{key} {dicto[key]}\n')
def sort_dict(dicto):
    items = dicto.items()
    sorted_items = sorted(items , key =lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict


