# --====================================================--
# Threat Information Management System (T.I.M.S.)
# Download Agent
# Group 2 - Fall 2018
# Darrell Miller, Doug Peck, Raymond Schmalzl, Trung Nguyen
#
# --====================================================--
#
# simple methods used for internal data stucture/database
# used as internal datastore to consolidate all data from all sources

from pprint import pprint
from datetime import datetime
import _sqlite3

class SQLiteDataStore:

    threatLibrary = dict()
    sqlStringDict = dict()
    log = dict()
    errorLog = dict()

    def __init__(self, threatResults):
    #def __init__(self):
        # clearing variables and setting up the log counters
        # --===========================================--
        self.log['lineCount'] = 0
        self.log['newCount'] = 0
        self.log['dupeCount'] = 0
        self.log['startTime'] = datetime.now()
        self.log['endTime'] = ""
        self.log['sqlEntries'] = 0
        self.log['SQLErrorCount'] = 0
        self.threatLibrary = threatResults.copy()
        # --===========================================--
        print ("Connecting to SQLite DB for storing IOCs..")
    # end constructor

    def checkDBForDuplicate(self, key, con):
        cursor = con.cursor()
        sqlString = "SELECT * FROM `RecordedThreatsDB` WHERE `indicator` ="
        sqlString += "'" + key + "'"
        cursor.execute(sqlString)
        msg = cursor.fetchone()
        if (cursor.rowcount) > 0:
            self.log['dupeCount'] += 1
            print ("dupe")
            return 1
        else:
            self.log['newCount'] += 1
            print ("nope,new")
            return 0
    # checkDBForDuplicate

    def insertRowIntoDB(self, sqlString,con):
        print (sqlString)
        cursor = con.cursor()
        cursor.execute(sqlString)
    # END insertRowIntoDB

    def processNewThreats(self):
        threatCounter = 1
        totalThreats = len(self.threatLibrary)
        currentDateTime = datetime.now()

        con = _sqlite3.connect('../../Threats.sqlite', detect_types=_sqlite3.PARSE_DECLTYPES)
        cursor = con.cursor()
        print ("--===================--")

        for item in self.threatLibrary:
            if self.checkDBForDuplicate(item, con) == 0:
                print("[", threatCounter, "/", totalThreats, "]", "Checking Database for Record:", item, ": New Threat")
                cursor.execute("INSERT INTO RecordedThreatsDB VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               [self.threatLibrary[item]['tlp'],
                                self.threatLibrary[item]['lasttime'],
                                self.threatLibrary[item]['reporttime'],
                                self.threatLibrary[item]['icount'],
                                self.threatLibrary[item]['itype'],
                                self.threatLibrary[item]['indicator'],
                                self.threatLibrary[item]['cc'],
                                self.threatLibrary[item]['gps'],
                                self.threatLibrary[item]['asn'],
                                self.threatLibrary[item]['asn_desc'],
                                self.threatLibrary[item]['confidence'],
                                self.threatLibrary[item]['description'],
                                self.threatLibrary[item]['tags'],
                                self.threatLibrary[item]['rdata'],
                                self.threatLibrary[item]['provider'],
                                self.threatLibrary[item]['threatkey'],
                                str(currentDateTime),
                                self.threatLibrary[item]['enriched'],
                                ])
                if threatCounter%5000==0: #saves db every 5000 records
                    con.commit()
            else:
                print("[", threatCounter, "/", totalThreats, "] Checking Database for Record:", item,
                      ": Already in Database")
            threatCounter += 1
        con.commit()
        con.close()
        print ("--===================--")
    # end processNewThreats

    def showDataInThreatDB(self):
        threatCounter = 1
        totalThreats = len(self.threatLibrary)

        con = _sqlite3.connect('../../Threats.sqlite', detect_types=_sqlite3.PARSE_DECLTYPES)
        cursor = con.cursor()
        print(str(datetime.now()))
        cursor.execute("SELECT * FROM RecordedThreatsDB;")
        print(cursor.fetchall());

        print("## ALL THREATS!! ##")
        # pprint (self.threatLibrary)
        print("## Done ## ")
    #end showDataInThreatDB

#end SQLiteDataStore

