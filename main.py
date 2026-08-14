import sys

class Evaluate:
    def lineReader(self, s):
        self.vars = {}
        lines = [x for x in s.split("\n") if x.strip() != ""] # Creates an array of all the lines, excluding empty ones
        pc = 0 #program counter
        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit = 1)[0]:
                case "while":
                    if self.execute(line.split(maxsplit = 1)[1]) == 1: pc += 1 #if the condition is true
                    else:
                        while lines[pc].split(maxsplit = 1)[0] != "end": pc += 1
                        pc += 1
                case "end":
                    while lines[pc].split(maxsplit = 1)[0] != "while": pc -= 1
                case "print":
                    (_, expr) = line.split(maxsplit = 1)
                    if expr in self.vars:
                        print(self.vars[expr])
                    else:
                        print(expr)
                    pc += 1
                case _:
                    (name, _, expr) = line.split(maxsplit = 2) #splits line into 3 parts: var name, ignores the equals, rest of the line
                    self.vars[name] = self.execute(expr)
                    pc += 1
    def execute(self, s):
        tokens = s.split()
        stack = [] # Reverse Polish Notation stack
        for token in tokens:
            if token.isdigit(): 
                stack.append(int(token))
            elif token in self.vars: stack.append(self.vars[token])
            else:
                rhs = stack.pop()
                if token == "not":
                    if rhs == 1: stack.append(0)
                    else: stack.append(1)
                else:
                    lhs = stack.pop()
                    if token == "+": stack.append(lhs + rhs)
                    elif token == "-": stack.append(lhs - rhs)
                    elif token == "/": stack.append(lhs / rhs)
                    elif token == "*": stack.append(lhs * rhs)
                    elif token == ">=":
                        if lhs >= rhs: stack.append(1)
                        else: stack.append(0) 
                    elif token == "<=":
                        if lhs <= rhs: stack.append(1)
                        else: stack.append(0)
                    elif token == ">":
                        if lhs > rhs: stack.append(1)
                        else: stack.append(0)
                    elif token == "<":
                        if lhs < rhs: stack.append(1)
                        else: stack.append(0)
                    elif token == "==":
                        if lhs == rhs: stack.append(1)
                        else: stack.append(0)
                    elif token == "!=":
                        if lhs != rhs: stack.append(1)
                        else: stack.append(0)
                    elif token == "and":
                        if lhs == 1 and rhs == 1: stack.append(1)
                        else: stack.append(0)
                    elif token == "or":
                        if lhs == 1 or rhs == 1: stack.append(1)
                        else: stack.append(0)
        return stack[0]

Evaluate().lineReader(open(sys.argv[1]).read()) #python main.py [text file (code)]