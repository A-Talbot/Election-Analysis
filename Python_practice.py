counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for i, j in counties_dict.items():
    print(i,"county has ", j," registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")