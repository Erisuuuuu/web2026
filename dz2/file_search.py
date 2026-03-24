import os
import sys

def find_and_print(script_dir, target_name, current_dir=None):
    if current_dir is None:
        current_dir = script_dir
    try:
        for entry in sorted(os.listdir(current_dir)):
            full = os.path.join(current_dir, entry)
            if os.path.isfile(full) and entry == target_name:
                with open(full, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f):
                        if i >= 5:
                            break
                        print(line.rstrip())
                return True
            if os.path.isdir(full):
                os.chdir(full)
                if find_and_print(script_dir, target_name, full):
                    return True
                os.chdir('..')
    except PermissionError:
        pass
    return False

if __name__ == '__main__':
    target = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    if not find_and_print(script_dir, target):
        print(f"Файл {target} не найден")
