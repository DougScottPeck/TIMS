# --====================================================--
# Threat Information Management System (T.I.M.S.)
# Download Agent
# Group 2 - Fall 2018
# Darrell Miller, Doug Peck, Raymond Schmalzl, Trung Nguyen
#
# --====================================================--
#
# Unit Test Object with methods for assessing functionality of
# TIMS IoC Modules

from UnitTest import Test_IoC
from IoC_Modules import * #Import All Available IoC Modules

class Test_IoC_AlienVault(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_AlienVault(self.SQLiteDataStore.getDBConn())	

class Test_IoC_CSIRTG(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_CSIRTG(self.SQLiteDataStore.getDBConn())	

class Test_IoC_EmergingThreats(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_EmergingThreatsv2(self.SQLiteDataStore.getDBConn())	

class Test_IoC_Feodotracker(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_Feodotracker(self.SQLiteDataStore.getDBConn())	

class Test_IoC_NetLabs360(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_NetLabs360(self.SQLiteDataStore.getDBConn())

class Test_IoC_NoThink(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_NoThink(self.SQLiteDataStore.getDBConn())	

class Test_IoC_OpenPhish(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_OpenPhish(self.SQLiteDataStore.getDBConn())	

class Test_IoC_PhishTank(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_PhishTankv2(self.SQLiteDataStore.getDBConn())	

class Test_IoC_SANsEDU(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_SANsEDU(self.SQLiteDataStore.getDBConn())	

class Test_IoC_SpamHaus(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_SpamHaus(self.SQLiteDataStore.getDBConn())	

class Test_IoC_Zeus(Test_IoC):
	def setUp(self):
		self.ThreatObject = IoC_Zeus(self.SQLiteDataStore.getDBConn())







