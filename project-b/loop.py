import llm
from pathlib import Path
import json
import asyncio
from fastmcp import Client
MAX_STEPS=10

client = Client(Path("server.py"))

async def main():
    async with client:
        raw_tools = await client.list_tools()
        tools = {}
        for tool in raw_tools:
            tools[tool.name] = {
                "descripton": tool.description,
                "input_schema": tool.input_schema
            }
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
                "content": """
                    Classify the unsorted files.
                """.strip()
            }
        ]

        steps = 0
        print("- "+messages[-2]["content"])
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
            
            if response.startswith("CALL"):
                # tool call
                try:
                    name_end = response.index(" ", len("CALL "))
                    tool_name = response[len("CALL "):name_end]
                    args = json.loads(response[name_end+1:].strip())
                    print("! "+tool_name)
                    tool_result = await client.call_tool(tool_name, args)
                    print(json.dumps(tool_result.structured_content))
                    messages.append({"role": "user", "content": f"TOOL RESULT: {json.dumps(tool_result.structured_content)}"})
                except Exception as e:
                    print(e)
                    messages.append({"role": "user", "content": f"INVALID TOOL CALL"})
            else:
                break # model is done
            

            

if __name__ == "__main__":
    asyncio.run(main())