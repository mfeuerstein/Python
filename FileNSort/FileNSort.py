# Read/write to txt file and sorts a list of numbers

infile = open(r'File.txt','r')
try:
    S = infile.readline()
    print('The file contains the following:')
    print(S)

finally:
    infile.close()

outfile = open(r'Write.txt','w')
try:
    S2 = "Poor Dan lost his match"
    outfile.write(S2)

finally:
    outfile.close()

infile2 = open(r'File2.txt','r')
try:
    S3 = infile2.readline()
    print('The file contains the following:')
    print(S3)

finally:
    infile2.close()

numbers = [5,1,7,3,2]
print('Here are your unsorted numbers:')
print(numbers)
numbers.sort()
print('Here are your sorted numbers:')
print(numbers)
