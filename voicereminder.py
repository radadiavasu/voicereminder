import instaloader

root = instaloader.Instaloader()
usr_name = "mr.sd_1235"
print(root.download_profile(usr_name,profile_pic_only=True))