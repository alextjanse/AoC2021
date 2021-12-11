f = open('./input/10.txt')

line = f.readline()

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

total_score = 0

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

            # opening and closing brackets don't match
            total_score += scores[c]
            break

    line = f.readline()

print(total_score)