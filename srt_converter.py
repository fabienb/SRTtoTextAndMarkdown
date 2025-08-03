# srt_converter.py
import re

def convert_srt_to_text(srt_content):
    # Extract subtitle text blocks
    lines = srt_content.split('\n')
    subtitle_blocks = []
    current_block = []
    
    for line in lines:
        line = line.strip()
        
        # Skip sequence numbers and timestamps
        if re.match(r'^\d+$', line) or '-->' in line:
            continue
        
        # If we hit an empty line and have content, save the block
        if not line and current_block:
            subtitle_blocks.append(' '.join(current_block))
            current_block = []
        elif line:  # Add non-empty lines to current block
            current_block.append(line)
    
    # Don't forget the last block
    if current_block:
        subtitle_blocks.append(' '.join(current_block))
    
    # Join blocks intelligently
    result_paragraphs = []
    current_paragraph = ""
    
    for block in subtitle_blocks:
        if not block:
            continue
            
        if not current_paragraph:
            current_paragraph = block
        else:
            # Check if previous block ends with sentence-ending punctuation
            if current_paragraph.rstrip().endswith(('.', '!', '?', ':', ';')):
                # Start new paragraph
                result_paragraphs.append(current_paragraph)
                current_paragraph = block
            else:
                # Continue same paragraph
                current_paragraph += " " + block
    
    # Add the final paragraph
    if current_paragraph:
        result_paragraphs.append(current_paragraph)
    
    return '\n'.join(result_paragraphs).strip()

def convert_srt_to_markdown(srt_content):
    # Use the same intelligent text conversion logic
    text_content = convert_srt_to_text(srt_content)
    
    # Split into paragraphs and format as Markdown
    paragraphs = text_content.split('\n')
    
    # Add double line breaks between paragraphs for proper Markdown formatting
    return '\n\n'.join(paragraph.strip() for paragraph in paragraphs if paragraph.strip())
