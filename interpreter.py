class Interpreter:
    def __init__(self):
        self.vars = {}

    def interpret(self, parsed):
        for statement in parsed:
            match statement["type"]:
                case "assignment":
                    self.vars[statement["name"]] = self.execute(statement["expression"])

                case "print":
                    print(self.execute(statement["expression"]))

                case "while":
                    while self.execute(statement["condition"]):
                        self.interpret(statement["body"])

    def execute(self, expression):
        stack = []
        for token in expression:
            tokenType = token[0]
            value = token[1]

            if tokenType == "NUMBER": stack.append(value)
            elif tokenType == "IDENTIFIER": stack.append(self.vars[value])
            elif tokenType == "OPERATOR":
                rhs = stack.pop()
                if value == "not":
                    if rhs == 1: stack.append(0)
                    else: stack.append(1)
                else:
                    lhs = stack.pop()
                    if value == "+": stack.append(lhs + rhs)
                    elif value == "-": stack.append(lhs - rhs)
                    elif value == "/": stack.append(lhs / rhs)
                    elif value == "*": stack.append(lhs * rhs)
                    elif value == ">=":
                        if lhs >= rhs: stack.append(1)
                        else: stack.append(0)
                    elif value == "<=":
                        if lhs <= rhs: stack.append(1)
                        else: stack.append(0)
                    elif value == ">":
                        if lhs > rhs: stack.append(1)
                        else: stack.append(0)
                    elif value == "<":
                        if lhs < rhs: stack.append(1)
                        else: stack.append(0)
                    elif value == "==":
                        if lhs == rhs: stack.append(1)
                        else: stack.append(0)
                    elif value == "!=":
                        if lhs != rhs: stack.append(1)
                        else: stack.append(0)
                    elif value == "and":
                        if lhs == 1 and rhs == 1: stack.append(1)
                        else: stack.append(0)
                    elif value == "or":
                        if lhs == 1 or rhs == 1: stack.append(1)
                        else: stack.append(0)
        return stack[0]