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
                You have one tool, roll_die, which rolls a six-sided die.
                To use it, reply with exactly:   CALL roll_die
                When you know the answer:        ANSWER <your answer>
                Reply in one of those two forms and nothing else.
            """.strip()
        },
        {
            "role": "user",
            "content": """
                Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
            """.strip()
        }
    ]

    print(messages[-1]["content"])
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
        messages.append(json.dumps(result))

        if tool_name == "complete_job": # special tool that breaks the loop
            break

            

if __name__ == "__main__":
    main()