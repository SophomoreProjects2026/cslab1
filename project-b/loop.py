import llm
import random
import re
import json
from tools import tools, parse_call
MAX_STEPS=10

def main():
    messages = [
        {
            "role": "system",
            "content": """
                You can make tool calls formatted as JSON.
                They look like: `{"tool": "tool_name", "arguments": {"optional_argument": "example"}}`
                They will return either a response or an error.
                In order to call a tool, output JSON directly with no markdown formatting.
                
                The tools available are:
                ```python
                read_file(path) # returns the contents of the file
                write_file(path, data) # saves data to a file
                count_matching_lines(path, word) # returns the number of lines in which word appears in the file
                complete_job(message) # signals that you are done with an optional message to show the operator
                ```
            """.strip()
        },
        {
            "role": "user",
            "content": """
                Tell me how many times "TODO" appears in notes.txt
            """.strip()
        }
    ]

    # print(messages[-1]["content"])
    steps = 0
    rolls = 0
    total = 0
    while True:
        if steps >= MAX_STEPS:
            print(f"Out of turns. Used {llm.get_total_tokens()} tokens.")
            return
        response = llm.chat(messages)
        if response == None: continue
        steps+=1
        print("- "+messages[-1]["content"])
        print("+ "+response)
        messages.append({"role": "assistant", "content": response})

        tool_call = parse_call(response)
        if isinstance(tool_call, str):
            messages.append({"role": "user", "content": tool_call})
            continue

        tool_name, arguments = tool_call
        
        if tool_name not in tools:
            messages.append({"role": "user", "content": "Requested tool does not exist. Please try again."})
            continue
        
        tool = tools.get(tool_name)

        (successful, detail) = tool(**arguments)

        result = {"successful": successful, "result": detail} if successful else {"successful": successful, "error": detail}
        messages.append({"role": "user", "content": json.dumps(result)})

        if tool_name == "complete_job": # special tool that breaks the loop
            break

            

if __name__ == "__main__":
    main()