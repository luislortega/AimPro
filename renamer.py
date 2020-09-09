import os 

foldername = "datasetposff"

for count, filename in enumerate(os.listdir(foldername + "/")): 
    dst ="datasetpos" + str(count) + ".jpg"
    src = foldername + '/'+ filename 
    dst = foldername + '/'+ dst 
    os.rename(src, dst) 
  