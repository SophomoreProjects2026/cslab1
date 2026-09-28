import subprocess
import sys

def run_lgrep(args):
    # Using sys.executable to ensure we use the same python interpreter
    result = subprocess.run([sys.executable, 'lgrep.py'] + args, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

with open('fruit.txt', 'w', encoding='utf-8') as f:
    f.write("apple banana apple\n")
    f.write("cherry\n")
    f.write("APPLE apple\n")

print("Running 'lgrep apple fruit.txt':")
print(run_lgrep(['apple', 'fruit.txt'])[0])

print("\nRunning 'lgrep -n apple fruit.txt':")
print(run_lgrep(['-n', 'apple', 'fruit.txt'])[0])

print("\nRunning 'lgrep -c apple fruit.txt':")
print(run_lgrep(['-c', 'apple', 'fruit.txt'])[0])

print("\nRunning 'lgrep -ci apple fruit.txt':")
print(run_lgrep(['-ci', 'apple', 'fruit.txt'])[0])

print("\nRunning 'lgrep -cv apple fruit.txt':")
print(run_lgrep(['-cv', 'apple', 'fruit.txt'])[0])
