import yaml, sys, collections

if __name__ == '__main__':

    safe = False
    sort = False

    # Load
    if safe:
        stream = open("new.yaml", 'r')
        dictionary = yaml.safe_load(stream)
    else:
        dictionary = yaml.load(sys.stdin, Loader=yaml.FullLoader)

    # Sort
    sorted_dictionary = dictionary.items()
    if sort:
        sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[0])

    # Print
    for key, value in sorted_dictionary:
        if 'def' in value.keys():
          print ("{}:\n  {}\n  {}{}\n".format(key, value['def'], str(value), type(value)))
        else:
          print ("{}:\n  {}, {}\n".format(key, str(value), type(value)))
