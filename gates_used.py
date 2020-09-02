file = open(r"file.txt") #replace file.txt with path name to cell report text file
buffer = file.read()  # put the file into a variable that can be accessed
file.seek(0)
file.close()

gates = ['inv', 'nand2', 'nand3', 'nand4', 'nor2 ', 'nor3', 'aoi12', 'aoi22', 'oai12', 'oai22', 'dff']
gate_flags = [False for i in range(0, len(gates))]

# check to see what gates are used
for i in range(0, len(gates)):
    if gates[i] in buffer:
        gate_flags[i] = True

# display result
print('{:7}{:6}'.format('Gate', 'Used 1/0'))
for i in range(0, len(gates)):
    print('{:7}{:6}'.format(gates[i], gate_flags[i]))