from lark import Lark, Transformer

with open("grammar.lark") as f:
    grammar = f.read()

parser = Lark(grammar, start="program")

class GrapeToDict(Transformer):
    def program(self, args):
        return {
            "type": "program",
            "statements": args,
        }
    def variable(self, args):
        return {
            "type": "variable",
            "name": args[0],
            "value": args[1],
        }
    def sequence(self, args):
        return {
            "type": "sequence",
            "actions": args,
        }
    NUMBER = lambda _, x: {
        "type": "NUMBER",
        "value": x,
    }
    PLUS = lambda _, x: {
        "type": "PLUS",
    }
    MINUS = lambda _, x: {
        "type": "MINUS",
    }
    DUMP = lambda _, x: {
        "type": "DUMP",
    }
    NAME = lambda _, x: {
        "type": "NAME",
        "value": x,
    }

grape_to_dict = GrapeToDict()
name_counter_var = 0
def name_counter():
    global name_counter_var
    result = name_counter_var
    name_counter_var += 1
    return result

def generate_c(tree, env = {}):
    match tree:
        case {
            "type": "program",
            "statements": statements
        }:
            new_statements = []
            for stmt in statements:
                stmt, env = generate_c(stmt, env)
                new_statements.append(stmt)
            return "\n".join(new_statements), env
        case {
            "type": "variable",
            "name": {
                "type": "NAME",
                "value": name,
            },
            "value": value,
        }:
            env[name] = value
            return "", env
        case {
            "type": "sequence",
            "actions": actions,
        }:
            new_actions = []
            for act in actions:
                act, env = generate_c(act, env)
                new_actions.insert(0, act)
            return "\n".join(new_actions), env
        case {
            "type": "DUMP",
        }:
            var = f"_pop_{name_counter()}"
            code = f"    int {var} = pop(&_stack);\n"
            code += f"    printf(\"%d\\n\", {var});\n"
            return code, env
        case {
            "type": "PLUS",
        }:
            a = f"_plus_{name_counter()}"
            b = f"_plus_{name_counter()}"
            code = f"    int {a} = pop(&_stack);\n"
            code += f"    int {b} = pop(&_stack);\n"
            code += f"    push(&_stack, {a} + {b});\n"
            return code, env
        case {
            "type": "MINUS",
        }:
            a = f"_plus_{name_counter()}"
            b = f"_plus_{name_counter()}"
            code = f"    int {a} = pop(&_stack);\n"
            code += f"    int {b} = pop(&_stack);\n"
            code += f"    push(&_stack, {a} - {b});\n"
            return code, env
        case {
            "type": "NUMBER",
            "value": value,
        }:
            code = f"    push(&_stack, {value});"
            return code, env
        case {
            "type": "NAME",
            "value": name,
        }:
            return generate_c(env[name], env)
    
    assert False, f"Unknown parse: {tree}"
        
