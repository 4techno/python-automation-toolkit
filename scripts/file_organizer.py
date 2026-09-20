import os
import sys
import shutil
from pathlib import Path

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json", ".cpp", ".c"],
    "Audio_Video": [".mp3", ".mp4", ".mkv", ".wav", ".avi"]
}

def organize_directory(target_path: str, dry_run: bool = False):
    target = Path(target_path).expanduser().resolve()
    if not target.exists() or not target.is_dir():
        print(f"Error: Directory '{target}' does not exist.")
        sys.exit(1)
        
    print(f"Organizing directory: {target} (Dry-run: {dry_run})")
    
    moved = 0
    for item in target.iterdir():
        if item.is_dir() or item.name.startswith("."):
            continue
            
        ext = item.suffix.lower()
        matched_category = "Other"
        for category, extensions in EXTENSIONS.items():
            if ext in extensions:
                matched_category = category
                break
                
        dest_dir = target / matched_category
        if not dry_run and not dest_dir.exists():
            dest_dir.mkdir(parents=True, exist_ok=True)
            
        dest_file = dest_dir / item.name
        print(f" -> Moving '{item.name}' to '{matched_category}/'")
        if not dry_run:
            shutil.move(str(item), str(dest_file))
        moved += 1
        
    print(f"Completed: Processed {moved} files.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    is_dry = "--dry-run" in sys.argv
    organize_directory(path, dry_run=is_dry)
