import os
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

# =====================================================
# CONFIG
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_FOLDER = os.path.join(BASE_DIR, "PORTFOLIO_READY")

TARGET_WIDTH = 1600
TARGET_HEIGHT = 900

BACKGROUND_COLOR = (10, 14, 25)

IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")

# =====================================================
# LOGO FILES (DO NOT MODIFY)
# =====================================================

SKIP_FILES = {
    "cisco.png",
    "college.png",
    "deloitte.png",
    "fav.png",
    "kolhapur-police.png",
    "shivaji-university.png",
    "tata.png",
    "unifiedmentor.png"
}

# =====================================================
# CREATE OUTPUT FOLDER
# =====================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("\n========================================")
print("SMART PORTFOLIO OPTIMIZER STARTED")
print("========================================\n")

# =====================================================
# PROCESS
# =====================================================

for file_name in os.listdir(BASE_DIR):

    if not file_name.lower().endswith(IMAGE_EXTENSIONS):
        continue

    input_path = os.path.join(BASE_DIR, file_name)

    try:

        # =================================================
        # SKIP LOGOS
        # =================================================

        if file_name in SKIP_FILES:

            img = Image.open(input_path)

            output_path = os.path.join(
                OUTPUT_FOLDER,
                file_name
            )

            img.save(output_path)

            print(f"SKIPPED LOGO : {file_name}")

            continue

        # =================================================
        # PROCESS CHARTS
        # =================================================

        img = Image.open(input_path).convert("RGB")

        img = ImageOps.autocontrast(img)

        img = img.filter(ImageFilter.SHARPEN)
        img = img.filter(ImageFilter.SHARPEN)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.08)

        img.thumbnail((TARGET_WIDTH, TARGET_HEIGHT))

        canvas = Image.new(
            "RGB",
            (TARGET_WIDTH, TARGET_HEIGHT),
            BACKGROUND_COLOR
        )

        x = (TARGET_WIDTH - img.width) // 2
        y = (TARGET_HEIGHT - img.height) // 2

        canvas.paste(img, (x, y))

        output_path = os.path.join(
            OUTPUT_FOLDER,
            file_name
        )

        canvas.save(
            output_path,
            quality=100,
            optimize=True
        )

        print(f"OPTIMIZED : {file_name}")

    except Exception as e:
        print(f"ERROR : {file_name}")
        print(e)

print("\n========================================")
print("ALL DONE")
print("========================================\n")