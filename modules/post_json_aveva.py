from ast import literal_eval
import requests
class PostJsonAveva:
    url = "https://online.wonderware.com/apis/upload/datasource"
    headersJSON = {
        'Content-type' : 'application/json'
    }
    jsonFinal = {}
    type = ""
    headersJSON["Authorization"] = open("token.txt").read()

    def mountJson(self):
        json = open( self.type + ".json", "r").read()       
        if json != "":                      #case type.json isnt empty
            json1 = literal_eval(json)      #cast string to dict
            return json1
        return 204

    def sendJson(self):
        json = self.mountJson()
        if json != 204:
            self.jsonFinal = json
            #print ("url:"+self.url)
            #print ("json:"+str(self.jsonFinal))
            #print ("header:"+str(self.headersJSON))
            #print (self.jsonFinal)
            return requests.post(self.url, json=json, headers=self.headersJSON)
        return {'message' : 'json empty'}, 204
         
    def __init__(self,type):
        self.type = type
