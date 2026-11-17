We're testing the project with Twitch chat logs, asking the model
to sort them based on the category it thinks was being streamed. 

The model usually scores above 30%, which is good. The scoring functions can never give a perfect score anyway, and the result depends on the contents of the chat log. Because of the design, a score over 30% is actually a good indication that the guess is correct.
Thge final guess for Chess is correct, but the scorer failed it because it was capitalized (a downside of this method).

Notably, it responded with the "unclear" category when it could not discern a category.

[
    {'id': 'boo', 'reply': 'minecraft', 'score': 0.7748831781444285}, 
    {'id': 'bot', 'reply': 'chess', 'score': 0.7480468697316439}, 
    {'id': 'bro', 'reply': 'leagueoflegends', 'score': 0.7304685115814209}, {'id': 'cli', 'reply': 'fortnite', 'score': 0.4929422155058304}, 
    {'id': 'dan', 'reply': 'leagueoflegends', 'score': 0.7031142104067812}, {'id': 'got', 'reply': 'chess', 'score': 0.6249999997671694}, 
    {'id': 'iss', 'reply': 'gtaiv', 'score': 0.49609375}, 
    {'id': 'jyn', 'reply': 'unclear', 'score': 0.2928932188134524}, 
    {'id': 'kes', 'reply': 'leagueoflegends', 'score': 0.30759830470336313}, {'id': 'low', 'reply': 'minecraft', 'score': 0.3745594558042839}, 
    {'id': 'pho', 'reply': 'minecraft', 'score': 0.9063509339545693}, 
    {'id': 'ray', 'reply': 'gtaiv', 'score': 0.4998778700828552}, 
    {'id': 'slu', 'reply': 'minecraft', 'score': 0.8101572380523802}, 
    {'id': 'spa', 'reply': 'fortnite', 'score': 0.5712701797033631}, 
    {'id': 'spe', 'reply': 'leagueoflegends', 'score': 0.4108696461865714}, {'id': 'str', 'reply': 'gtaiv', 'score': 0.4687499403953552}, 
    {'id': 'swe', 'reply': 'fortnite', 'score': 0.673839993453023}, 
    {'id': 'syp', 'reply': 'fortnite', 'score': 0.43749988079071045}, 
    {'id': 'tan', 'reply': 'minecraft', 'score': 0.6197916516088091}, 
    {'id': 'wit', 'reply': 'Chess', 'score': 0}
]

OUR SCORING FUNCTION:
The scoring function looks for certain terms related to the guessed category using regular expressions. It returns a higher value when the term is seen more frequently. Each term or set of terms is multiplied by a weight chosen by how strongly we feel a certain term indicates the specific game. Finally, this number is run through an exponential function to make sure it never exceeds 1.
A reply with a categoty not present in the available options results in a score of zero.

A weakness is that the frequency of the terms may vary wildly depending on the content of the stream and the type of audience, even if the ctegory is correct.
This is why we accept low non-zero scores as passing.

FAILURES:
The final case eval scored 0 despite a technically correct response because the category name wasn't exact.
"jyn" was categorized as unclear, when its result should have been Fortnite.
A few cases such as "iss" take a ridiculously long time to run (over 7 minutes).

WHY THESE TWENTY:
We made sure to use multiple cases for each category to ensure the model was consistent with its guesses. We also made sure to have a variety of games (sandbox, MOBA, FPS, etc.). No creator is repeated to ensure a variety of audiences with different personalities. We also have a mix of large and small creators to ensure a mix of slow/intimate chats and fast/chaotic chats.