import time
start_time = time.time()

data = [[*map(int, string.split())]#parse data into data
         for string in open('data.txt')]

def find(line):
    diffs = [b-a for a,b in zip(line, line[1:])] #find diffs for passed line 

    return line[-1] + find(diffs) if line else 0

for dir in 1, -1:
    print(sum(find(line[::dir]) for line in data)) # prints sum of diff for each line in data 


end_time = time.time()
execution_time = (end_time - start_time) * 1000  # convert to milliseconds

print("Execution time:", execution_time, "milliseconds\n")