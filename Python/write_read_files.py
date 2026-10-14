"""
File Handling in Python
    Python makes reading and writing files pretty simple using the built-in open() function.
"""

# Opening a File
# file = open("filename.txt", "mode")

"""
Common modes:
Mode	Meaning
----    --------------------------------------
'r'	    Read (default) — file must exist
'w'	    Write — creates file if missing, overwrites existing content
'a'	    Append — adds to end of file, creates if missing
'x'	    Create — fails if file already exists
'r+'	Read and write
'b'	    Binary mode (combine with above, e.g. 'rb', 'wb')
't'	    Text mode (default)
"""
#--------------------------------------------------------------------------------
# Writing to a File

# Overwrite (or create) the file
with open("notes.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a new line.\n")

# Append to the file
with open("notes.txt", "a") as f:
    f.write("Adding another line.\n")

# write() writes a string as-is (no automatic newline). Use \n explicitly, or writelines() for a list of strings:
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("notes.txt", "a") as f:
    f.writelines(lines)

#--------------------------------------------------------------------------------
# Reading a File
# Read entire file as one string
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
    '''
        Hello, world!
        This is a new line.
        Adding another line.
        First line
        Second line
        Third line
    '''

# Read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()   # ['First line\n', 'Second line\n', ...]

# Read one line at a time
with open("notes.txt", "r") as f:
    line = f.readline()

# Loop through file line by line (memory-efficient for large files)
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes the trailing newline

#--------------------------------------------------------------------------------
"""
Why with open(...) as f: matters ?
    The with statement is the recommended way to handle files because it automatically closes the
    file for you, even if an error occurs inside the block.
"""
with open("notes.txt", "r") as f:
    data = f.read()
# file is automatically closed here

# Without with, you'd have to close it manually:
f = open("notes.txt", "r")
data = f.read()
f.close()  # easy to forget, especially if an exception happens first
#----------------------------------------------------------------------------------
# Handling Errors
# Since reading a nonexistent file raises an error, it's good practice to handle it:
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist.")
#----------------------------------------------------------------------------------
# Working with Binary Files (e.g. images)
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)
#----------------------------------------------------------------------------------
# Quick Reference Summary

# Write
with open("file.txt", "w") as f:
    f.write("some text")

# Append
with open("file.txt", "a") as f:
    f.write("more text")

# Read all
with open("file.txt", "r") as f:
    text = f.read()

# Read lines
with open("file.txt", "r") as f:
    for line in f:
        print(line)
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
""" Working with CSV, JSON, and pathlib """

############## CSV Files ###############
"""
A CSV file (Comma-Separated Values file) is a simple text file used to store data in a table
    format, where each line is a row and the values are usually separated by commas.
Example:
    Name,Age,City
    Rahul,25,Delhi
    Anita,23,Mumbai

In simple words: A CSV file stores table-like data as plain text.
"""
#---------------------------------------------------------------------------------
# Reading CSV:
import csv

with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # row is a list of strings, e.g. ['Alice', '25', 'NYC']

#---------------------------------------------------------------------------------
# Reading as dictionaries (using the header row as keys):
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row["name"], row["age"])
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
# Writing CSV:
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 25, "NYC"])
    writer.writerow(["Bob", 30, "LA"])
#---------------------------------------------------------------------------------
# Writing from dictionaries:
data = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"},
]
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

"""
Note: always pass newline="" when opening CSV files — it prevents extra blank lines on Windows.
"""
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
############## JSON Files ###############
"""
The json module converts directly between Python objects (dicts, lists) and JSON text.
"""
import json

with open("data.json", "r") as f:
    data = json.load(f)   # returns a dict or list
    print(data)
print(data["name"])

#---------------------------------------------------------------------------------
# Writing JSON:
data = {"name": "Alice", "age": 25, "hobbies": ["reading", "coding"]}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)   # indent=4 makes it human-readable

#---------------------------------------------------------------------------------
# Converting to/from JSON strings (not files) — useful for APIs:
json_string = json.dumps(data)      # dict -> string
print(json_string)
parsed = json.loads(json_string)    # string -> dict
print(parsed)

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
############ Using pathlib (modern, cleaner path handling) ###################

data = "C:\\Users\\rbr100\\OneDrive - Cambium Networks Limited\\Documents\\PycharmProjects\\Practice\\Python"

from pathlib import Path

p = Path(data) / "notes.txt"   # cross-platform path joining (no manual '/' or '\')

# Read/write shortcuts — no need for `with open(...)`
text = p.read_text()
print(text)
p.write_text("Hello, world!")

