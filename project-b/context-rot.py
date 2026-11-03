import llm
import random
import string

names = "Liam Emma Noah Olivia William Ava James Isabella Oliver Sophia Benjamin Mia Lucas Charlotte Henry Amelia Alexander Evelyn Sebastian Abigail Jack Harper Daniel Emily Michael Elizabeth Matthew Sofia Samuel Avery David Ella Joseph Scarlett Carter Victoria Owen Aria Wyatt Grace John Chloe Jack Camila Luke Layla Isaac Lillian Gabriel Nora Julian Zoey Levi Mila Anthony Penelope Grayson Riley Christopher Eleanor Joshua Hannah Lillian Lincoln Addison Mateo Aubrey Ryan Ellie Jaxon Stella Caleb Natalie Nathan Leah Aaron Hazel Charles Violet Thomas Aurora Josiah Savannah Isaiah Audrey Brooklyn Eli Claire Aaron Skylar Connor Lucy Christian Paisley Hunter Elena Adrian Maya".split(" ")
verbs = ["has", "buys", "eats", "gets", "loses", "gains", "gives away", "finds"]
def generate_junk(length: int) -> str:
    out = ""
    # each segment has about 5 tokens
    for i in range(length//5):
        out += f"{random.choice(names)} {random.choice(verbs)} {random.randint(2, 10)} apples. "
    # remove final space
    return out[0:len(out)-1]

def run_harness(junk_amt: int, junk_per_message_pair: int):
    """
    Runs the context rot harness.
    
    Args:
        iterations: Number of steps to run.
        base_junk: Base number of characters of junk to add each step.
    """
    messages = [{"role": "user", "content": "Andy has 5 apples. He then buys 7 more apples. He eats 3 apples."}]
    
    print(f"Starting context rot: {junk_amt//junk_per_message_pair} messages, {junk_amt} junk \n")

    real_data_bits = [
        "Andy has 5 apples.",
        "Andy buys 7 apples.",
        "Andy eats 3 apples.",
        "How many apples does Andy have left?"
    ]
    n_message_pairs = junk_amt//junk_per_message_pair - (len(real_data_bits))

    # mix the real data in with the junk
    for bit in real_data_bits:
        for i in range(n_message_pairs//len(real_data_bits)):
            messages.append({"role": "user", "content": generate_junk(junk_per_message_pair//2)})
            messages.append({"role": "assistant", "content": generate_junk(junk_per_message_pair//2)})
        
        messages.append({"role": "user", "content": f"{generate_junk(junk_per_message_pair//4)} {bit} {generate_junk(junk_per_message_pair//4)}"})
        messages.append({"role": "assistant", "content": generate_junk(junk_per_message_pair//2)})
    
    messages.pop()  
    print("Context Generated. Waiting on model...")

    response = llm.chat(messages)

    print(response)

if __name__ == "__main__":
    for i in range(5):
        print(f"RUN {i+1}")
        run_harness(4000, 200)
