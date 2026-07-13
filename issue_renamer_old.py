import os, shutil, zipfile
import xml.etree.ElementTree as ET


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False
    

def edit_title(string: str):
    title = string

    if "annual" in title.lower():
        if title[0] == "#":
            title = title[1:]
        if title[7] != "#":
            title = title[:7] + "#" + title[7:]
    
    if "issue" in title.lower():
        if title[0] == "#":
            title = title[1:]
        title = title[6:]

    if not "annual" in title.lower():
        if title[0] != "#":
            title = "#" + title
    
    return title


input_dir = "trades/"
output_dir = "output/"
all_issues = os.listdir(input_dir)
for issue in all_issues:

    with zipfile.ZipFile(input_dir+issue, "r") as zip_file:
        with zip_file.open("ComicInfo.xml") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            series = root.find("Series").text
            title = edit_title(root.find("Title").text)

            if series[-1] == ")":
                bracket_start_idx = series.find("(")
                series = series[:bracket_start_idx-1]
    
    new_name = f"{series} {title}.cbz"
    os.rename(input_dir+issue, output_dir+new_name)