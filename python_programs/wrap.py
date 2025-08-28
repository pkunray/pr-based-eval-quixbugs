def wrap(text, cols):
    if not isinstance(cols, int) or cols <= 0:
        raise ValueError('cols must be a positive integer')
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:].lstrip()
        lines.append(line)
    if text:
        lines.append(text)
    return lines
