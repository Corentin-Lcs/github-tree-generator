import requests

# Replace 'YOUR_GITHUB_ACCESS_TOKEN' with your actual GitHub access token.
ACCESS_TOKEN = 'YOUR_GITHUB_ACCESS_TOKEN'

def get_github_repo_tree(repo_url):
    """
    Fetches the directory tree of a GitHub repository.

    Parameters:
    repo_url (str): The URL of the GitHub repository.

    Returns:
    tuple: A tuple containing the directory tree structure and the repository name.
           If unsuccessful, returns (None, None).
    """
    parts = repo_url.strip("/").split("/")
    username, repo_name = parts[-2], parts[-1]
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/contents"
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        contents = response.json()
        tree = process_contents(contents)
        return tree, repo_name
    else:
        print(f"Failed to fetch repository contents. Status Code: {response.status_code}")
        return None, None

def process_contents(contents):
    """
    Recursively processes the contents fetched from GitHub.

    Parameters:
    contents (list): List of files and directories in the repository.

    Returns:
    list: A structured representation of the repository's directory tree.
    """
    tree = []
    for index, item in enumerate(contents):
        is_last = index == len(contents) - 1
        if item["type"] == "file":
            tree.append((item["name"], is_last))
        elif item["type"] == "dir":
            subdir_contents = get_subdirectory_contents(item["url"])
            subtree = (item["name"], process_contents(subdir_contents))
            tree.append((subtree, is_last))
    return tree

def get_subdirectory_contents(url):
    """
    Fetches contents of a subdirectory from GitHub.

    Parameters:
    url (str): URL of the subdirectory.

    Returns:
    list: Contents of the subdirectory.
    """
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def display_project_tree(tree, indent=""):
    """
    Displays the GitHub repository directory tree structure.

    Parameters:
    tree (list): Directory tree structure to display.
    indent (str): Current level of indentation for visual hierarchy.
    """
    for _, item in enumerate(tree):
        name, is_last = item
        branch_symbol = "└─" if is_last else "├─"
        if isinstance(name, tuple):
            subdir_name, subdir_contents = name
            print(f"{indent}{branch_symbol} {subdir_name}/")
            display_project_tree(subdir_contents, indent + ("    " if is_last else "│   "))
        else:
            print(f"{indent}{branch_symbol} {name}")

def save_project_tree_to_file(tree, repo_name, indent=""):
    """
    Saves the GitHub repository directory tree structure to a file.

    Parameters:
    tree (list): Directory tree structure to save.
    repo_name (str): Name of the GitHub repository.
    indent (str): Current level of indentation for visual hierarchy in the file.

    Returns:
    str: Filename where the project tree was saved.
    """
    filename = f"{repo_name.rstrip('/').replace('/', '_')}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"{repo_name}/\n")
        write_project_tree_to_file(tree, repo_name, indent, file)
    return filename

def write_project_tree_to_file(tree, repo_name, indent, file):
    """
    Helper function to recursively write the GitHub repository directory tree to a file.

    Parameters:
    tree (list): Directory tree structure to write.
    repo_name (str): Name of the GitHub repository.
    indent (str): Current level of indentation for visual hierarchy in the file.
    file (file object): File object to write the directory tree structure.
    """
    for _, item in enumerate(tree):
        name, is_last = item
        branch_symbol = "└─" if is_last else "├─"
        if isinstance(name, tuple):
            subdir_name, subdir_contents = name
            file.write(f"{indent}{branch_symbol} {subdir_name}/\n")
            write_project_tree_to_file(subdir_contents, repo_name, indent + ("    " if is_last else "│   "), file)
        else:
            file.write(f"{indent}{branch_symbol} {name}\n")

if __name__ == "__main__":
    """Main function to execute the program."""
    print("|------------------------------[ GitHub Tree Generator ]------------------------------|")
    repo_url = input("\nEnter the GitHub repository URL: ")
    project_tree, repo_name = get_github_repo_tree(repo_url)
    if project_tree and repo_name:
        print(f"\n{repo_name}/")
        display_project_tree(project_tree)
        save_option = input("\nDo you want to save the project tree to a file ? (Y/N): ").upper()
        if save_option == 'Y':
            filename = save_project_tree_to_file(project_tree, repo_name)
            print(f"\nProject tree saved to {filename} !")
        elif save_option == 'N':
            print("\nProject tree not saved.")
        else:
            print("\nInvalid option selected. Project tree not saved.")