import sqlite3
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "circle.db"
BACKUP_DIR = BASE_DIR / "backups"
MAX_BACKUPS = 30


def create_backup():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"circle_{timestamp}.db"

    source = sqlite3.connect(DB_PATH)
    destination = sqlite3.connect(backup_path)

    try:
        source.backup(destination)
    finally:
        destination.close()
        source.close()

    check = sqlite3.connect(backup_path)
    try:
        result = check.execute("PRAGMA integrity_check;").fetchone()[0]
    finally:
        check.close()

    if result != "ok":
        raise RuntimeError("Backup integrity check failed")

    backups = sorted(
        BACKUP_DIR.glob("circle_*.db"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    for old_file in backups[MAX_BACKUPS:]:
        old_file.unlink()
