from concurrent.futures import ThreadPoolExecutor
import time
import asyncio
from fastmcp import Client
import json
from pathlib import Path
import score
import llm
import random

MAX_STEPS=10


class FakeToolResopnse:
    def __init__(self, structured_content):
        self.structured_content = structured_content

async def agent(fileId: str) -> str:
    client = Client(Path("server.py"))
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
                    Classify the unsorted Twitch chat logs into the category you think was being streamed.
                """.strip()
            }
        ]

        steps = 0
        # print("- "+messages[-2]["content"])
        while True:
            if steps >= MAX_STEPS:
                print(f"Out of turns. Used {llm.get_total_tokens()} tokens.")
                return "ERROR"
            response = llm.chat(messages)
            if response == None: continue
            steps+=1
            # print("- "+messages[-1]["content"])
            # print("+ "+response)
            messages.append({"role": "assistant", "content": response})
            
            if response.startswith("CALL"):
                # tool call
                try:
                    name_end = response.index(" ", len("CALL "))
                    tool_name = response[len("CALL "):name_end]
                    args = json.loads(response[name_end+1:].strip())
                    # print("! "+tool_name)
                    if tool_name == "get_unclassified_file":
                        file = open("eval/cases/"+fileId)
                        data = file.read()
                        file.close()
                        tool_result = FakeToolResopnse({"data": [fileId, data]})
                    elif tool_name == "classify":
                        return args["category"] 
                    else:
                        tool_result = await client.call_tool(tool_name, args)
                    messages.append({"role": "user", "content": f"TOOL RESULT: {json.dumps(tool_result.structured_content)}"})
                except Exception as e:
                    print(e)
                    messages.append({"role": "user", "content": f"INVALID TOOL CALL"})
            else:
                return "ERROR"
            

def run_case(case): 
    print("running", case["id"])
    reply = with_backoff(lambda case: asyncio.run(agent(case)), case["input"]) 
    print("scoring", case["id"])
    this_score = score.score(case, reply)
    print("done", case["id"])
    return {"id":    case["id"], 
            "reply": reply, 
            "score": this_score}

def with_backoff(fn, *args, attempts=5): 
    delay = 1.0 
    for attempt in range(attempts): 
        try: 
            return fn(*args) 
        except Exception as e: 
            print("ERR", e)
            if attempt == attempts - 1: 
                raise              # out of retries; let it fail 
            time.sleep(delay + random.random() * delay) 
            delay *= 2 

if __name__ == "__main__":
    file = open("eval/cases.json")
    data = file.read()
    file.close()
    cases = json.loads(data)
    with ThreadPoolExecutor(max_workers=2) as pool: 
        results = list(pool.map(run_case, cases)) 
    print(results)


