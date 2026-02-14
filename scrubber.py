# Open the list you just verified with 'ls'
with open("banned_list.txt", "r") as f:
    banned_words = [line.strip().lower() for line in f if line.strip()]

# Test it with a "fluffy" procurement sentence
draft = "We need to leverage our holistic ecosystem to streamline the cutting-edge process."

found = [word for word in banned_words if word in draft.lower()]

if found:
    print(f"Banned words detected: {', '.join(found)}")
    print("Suggestion: Strip the fluff. Use plain words.")
else:
    print("Clean draft. McMurtry would be proud.")# List of some banned words from your Anti-AI prompt
banned_words = ["leverage", "synergy", "holistic", "streamline", "cutting-edge"]

draft = "We need to leverage our holistic ecosystem to streamline the cutting-edge procurement process."

found = []
for word in banned_words:
    if word in draft.lower():
        found.append(word)

if found:
    print(f"Banned words found: {', '.join(found)}")
    print("Suggestion: Cut the fluff. Use plain words.")
else:
    print("Clean draft. McMurtry would be proud.")
