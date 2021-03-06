""" the error log contains all of the errors that the program encounters"""
error_log = []

"""the command list contains all of the commands for the program"""
command_list = []

""" the stacks variable holds all of the natural values of the stacks starting at 0"""
stacks = []

"""holds the index of the current line being run"""
line_num = 0

"""this function halts the code because an error has occured"""
def halt_code(line):
    global line_num
    line_num = len(command_list)
    error_log.append("CODE HALTED FOR FATAL ERROR AT LINE |" + str(line) + "| ")
    
"""the increment function. increments stack a"""
def increment(line,a):
    try:
        stacks[a] += 1
    except:
        if len(stacks) <= a:
            error_log.append("error at line |"+str(line)+"| Tried to increment stack that didnt yet exist ")
            while len(stacks) <= a:
                stacks.append(0)
            stacks[a] += 1
            
"""the decrement function. decrements stack a if a is greater then zero."""
def decrement(line,a):
    try:
        stacks[a] -= 1
        if stacks[a] < 0:
            error_log.append("error at line |"+str(line)+"| Tried to decrement stack that was allready at zero ")
            stacks[a] += 1
            halt_code(line)
    except:
        if len(stacks) <= a:
            error_log.append("|"+str(line)+"| Tried to decrement stack that didnt yet exist")
            while len(stacks) <= a:
                stacks.append(0)
            stacks[a] -= 1
            
"""the copy function. copys the contents of stack a into stack b"""
def copy(line,a,b):
    try:
        stacks[b] = stacks[a]
    except:
        if len(stacks) <= a:
            error_log.append("error at line |"+str(line)+"| tried to copy from stack that didnt exist. stack:"+str(a))
            while len(stacks) <= a:
                stacks.append(0)
        if len(stacks) <= b:
            error_log.append("error at line |"+str(line)+"| tried to copy to stack that didnt exist. stack:"+str(b))
            while len(stacks) <= b:
                stacks.append(0)
        stacks[b] = stacks[a]

"""the test function. if stack a is = to zero then goto line b."""
def test(line,a,b):
    global line_num
    try:
        if stacks[a] == 0:
            line_num = b-1
        else:
            pass
    except:
        if len(stacks) <= a:
            error_log.append("error at line |"+str(line)+"| Tried to test stack that didnt yet exist ")
            while len(stacks) <= a:
                stacks.append(0)
        line_num = b-1
            
"""the goto function. goto line a."""
def goto(line,a):
    global line_num
    line_num = a-1
    
"""the run function. go's through all the commands in command_list and runs them."""
def run():
    global line_num
    while line_num < len(command_list):

        command = command_list[line_num]
        if command[1] == "inc":
            increment(command[0],command[2])
        elif command[1] == "dec":
            decrement(command[0],command[2])
        elif command[1] == "tes":
            test(command[0],command[2],command[3])
        elif command[1] == "got":
            goto(command[0],command[2])
        elif command[1] == "cop":
            copy(command[0],command[2],command[3])
        else:
            error_log.append("error at line |"+str(command[0])+"| Command not found: " + str(command[1]))
        
        line_num += 1

    
"""This is the area where test programs are written does not change the function of the machine """





""""-----------------------------------the test area has finished.------------------------------"""

"""the code that runs the program and prints all errors"""
run()
print stacks
for error in error_log:
    print error




