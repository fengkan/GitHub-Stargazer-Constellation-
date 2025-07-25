import requests
from collections import Counter
import time
import argparse
import os
import sys

# Load GitHub token from environment variable
TOKEN = os.getenv('GITHUB_TOKEN')
if not TOKEN:
    print("Error: Please set the GITHUB_TOKEN environment variable.")
    sys.exit(1)

HEADERS = {'Authorization': f'token {TOKEN}'}

# Extract owner/repo from a GitHub URL
def extract_repo_from_url(url):
    if url.startswith("https://github.com/"):
        return "/".join(url.split('/')[-2:])
    else:
        raise ValueError("Invalid GitHub URL format. Please provide a URL in the form 'https://github.com/owner/repo'.")

# Get stargazers for a repository, with optional limit
def get_stargazers(repo, limit):
    url = f'https://api.github.com/repos/{repo}/stargazers'
    stargazers = []
    page = 1

    while True:
        response = requests.get(url, headers=HEADERS, params={'per_page': 100, 'page': page})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch stargazers: {response.status_code}")
        
        data = response.json()
        if not data:
            break
        stargazers.extend([user['login'] for user in data])
        page += 1

        if limit != 0 and len(stargazers) >= limit:
            break

    return stargazers if limit == 0 else stargazers[:limit]

# Get starred repositories of a user, with optional limit
def get_user_stars(user, limit):
    print(f"Fetching starred repositories for {user}...")
    url = f'https://api.github.com/users/{user}/starred'
    stars = []
    page = 1

    while True:
        response = requests.get(url, headers=HEADERS, params={'per_page': 100, 'page': page})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch starred repos for {user}: {response.status_code}")
        
        data = response.json()
        if not data:
            break
        stars.extend([repo['full_name'] for repo in data])
        page += 1

        if limit != 0 and len(stars) >= limit:
            break

    return stars if limit == 0 else stars[:limit]

# Main function: analyze stargazers and count what other repositories they starred
def main(repo_url, limit):
    repo = extract_repo_from_url(repo_url)
    print(f"Processing repository: {repo}")

    stargazers = get_stargazers(repo, limit)
    print(f"Found {len(stargazers)} stargazers for repository {repo}.")

    star_count = Counter()

    try:
        for user in stargazers:
            stars = get_user_stars(user, limit)
            star_count.update(stars)
            print(f"{user} has starred {len(stars)} repositories.")
            time.sleep(1)
    except Exception as e:
        print(f"Error fetching stars for {user}: {e}")

    top_projects = star_count.most_common(10)

    print("\nTop 10 most starred repositories by stargazers:")
    for repo_name, count in top_projects:
        print(f"{repo_name}: {count} stargazers")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch and sort GitHub stargazers by their starred repositories.')
    parser.add_argument('repo_url', type=str, help='GitHub repository URL in the format "https://github.com/owner/repo"')
    parser.add_argument('--limit', type=int, default=100, help='Limit the number of stargazers and starred repos. Use 0 for no limit.')

    args = parser.parse_args()
    main(args.repo_url, args.limit)
