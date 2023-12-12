data = [[*map(int, string.split())]#parse data into data
    for string in open('data.txt')]
def find(line):
    diffs = [b-a for a,b in zip(line, line[1:])] #find diffs for passed line 
    return line[-1] + find(diffs) if line else 0
for dir in 1, -1: #find the sum in both directions 
    print(sum(find(line[::dir]) for line in data))