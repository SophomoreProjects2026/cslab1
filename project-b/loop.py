import llm
import random
import re
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
        if (response == "CALL roll_die"):
            roll = random.randrange(1, 7)
            rolls += 1
            total += roll
            msg = f"roll_die returned {roll}"
            messages.append({"role": "user", "content": msg})
            print("- " + msg)
        elif (response.startswith("ANSWER")):
            
            collected = []
            for n in re.compile(r"\d+").finditer(response):
                collected.append(int(n[0]))
            if len(collected) != 2:
                msg = f"Malformed command. Please try again."
                messages.append({"role": "user", "content": msg})
                print("- " + msg)
            else:
                reported_total = collected[0]
                reported_rolls = collected[1]
                if reported_total != total or reported_rolls != rolls:
                    print("# EXTREMELY LOUD INCORRECT BUZZER")
                    print(f"# total {total}; {rolls} rolls.")
                else:
                    print(f"# yeah that's right.")
                print(f"Tokens used: {llm.get_total_tokens()}")
                return

        else:
            msg = f"Malformed command. Please try again."
            messages.append({"role": "user", "content": msg})
            print("- " + msg)
            return

if __name__ == "__main__":
    main()