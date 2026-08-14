def parse(tokens):
    parsed = []
    lines = tokens
    pc = 0 #program counter
    while pc < len(lines):
        line = lines[pc]
        firstToken = line[0]
        match firstToken[0]:
            case "KEYWORD":
                if firstToken[1] == "while":
                    body = []
                    while True:
                        pc += 1
                        newline = lines[pc]
                        if newline[0][1] != "end":
                            body.append(newline)
                        else:
                            break
                    parsed.append({
                        "type": "while",
                        "condition": line[1:],
                        "body": parse(body)
                    })
                else:
                    parsed.append({
                       "type": firstToken[1],
                        "expression": line[1:]
                    })
            case "IDENTIFIER":
                if line[1][0] == "ASSIGN":
                    parsed.append({
                        "type": "assignment",
                        "name": firstToken[1],
                        "expression": line[2:]
                    })
        pc += 1
    return parsed