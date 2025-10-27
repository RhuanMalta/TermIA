"""
Parser do TermIA (parcial) usando PLY (yacc).
Gera uma AST (dicionários) adequada para integrar execução na próxima etapa.
"""
# Import será resolvido no seu ambiente local ao instalar ply
import ply.yacc as yacc
from .tokens import tokens, build_lexer
from .ast import node

# Precedências (não estritamente necessárias aqui, mas deixadas para expansão futura)
precedence = ()

# Entrada inicial
def p_input(p):
    "input : command"
    p[0] = p[1]

def p_command(p):
    """command : sys_command
               | ia_command
               | EXIT"""
    if p.slice[1].type == "EXIT":
        p[0] = node("exit")
    else:
        p[0] = p[1]

def p_sys_command_ls(p):
    """sys_command : LS
                   | LS PATH"""
    path = p[2] if len(p) == 3 else None
    p[0] = node("ls", path=path)

def p_sys_command_mkdir(p):
    "sys_command : MKDIR name"
    p[0] = node("mkdir", name=p[2])

def p_sys_command_cd(p):
    "sys_command : CD path"
    p[0] = node("cd", path=p[2])

def p_ia_command(p):
    """ia_command : IA ia_ask
                  | IA ia_summarize
                  | IA ia_codeexplain"""
    p[0] = node("ia", action=p[2])

def p_ia_ask(p):
    "ia_ask : ASK STRING"
    p[0] = node("ia.ask", prompt=p[2])

def p_ia_summarize(p):
    "ia_summarize : SUMMARIZE STRING"
    p[0] = node("ia.summarize", text=p[2])

def p_ia_codeexplain_str(p):
    "ia_codeexplain : CODEEXPLAIN STRING"
    p[0] = node("ia.codeexplain", target=p[2], kind="string")

def p_ia_codeexplain_path(p):
    "ia_codeexplain : CODEEXPLAIN path"
    p[0] = node("ia.codeexplain", target=p[2], kind="path")

def p_ia_codeexplain_name(p):
    "ia_codeexplain : CODEEXPLAIN name"
    p[0] = node("ia.codeexplain", target=p[2], kind="name")

def p_path_name(p):
    "path : PATH"
    p[0] = p[1]

def p_name(p):
    "name : NAME"
    p[0] = p[1]

def p_error(p):
    if p is None:
        raise SyntaxError("Erro de sintaxe: entrada inesperadamente incompleta.")
    else:
        raise SyntaxError(f"Erro de sintaxe próximo a '{p.value}' (token {p.type}) na linha {p.lineno}.")

def build_parser(debug=False):
    """Constrói lexer+parser integrados e retorna uma função parse(s: str) -> AST."""
    lexer = build_lexer()
    parser = yacc.yacc(debug=debug, write_tables=False)
    def parse(source: str):
        return parser.parse(source, lexer=lexer)
    return parse
