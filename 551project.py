import sys

data = dict(dict())
ask = "what do you want to do today\n 1.import\n 2.create table\n 3.view tables\n 4.run query\n 5.exit\n"
num = 0
print("Welcome to data system, what do you want to do today\n")
welcome = input(ask)
names = list()
currentdata = dict()
title = dict()

while welcome != "exit":
    if welcome == "import":
        get = input("Please input file name")
        f = open(get, "r")
        if(f == FileNotFoundError):
            continue
            get = input("Please input file name")
            f = open(get, "r")
        count = 0
        lines = f.readlines()
        titles = lines[0]
        lines.pop(0)
        for line in lines:
            data[num][count] = line.split(",")
            count += 1
        print("loaded " + count + " lines.\n")
        f.close()
        names.append(get)
        title[num] = titles.split(",")
        num += 1

    elif "create table" in welcome:
        print("table " + welcome[13:] + " created\n")
        names.append(welcome[13:])
        titles = input("Please input the columns names, seperate by ,\n")
        title[num] = titles.split(",")
        num += 1

    elif "view" in welcome:
        for x in range(len(names)):
            print(str(x) + ":" + names[x])
        print("Please use the form of 'table(index)' for tables\n")
    
    elif "insert" in welcome:
        indexs = welcome.find("table(")
        indexe = welcome.find(")")
        index = welcome[indexs + 1, indexe]
        currentdata = data[int(index)]
        words = welcome.split()
        currentdata[len(currentdata.keys())] = words[words.index("into")-1]
        data[int(index)] = currentdata
    
    elif "delete" in welcome:
        indexs = welcome.find("table(")
        indexe = welcome.find(")")
        index = welcome[indexs + 1, indexe]
        currentdata = data[int(index)]
        words = welcome.split()
        currentdata.pop(words[words.index("from")-1])
        data[int(index)] = currentdata

    elif "update" in welcome:
        indexs = welcome.find("table(")
        indexe = welcome.find(")")
        index = welcome[indexs + 1, indexe]
        currentdata = data[int(index)]
        newdataend = welcome.find("from")
        words = welcome.split()
        currentdata[len(currentdata.keys())] = words[words.index("from")-1]
        currentdata.pop(welcome[newdataend + 5])
        data[int(index)] = currentdata

    elif "show" in welcome:
        indexs = welcome.find("table(")
        indexe = welcome.find(")")
        index = welcome[indexs + 1, indexe]
        print(title(int(index)) + "\n")
        print(data[int(index)])


    elif "find" in welcome:
        indexs = welcome.find("table(")
        indexe = welcome.find(")")
        index = welcome[indexs + 1, indexe]
        dataindexe = welcome.find("which")
        dataname = welcome[5, dataindexe]
        dataindex = title[int(index)].index(dataname)
        result = list()
        alg = welcome[dataindexe + 5,]
        algb = False
        for a in range(len(data[int(index)])):
            if algb == True: 
                result.append(data[int(index)][dataindex])
        if "group" in welcome:
            cnt = 0
            max = 0
            groupby = welcome[welcome.find("by"),]
            group = title[int(index)].index(groupby)
            for x in data[int(index)][group]:
                if x > max :
                    max = x
                count += 1

    else:
        print("Invalid input, please try again\n")
    
welcome = input(ask)
outputf = open("output.txt", "w")
output = open("output.txt", "a")
output.write(data.items())
output.close()

        