# Binary equivalents
data = p.read_bytes()
p.write_bytes(b"\x00\x01\x02")

# Useful checks
p.exists()        # True/False
p.is_file()
p.is_dir()
p.suffix          # '.txt'
p.stem            # 'notes'
p.parent          # Path("data")

# Create directories
Path("logs").mkdir(parents=True, exist_ok=True)

# List files in a directory
for file in Path(".").glob("*.txt"):
    print(file)

# pathlib still plays nicely with open() too:
with open(p, "r") as f:
    content = f.read()
    print(content)

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
# Quick Reference

# CSV
import csv
with open("f.csv", "r", newline="") as f:
    for row in csv.reader(f): ...

#--------------------------------------------------------------------------------------
# JSON
import json
with open("f.json", "r") as f:
    data = json.load(f)

#--------------------------------------------------------------------------------------
# pathlib
from pathlib import Path
Path("f.txt").write_text("hello")
content = Path("f.txt").read_text()


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================
# NOTE: the examples below are SELF-CONTAINED - they create their own
# temporary sample files (and clean them up at the end) so this section runs
# independently, unlike some snippets above the file which reference
# pre-existing files (data.csv, data.json, image.png) as illustrative examples.

import os

# -------------------------
# 1. File modes in depth - what happens to EXISTING content for each mode
# -------------------------
"""
'r'   -> Read only. File MUST exist, or FileNotFoundError is raised.
'w'   -> Write. TRUNCATES (erases) existing content immediately on open,
          even if you never call .write()! Creates the file if missing.
'a'   -> Append. Existing content is PRESERVED; new writes go to the END.
          Creates the file if missing.
'x'   -> Exclusive creation. Raises FileExistsError if the file ALREADY exists -
          useful for "create only if it doesn't already exist" logic.
'r+'  -> Read AND write, but does NOT truncate. File must already exist.
'w+'  -> Write AND read, but DOES truncate (erases existing content first).
'a+'  -> Append AND read. Existing content preserved, writes go to the end,
          but the read/write POSITION starts at the end too (careful when
          reading right after opening in 'a+' mode).
"""

# Demonstrating 'w' mode TRUNCATES immediately, even with an empty write:
with open("demo_truncate.txt", "w") as f:
    f.write("original content")
print("Before 2nd open:", open("demo_truncate.txt").read())   # 'original content'

with open("demo_truncate.txt", "w") as f:
    pass   # didn't even write anything, but 'w' mode ALREADY erased the file on open!
print("After re-opening in 'w' mode:", repr(open("demo_truncate.txt").read()))   # '' -> gone!

os.remove("demo_truncate.txt")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 2. 'x' mode - exclusive creation, avoiding accidental overwrites
# -------------------------
with open("demo_exclusive.txt", "x") as f:
    f.write("created fresh")

try:
    with open("demo_exclusive.txt", "x") as f:   # file ALREADY exists now
        f.write("this will never run")
except FileExistsError as e:
    print("FileExistsError:", e)

os.remove("demo_exclusive.txt")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 3. File pointer / cursor - seek() and tell()
# -------------------------
with open("demo_seek.txt", "w") as f:
    f.write("Hello, World!")

with open("demo_seek.txt", "r") as f:
    print(f.tell())        # 0 -> cursor starts at the beginning
    print(f.read(5))         # 'Hello' -> reads 5 characters, cursor MOVES forward
    print(f.tell())            # 5 -> cursor position after reading
    f.seek(0)                    # move cursor back to the START of the file
    print(f.read())                # 'Hello, World!' -> reads from position 0 again
    f.seek(7)                        # jump to a SPECIFIC position
    print(f.read())                    # 'World!' -> reads from position 7 onward

os.remove("demo_seek.txt")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 4. Reading a LARGE file efficiently - chunk by chunk, NOT all at once
# -------------------------
with open("demo_large.txt", "w") as f:
    for i in range(1000):
        f.write(f"line {i}\n")

# BAD for huge files: f.read() loads the ENTIRE file into memory at once
with open("demo_large.txt", "r") as f:
    total_lines_readlines = len(f.readlines())   # loads ALL lines into a list in memory
print("Total lines (readlines, all in memory):", total_lines_readlines)

# GOOD for huge files: iterate line-by-line, only ONE line in memory at a time
line_count = 0
with open("demo_large.txt", "r") as f:
    for line in f:          # memory-efficient - reads lazily, one line at a time
        line_count += 1
print("Total lines (line-by-line iteration):", line_count)

