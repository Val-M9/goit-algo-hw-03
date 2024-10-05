import sys
from pathlib import Path
import shutil


source = Path(sys.argv[1])
destination = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')


def copy_files(source: Path, destination: Path) -> None:
    try:
        for p in source.iterdir():
            if p.is_dir():
                copy_files(p, destination)
            else:
                extension = p.suffix if p.suffix else 'others'
                new_path = destination / extension
                new_path.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, new_path / p.name)
    except FileNotFoundError as e:
        print(f'Sorry, input directory was not found! {e}')
    except Exception as e:
        print(f'Sorry, an error ocurred! {e}')


copy_files(source, destination)
