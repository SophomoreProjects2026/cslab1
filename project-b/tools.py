
import json
import types
from fastmcp import FastMCP

mcp = FastMCP("NOVIN-SIMTH-AGENT")

# returns a string if an error occurred, else a tuple containing
# the tool name and the args
def parse_call(raw):
    try:
        tool_call = json.loads(raw)
    except:
        return "Malformed tool call. If you are finished, call complete_job."

    if not isinstance(tool_call, dict):
        return "Tool call must be an object."

    if "tool" not in tool_call:
        return "Tool call must contain a \"tool\" field."

    tool_name = tool_call["tool"]

    # arguments is allowed to not exist, but if it does, it must be a dict
    arguments = tool_call["arguments"] if "arguments" in tool_call else {}
    
    if not isinstance(arguments, dict):
        return "Arguments must be an object."

    return (tool_name, arguments)
    
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





if __name__ == "__main__":
    mcp.run(transport="stdio")