# ALSO good: read in fixed-size BYTE chunks (useful for non-line-oriented data)
with open("demo_large.txt", "r") as f:
    chunk_count = 0
    while chunk := f.read(1024):   # walrus operator: read 1024 chars at a time until empty
        chunk_count += 1
print("Number of 1024-char chunks read:", chunk_count)

os.remove("demo_large.txt")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 5. Encoding - a REAL production bug source, especially cross-platform
# -------------------------
# ALWAYS specify encoding explicitly for text files, rather than relying on
# the SYSTEM DEFAULT (which can differ between Windows/Linux/macOS and cause
# "works on my machine" bugs):
with open("demo_encoding.txt", "w", encoding="utf-8") as f:
    f.write("café résumé naïve")   # contains non-ASCII characters

with open("demo_encoding.txt", "r", encoding="utf-8") as f:
    print(f.read())   # 'café résumé naïve' -> correctly decoded

# Without specifying encoding, Python uses locale.getpreferredencoding(),
# which is NOT guaranteed to be UTF-8 on every system (notably older Windows
# setups often default to something like cp1252) - this can cause
# UnicodeDecodeError when a file is later read on a DIFFERENT system.
os.remove("demo_encoding.txt")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 6. Context manager mechanics - what 'with open(...) as f' actually does
#    under the hood (ties file handling back to general Python OOP concepts)
# -------------------------
# 'with' works because file objects implement the context manager protocol:
# __enter__ (called at the START of the 'with' block) and __exit__ (called
# at the END, even if an exception occurred inside the block).
f = open("demo_manual.txt", "w")
print(hasattr(f, "__enter__"), hasattr(f, "__exit__"))   # True True -> proves file objects ARE context managers
f.close()
os.remove("demo_manual.txt")   # cleanup

# This is WHY the file gets closed automatically even if an exception is
# raised mid-block - __exit__ runs regardless of how the block ends.
try:
    with open("demo_exception.txt", "w") as f:
        f.write("before error")
        raise ValueError("Something went wrong!")
except ValueError:
    print("Caught the error, but let's check if file was still closed properly:")
    print("File closed?", f.closed)   # True -> __exit__ ran and closed it, DESPITE the exception
os.remove("demo_exception.txt")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 7. csv.QUOTE options and delimiter customization - handling real-world
#    messy CSV data (commas inside quoted fields, different delimiters, etc.)
# -------------------------
import csv

with open("demo.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")   # semicolon-delimited instead of comma
    writer.writerow(["name", "bio"])
    writer.writerow(["Alice", "Loves coding; hiking; and reading"])   # bio contains semicolons!

with open("demo.csv", "r", newline="") as f:
    reader = csv.reader(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)   # csv correctly handles the QUOTED field containing the delimiter

os.remove("demo.csv")   # cleanup

print(f"{'*' * 60}")

# -------------------------
# 8. JSON gotchas - things that DON'T serialize directly, custom encoders
# -------------------------
import json
from datetime import datetime

data_with_date = {"name": "Alice", "created": datetime.now()}
try:
    json.dumps(data_with_date)   # TypeError! datetime objects are NOT natively JSON-serializable
except TypeError as e:
    print("TypeError:", e)   # Object of type datetime is not JSON serializable

# FIX: provide a custom 'default' function to handle non-standard types
def json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()   # convert datetime to an ISO string
    raise TypeError(f"Type {type(obj)} not serializable")

json_str = json.dumps(data_with_date, default=json_default)
print(json_str)   # now works - datetime became an ISO-format string

# Also common: JSON has NO tuple type - tuples become JSON arrays (lists),
# and converting back gives you a LIST, not the original tuple:
tuple_data = {"point": (1, 2)}
json_str2 = json.dumps(tuple_data)
print(json_str2)                        # '{"point": [1, 2]}' -> tuple became a JSON array
print(json.loads(json_str2))              # {'point': [1, 2]} -> comes back as a LIST, not a tuple!

print(f"{'*' * 60}")

# -------------------------
# 9. pathlib - additional commonly-used methods beyond what's shown above
# -------------------------
from pathlib import Path

p = Path("demo_dir") / "subdir" / "file.txt"
print(p)                          # demo_dir/subdir/file.txt -> cross-platform path joining

p.parent.mkdir(parents=True, exist_ok=True)   # creates demo_dir/subdir/ if missing
p.write_text("hello from pathlib")
print(p.read_text())

