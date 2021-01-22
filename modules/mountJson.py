from datetime import datetime
from resourse.error_log import ERROR_LOG

class MountJson:

    def putDateTime(self):
        now = datetime.now()
        return self.putTag("dateTime",str(now.date()) + "T" + str(now.time()) + "Z")

    def putTag(self,tag,value):
        self.jsonBuffer[tag] = value
        return self.jsonBuffer

    def putTagNow(self,tag,value):  # insta create a data with datatime and tag
        self.putDateTime()
        self.putTag(tag,value)
        self.inserJson()
        self.jsonBuffer = {}     

    def inserJson(self):
        return self.json[self.type].append(self.jsonBuffer)
    
    def save_file(self):
        return open(self.type + ".json", "w").write(str(self.json))

    def resetJson(self):
        self.jsonBuffer = {}
        self.json = {
            self.type : []
        }
        return self.jsonBuffer, self.json

    def __init__(self,type):
        if type == "data" or type == "metadata":
            print("obj created")
            self.type = type
            self.resetJson()
        else:
            print("Fail to create")
