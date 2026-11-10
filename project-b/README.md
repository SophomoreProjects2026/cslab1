# File Classification Tools

A simple set of MCP tools for organizing files into categories.

These tools allow you to retrieve uncategorized files, inspect their contents, view available categories, and move files into the appropriate category.

## Tools

### `get_unclassified_file()`

Returns a randomly selected file from the `workspace/unsorted` directory.

**Returns:**
- `id` (`str`): The file name.
- `contents` (`str`): The contents of the file.

**Raises:**
- `RuntimeError`: If there are no more uncategorized files.

**Example:**
```python
id, contents = get_unclassified_file()
```

### `classify(id, category)`

Moves a file from `workspace/unsorted` into the specified category directory.

**Parameters:**
- `id` (`str`): The file name returned by `get_unclassified_file()`.
- `category` (`str`): The destination category.

**Example:**
```python
classify("example.txt", "documents")
```

This moves the file to:

```text
workspace/documents/example.txt
```

**Raises:**
- `ValueError`: If the file ID or category contains `..`.

### `get_categories()`

Returns a list of available categories in the `workspace` directory.

The `unsorted` directory is excluded from the results.

**Returns:**
- `list[str]`: Available category names.

**Example:**
```python
categories = get_categories()
```

## Directory Structure

The workspace should contain an `unsorted` directory and one or more category directories.

```text
workspace/
├── unsorted/
│   ├── example.txt
│   └── notes.md
├── documents/
├── images/
└── other/
```

Files in `unsorted` are waiting to be classified.

Category directories are the destinations for classified files.

## Typical Workflow

1. Call `get_categories()` to see the available categories.
2. Call `get_unclassified_file()` to retrieve a file and its contents.
3. Read the contents and determine the appropriate category.
4. Call `classify(id, category)` to move the file.
5. Repeat until no uncategorized files remain.

## Notes

- Files are selected randomly from the unsorted directory.
- Classification moves files rather than copying them.
- The destination category must already exist.
- The file ID is the file name, not a unique database identifier.
- When the unsorted directory is empty, `get_unclassified_file()` raises a `RuntimeError`.

## Error Handling

Handle errors when retrieving or classifying files.

```python
try:
    id, contents = get_unclassified_file()
    # Determine the appropriate category.
    classify(id, "documents")

except RuntimeError:
    print("No more uncategorized files.")

except ValueError as error:
    print(f"Invalid classification: {error}")
```

## Purpose

These tools provide a simple workflow for automated file organization using an MCP server. An MCP client can inspect file contents, choose a suitable category, and classify files through the available tools.

