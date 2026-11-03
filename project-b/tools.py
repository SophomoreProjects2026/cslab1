
import json
import types
from fastmcp import FastMCP
    
@mcp.tool
def read_file(path: str) -> tuple[bool, str]:
    if ".." in path:
        return (False, "Path may not go up a level.")

    try:
        file = open("workspace/"+path)
        return (True, file.read())
    except Exception as err:
        return (False, str(err))
    finally:
        file.close()

@mcp.tool
def write_file(path: str , data: str ) -> tuple[bool, str]:
    if ".." in path:
        return (False, "Path may not go up a level.")

    try:
        file = open("workspace/"+path, "w")
        file.write(data)
        return (True, None)
    except Exception as err:
        return (False, str(err))
    finally:
        file.close()

@mcp.tool
def count_matching_lines(path: str , word: str ) -> tuple[bool, str]:
    if ".." in path:
        return (False, "Path may not go up a level.")

    try:
        file = open("workspace/"+path)
        count = [(word in line) for line in file.read().split("\n")].count(True)
        return (True, count)
    except Exception as err:
        return (False, str(err))
    finally:
        file.close()

@mcp.tool
def complete_job(message: str ="") -> tuple[bool, str]:
    return (True, message)

tools: dict[str, types.FunctionType] = {
    "read_file": read_file,
    "write_file": write_file,
    "count_matching_lines": count_matching_lines,
    "complete_job": complete_job,
}