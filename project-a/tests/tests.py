from hypothesis import given, strategies as st
import subprocess

def lgrep(args, input=None):
    # call lgrep
    compl = subprocess.run(("python3 lgrep.py "+args).split(" "), capture_output=True, input=input, text=True)
    return compl.stdout

# basic

def test_stdin():
    assert lgrep("hello -", "hello world") == "hello world"
    

@given(
    st.lists(["-i", "-v", "-n", "-c", "-w"], unique=True), 
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz".split()),
    st.text()
)
def test_exit_0(flags, pattern, input):
    compl = subprocess.run("lgrep "+flags.join(" ")+" "+pattern+" -", stdin=input)
    assert compl.returncode == 0

# flags

def test_i():
    assert lgrep("-i HELLO -", "hello world") == "hello world"

def test_v():
    assert lgrep("-v goodbye -", "hello world") == "hello world"

def test_n():
    assert lgrep("-n goodbye -", "hello world\ngoodbye world").startswith("13")

def test_c():
    assert lgrep("-c world -", "hello world, goodbye world") == "2"
    
def test_w():
    assert lgrep("-w world -", "hello world\nhelloworld\nhello world hello") == "hello world\nhello world hello"

def test_cv():
    assert lgrep("-w -c goodbye -", "hello world") == "1"

# output

def test_file():
    file1 = open("single_file.txt", "w+")
    file1.write("hello world, goodbye world")
    file1.close()

    assert lgrep(f"-c world single_file.txt").strip() == "2"


def test_multifile(tmp_path_factory):
    file1 = open("1.txt", "w+")
    file1.write("hello world")
    file1.close()
    file2 = open("2.txt", "w+")
    file2.write("goodbye world")
    file2.close()

    assert lgrep(f"-c world 1.txt 2.txt").strip() == "2"
    assert lgrep(f"world 1.txt 2.txt").startswith("1.txt:")

#errors
def test_unreadablefile():
    compl = subprocess.run("pattern nonexistent.txt", capture_output=True)
    assert compl.stderr != ""
    assert "nonexistent.txt" in compl.stderr

    
# examples
fruit = """apple banana apple
cherry
APPLE apple
"""

def test_apple():
    assert lgrep("apple -", fruit) == "apple banana apple\nAPPLE apple"
def test_n_apple():
    assert lgrep("-n apple -", fruit) == "0:apple banana apple\n26:APPLE apple"
def test_c_apple():
    assert lgrep("-c apple -", fruit).strip() == "3"
def test_ci_apple():
    assert lgrep("-ci apple -", fruit).strip() == "4"
def test_cv_apple():
    assert lgrep("-cv apple -", fruit).strip() == "1"
def test_zebra():
    assert lgrep("zebra -", fruit).strip() == ""