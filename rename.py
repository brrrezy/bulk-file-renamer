import os
import sys


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def panel(title):
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)


def main():
    clear()
    panel("BULK FILE RENAMER")

    print()
    path = input("📁 Paste folder path: ").strip()
    print()

    if not os.path.exists(path):
        print("❌ Invalid path. Exiting...")
        sys.exit()

    file_list = os.listdir(path)

    if len(file_list) == 0:
        print("⚠️  No files found in this folder.")
        sys.exit()

    print(f"✅ Found {len(file_list)} files")
    print()

    prefix = input("🔤 Enter prefix: ").strip()
    print()

    print("Renaming files...\n")

    count = 1
    for filename in file_list:
        old_path = os.path.join(path, filename)

        if os.path.isfile(old_path):
            suffix = str(count).zfill(3)
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}_{suffix}{ext}"
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            print(f"✔ {filename}  →  {new_name}")
            count += 1

    print()
    print("=" * 50)
    print(f"🎉 {count - 1} files successfully renamed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
