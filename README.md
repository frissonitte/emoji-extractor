# EmojiScan

A Python package to extract and filter unique emojis from files, helping users identify which emojis are compatible with specific platforms. The project supports HTML and TXT files, making it ideal for testing emoji compatibility on platforms like listing sites (e.g., Sahibinden), where certain emojis may not display correctly.

## Installation

You can install EmojiScan via pip:

pip install emojiscan

Usage
Extracting Emojis from Files

To extract unique emojis from files in a directory, use the emoji_extractor function:
python
Copy

from emojiscan import emoji_extractor

# Specify the input and output directories
input_directory = "path/to/input"
output_directory = "path/to/output"

# Extract emojis
emoji_extractor(input_directory, output_directory)

This will scan all .html and .txt files in the input_directory, extract unique emojis, and save them to the output_directory.

Supported Platforms

EmojiScan is designed to help you test emoji compatibility on various platforms, such as:

    Listing sites (e.g., Sahibinden)

    Social media platforms

    Messaging apps

Why Use EmojiScan?

    Easy to Use: Simple API for extracting and filtering emojis.

    Platform Compatibility: Identify emojis that may not display correctly on specific platforms.

    File Support: Works with HTML and TXT files.

Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

    Fork the repository.

    Create a new branch for your feature or bugfix.

    Submit a pull request.

For more details, check out our Contributing Guidelines.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Links

    PyPI: emojiscan

    GitHub Repository: emojiscan

    Issue Tracker: GitHub Issues