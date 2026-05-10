import os, shutil

all_issues = os.listdir("trades/")
os.makedirs("temp/")
for issue in all_issues:
    shutil.unpack_archive(f"trades/{issue}", "temp/", "zip")
shutil.make_archive("output/trade", "zip", "temp/")
os.rename("output/trade.zip", "output/trade.cbz")
shutil.rmtree("temp/")



"""
Place every issue in the trades folder and a file named 'trade.cbz' will appear in the output folder that compiles every issue
"""