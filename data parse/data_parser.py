#!/usr/bin/env python
import sys, ast

if __name__ == "__main__":
    print("blablabla")
    output_file_name = sys.argv[1]
    print(output_file_name)
    with open(output_file_name, "w") as f:
        for line in sys.stdin:
            try:
                output = int(line)
            except Exception as e:
                f.write("\n"+line.rstrip())
                continue

            f.write(","+str(output))
    
        f.write("\n")