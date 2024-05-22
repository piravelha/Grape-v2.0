from grape_parser import parser, grape_to_dict, generate_c
import subprocess

with open("Main.grp") as f:
    text = f.read()

code, env = generate_c(grape_to_dict.transform(parser.parse(text)))

with open("out.c", "w") as f:
    f.write("#include <stdio.h>\n")
    f.write("#include \"lib.h\"\n\n")
    f.write("int main() {\n")
    f.write("    Stack _stack;\n")
    f.write("    init(&_stack);\n")
    f.write(code)
    f.write("    return 0;\n")
    f.write("}\n")

subprocess.call(["gcc", "-o", "out", "out.c", "lib.c"])