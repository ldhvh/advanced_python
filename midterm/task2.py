print()
import os
def print_docs(directory):
    for (a, b, c) in os.walk(directory):
        for f in c:
             print(f)
dir = "C://Users//user//eclipse"
print_docs(dir)
