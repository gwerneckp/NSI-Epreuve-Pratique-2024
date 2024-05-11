import re
import os
import shutil
from typing import Generator, Tuple
from black import format_file_contents, FileMode
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_sections(content: list) -> Generator[Tuple[int, str, list], None, None]:
    """Yield sujet number, directory name, and section content dynamically."""
    header_pattern = re.compile(r"^#\sSujet_(\d+)")
    buffer = []
    sujet_number = None
    for line in content:
        header_match = header_pattern.match(line)
        if header_match:
            if buffer:
                yield sujet_number, f"sujet_{sujet_number}", buffer
                buffer = []
            sujet_number = header_match.group(1)
        buffer.append(line)
    if buffer and sujet_number:
        yield sujet_number, f"sujet_{sujet_number}", buffer


def read_file(filename: str) -> list:
    """Read and return lines of a given file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        logging.error("The file does not exist.")
        return []


def format_python_code(content: list) -> list:
    """Format Python code blocks found in Markdown using Black."""
    code_block_pattern = re.compile(r"(```python)(.*?)(```)", re.DOTALL)
    formatted_content = []
    buffer = "".join(content)  # Join lines to handle multi-line matching

    def replace_func(match):
        code = match.group(2).strip()
        try:
            formatted_code = format_file_contents(code, fast=False, mode=FileMode())
            logging.info("Successfully formatted Python code block.")
        except Exception as e:
            logging.error(f"Error formatting Python code: {e}")
            formatted_code = code
        return f"```python\n{formatted_code.strip()}\n```"

    formatted_buffer = re.sub(code_block_pattern, replace_func, buffer)
    formatted_content = formatted_buffer.splitlines(True)
    return formatted_content


def replace_subheaders(content: list, sujet_number: str) -> list:
    """Replace specific subheaders within a sujet."""
    replaced_content = []
    for line in content:
        if match := re.match(r"## s_\d+\.(\d+)", line.strip()):
            exercise_number = match.group(1)
            replaced_content.append(f"## Exercice {exercise_number}\n")
            continue

        replaced_content.append(line)
    return replaced_content


def extract_python_code(content: list) -> str:
    """Extract Python code from Markdown content."""
    code = ""
    in_code_block = False
    for line in content:
        if line.strip().startswith("```python"):
            in_code_block = True
            continue
        elif line.strip() == "```" and in_code_block:
            in_code_block = False
            code += "\n"
            continue
        if in_code_block:
            code += line
    return code


def write_section(
    directory: str, filename: str, content: list, image_pattern: re.Pattern
) -> None:
    """Write content to a file and handle image copying."""
    images_directory = os.path.join(directory, "images")
    os.makedirs(images_directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        for line in content:
            image_match = image_pattern.search(line)
            if image_match:
                handle_image_copy(image_match.group(1), directory)
            file.write(line)
    logging.info(f"Written content and handled images for {filename}")


def handle_image_copy(image_path: str, directory: str) -> None:
    """Copy image files to the correct directory."""
    source_path = image_path
    target_path = os.path.join(directory, image_path)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    if os.path.exists(source_path):
        shutil.copy(source_path, target_path)
        logging.info(f"Copied image from {source_path} to {target_path}")
    else:
        logging.warning(f"Image source path does not exist: {source_path}")


def markdown_pipeline(filename: str) -> None:
    """Process Markdown file: format code, split by headers, handle images."""
    content = read_file(filename)
    if not content:
        return
    formatted_content = format_python_code(content)
    image_pattern = re.compile(r"!\[.*?\]\((images/.+?)\)")

    for sujet_number, directory_name, section in find_sections(formatted_content):
        replaced_section = replace_subheaders(section, sujet_number)
        write_section(
            directory_name, f"Sujet_{sujet_number}.md", replaced_section, image_pattern
        )
        # Extract and write Python code to files
        python_code = extract_python_code(replaced_section)
        with open(
            os.path.join(directory_name, f"sujet_{sujet_number}.py"), "w"
        ) as py_file:
            py_file.write(python_code)
        with open(
            os.path.join(directory_name, f"sujet_answer_{sujet_number}.py"), "w"
        ) as ans_file:
            ans_file.write(
                python_code
            )  # Adjust this as necessary for different content

    logging.info("Markdown file processed successfully.")


# Usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        markdown_pipeline(sys.argv[1])