print(p.absolute())     # full absolute path
print(p.name)              # 'file.txt' -> just the filename
print(p.stem)                # 'file' -> filename WITHOUT the extension
print(p.suffix)                # '.txt' -> just the extension
print(list(p.parent.iterdir()))  # lists all entries in the parent directory

# cleanup
p.unlink()                    # deletes the file (like os.remove, but as a Path method)
p.parent.rmdir()                # removes the now-empty 'subdir'
Path("demo_dir").rmdir()          # removes the now-empty 'demo_dir'

print(f"{'*' * 60}")

# -------------------------
# 10. os.path vs pathlib - the older (functional) vs newer (object-oriented) approach
# -------------------------
import os.path

# Old style (os.path) - functional, string-based
old_path = os.path.join("folder", "subfolder", "file.txt")
print(old_path)                       # 'folder/subfolder/file.txt'
print(os.path.splitext(old_path))       # ('folder/subfolder/file', '.txt')
print(os.path.basename(old_path))         # 'file.txt'
print(os.path.dirname(old_path))            # 'folder/subfolder'

# New style (pathlib) - object-oriented, generally preferred in modern Python
new_path = Path("folder") / "subfolder" / "file.txt"
print(new_path)                          # folder/subfolder/file.txt
print(new_path.suffix, new_path.name, new_path.parent)   # .txt file.txt folder/subfolder

# pathlib is generally recommended for NEW code (more readable, more methods,
# works consistently across OSes), but os.path is still extremely common in
# older/existing codebases and worth recognizing.


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON FILE HANDLING (files, CSV, JSON, pathlib)
## ==========================================================

# 1. What is the difference between opening a file in 'w' mode versus 'a'
#    mode? What happens to EXISTING content in each case?
#
# 2. Does 'w' mode truncate the file immediately upon opening, or only after
#    you call .write()? How would you demonstrate this?
#
# 3. What does 'x' mode do, and what exception does it raise if the file
#    already exists? What real-world scenario would this be useful for?
#
# 4. Why is `with open(...) as f:` preferred over manually calling
#    `f = open(...)` and `f.close()`? What Python protocol (dunder methods)
#    makes the `with` statement work with file objects?
#
# 5. If an exception is raised INSIDE a `with open(...) as f:` block, is the
#    file still properly closed? Why?
#
# 6. What is the difference between `f.read()`, `f.readline()`, and
#    `f.readlines()`? Which one is most memory-efficient for very large
#    files, and why?
#
# 7. Why is iterating over a file object directly (`for line in f:`)
#    generally preferred over `f.readlines()` for large files?
#
# 8. What do `f.seek()` and `f.tell()` do? Give a scenario where you'd need
#    to move the file's read/write cursor manually.
#
# 9. Why should you always explicitly specify an `encoding` (like 'utf-8')
#    when opening text files, instead of relying on the system default?
#    What kind of bug can this prevent?
#
# 10. Why do CSV files need `newline=""` when opened in Python (on Windows in
#     particular)? What problem does omitting it cause?
#
# 11. How would you handle a CSV file where a field itself contains a comma
#     (e.g., an address field like "123 Main St, Apt 4")? Does the `csv`
#     module handle this automatically if the field is quoted?
#
# 12. What is the difference between `csv.reader`/`csv.writer` and
#     `csv.DictReader`/`csv.DictWriter`? When would you prefer one over the
#     other?
#
# 13. Why does `json.dumps()` raise a TypeError when given a dictionary
#     containing a `datetime` object? How would you fix this using the
#     `default` parameter?
#
# 14. If you serialize a tuple to JSON and then parse it back with
#     `json.loads()`, do you get back a tuple? Why or why not?
#
# 15. What's the difference between `json.dump()`/`json.load()` (files) and
#     `json.dumps()`/`json.loads()` (strings)? When would you use each pair?
#
# 16. What are the main advantages of `pathlib.Path` over the older `os.path`
#     module for working with file paths? Is one deprecated in favor of the
#     other?
#
# 17. How would you check if a file exists before trying to open it, and why
#     might using a try/except around `open()` be preferable to checking
#     existence first (hint: think about race conditions - EAFP vs LBYL)?
#
# 18. What's the difference between `Path.read_text()`/`Path.write_text()`
#     and manually using `open()` with a `with` block? Are there any
#     trade-offs to the shortcut methods?
#
# 19. How would you safely read a huge file (larger than available RAM)
#     without loading the entire thing into memory at once?
#
# 20. What does `Path("a") / "b" / "c"` do, and why is this considered more
#     robust/cross-platform than manually concatenating path strings with
#     '/' or '\\'?