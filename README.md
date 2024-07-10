<h1 align="center">GitHub Tree Generator</h1>

The "GitHub Tree Generator" GitHub project is a powerful tool to visualize the structure of GitHub repositories in a tree format. It allows users to see the hierarchical organization of files and directories, making it easier to navigate and understand complex projects.

> [!CAUTION]
> Ensure the GitHub access token remains secure and is not publicly exposed. Public exposure can lead to unauthorized access to repositories, data breaches, and potential abuse of the GitHub account.

<p align="center">
  <img src="https://github.com/Corentin-Lcs/github-tree-generator/blob/main/GitHub_Tree.png" alt="GitHub_Tree.png"/>
</p>

## Usage

To use the program from the command prompt, run the following command :

```
python script.py
```

To illustrate the execution, here is an example :

```
|-----------------------------------[ GitHub Tree Generator ]-----------------------------------|

Enter the GitHub repository URL: https://github.com/Corentin-Lcs/periodic-table-of-elements

periodic-table-of-elements/
├─ LICENSE
├─ Periodic_Table.jpg
├─ README.md
├─ With_Lines.png
├─ Without_Lines.png
└─ src/
    ├─ EN/
    │   ├─ Periodic Table of Elements.pdf
    │   └─ Periodic_Table_of_Elements.tex
    ├─ FR/
    │   ├─ Tableau Périodique des Éléments.pdf
    │   └─ Tableau_Périodique_des_Éléments.tex
    └─ LaTeX LPPL.pdf

Do you want to save the project tree to a file ? (Y/N): Y

Project tree saved to periodic-table-of-elements.txt !
```

> The program requires a GitHub token, generated from _Settings > Developer settings > Personal access tokens > Tokens (classic)_.

## Project's Structure

```
github-tree-generator/
├─ README.md
├─ LICENSE
├─ GitHub_Tree.png
└─ src/
   └─ script.py
```

## Meta

Created by [@Corentin-Lcs](https://github.com/Corentin-Lcs). Feel free to contact me !

Distributed under the GNU GPLv3 license. See [LICENSE](https://github.com/Corentin-Lcs/github-tree-generator/blob/main/LICENSE) for more information.
