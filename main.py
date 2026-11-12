from groq import generate_response
import time
def temp_prompt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGINEERING: INSTRUCTION & TEMPERATURE")
    print("="*70)
    print ("part 1:temperature exploration ")
    base = input("Enter a creative prompt: ").strip()
    for t,lebel in [(0.0,"deterministic"),(0.3,"creative"),(0.7,"very creative")]:
        print(f"\n\nTemperature: {t} ({lebel})\n")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)   
    print("part 2: instruction exploration ")
    topic = input("Enter a topic for instruction exploration: ").strip()
    prompts = [
        f"Write a detailed essay about {topic}.",
        f"Write a detailed essay about {topic} in the style of Shakespeare.",
        f"Write a detailed essay about {topic} in the style of Shakespeare, but make it humorous.",
        f"explain {topic} to a 5-year-old.",
        f"explain {topic} in real detail, with examples and analogies.",
    ] 
    for i,p in enumerate(prompts,1):
        print(f"\n\nPrompt {i+1}: {p}\n")
        print(generate_response(p, temperature=0.3, max_tokens=512))
        time.sleep(1)
if __name__ == "__main__":
    temp_prompt_activity()