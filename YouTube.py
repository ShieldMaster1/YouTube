import time
import webbrowser

# Color codes
GREEN = '\033[0;32m'
NC = '\033[31m\a\a'  # No Color

print(f"{GREEN}\n"
      f"@#$    @#$    @#@#@#@#    @#@    @#@"
      f" @#$  @#$     @#    @#    @#@    @#@"
      f"  @#4@#$      @#    @#    @#@    @#@"
      f"    @#        @#    @#    @#@    @#@"
      f"    @#        @#    @#    @#@    @#@"
      f"    @#        @#@#@#@#    @#@#@#@#@#\n"
      f"{NC}")

print("Youtube Subscribers Simple Tool")
print("Author: ./Cyber_Dila\n")

id = input("Enter Youtube Channel Name (With @): ")
count = input("Enter the Desired Number of Subscribers: ")

print("Starting Program...")
time.sleep(2)

# Open the YouTube channel in the default web browser
webbrowser.open(f"https://www.youtube.com/{id}")
