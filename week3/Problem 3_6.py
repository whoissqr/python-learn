import sys

def problem3_6(file1, file2): 
    infile = open(file1,'r') 
    outfile= open(file2,'w')
    for line in infile:
        outfile.write(str(len(line.strip("\n"))))
        outfile.write("\n")
    infile.close()
    outfile.close()

if __name__ == "__main__":
    problem3_6(sys.argv[1], sys.argv[2])
