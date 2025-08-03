# SRT to Text and Markdown Converter

A Sublime Text plugin that converts SRT (SubRip Subtitle) files into clean, readable text or Markdown format.

## Features

- **Convert SRT to Text**: Transforms subtitle files into clean, paragraph-formatted text
- **Convert SRT to Markdown**: Converts subtitle files into properly formatted Markdown documents
- **Intelligent Text Processing**: Automatically combines subtitle blocks into coherent paragraphs
- **Easy Integration**: Seamlessly integrates with Sublime Text's command palette

## Installation

1. Download the plugin files
2. Place them in your Sublime Text Packages directory:
   - **Windows**: `%APPDATA%\Sublime Text\Packages\SRTtoTextAndMarkdown\`
   - **macOS**: `~/Library/Application Support/Sublime Text/Packages/SRTtoTextAndMarkdown/`
   - **Linux**: `~/.config/sublime-text/Packages/SRTtoTextAndMarkdown/`

Alternatively, you can install the `.sublime-package` file directly.

## Usage

### Method 1: Command Palette
1. Open an SRT file in Sublime Text
2. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS)
3. Type and select one of the following commands:
   - **"Convert SRT to Text"** - Converts to plain text format
   - **"Convert SRT to Markdown"** - Converts to Markdown format

### Method 2: Menu Access
The conversion commands are also available through Sublime Text's menu system.

## How It Works

### SRT Input Format
The plugin processes standard SRT subtitle files with the following format:
```
1
00:00:01,000 --> 00:00:04,000
This is the first subtitle line.

2
00:00:05,000 --> 00:00:08,000
This is the second subtitle line.
```

### Text Output
The plugin intelligently combines subtitle blocks into coherent paragraphs by:
- Removing sequence numbers and timestamps
- Combining related subtitle blocks into paragraphs
- Creating paragraph breaks when sentences end with punctuation (`.`, `!`, `?`, `:`, `;`)
- Preserving the natural flow of speech and content

### Markdown Output
The Markdown conversion:
- Uses the same intelligent text processing as the text converter
- Formats paragraphs with proper Markdown spacing (double line breaks)
- Creates clean, readable Markdown documents suitable for documentation or publishing

## Example

**Input SRT:**
```
1
00:00:01,000 --> 00:00:04,000
Welcome to our tutorial on

2
00:00:04,500 --> 00:00:07,000
how to use this amazing plugin.

3
00:00:08,000 --> 00:00:11,000
It's really quite simple!

4
00:00:12,000 --> 00:00:15,000
First, you open your SRT file
```

**Text Output:**
```
Welcome to our tutorial on how to use this amazing plugin.

It's really quite simple!

First, you open your SRT file
```

**Markdown Output:**
```
Welcome to our tutorial on how to use this amazing plugin.

It's really quite simple!

First, you open your SRT file
```

## Features in Detail

### Intelligent Paragraph Formation
- Automatically detects sentence boundaries
- Combines related subtitle blocks into coherent paragraphs
- Preserves natural reading flow

### Clean Output
- Removes all SRT formatting (sequence numbers, timestamps)
- Eliminates unnecessary line breaks
- Maintains proper spacing between paragraphs

### Sublime Text Integration
- Creates new scratch buffers for converted content
- Preserves original SRT file unchanged
- Easy access through Command Palette

## File Structure

```
SRTtoTextAndMarkdown/
├── __init__.py                    # Sublime Text command classes
├── srt_converter.py              # Core conversion logic
├── Default.sublime-commands      # Command palette integration
└── SRTtoTextAndMarkdown.sublime-package  # Packaged plugin
```

## Requirements

- Sublime Text 3 or 4
- Python 3.3+ (included with Sublime Text)

## License

This plugin is provided as-is for educational and productivity purposes.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this plugin.

## Changelog

### Version 1.0
- Initial release
- SRT to Text conversion
- SRT to Markdown conversion
- Intelligent paragraph formation
- Sublime Text Command Palette integration
