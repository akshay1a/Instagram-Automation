from instagrapi import Client
import os

cl = Client()
cl.login(username=input("please enter your ID: "), password=input("please enter your password: "))


def func():
    b = input("Enter caption for the post: ")
    a = input("What media do you want to upload? Reels or Photos?\n Enter 1 for reels and 2 for photos: ")
    if a == '1':
        dir_reel = input("Now enter the folder location\nExample:'C:/Users/computer/Desktop/insta/reels/'\nLoc: ")
        for clip in os.listdir(dir_reel):
            cl.clip_upload(dir_reel + clip, caption=b)
    elif a == '2':
        dir_image = input("Now enter the folder location\nExample:'C:/Users/computer/Desktop/insta/images/'\nLoc: ")
        for image in os.listdir(dir_image):
            cl.photo_upload(dir_image + image, caption=b)


func()
while True:
    x = input("\nEnter 1 to continue or 0 to exit: ")
    if x == '1':
        func()
    elif x == '0':
        print('Bye! See You Next Time...')
        break
