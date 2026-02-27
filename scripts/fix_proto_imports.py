#!/usr/bin/env python3
import os
from pathlib import Path

# Packages that should not have their imports rewritten
EXCLUDED_PACKAGES = [
    'google.protobuf',
    'collections',
    'typing',
    'typing_extensions',
    'builtins',
    'abc',
    'enum',
    'sys',
    'os',
    'io',
    're',
    'functools',
    'itertools',
]

def rewrite_imports(file_path: str, package_prefix: str) -> None:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        if line.startswith('from '):
            # Check if the import starts with any excluded package
            should_exclude = any(line.startswith(f'from {pkg}') for pkg in EXCLUDED_PACKAGES)
            if not should_exclude and not line.startswith(f'from {package_prefix}'):
                # Add our package prefix
                line = f'from {package_prefix}' + line[5:]
        modified_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(modified_lines)

def process_directory(directory: str, package_prefix: str) -> None:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('_pb2.py') or file.endswith('_pb2.pyi'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                rewrite_imports(file_path, package_prefix)

if __name__ == '__main__':
    proto_dir = Path('src/poktroll_clients/proto')
    prefix = 'poktroll_clients.proto.'
    process_directory(str(proto_dir), prefix)
    print("Done processing protobuf imports!")