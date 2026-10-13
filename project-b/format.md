
A call looks like:
```json
{
    "tool": "example",
    "arguments": {
        "a": 1,
        "b": false,
        "c": "hello world"
    }
}
```

A response looks like:
```json
{
    "successful": true,
    "result": "example result"
}
```

Or:
```json
{
    "successful": false,
    "error": "example error"
}
```


How does the model say it is finished? A separate {"answer": ...} object, as above, or a reserved tool named finish? One of those makes your parser simpler; the other makes your prompt simpler. Pick one and name what you gave up.

It will use a tool called `complete_job` or something similar.

2. Where do arguments go? Nested under "args", as above, or flat beside "tool"? Flat is shorter for the model to get right. Nested means a tool can never have an argument named tool.

Arguments will go inside their own `"arguments": {}` object.

3. What does a tool failure look like coming back? read_file("nope.txt") on a file that is not there is not a crash, and it is not a format error — it is information the model needs in order to do something else. Decide how you phrase it, because the model only ever sees text.

`{"successful": false, "error": "error here"}`

4. Do you resend the tool list on every call, or only the first? Both work. They cost different amounts, and in Lab 8 you will measure the difference.

Only at first. Keep it in the system prompt.