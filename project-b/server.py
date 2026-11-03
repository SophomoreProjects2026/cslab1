import os
import random
from fastmcp import FastMCP
mcp = FastMCP("NOVIN-SIMTH-AGENT")

@mcp.tool
def get_unclassified_file() -> tuple[str, str]:
    """Get the id (file name) and contents of an unclassified file."""

    available_files = os.listdir("workspace/unsorted")
    if len(available_files) == 0:
        raise RuntimeError("No more uncategorized files.")
    
    choice = random.randint(0, len(available_files)-1)

    file = open("workspace/unsorted/"+available_files[choice])
    data = file.read()
    file.close()
    return (available_files[choice], data)
    

@mcp.tool
def classify(id: str , category: str ) -> None:
    """Classify a file by its id (file name)."""
    
    if ".." in id or ".." in category:
        raise ValueError("Path may not go up a level.")

    os.rename(f"workspace/unsorted/{id}", f"workspace/{category}/{id}")

@mcp.tool
def get_categories() -> list[str]:
    """Get the list of available categories."""

    directories = os.listdir("workspace")
    directories.remove("unsorted")
    return directories
    

if __name__ == "__main__":
    mcp.run(transport="stdio")
