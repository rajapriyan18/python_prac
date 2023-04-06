coun_file=open('D:/Read_Write/countries.txt','r')
print(coun_file.readlines()) #everylines
print(coun_file.readline()) #first one
print(coun_file.readlines()[2])  #which array req


coun_file.close()





for countries in coun_file.readlines():
    print(countries)
coun_file.close()