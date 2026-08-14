import sys
import tokeniser
import parser
from interpreter import Interpreter

interpreter = Interpreter()

tokens = tokeniser.tokenise(open(sys.argv[1]).read()) #python main.py [text file (code)]
parsed = parser.parse(tokens)
interpreter.interpret(parsed)