def find_recent_version(array):
    ans = []
    while array:
        k = find_max(array)
        next_arr = []
        for _, value in enumerate(array):
            if value == "":
                continue
            try:
                temp  = int(value[:value.find(".")])
            except ValueError:
                continue
            if temp == k and temp != -1:
                next_arr.append(value[value.find(".") + 1:])
        array = next_arr
        if k not in ans:
            ans.append(str(k))
    return ".".join(ans)

def find_max(array):
    max_unit_digit = -1
    for i in array:
        try:
            if (len(i) == 1 and int(i) < max_unit_digit) or not i:
                continue
            l = i.find(".")
            if l == -1 and int(i) > max_unit_digit:
                max_unit_digit = int(i)
                continue
            version = int(i[:l])
            if version > max_unit_digit:
                max_unit_digit = version
        except ValueError:
            continue

    if max_unit_digit != -1:
        return max_unit_digit
    return max(array)

def main():
    version_list = ["10.1.1.3","1","10.1.1.9","10.2","10.4.6", "9.5", "8.2","  " ,"", "10.4.0.1.1", "10.4.2.1.7", "10.4.0.1.8", "abcs"]
    most_recent = find_recent_version(version_list)
    print(f"{most_recent} is the most recent version among the version list.")
    
if __name__ == "__main__":
    main()
