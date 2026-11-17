import llm
from pathlib import Path
import json
import asyncio
from fastmcp import Client

MAX_STEPS=50

client = Client(Path("server.py"))

async def main():
    async with client:
        # get clarification on how to sort the files
        print("Please enter a description of how these files should be classified:")
        clarification = input()

        # prep tools for enumeration
        raw_tools = await client.list_tools()
        tools = {}
        for tool in raw_tools:
            tools[tool.name] = {
                "descripton": tool.description,
                "input_schema": tool.input_schema
            }

        # initial thread
        messages = [
            {
                "role": "system",
                "content": f"""
                    You can make tool calls with arguments formatted as JSON.
                    They look like: `CALL tool_name {{"arg1": "abcdefg", "arg2": 456.2}}`
                    If a tool call requires no arguments, specify an empty object.
                    They will return either a response or an error.
                    In order to call a tool, output text in that format directly with no markdown formatting.
                    
                    A non-tool call message will indicate the end of the job.

                    The tools available are:
                    ```json
                    {json.dumps(tools)}
                    ```
                """.strip()
            },
            {
                "role": "user",
                "content": f"""
                    Classify the unsorted files adhering to this clarification: {clarification}.
                """.strip()
            }
        ]
        print("- "+messages[-2]["content"])

        steps = 0
        while True:
            if steps >= MAX_STEPS:
                print(f"Out of turns. Used {llm.get_total_tokens()} tokens.")
                return
            
            response = llm.chat(messages)
            steps+=1
            if response == None: continue
            print("- "+messages[-1]["content"])
            print("+ "+response)
            messages.append({"role": "assistant", "content": response})
            
            if response.startswith("CALL"):
                # tool call
                try:

                    name_end_index = response.index(" ", len("CALL "))
                    tool_name = response[len("CALL "):name_end_index]
                    args = json.loads(response[name_end_index+1:].strip())
                    tool_result = await client.call_tool(tool_name, args)
                    print("! tool " + tool_name + " was called")
                    messages.append({"role": "user", "content": f"TOOL RESULT: {json.dumps(tool_result.structured_content)}"})
                    
                    # Compact memory on classify
                    if tool_name == "classify":
                        for i in range(len(messages)):
                            message = messages[i]
                            if message["role"] != "assistant": continue
                            if message["content"].startswith("CALL get_unclassified_file"):
                                messages[i+1]["content"] = "[Tool response redacted to save memory.]"
                                
                except Exception as e:
                    print("AN ERROR OCCURRED:", e)
                    messages.append({"role": "user", "content": f"ERROR IN TOOL CALL"})
            else:
                break # model is done
            

            

if __name__ == "__main__":
    asyncio.run(main())