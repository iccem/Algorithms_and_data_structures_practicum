

def get_max_length_uniqal_substring():
    substring = ''
    line = input().strip()
    max_length = 0
    for i in range(len(line)):
        if line[i] not in substring:
            substring += line[i]
        else:
            max_length = max(max_length, len(substring))
            while line[i] in substring:
                substring = substring[1:]
            substring += line[i]
    max_length = max(max_length, len(substring))
    return max_length


print(get_max_length_uniqal_substring())
