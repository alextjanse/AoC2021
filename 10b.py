f = open('./input/10.txt')

line = f.readline()

# values of the brackets. I use opening brackets so I don't have to
# check what bracket is missing, just what bracket hasn't been closed yet.
values = {'(': 1, '[': 2, '{': 3, '<': 4}

# list of scores of incomplete lines
scores = []

while line != '':
    stack = []
    for c in line:
        if c == '\n': break # oh \n, thou heartless bastard

        if c in '([{<':
            stack.append(c)
        else: # c is a closing bracket
            opening = stack.pop()
            
            if opening == '(' and c == ')' or \
               opening == '[' and c == ']' or \
               opening == '{' and c == '}' or \
               opening == '<' and c == '>': continue

            # opening and closing brackets don't match, line is corrupted
            stack.clear()
            break
    
    score = 0
    while len(stack) > 0:
        c = stack.pop()
        score = 5 * score + values[c]
    
    if score > 0:
        scores.append(score)

    line = f.readline()

scores.sort()

print(scores[len(scores) // 2])