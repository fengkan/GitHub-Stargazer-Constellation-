# GitHub Stargazer Constellation

**GitHub Stargazer Constellation** is a Python-based tool that analyzes the stargazers of a GitHub repository and maps which other projects they have also starred. This reveals meaningful connections between open-source projects and helps uncover new, relevant repositories with overlapping communities.

---

## 🔧 Features

- Fetches stargazers of any public GitHub repository
- Analyzes what other repositories those users have starred
- Ranks and displays the top commonly starred projects
- Helps discover related or trending repositories
- Simple command-line interface

---

## 🚀 Usage

### 1. Set your GitHub token

Set your GitHub Personal Access Token via environment variable:

```bash
export GITHUB_TOKEN=ghp_xxx123yourtoken   # macOS/Linux
set GITHUB_TOKEN=ghp_xxx123yourtoken      # Windows CMD
$env:GITHUB_TOKEN="ghp_xxx123yourtoken"   # PowerShell
```

You can create a token in your [GitHub developer settings](https://github.com/settings/tokens).

### 2. Run the script

```bash
python stargazer_constellation.py https://github.com/owner/repo --limit 50
```

## 📦 Requirements
- Python 3.6+
- requests library
Install with:
```bash
pip install requests
```
---
## 🙌 Contributions
This repo was generated by ChatGPT.
