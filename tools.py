def write_content_to_file(content, filename, extension="md"):
    """
    Takes in a filename, content, and file extension to write to the file.
    -> write the content to the file with the correct extension
    """
    with open(f"{filename}.{extension}", "w") as f:
        f.write(content)
    print(f"--Content written to {filename}.{extension}--")
    return
