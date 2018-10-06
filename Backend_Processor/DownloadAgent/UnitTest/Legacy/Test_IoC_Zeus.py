# --====================================================--
# Threat Information Management System (T.I.M.S.)
# Download Agent
# Group 2 - Fall 2018
# Darrell Miller, Doug Peck, Raymond Schmalzl, Trung Nguyen
#
# --====================================================--
#
# Unit Test Object with methods for assessing functionality of
# TIMS Zeus Module

from UnitTest import Test_IoC
from IoC_Modules import IoC_Zeus #Import Emerging Threats IoC

class Test_IoC_Zeus(Test_IoC):

	def setUp(self):
		self.ThreatObject = IoC_Zeus(self.SQLiteDataStore.getDBConn())	

if __name__ == '__main__':
	unittest.main()

