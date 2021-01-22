# AvevaInsightTools
Some tools to Aveva Insigth in Python

001 - Post Json 
  just pasta your token in token.txt and save, put yours metadata or data in "metadata.json" or "data.json".
  create an object with "metadata" or "data" on contructor and call sendJson(). Take look at app.py 
 
    from modules.post_json_aveva import PostJsonAveva

    postMetadata = PostJsonAveva("metadata")
    print (str(postMetadata.sendJson()))
    postData = PostJsonAveva("data")
    print (str(postMetadata.sendJson()))

002 - Mount Json
  mount a file (.json) with tags and values
  
    from modules.mountJson import MountJson
    mountjson = MountJson("data")
    mountjson.putTagNow("test",5465464)
    mountjson.putTagNow("test2",123321)
    mountjson.save_file()
