
text_file = open("Test.gcode", "r")
commands = text_file.readlines()
text_file.close()

i = 0

while i < len(commands):
    if "Z10" in commands[i] and i != (len(commands) - 1):
        commands[i] = commands[i].replace("Z10","")
        commands.insert(i, "P5\n")

    if "Z0.3" in commands[i]: 
        commands[i] = commands[i].replace("Z0.3","")
        commands.insert(i+1, "P4 I-0.4 R500.0 T0.09 C7\n")

    i += 1

commands.append("\n G1 F1000 Z10")


output = "".join(commands)
print("".join(commands))
f = open("Output.txt", "a")
f.write(output)
f.close()
