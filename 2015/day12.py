import json
import advent


def find_nums(j, part=1):
    if j is None:
        return []
    if isinstance(j, int):
        return [j]
    nums = []
    it = None
    if isinstance(j, dict):
        if part == 2 and 'red' in j.values():
            return []
        it = j.values()
    elif isinstance(j, list):
        it = j
    if it is not None:
        for child in it:
            nums.extend(find_nums(child, part))
    return nums


def main():
    js = json.loads(advent.get_input(2015, 12,'json'))
    # js = json.loads('{"a":2,"b":4}')
    # js = json.loads('{"a":{"b":4},"c":-1}')
    # js = json.loads('[-1,{"a":1}]')
    print(sum(find_nums(js)))
    print(sum(find_nums(js, part=2)))


if __name__ == '__main__':
    main()
