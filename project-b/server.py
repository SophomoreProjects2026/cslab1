from fastmcp import FastMCP
mcp = FastMCP("NOVIN-SIMTH-AGENT")

@mcp.tool
def read_file(path: str) -> tuple[bool, str]:
    """Read a file from a path within the workspace."""
    
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
    """Write a file to a path within the workspace."""
    
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
    """Count the number of lines containing [word] in the specified file within the workspace."""
    
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


if __name__ == "__main__":
    mcp.run(transport="stdio")
