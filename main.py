import re
import os
import copy

a, b, c, d = input().split()

txt_files = []
for i in os.listdir("C:/Users/user/PycharmProjects/Grep_Prog"):  # you should delete content which is in os.listdir
    if '.' in i and i.split('.')[-1] == "txt":
        txt_files.append(i)

if d != "*":
    txt_files.clear()
    txt_files = d.split(',')

new_str = c.replace('\"', '')

# -c : This prints only a count of the lines that match a pattern
if a == "grep":
    if b == "-c":
        counter = 0
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:

                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            counter += 1

                        if not line:
                            break
            except Exception as exp:
                print(exp)
        print(counter)

    elif b == "-cR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        counter = 0
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:

                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            counter += 1

                        if not line:
                            break
            except Exception as exp:
                print(exp)
        print(counter)

    # -h : Display the matched lines, but do not display the filenames
    elif b == "-h":
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-hR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    # -i : Ignores, case for matching
    elif b == "-i":
        new_str = fr'\b{new_str.lower()}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if re.search(new_str, line.lower()):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-iR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'\b{new_str.lower()}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if re.search(new_str, line.lower()):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    # -l : Displays list of filenames only.
    elif b == "-l":
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            print(i)
                            break

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-lR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            print(i.split('/')[-1])
                            break

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    # -n : Display the filenames, matched lines and their line numbers.
    elif b == "-n":
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    counter = 0
                    while True:
                        line = f.readline()
                        counter += 1

                        if re.search(new_str, line):
                            print(f'{i}, {counter}, {line}')

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-nR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    counter = 0
                    while True:
                        line = f.readline()
                        counter += 1

                        if re.search(new_str, line):
                            print(f'{i.split('/')[-1]}, {counter}, {line}')

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    # -v : This prints out all the lines that do not match the pattern
    elif b == "-v":
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if not re.search(new_str, line):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-vR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'\b{new_str}\W'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        line = f.readline()

                        if not re.search(new_str, line):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    # -o : Print only the matched parts of a matching line
    elif b == "-o":
        new_str = fr'\S*{new_str}\S*'
        for i in txt_files:
            try:
                with open(i, 'r') as f:

                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            for word in re.findall(new_str, line):
                                print(word)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-oR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'\S*{new_str}\S*'
        for i in txt_files:
            try:
                with open(i, 'r') as f:

                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            for word in re.findall(new_str, line):
                                print(word)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    # -w : Match whole word
    elif b == "-w":
        new_str = fr'{new_str}'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    new_str = fr'{new_str}\S*'
                    while True:
                        line = f.readline()

                        if re.search(new_str, line):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b == "-wR":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        new_str = fr'{new_str.lower()}'
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    new_str = fr'{new_str}\S*'
                    while True:
                        line = f.readline()

                        if re.search(new_str, line.lower()):
                            print(line)

                        if not line:
                            break
            except Exception as exp:
                print(exp)

    elif b[0] == "-" and b[1] == "A" and b[2] == "R":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        line_num = int(b[3:])
        new_str = fr'\b{new_str}\W'

        line_dict = {}
        for i in txt_files:
            counter = []
            counter_new = copy.copy(counter)
            cnt = 0
            try:
                with open(i, 'r') as f:
                    while True:
                        cnt += 1
                        line = f.readline()

                        line_dict[cnt] = line

                        if re.search(new_str, line):
                            counter.append(cnt)

                        if not line:
                            break

                for c in counter:
                    for j in range(c, c + line_num + 1):
                        counter_new.append(j)

                for cn in set(counter_new):
                    print(line_dict.get(cn, ''))

            except Exception as exp:
                print(exp)

    elif b[0] == "-" and b[1] == "A":
        line_num = int(b[2:])
        new_str = fr'\b{new_str}\W'
        counter = []
        counter_new = copy.copy(counter)
        cnt = 0
        line_dict = {}
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        cnt += 1
                        line = f.readline()

                        line_dict[cnt] = line

                        if re.search(new_str, line):
                            counter.append(cnt)

                        if not line:
                            break

                for c in counter:
                    for j in range(c, c + line_num + 1):
                        counter_new.append(j)

                for cn in set(counter_new):
                    print(line_dict.get(cn, ''))

            except Exception as exp:
                print(exp)

    elif b[0] == "-" and b[1] == "B" and b[2] == "R":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        line_num = int(b[3:])
        new_str = fr'\b{new_str}\W'

        line_dict = {}
        for i in txt_files:
            counter = []
            counter_new = copy.copy(counter)
            cnt = 0
            try:
                with open(i, 'r') as f:
                    while True:
                        cnt += 1
                        line = f.readline()

                        line_dict[cnt] = line

                        if re.search(new_str, line):
                            counter.append(cnt)

                        if not line:
                            break

                for c in counter:
                    for j in range(c - line_num, c + 1):
                        counter_new.append(j)

                for cn in set(counter_new):
                    print(line_dict.get(cn, ''))

            except Exception as exp:
                print(exp)

    elif b[0] == "-" and b[1] == "B":
        line_num = int(b[2:])
        new_str = fr'\b{new_str}\W'
        counter = []
        counter_new = copy.copy(counter)
        cnt = 0
        line_dict = {}
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        cnt += 1
                        line = f.readline()

                        line_dict[cnt] = line

                        if re.search(new_str, line):
                            counter.append(cnt)

                        if not line:
                            break

                for c in counter:
                    for j in range(c - line_num, c + 1):
                        counter_new.append(j)

                for cn in set(counter_new):
                    print(line_dict.get(cn, ''))

            except Exception as exp:
                print(exp)

    elif b[0] == "-" and b[1] == "C" and b[2] == "R":
        for i in os.listdir(d.replace('\\', '/')):
            if '.' in i and i.split('.')[-1] == "txt":
                txt_files.append(f'{d.replace('\\', '/')}/{i}')
        line_num = int(b[3:])
        new_str = fr'\b{new_str}\W'

        line_dict = {}
        for i in txt_files:
            counter = []
            counter_new = copy.copy(counter)
            cnt = 0
            try:
                with open(i, 'r') as f:
                    while True:
                        cnt += 1
                        line = f.readline()

                        line_dict[cnt] = line

                        if re.search(new_str, line):
                            counter.append(cnt)

                        if not line:
                            break

                for c in counter:
                    for j in range(c - line_num, c + line_num + 1):
                        counter_new.append(j)

                for cn in set(counter_new):
                    print(line_dict.get(cn, ''))

            except Exception as exp:
                print(exp)

    elif b[0] == "-" and b[1] == "C":
        line_num = int(b[2:])
        new_str = fr'\b{new_str}\W'
        counter = []
        counter_new = copy.copy(counter)
        cnt = 0
        line_dict = {}
        for i in txt_files:
            try:
                with open(i, 'r') as f:
                    while True:
                        cnt += 1
                        line = f.readline()

                        line_dict[cnt] = line

                        if re.search(new_str, line):
                            counter.append(cnt)

                        if not line:
                            break

                for c in counter:
                    for j in range(c - line_num, c + line_num + 1):
                        counter_new.append(j)

                for cn in set(counter_new):
                    print(line_dict.get(cn, ''))

            except Exception as exp:
                print(exp)

    else:
        print("No such command.")
else:
    print("No such command.")
