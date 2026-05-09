import os, json, shutil, math, cv2

with open("config.json", "r") as file:
    db = json.load(file)

all_trade_files = os.listdir("trades/")
trade_files = []
for trade in db["trades"]:
    trade_files.append(all_trade_files[trade])

for trade in trade_files:
    shutil.unpack_archive(f"trades/{trade}", "temp/", format="zip")
temp_files = os.listdir("temp/")

i = db["intro"]
for issue in db["issues"]:
    if i >= len(temp_files): break

    if type(issue) == str: issue_name = issue
    else: issue_name = f"{db['default_name']} #{issue}"
    
    os.makedirs(f"temp2/{issue_name}")
    shutil.copy(f"temp/{temp_files[i]}", f"temp2/{issue_name}")
    i += 1

    if str(issue) in db["special_page_counts"]: page_count = db["special_page_counts"][str(issue)]
    else: page_count = db["page_count"]
    if issue in db["buffer_pages"]: page_count += 1

    while page_count > 0:
        if i >= len(temp_files): break

        shutil.copy(f"temp/{temp_files[i]}", f"temp2/{issue_name}")
        i += 1

        image = cv2.imread(f"temp/{temp_files[i]}")
        height, width = image.shape[:2]
        page_count -= math.ceil(width/height)
    
    shutil.make_archive(f"output/{issue_name}", "zip", f"temp2/{issue_name}")
    os.rename(f"output/{issue_name}.zip", f"output/{issue_name}.cbz")

shutil.rmtree("temp/")
shutil.rmtree("temp2/")