import os 

foldername = "datasetnegff"

for count, filename in enumerate(os.listdir(foldername + "/")): 
    dst = foldername + str(count) + ".jpg"
    src = foldername + '/'+ filename 
    dst = foldername + '/'+ dst 
    os.rename(src, dst) 
  