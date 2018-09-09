# --====================================================--
# Threat Information Management System (T.I.M.S.)
# Download Agent
# Group 2 - Fall 2018
# Darrell Miller, Doug Peck, Raymond Schmalzl, Trung Nguyen
#
# --====================================================--
#
# Unit Test Object with methods for assessing functionality of
# TIMS Data Store Modules

import unittest
from Backend_Processor.DownloadAgent.DataStore_Modules import DataStore_SQLite #Import SQLite Data Store Object

class DataStore_Internal_UnitTests(unittest.TestCase)

	# /*
	# Example Test Format
	# #Test -- Not Corrected From Java
	# def  ExampleTest(){
	#  // This test should pass
	#  self.assertTrue(1==1)
	# }

	# #Test -- Not Corrected From Java
	# def  ExampleTest2(){
	#  // This test should fail
	#  self.assertTrue(1==0)
	# }
	#  */

	#Test -- Not Corrected From Java
	def  AddResourceToListOfMonitoredResources(self):
		existingList = GetExistingList()
		itemToAdd = dict()
		updatedList = HGMMethods.AddItem(existingList, itemToAdd)
		self.assertTrue(updatedList.contains(itemToAdd))

	#Test -- Not Corrected From Java
	def  AddThreatToDatabaseTest(self):
		String uri = "www.examplelocation.com/databasethreatexample"
		MockDatabase mockDatabase = new MockDatabase()
		ArrayList<HGMObject> importResult = HGMMethods.Import(uri, mockDatabase)
		self.assertTrue(importResult.element.sourceReference == uri)

	#Test -- Not Corrected From Java
	def  ExportThreatListTest(self):
		ArrayList<HGMObject> threats = HGMMethods.GetThreatList()
		ArrayList<String> exportedThreats = HGMMethods.ExportThreatlistToType(threats, HGMType.Text)
		self.assertTrue(exportedThreats.get(1) instanceof String)

	#Test -- Not Corrected From Java
	def  SearchAThreat(self):
		ThreatList = HGMMethods.SearchAThreat(keyword)
		self.assertTrue(ThreatList == ExpectedThreatList)


if __name__ == '__main__':
    unittest.main()