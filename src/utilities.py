def import_data(day):
    input_raw = open('../input/day'+str(day), 'r')
    input_list = input_raw.read().split('\n')
    input_raw.close()
    return input_list
