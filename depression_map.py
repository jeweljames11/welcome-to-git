# Depression mapping Python script
import datetime
import json
import pprint
import matplotlib.pyplot as plt

# Read current data from JSON file
path_to_data = '/home/pro/Dropbox/Code/Python/data.json'
try :
	file = open(path_to_data,"r")
	data = json.loads(file.read())
	file.close()
	print(data)
except json.decoder.JSONDecodeError:
	data = {}
while True:
	print("1) Add new entry\n2) Plot the graph")
	choice = int(input("(1/2): "))
	if choice == 1:
		# Entering the time data and state
		print("Enter your state [-5 to 5]")
		state = input("Enter state: ")
		time = input("Enter time: ")
		day = input("Enter day: ")
		month = input("Enter month: ")
		if month not in data:
			data[month] = {}
			data[month][day] = {}
		if day not in data[month]:
			data[month][day] = {}
		data[month][day][time] = state
		pprint.pprint(data)
	elif choice == 2:
		# Plotting the graph with the data
		keys = list(data['12']['9'].keys())
		values =list(data['12']['9'].values())
		plt.plot(keys,values)
		plt.show()
	else:
		print("Invalid Choice!")
	print("Again?")
	choice = input("(y/n): ")
	if choice != 'y':
		file = open(path_to_data,"w")
		file.write(json.dumps(data, indent=4, sort_keys=True))
		file.close()
		break
		
