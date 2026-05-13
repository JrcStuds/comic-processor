import os, shutil, cv2

# === CHANGE THESE VALUES === #
watermark_size = (1008, 1600)
normal_size = (1041, 1600)

aspect_ratio = normal_size[0] / normal_size[1]
crop_size = (watermark_size[0], int(watermark_size[0]//aspect_ratio))

trades = os.listdir("trades/")
for trade in trades:
    os.makedirs("temp/")
    shutil.unpack_archive(f"trades/{trade}", "temp/", "zip")

    for file in os.listdir("temp/"):
        page = cv2.imread(f"temp/{file}")
        if (watermark_size[1], watermark_size[0]) == page.shape[:2]:
            cropped_page = page[0:crop_size[1], 0:crop_size[0]]
            cv2.imwrite(f"temp/{file}", cropped_page)

    shutil.make_archive(f"output/{trade}", "zip", "temp/")
    os.rename(f"output/{trade}.zip", f"output/{trade}.cbz")
    shutil.rmtree("temp/")