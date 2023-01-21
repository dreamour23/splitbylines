Input = input('Please give name of the textfile: ')

textfile = Input + '.txt'

print(textfile)

def chunks(l, n):
    """Chunks iterable into n sized chunks"""
    for i in range(0, len(l), n):
        yield l[i:i + n]

# Collect all lines, without loading whole file into memory
lines = []
with open(textfile,encoding='utf-8') as main_file:
    for line in main_file:
        lines.append(line)

# Write each group of lines to separate files
for i, group in enumerate(chunks(lines, n=400000), start=1):
    with open('File%d.txt' % i, encoding='utf-8',mode="w") as out_file:
        for line in group:
            out_file.write(line)
