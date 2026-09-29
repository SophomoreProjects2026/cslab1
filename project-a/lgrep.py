import sys
import re

def main():
    args = sys.argv[1:]
    
    options = {
        'i': False,
        'v': False,
        'n': False,
        'c': False,
        'w': False
    }
    
    idx = 0
    while idx < len(args) and args[idx].startswith('-'):
        opt_str = args[idx][1:]
        for char in opt_str:
            if char == 'i': options['i'] = True
            elif char == 'v': options['v'] = True
            elif char == 'n': options['n'] = True
            elif char == 'c': options['c'] = True
            elif char == 'w': options['w'] = True
        idx += 1
    
    if idx >= len(args):
        sys.stderr.write("lgrep: usage: lgrep [OPTIONS] PATTERN [FILE...]\n")
        sys.exit(0)

    pattern_str = args[idx]
    files = args[idx+1:]
    if not files:
        files = ['-']

    flags = 0
    if options['i']:
        flags |= re.IGNORECASE
    
    regex_pattern = pattern_str
    if options['w']:
        regex_pattern = r'(?<!\w)' + regex_pattern + r'(?!\w)'
    
    try:
        regex = re.compile(regex_pattern, flags)
    except re.error as e:
        sys.stderr.write(f"lgrep: invalid regular expression: {e}\n")
        sys.exit(0)

    multiple_files = len(files) > 1
    total_count = 0

    for filename in files:
        try:
            if filename == '-':
                f = sys.stdin.buffer
            else:
                f = open(filename, 'rb')
        except Exception as e:
            sys.stderr.write(f"lgrep: {filename}: {e}\n")
            continue

        file_count = 0
        offset = 0
        
        while True:
            line_bytes = f.readline()
            if not line_bytes:
                break
            
            try:
                line_text = line_bytes.decode('utf-8')
            except UnicodeDecodeError:
                line_text = line_bytes.decode('latin-1')

            matches = list(regex.finditer(line_text))
            num_matches = len(matches)
            
            if options['c']:
                if options['v']:
                    if num_matches == 0:
                        file_count += 1
                else:
                    file_count += num_matches
            else:
                selected = False
                if options['v']:
                    if num_matches == 0:
                        selected = True
                else:
                    if num_matches > 0:
                        selected = True
                
                if selected:
                    output = line_text
                    if options['n']:
                        output = f"{offset}:{output}"
                    if multiple_files:
                        output = f"{filename}:{output}"
                    sys.stdout.buffer.write(output.encode('utf-8'))

            offset += len(line_bytes)
        
        f.close()
        
        if options['c']:
            if multiple_files:
                total_count += file_count
            else:
                # If only one file, output the count for that file.
                # The spec says: "When multiple files are used, output the sum of all matches."
                # This implies if only one file is used, we don't necessarily output the sum (which is the same).
                # But for consistency, we can just print the count.
                sys.stdout.buffer.write(f"{file_count}\n".encode('utf-8'))
                # We return to avoid printing the sum again.
                return

    if options['c'] and multiple_files:
        sys.stdout.buffer.write(f"{total_count}\n".encode('utf-8'))

if __name__ == "__main__":
    main()

