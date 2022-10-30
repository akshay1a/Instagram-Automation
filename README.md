# Instagram-Automation
We can upload daily content post, videos and even reels of today's gen with the help of this library. 
```Python
  from instagrapi import Client
```
## With the code you can do the following tasks:
    1. Login to you Instagram Account
    2. Uploading photos with specified caption from specified location.
    3. Uploading media in form of reels with specified caption from specified location.
    4. Uploading any media in bulk.

## Installation
  Download this repo and extract the login.py file from ZIP for your use.
  
## Usage 
```Python
  from instagrapi import Client
  import os
  
  #login to your account
  cl = Client()
  cl.login(username=input("please enter your ID: "), password=input("please enter your password: "))
  
  #Code to upload reels
   dir_reel = input("Now enter the folder location\nExample:'C:/Users/computer/Desktop/insta/reels/'\nLoc: ")
        for clip in os.listdir(dir_reel):
            cl.clip_upload(dir_reel + clip, caption=b)
            
  #Code to upload images
  dir_image = input("Now enter the folder location\nExample:'C:/Users/computer/Desktop/insta/images/'\nLoc: ")
        for image in os.listdir(dir_image):
            cl.photo_upload(dir_image + image, caption=b)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

***

&copy; Copyrights Claimed by Akshay Arora
