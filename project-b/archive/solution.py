import random
from llm import chat

def roll_die():
    """Rolls a six-sided die and returns the result."""
    return random.randint(1, 6)

def run_agent_task(system_prompt_path, user_job):
    """
    Runs the agent task by interacting with the LLM and verifies the result.
    
    Args:
        system_prompt_path: Path to the file containing the system prompt.
        user_job: The task sent to the agent.
        
    Returns:
        A tuple containing (answer, is_correct, actual_rolls).
    """
    try:
        with open(system_prompt_path, 'r') as f:
            system_prompt = f.read().strip()
    except FileNotFoundError:
        raise ValueError(f"System prompt file not found: {system_prompt_path}")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_job},
    ]

    max_turns = 100  # Prevent infinite loops
    turns = 0
    actual_rolls = 0

    while turns < max_turns:
        turns += 1
        response = chat(messages).strip()

        if response == "CALL roll_die":
            die_result = roll_die()
            actual_rolls += 1
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": str(die_result)})
        elif response.startswith("ANSWER "):
            answer_str = response[len("ANSWER "):].strip()
            try:
                answer_val = int(answer_str)
                is_correct = (answer_val == actual_rolls)
            except ValueError:
                is_correct = False
            return answer_str, is_correct, actual_rolls
        else:
            # If the model doesn't follow the strict format, we tell it to do so.
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": "Please follow the instructions. Reply with 'CALL roll_die' or 'ANSWER <answer>' only."})

    raise RuntimeError("Agent exceeded maximum number of turns.")

if __name__ == "__main__":
    import sys
    import os

    # Get current directory to resolve paths correctly
    base_dir = os.path.dirname(os.path.abspath(__file__))
    system_prompt_file = os.path.join(base_dir, "system_prompt.txt")
    
    job = "Roll a die until you get a six. Tell me how many rolls it took."
    
    try:
        answer, is_correct, actual_rolls = run_agent_task(system_prompt_file, job)
        print(f"Agent Result: {answer}")
        print(f"Correct: {is_correct}")
        print(f"Actual Rolls: {actual_rolls}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
