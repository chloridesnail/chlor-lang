def tokenise(s):
    tokens = []
    operators = {"+", "-", "*", "/", ">=", "<=", ">", "<", "==", "!=", "and", "or", "not"}
    keywords = {"while", "end", "print"}

    for line in s.split("\n"):
        if line.strip() == "": continue

        lineTokens = []

        for token in line.split():
            if token.isdigit():
                lineTokens.append(("NUMBER", int(token)))
            elif token in operators:
                lineTokens.append(("OPERATOR", token))
            elif token in keywords:
                lineTokens.append(("KEYWORD", token))
            elif token == "=":
                lineTokens.append(("ASSIGN", token))
            else:
                lineTokens.append(("IDENTIFIER", token))

        tokens.append(lineTokens)

    return tokens