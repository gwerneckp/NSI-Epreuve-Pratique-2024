import os
import re

base_dir = "/home/gwern/Projects/NSI-Epreuve-Pratique-2024/pre_pipeline/2024/"


def transform_repl_into_unittest(code: str) -> str:
    # Extract function name and cases using regex
    function_name_match = re.search(r">>> ([\w\.]+)\(", code)
    if not function_name_match:
        raise ValueError("No function name found in the input code.")
    function_name = function_name_match.group(1)

    # Extract the test cases
    test_cases = re.findall(r">>> (.*?)\n(.*?)$", code, re.MULTILINE)

    # Start forming the class string
    # class_str = f"class TestSujet{sujet:02d}(TestCase):\n"
    class_str = ""

    for i, (call, result) in enumerate(test_cases, start=1):
        # Determine the assertion type
        if result.strip() == "False":
            assertion = "assertFalse"
        elif result.strip() == "True":
            assertion = "assertTrue"
        else:
            assertion = "assertEqual"
            result = result.strip()

        # Add the test method to the class string
        class_str += f"    def test_{function_name}_case_{i}(self) -> None:\n"
        if assertion == "assertEqual":
            class_str += f"        self.{assertion}({call}, {result})\n"
        else:
            class_str += f"        self.{assertion}({call})\n"
        class_str += "\n"

    return class_str


def is_fake_repl(code: str) -> bool:
    # Define the regular expression pattern to match the REPL format
    pattern = r">>> \w+\(.*?\)\n.*"

    # Find all matches of the pattern in the input code
    matches = re.findall(pattern, code, re.MULTILINE)

    # Check if the matches cover the entire input code (excluding leading/trailing whitespace)
    code_cleaned = code.strip()
    matches_combined = "\n".join(matches).strip()

    return code_cleaned == matches_combined


if __name__ == "__main__":
    for i in range(25, 49):
        dir_name_1 = f"{i}_1"
        dir_name_2 = f"{i}_2"

        dir_path_1 = os.path.join(base_dir, dir_name_1)
        dir_path_2 = os.path.join(base_dir, dir_name_2)

        # Perform operations on the directories
        # For example, you can print the directory paths
        output_dir = os.path.join(base_dir, "output", f"sujet_{i}")
        os.makedirs(output_dir, exist_ok=True)

        enonce_1_path = os.path.join(dir_path_1, "enonce.md")
        enonce_2_path = os.path.join(dir_path_2, "enonce.md")

        with open(enonce_1_path, "r") as enonce_1_file:
            enonce_1 = enonce_1_file.read()

        with open(enonce_2_path, "r") as enonce_2_file:
            enonce_2 = enonce_2_file.read()

        combined_enonce = (
            f"# Sujet {i}\n\n## Exercice 1\n\n{enonce_1}\n\n## Exercice 2\n\n{enonce_2}"
        )
        # replace ’ with '
        combined_enonce = combined_enonce.replace("’", "'")

        # remove linenums='1'
        combined_enonce = re.sub(r"linenums='\d+'", "", combined_enonce)

        output_file_path = os.path.join(output_dir, f"Sujet_{i}.md")
        with open(output_file_path, "w") as output_file:
            output_file.write(combined_enonce)

        python_file_path = os.path.join(output_dir, f"sujet_{i}.py")
        python_answer_path = os.path.join(output_dir, f"sujet_answer_{i}.py")
        unittests: str = f"class TestSujet{i}(TestCase):\n"
        with open(python_file_path, "w") as python_file:
            # Find all Python code blocks in the combined_enonce
            code_blocks = re.findall(r"```python(.*?)```", combined_enonce, re.DOTALL)
            for code_block in code_blocks:
                # Check if the code block is a fake REPL
                if is_fake_repl(code_block):
                    # If it is a fake REPL, add the unittests instead
                    unittests += transform_repl_into_unittest(code_block)
                else:
                    # If it is not a fake REPL, write the code block to the Python file
                    python_file.write(code_block.strip())
                    python_file.write("\n\n")

        # copy python file to answer file
        with open(python_file_path, "r") as python_file:
            with open(python_answer_path, "w") as python_answer_file:
                python_answer_file.write("""from unittest import TestCase, main\n\n""")
                python_answer_file.write(python_file.read())
                python_answer_file.write(unittests)
                python_answer_file.write(
                    """if __name__ == "__main__":
        main()"""
                )
