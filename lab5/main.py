import time


def find_matches(text: str, pattern: str) -> [int]:
    match_table = {}
    for i in range(len(pattern)):
        match_table.update({pattern[i]: max(1, len(pattern) - i - 1)})
    index_in_text = len(pattern) - 1
    result = []
    while index_in_text < len(text):
        shift_index = 1
        if text[index_in_text] != pattern[len(pattern) - 1]:
            for i in match_table.keys():
                if i == text[index_in_text]:
                    shift_index = match_table[i]
                    break
                else:
                    shift_index = len(pattern)
        else:
            current_substring = text[index_in_text - len(pattern) + 1: index_in_text]
            for i in range(len(current_substring)):
                if current_substring[len(current_substring) - i - 1] != pattern[len(pattern) - i - 2]:
                    break
                else:
                    if i == len(current_substring) - 1:
                        result.append(index_in_text - len(pattern) + 1)
                        shift_index = 1
        index_in_text += shift_index
    return result


def main() -> None:
    with open('input1.txt', 'r') as file:
        print(len(find_matches(file.read(), 'aaa')))
    t1 = time.process_time()
    print(t1)
    with open('input2.txt', 'r') as file:
        print(find_matches(file.read(), 'kitty'))
    t2 = time.process_time() - t1
    print(t2)
    with open('input3.txt', 'r') as file:
        print(find_matches(file.read(), 'qwe'))
    t3 = time.process_time() - t2
    print(t3)


if __name__ == '__main__':
    main()
