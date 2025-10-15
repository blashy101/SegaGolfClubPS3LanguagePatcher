# -*- coding: utf-8 -*-
import os
import shutil
import sys

def main():
    print("Place me in PS3_GAME\\USRDIR\\MEDIA\n")
    print("1. English")
    print("2. German (*)")
    print("3. Spanish (*)")
    print("4. French (*)")
    print("5. Italian (*)")
    print("(* Accent marks not currently supported)\n")

    choice = input("Select a language (1-5): ").strip()

    cwd = os.path.basename(os.getcwd())
    if cwd.upper() != "MEDIA":
        print("\n[Error] This script must be placed and run inside the 'MEDIA' directory.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    mapping = {
        "1": ("ENGLISH", "ENGLISH"),
        "2": ("DEUTSCH", "DEUTSCH"),
        "3": ("ESPANOL", "ESPANOL"),
        "4": ("FRANCAIS", "FRANCAIS"),
        "5": ("ITALIANO", "ITALIANO")
    }

    if choice not in mapping:
        print("\n[Error] Invalid selection.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    lang_dir, lang_text = mapping[choice]

    sprite_path = os.path.join(os.getcwd(), "SPRITE")
    src_dir = os.path.join(sprite_path, lang_dir)
    dst_dir = os.path.join(sprite_path, "JAPANESE")

    if not os.path.isdir(src_dir):
        print(f"\n[Error] Missing source directory: {src_dir}")
        input("\nPress Enter to exit...")
        sys.exit(1)

    if not os.path.isdir(dst_dir):
        print(f"\n[Error] Missing destination directory: {dst_dir}")
        input("\nPress Enter to exit...")
        sys.exit(1)

    for item in os.listdir(dst_dir):
        item_path = os.path.join(dst_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

    for item in os.listdir(src_dir):
        s = os.path.join(src_dir, item)
        d = os.path.join(dst_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    text_path = os.path.join(os.getcwd(), "TEXT")
    src_file = os.path.join(text_path, f"GLF_TEXT_{lang_text}.DAT")
    dst_file = os.path.join(text_path, "GLF_TEXT_JAPANESE.DAT")

    if not os.path.exists(src_file):
        print(f"\n[Error] Missing source text file: {src_file}")
        input("\nPress Enter to exit...")
        sys.exit(1)

    if os.path.exists(dst_file):
        os.remove(dst_file)
    shutil.copy2(src_file, dst_file)

    print("\nOperation Completed Successfully!")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
