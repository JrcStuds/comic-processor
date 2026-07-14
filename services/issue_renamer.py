import zipfile
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


def parse_name(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_file:
        with zip_file.open("ComicInfo.xml") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            series = root.find("Series").text
            title = edit_title(root.find("Title").text)

            if series[-1] == ")":
                bracket_start_idx = series.find("(")
                series = series[:bracket_start_idx-1]

    new_name = f"{series} {title}.cbz"
    return new_name