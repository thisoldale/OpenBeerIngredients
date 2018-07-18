#https://github.com/thisoldale/OpenBeerIngredients

#imports
import csv

#create a blank array to store csv data
results = []

#read the csv file
with open('data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		
	#store csv data in array
	for row in reader:
		results.append(row)
	csvfile.close()

#Debug output	
print(len(results[0]))
print(len(results))
#print(results[0][4])

#variables
num_columns = len(results[0])
num_rows = len(results)

#write the XML file		
with open('output.xml', 'w') as f:
	
	#write file headers
	f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
		'<beer_xml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BeerXML.xsd">\n'
		'\t<version>2.01</version>\n'
		'\t<fermentables>\n')

	#write XML entries
	#loops rows and columns using the column header as the XML tags
	#special cases to eliminate blank entries (or entries with a dash '-')
	#and for 'fine_grind' and 'fine_coarse_difference
	for r in range(1, (num_rows)):
		f.write('\t\t<fermentable>\n')
		for c in range(0, num_columns):
			if results[r][c] != "" and results[r][c] != '-':
				if results[0][c] == 'fine_grind':
					f.write('\t\t\t<yield_dry_basis>\n')
					f.write('\t\t\t\t<' + results[0][c] + '>' + results[r][c] + '</' + results[0][c] + '>\n')
					#checks if 'fine_coarse difference' is blank and adds the closing tag if so
					if results[r][c+1] == "" or results[r][c+1] == '-':
						f.write('\t\t\t</yield_dry_basis>\n')
				elif results[0][c] == 'fine_coarse_difference':
					f.write('\t\t\t\t<' + results[0][c] + '>' + results[r][c] + '</' + results[0][c] + '>\n')
					f.write('\t\t\t</yield_dry_basis>\n')
				else:
					f.write('\t\t\t<' + results[0][c] + '>' + results[r][c] + '</' + results[0][c].split(' ', 1)[0] + '>\n')
		f.write('\t\t</fermentable>\n')

	#write file footers
	f.write('\t</fermentables>\n'
			'</beer_xml>\n')
	f.close()
	
#TODO: 	#what about cases where only fine_grind is entered? ) 