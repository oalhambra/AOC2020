class Console:
    acc = 'acc'
    jmp = 'jmp'
    nop = 'nop'

    def __init__(self, accumulator=0, i_pointer=0, i_list=None):
        if i_list is None:
            i_list = []
        self.accumulator = accumulator
        self.i_pointer = i_pointer
        self.i_list = i_list

    def exec_instruction(self):
        i = self.i_list[self.i_pointer]

        if i[0] == Console.acc:
            self.accumulator += i[1]
            self.i_pointer += 1
        elif i[0] == Console.nop:
            self.i_pointer += 1
        elif i[0] == Console.jmp:
            self.i_pointer += i[1]

    def exec_no_rep(self):
        i_exec = set()
        while self.i_pointer not in i_exec:
            i_exec.add(self.i_pointer)
            self.exec_instruction()
        return self.accumulator


f = open('day8.txt', 'r')
data = f.readlines()

data = list(map(lambda x: x.split(' '), data))
data = list(map(lambda x: [x[0], int(x[1])], data))

c = Console(i_list=data)

print(c.exec_no_rep())
