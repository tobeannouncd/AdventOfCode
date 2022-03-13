import advent


class Console:
    def __init__(self, code) -> None:
        self.i = 0
        self.code = tuple(code)
        self.acc = 0

    def step(self):
        instr, n = self.code[self.i].split()

        if instr == 'acc':
            self.acc += int(n)
            self.i += 1
        elif instr == 'jmp':
            self.i += int(n)
        elif instr == 'nop':
            self.i += 1


def main():
    data = advent.get_input(2020, 8).strip().splitlines()

    print(check_for_loop(data)[0])

    print(find_bad_instruction(data)[0])


def find_bad_instruction(data):
    jmp_nop_locs = []
    for i, line in enumerate(data):
        if line[:3] in ('jmp', 'nop'):
            jmp_nop_locs.append(i)

    for i in jmp_nop_locs:
        data_copy = data.copy()
        if 'jmp' in data_copy[i]:
            data_copy[i] = data_copy[i].replace('jmp', 'nop')
        else:
            data_copy[i] = data_copy[i].replace('nop', 'jmp')
        acc, will_loop = check_for_loop(data_copy)
        if not will_loop:
            return acc, i


def check_for_loop(data):
    console = Console(data)
    history = []
    while True:
        line = console.i
        if line not in range(len(console.code)):
            return console.acc, False
        if line in history:
            return console.acc, True
        history.append(console.i)
        console.step()


if __name__ == '__main__':
    main()
