import os
import emoji
import patterns as p


def extract_unique_emojis(text):
    emojis = set(char for char in text if emoji.is_emoji(char) or p.emoji_pattern.match(char))

    return "".join((emojis))

def emoji_extractor(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
            if not filename.endswith((".html", ".txt")):
                continue
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"emojis_{filename}")

            with open(input_path, "r", encoding="utf-8") as file:
                content = file.read()
                
            content = " ".join(content.split())

            emojis = extract_unique_emojis(content)

            with open(output_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sorted(emojis)))
            print(f"{filename} file processed, {len(emojis)} different emojis found.")


if __name__ == "__main__":
    INPUT_DIR = "input"
    OUTPUT_DIR = "output"
    emoji_extractor(INPUT_DIR, OUTPUT_DIR)
    
