import re

emoji_pattern = re.compile(
    r"[\U0001F600-\U0001F64F"  # Emoticons
    r"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
    r"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
    r"\U0001F700-\U0001F77F"  # Alchemical Symbols
    r"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    r"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    r"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    r"\U0001FA00-\U0001FA6F"  # Chess Symbols
    r"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    r"\U0001FAB0-\U0001FABF"  # Bugs (Böcekler)
    r"\U0001FAC0-\U0001FACF"  # Plants (Bitkiler)
    r"\U0001FAD0-\U0001FADF"  # Miscellaneous Symbols
    r"\U0001FAE0-\U0001FAFF"  # More Symbols
    r"\U00002702-\U000027B0"  # Dingbats
    r"\U000024C2-\U0001F251"  # Enclosed characters
    r"|[\U0001F1E6-\U0001F1FF]{2}"  # Country flags (regional indicators)
    r"|[\U0001F1E6-\U0001F1FF]{2}"  # Duplicate flag support
    r"|\u200D"  # Zero Width Joiner (ZWJ) desteği
    r"|\uFE0F",  # Variation Selector (emoji renklendirme için)
    flags=re.UNICODE,
)

blank_pattern = re.compile(
    r"[\uE000-\uF8FF\uF0000-\uFFFFD\u100000-\u10FFFD]"  # Special space characters
)