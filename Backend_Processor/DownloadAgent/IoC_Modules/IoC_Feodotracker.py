# Feodotracker class with inheritance from IoC_Methods
from .IoC_Methods import IoC_Methods

import urllib.request
import urllib.parse
import datetime
import pprint

class IoC_Feodotracker(IoC_Methods):
    threatCounter = 0
    recordedThreats = dict()  # where threats are stored to put uploaded to database

    def __init__(self,conn):
        IoC_Methods.__init__(self,conn)
        print("FeodoTracker")
    #END Constructor

    def pull(self):
        lineCount = 0
        feodoThreat = dict()
        linkList = [
            "https://feodotracker.abuse.ch/blocklist/?download=ipblocklist",
            "https://feodotracker.abuse.ch/blocklist/?download=domainblocklist"
        ]
        for linkItem in linkList:
            print (linkItem)
            self.TIMSlog['startTime']=datetime.datetime.utcnow()
            threatConfidence = 0
            self.threatCounter=0
            lineCount=0
            threatTags = "feodo,botnet"
            threatLoggerComment = ""
            if linkItem == "https://feodotracker.abuse.ch/blocklist/?download=ipblocklist":
                threatItype = "ipv4"
                threatConfidence = 8
                threatLoggerComment = "ipblocklist"

            if linkItem == "https://feodotracker.abuse.ch/blocklist/?download=domainblocklist":
                threatItype = "fqdn"
                threatConfidence = 6
                threatLoggerComment = "domainblocklist"

            dresponse = urllib.request.urlopen(linkItem)
            ddata = dresponse.read()  # a `bytes` object
            dtext = ddata.decode('utf-8')  # a `str`; this step can't be used if data is binary
            dlist = dtext.split('\n')
            # print (dlist)
            for x in dlist:
                if x.startswith('#'):
                    #print ("skipping line, just a comment")
                    continue  # comment line, just skipping it
                else:
                    feodoThreat['threatkey'] = ""
                    feodoThreat['tlp'] = "green"
                    feodoThreat['reporttime'] = str(datetime.datetime.utcnow())
                    feodoThreat['lasttime'] = str(datetime.datetime.utcnow())
                    feodoThreat['icount'] = 1
                    feodoThreat['itype'] = threatItype
                    feodoThreat['indicator'] = x
                    feodoThreat['cc'] = ""
                    feodoThreat['gps']=""
                    feodoThreat['asn'] = ""
                    feodoThreat['asn_desc'] = ""
                    feodoThreat['confidence'] = threatConfidence
                    feodoThreat['description'] = " Feodo"
                    feodoThreat['tags'] = threatTags
                    feodoThreat['rdata'] = ""
                    feodoThreat['provider'] = "feodotracker.abuse.ch"
                    feodoThreat['enriched'] = 0

                    #tempKey = feodoThreat['indicator'] + ":" + feodoThreat['provider']
                    tempKey = feodoThreat['indicator']
                    feodoThreat['threatkey'] = self.createMD5Key(tempKey)
                    self.recordedThreats[self.threatCounter] = feodoThreat.copy()
                    self.threatCounter += 1
                    feodoThreat.clear()
            self.processData("Feodotracker")
    #End Pull
#End EmergingThreatsv2
