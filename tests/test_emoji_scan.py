from emoji_scan.emoji_utils import extract_unique_emojis, emoji_extractor

def test_extract_unique_emojis():
    text = "Hello! 😃🌍"
    result = extract_unique_emojis(text)
    assert set(result) == set("😃🌍"), f"Expected '😃🌍', but got {result}"

    text = "Hello world!"
    result = extract_unique_emojis(text)
    assert result == "", f"Expected '', but got {result}"

    text = "Python is fun! 🐍🔥"
    result = extract_unique_emojis(text)
    assert set(result) == set("🐍🔥"), f"Expected '🐍🔥', but got {result}"

def test_emoji_extractor(tmpdir):
    input_dir = tmpdir.mkdir("input")
    output_dir = tmpdir.mkdir("output")

    test_file = input_dir.join("test.txt")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Hello! 😃🌍")

    emoji_extractor(str(input_dir), str(output_dir))

    output_file = output_dir.join("emojis_test.txt")
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
        assert set(content.split("\n")) == set("😃🌍"), f"Unexpected output: {content}"