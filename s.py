import re
from typing import List

class Lexeme:
    def __init__(self, token: str, value: str):
        self.token = token
        self.value = value

    def __repr__(self):
        return f"Lexeme(token='{self.token}', value='{self.value}')"

KEYWORDS = [ "@PROG", "@DECL", "@CORPS", "CORPS@", "PROG@", "DECL@", "ENTIER", "REEL", "CARACTERE", "TABLEAU", "DE", "FOR", "ECRIRE", "IF", "THEN", "ELSE" ]
DELIMITERS = [ ",", ";", r"\(", r"\)", r"\[", r"\]", r"\{", r"\}" ]
ARITHMETIC_OPERATORS = ["ADD", "SOUS", "MULT", "DIV"]
ASSIGNMENT_OPERATORS = [":=", r"\+\+", r"\-\-"]
COMPARISON_OPERATORS = ["<", "<=", ">", ">=", "==", "<>"]
LOGICAL_OPERATORS = ["&&", r"\|\|", "!"]
IDENTIFIER_REGEX = r"%[0-9]+|[a-zA-Z][a-zA-Z0-9]*"
INTEGER_REGEX = r"[0-9]+"
REAL_REGEX = r"\d+\.\d*"
STRING_REGEX = r'"[^"]*"'
CHARACTER_REGEX = r"'.'"

KEYWORDS_REGEX = re.compile(f"({'|'.join(KEYWORDS)})")
DELIMITERS_REGEX = re.compile(f"({'|'.join(DELIMITERS)})")
ARITHMETIC_OPERATORS_REGEX = re.compile(f"({'|'.join(ARITHMETIC_OPERATORS)})")
ASSIGNMENT_OPERATORS_REGEX = re.compile(f"({'|'.join(ASSIGNMENT_OPERATORS)})")
COMPARISON_OPERATORS_REGEX = re.compile(f"({'|'.join(COMPARISON_OPERATORS)})")
LOGICAL_OPERATORS_REGEX = re.compile(f"({'|'.join(LOGICAL_OPERATORS)})")
IDENTIFIER_REGEX_REGEX = re.compile(f"({IDENTIFIER_REGEX})")
INTEGER_REGEX_REGEX = re.compile(f"({INTEGER_REGEX})")
REAL_REGEX_REGEX = re.compile(f"({REAL_REGEX})")
CHARACTER_REGEX_REGEX = re.compile(f"({CHARACTER_REGEX})")

def lexeme(code: str) -> List[Lexeme]:
    result: List[Lexeme] = []
    regex = re.compile(
        f"({'|'.join(KEYWORDS)}|{'|'.join(DELIMITERS)}|{'|'.join(ARITHMETIC_OPERATORS)}|{'|'.join(ASSIGNMENT_OPERATORS)}|{'|'.join(COMPARISON_OPERATORS)}|{'|'.join(LOGICAL_OPERATORS)}|{IDENTIFIER_REGEX}|{INTEGER_REGEX}|{REAL_REGEX}|{STRING_REGEX}|{CHARACTER_REGEX})"
    )

    for match in regex.finditer(code):
        token = match.group()
        if KEYWORDS_REGEX.match(token):
            result.append(Lexeme(token=token, value=token))
        elif DELIMITERS_REGEX.match(token):
            result.append(Lexeme(token="DELIMITERS_", value=token))
        elif ARITHMETIC_OPERATORS_REGEX.match(token):
            result.append(Lexeme(token="ARITHMETIC_OPERATOR", value=token))
        elif ASSIGNMENT_OPERATORS_REGEX.match(token):
            result.append(Lexeme(token="ASSIGNMENT_OPERATOR", value=token))
        elif COMPARISON_OPERATORS_REGEX.match(token):
            result.append(Lexeme(token="COMPARISON_OPERATOR", value=token))
        elif LOGICAL_OPERATORS_REGEX.match(token):
            result.append(Lexeme(token="LOGICAL_OPERATOR", value=token))
        elif IDENTIFIER_REGEX_REGEX.match(token):
            result.append(Lexeme(token="IDENTIFIER", value=token))
        elif INTEGER_REGEX_REGEX.match(token):
            result.append(Lexeme(token="INTEGER", value=token))
        elif REAL_REGEX_REGEX.match(token):
            result.append(Lexeme(token="REAL", value=token))
        elif CHARACTER_REGEX_REGEX.match(token):
            result.append(Lexeme(token="CHARACTER", value=token))
        else:
            result.append(Lexeme(token="STRING", value=token))

    return result

# code = """
# @PROG
# @DECL
# %1:ENTIER,%2:REEL
# DECL@
# @CORPS
# ECRIRE("Hello, world!");
# CORPS@
# PROG@
# """
with open('input.new', 'r') as file:
        code = file.read()

print("program start: ")
print(lexeme(code))

with open('lexemes.txt', 'w') as f:
    for token in lexeme(code):
        f.write(f'{token.token}: {token.value}\n')
