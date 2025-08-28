def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end].rstrip(), text[end:].lstrip()
        lines.append(line)
        
    return lines
