import matplotlib.pyplot as plt

def getDict(array, character):
	for dict in array:
		if dict['Character'] == character:
			return dict
	return False

def printDict(array):
	array = sorted(array, key=lambda k: k['Time used'], reverse=True)
	height = []

	for dict in array:
		height.append(dict['Time used'])
		print(dict)

	plt.bar(len(array), height)

	plt.xlabel('x - axis')
# naming the y-axis
	plt.ylabel('y - axis')
# plot title
	plt.title('My bar chart!')
 
	plt.show()

file = open('livre.txt')
characterMapping = []

for line in file:
	for char in line:
		if char.isalpha():
			dict = getDict(characterMapping, char)

			if dict:
				dict['Time used'] += 1		
			else:
				characterMapping.append({
					"Character": char,
					"Time used": 1
				})

printDict(characterMapping)
