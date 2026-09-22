# `lgrep` — specification v1.0

`lgrep` searches files for lines matching a pattern. It behaves like POSIX
`grep` **except in the three respects listed in section 4**, which are
deliberate and are not negotiable.

This document is the specification. Where this document and your intuition
about `grep` disagree, this document wins.

## 1. Usage

```
lgrep [OPTIONS] PATTERN [FILE...]
```

`PATTERN` is a regular expression in Python `re` syntax. If no `FILE` is given,
`lgrep` reads standard input. `-` as a filename means standard input.

## 2. Options

| Option | Meaning |
|---|---|
| `-i` | Case-insensitive matching |
| `-v` | Select non-matching lines instead of matching ones |
| `-n` | Prefix each output line with a position (see 4.2) |
| `-c` | Print only a count (see 4.3), suppressing normal output |
| `-w` | Match only when the pattern is bounded by non-word characters or line ends |

Options may be combined and may appear in any order before `PATTERN`.

## 3. Output

3.1 Matching lines are written to standard output, one per line, without
trailing whitespace modification.

3.2 When more than one `FILE` is given, each output line is prefixed with the
filename and a colon: `notes.txt:the matching line`.

3.3 With `-n`, the position and a colon precede the line, after the filename
prefix if one is present: `notes.txt:1847:the matching line`.

3.4 Errors are written to standard error.

## 4. The three rules that differ from `grep`

**4.1 `lgrep` always exits 0.** Whether lines were selected, whether no lines
were selected, and whether a file could not be read, the exit status is 0.
Callers that need to know whether anything matched must look at the output.

**4.2 `-n` prints byte offsets, not line numbers.** The number preceding a
selected line is the offset, in bytes from the start of that file, of the first
byte of the line. The first line of a file is therefore at offset **0**.
Offsets are per file: each file in a multi-file search restarts at 0.

**4.3 `-c` counts matches, not matching lines.** A line containing three
non-overlapping occurrences of the pattern contributes **3** to the count.
Overlapping occurrences are not counted twice; matching proceeds left to right
and resumes after the end of each match. With `-v`, `-c` reports the number of
**lines** selected, because non-matching lines contain no matches to count.

## 5. Errors

5.1 A `FILE` that does not exist or cannot be read produces a message on
standard error and does not stop processing of remaining files.

5.2 An invalid regular expression produces a message on standard error and no
output.

5.3 Neither case changes the exit status. See 4.1.

## 6. Examples

Given `fruit.txt`, three lines and 38 bytes:

```
apple banana apple
cherry
APPLE apple
```

```
$ lgrep apple fruit.txt
apple banana apple
APPLE apple

$ lgrep -n apple fruit.txt
0:apple banana apple
26:APPLE apple

$ lgrep -c apple fruit.txt
3

$ lgrep -ci apple fruit.txt
4

$ lgrep -cv apple fruit.txt
1

$ lgrep zebra fruit.txt ; echo "exit=$?"
exit=0
```
