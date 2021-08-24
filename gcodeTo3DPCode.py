import json
import sys

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if len(sys.argv) == 3:
    #SYS Args
    inputFileName = sys.argv[1]
    configFileName = sys.argv[2]
    
    # Load Config
    config = None
    with open(configFileName) as f:
        config = json.load(f)

    #Load GCode
    inputFile = open(inputFileName, "r")
    commands = inputFile.readlines()
    inputFile.close()

    printProgressBar(0, len(commands), prefix = 'Progress:', suffix = 'Complete', length = 50)

    # No. lines replaced
    count = 0
    
    currentApplied = False

    def itemInArrayStartsWith(arr, string):
        for i in arr:
            if i.startswith(string):
                return True
        return False


    i = 0
    while i < len(commands):
        if not (commands[i].startswith(";")):
            if currentApplied:

                for j in config["stopOn"]:
                    jContained = [itemInArrayStartsWith(commands[i].split(" "), k) for k in j]

                    if all(jContained):
                        for k in config["stopCommand"]:
                            commands.insert(i, k + "\n")
                        currentApplied = False
                        count += len(config["startCommand"])
                        i += len(config["startCommand"])
                        break
            else:
                for j in config["startOn"]:
                    
                    jContained = [itemInArrayStartsWith(commands[i].split(" "), k) for k in j]

                    if all(jContained):

                        for k in config["startCommand"]:
                            commands.insert(i, k + "\n")
                        currentApplied = True
                        count += len(config["startCommand"])
                        i += len(config["startCommand"])
                        break

        i += 1
        printProgressBar(i, len(commands), prefix = 'Progress:', suffix = 'Complete', length = 50)


    print("No. Lines Inserted: " + str(count))
    output = "".join(commands)
    f = open("Output.txt", "a")
    f.write(output)
    f.close()

else: 
    print("Please enter Input File and Config File")




# print(inputFile)
# print(configFile)

# text_file = open("Test.gcode", "r")
# commands = text_file.readlines()
# text_file.close()

# i = 0

# while i < len(commands):
#     if "Z10" in commands[i] and i != (len(commands) - 1):
#         commands[i] = commands[i].replace("Z10","")
#         commands.insert(i, "P5\n")

#     if "Z0.3" in commands[i]: 
#         commands[i] = commands[i].replace("Z0.3","")
#         commands.insert(i+1, "P4 I-0.4 R500.0 T0.09 C7\n")

#     i += 1

# commands.append("\n G1 F1000 Z10")


# output = "".join(commands)
# print("".join(commands))
# f = open("Output.txt", "a")
# f.write(output)
# f.close()
