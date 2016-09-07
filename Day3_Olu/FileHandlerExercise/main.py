
#to create a set, you use the set function
population = set()

population.add(40)
population.add(80)
population.add(20)
population.add(50)


print(population)

# #empty list
# p = {40, 80, 20, 50}
#
# print(p)

#save the population in a file,
#use the open function
# fw = open("example.txt", "w")
with open("example.txt", "w") as fw:

    fw.write(str(population))

    fw.write("\n")

    for item in population:

        #write to file
        fw.write(str(item))

        fw.write("\n")

    else:
        print("Finished writing")


#read from file
print()
print("Reading file")
with open("example.txt", "r") as fr:

    line = fr.read() #fr.readline()

    print(line)