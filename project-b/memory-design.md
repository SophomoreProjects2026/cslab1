The model falters quickly past 60,000 tokens, so we will compact memory around that point.
Possibly earlier at around 50,000 just to be safe.
To compact memory, old blocks of messages will be summarized by the LLM.

Conveniently, after a file is classified, its contents are no longer relevant, and can be 
purged from memory. This should keep context lengths down while not needing to truncate files.