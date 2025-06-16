import instaloader

loader = instaloader.Instaloader()
nickname = input("enter instagram nickname: ")
dp = nickname
loader.download_profile(dp, profile_pic_only=True)


print(f"Profile picture for {dp} downloaded successfully!")