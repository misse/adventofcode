
def add(x,y,z):
    program[z] = x + y

def times(x,y,z):
    program[z] = x * y
def doit(program, noun, verb):
    for pos, num in enumerate(program):
        if pos == 0 or pos % 4 == 0:
            x = program[program[pos + 1]]
            y = program[program[pos + 2]]
            z = program[pos + 3]
            if num == 1:
                add(x,y,z)
            elif num == 2:
                times(x,y,z)
            elif num == 99:
                break
    return program

noun = 0
verb = 0

while noun <= 99:
    while verb <= 99:
        program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
        program[1] = noun
        program[2] = verb
        programresult = doit(program, noun, verb)
        if programresult[0] == 19690720:
            print(noun, verb, programresult[0])
        verb += 1
    noun += 1
    verb = 0
