from modules.post_json_aveva import PostJsonAveva

print("a")
postMetadata = PostJsonAveva("metadata")
print (str(postMetadata.sendJson()))
postData = PostJsonAveva("data")
print (str(postMetadata.sendJson()))