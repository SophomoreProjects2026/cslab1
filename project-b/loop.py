import llm
import random

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
                Roll a die until you get a six. Answer with how many rolls it took.
            """.strip()
        }
    ]

    print(messages[-1]["content"])
    steps = 0
    while True:
        if steps >= MAX_STEPS:
            print("Out of turns.")
            return
        response = llm.chat(messages)
        steps+=1
        print("+ "+response)
        messages.append({"role": "assistant", "content": response})
        if (response == "CALL roll_die"):
            msg = f"roll_die returned {random.randrange(1, 7)}"
            messages.append({"role": "user", "content": msg})
            print("- " + msg)
        elif (response.startswith("ANSWER")):
            return
        else:
            print("aaAAAAuugghhHHH i can't handle that kind of response!!!!!!!")
            return

if __name__ == "__main__":
    main()