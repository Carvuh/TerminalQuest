import json

## Trying to keep this as abstract as possible.
## Abstract in terms of: nothing should have to be imported into this file besides bare necessities.

class GlobalDatabase:
	
	## This class is strictly for parsing the very large json file that will be procedurally generated.
	# FileHandler.parseGenericJSON()

class FileHandler:

	global parsedPlayerData
	global parsedItemData
	global parsedNPCData

	## Usually data that will be passed as the global DB.
	global genericData
	def parseGenericJSON(filename):
		with open(filename) as data_file:
			genericData = json.load(data_file)

	## This is particularly only for player stats, classes, races, etc.
	## player spells, anything related to the player itself, NOT THE WORLD.
	def parseCharacterSheetData(fileName):
		with open(filename) as data_file:
			parsedPlayerData = json.load(data_file)

	## This is for every item that can currently load into the game.
	## All stats, price, and bio of every item.
	def parseItemSheetData(filename):
		with open(filename) as data_file:
			parsedItemData = json.load(data_file)


	## We'll call this function when we need to write information to a JSON file.
	def writeJson(fileName, jsonDumpVariable):
		## Here thet JSON must already be in a json-compilable format.
		## If not already, will create function to create JSON text.

		with open(fileName, 'w') as outfile:
			json.dump(data, outfile)
