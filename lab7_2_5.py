import numpy as np

data = []
mean = []

gene = ['A2M','FOS','BRCA2','CPOX']

for i in gene:
    print("\nEnter the data of ",i)

    data.append([float(n) for n in input("Enter the data according to different 4 data slots (Seperate using Comma): ").split(',')])

data = np.array(data)

print("\n================================================================")
print(data)

for i in range(len(gene)):
    mean.append([np.mean(data[i]),gene[i]])
    
mean.sort()

m,gene = mean[0]

print("\n================================================================")
print("\n{} having the maximum mean value is := {}".format(gene,m))
