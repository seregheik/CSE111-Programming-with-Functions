with open('courses.txt') as courses:
    for line in courses:
        line=line.strip()
        parts = line.split(',')
        print(parts)