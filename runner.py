import os

filename = "warning.txt"
message = """
🚫 WARNING 🚫

wowi! You actually downloaded this file.

if it wasnt by me it would definitely already have taken all of your personal infomation

you're Lucky today as
this doesn't do anything harmful.

But this is a lesson:
Don't download random files online.
Especially things like
"vary-reel-friii-robaux-101%-woarking-methad".

Stay safe! and  remember to uninstall this.
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(message)

if os.name == "nt":  
    os.startfile(filename)
elif os.name == "posix":  
    os.system(f"open {filename}")
