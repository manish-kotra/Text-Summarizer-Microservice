import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


def create_directories_and_files(project_name: str, list_of_files: list) -> None:
    """
    Create directories and files based on the provided list of files.

    Args:
        project_name (str): The name of the project.
        list_of_files (list): A list of file paths to create.

    Returns:
        None
    """
    for file_path in list_of_files:
        file_path = Path(file_path)
        filedir, filename = os.path.split(file_path)

        if filedir != "":
            # Create the directory if it doesn't exist
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory '{filedir}' created.")

        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            # Create the file if it doesn't exist or is empty
            with open(file_path, 'w') as f:
                pass
                logging.info(f"Creating empty file '{file_path}'")
        else:
            logging.info(f"File '{file_path}' already exists.")



if __name__ == "__main__":
    project_name = "Text-Summarizer"

    list_of_files = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/utils/logging/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        f"src/{project_name}/notebooks/trial.ipynb",
        f"src/{project_name}/logging/__init__.py",
        "config/config.yaml",
        "parameters.yaml",
        "README.md",
        "requirements.txt",
        "setup.py",
        "main.py",
        "Dockerfile",
        "app.py", 
    ]

    # Create the project directory if it doesn't exist
    project_dir = Path(project_name)
    os.makedirs(project_dir, exist_ok=True)
    logging.info(f"Project directory '{project_name}' created.")

    # Change the current working directory to the project directory
    os.chdir(project_dir)

    # Create directories and files
    create_directories_and_files(project_name, list_of_files)