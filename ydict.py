import yaml, sys, collections

if __name__ == '__main__':

    safe = False
    if safe:
        stream = open("new.yaml", 'r')
        dictionary = yaml.safe_load(stream)
    else:
        dictionary = yaml.load(sys.stdin, Loader=yaml.FullLoader)
    sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[0])
    
    for key, value in sorted_dictionary:
        print (key + " : " + str(value))