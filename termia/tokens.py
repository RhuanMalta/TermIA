"""
Lexer do TermIA (parcial) usando PLY (lex).
Reconhece tokens básicos para comandos de SO e IA.
"""
import ply.lex as lex

# Lista de tokens
tokens = (
    "LS", "MKDIR", "CD", "EXIT",
    "IA", "ASK", "SUMMARIZE", "CODEEXPLAIN",
    "STRING", "PATH", "NAME",
)

# Palavras-chave (case-sensitive; se quiser case-insensitive, faça .lower())
reserved = {
    "ls": "LS",
    "mkdir": "MKDIR",
    "cd": "CD",
    "exit": "EXIT",
    "ia": "IA",
    "ask": "ASK",
    "summarize": "SUMMARIZE",
    "codeexplain": "CODEEXPLAIN",
}

t_ignore = ' \t'

def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

# Um PATH inicia com / ou contém /
def t_PATH(t):
    r'(\/[\w\.\-\/]*)|([\w\.\-]+\/[\w\.\-\/]*)'
    return t

def t_NAME(t):
    r'[\w\.\-]+'
    # Se o lexema for palavra-chave, converte o tipo do token
    t.type = reserved.get(t.value, "NAME")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise SyntaxError(f"Caractere inválido no lexer: '{t.value[0]}' na posição {t.lexpos}")

def build_lexer(**kwargs):
    return lex.lex(**kwargs)