import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    if field not in{"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None
    file_path= os.path.join(cwd_path, file_name)
    with open (file_path, "r") as fil:
        data= json.load(fil)

    return data[field]

    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

def linear_search(seq, cislo):
    pos=[]
    for z, value in enumerate(seq):
        if value== cislo:
            pozice.append(z)
    result={"positions":pos,
            "count": len(pos)
    }

    return result


def binary_search(seq, cislo):
    l=0
    r=len(seq)-1
    while l<= r:
        mid= (l+r)//2
        if seq[mid]==cislo:
            return mid
        elif seq[mid]<cislo:
            l=mid+1
        else:
            r= mid -1
    return None
def

def main():
    ordered_data=read_data("sequential.json","ordered_numbers")
    number=5
    result=binary_search(ordered_data, number)
    print("index:", result)


    pass


if __name__ == '__main__':
    main()