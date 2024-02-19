# place your code to clean up the data file below.
f1 = open('./data/FYFSD-2.csv','r')
lines1 = f1.readlines()

f2 = open('./data/fredgraph-2.csv','r')
lines2 = f2.readlines()

f3 = open('./data/NGDPSAXDCUSQ.csv','r')
lines3 = f3.readlines()

newline = []
newline.append("Year,Budget Deficit,Export,Import\n")


# since the data is recorded according to the fiscal year (in millions of dollars)
# I use the data on the date to represent the whole year
# and calculated them as percentages of the nominal GDP
# they're formatted to two decimal points
for i in range(len(lines1)-1):
    words = lines1[i+1].strip().split(',')
    words1 = lines3[i+1].strip().split(',')
    newline.append(words[0][:4] + "," + format(float(words[1])*100/float(words1[1]), ".2f"))



# I downloaded the data of exports and imports anually aggregating by the average (in billions of dollars)
# and calculated them as percentages of the nominal GDP
# they're formatted to two decimal points
for i in range(len(lines2)-1):
    words = lines2[i+1].split(',')
    words1 = lines3[i+1].strip().split(',')
    newline[i+1] = newline[i+1] + "," + format(float(words[1])*100000/float(words1[1]), ".2f") + "," + format(float(words[2])*100000/float(words1[1]), ".2f") + "\n"

# print(newline)

newf = open('./data/clean_data.csv', 'w')

for i in range(len(newline)):
    newf.write(newline[i])

