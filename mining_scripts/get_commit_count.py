import requests

base_url = 'https://api.github.com'


def get_all_commits_count(owner, repo, sha):
    first_commit = get_first_commit(owner, repo)
    compare_url = '{}/repos/{}/{}/compare/{}...{}'.format(base_url, owner, repo, first_commit, sha)

    commit_req = requests.get(compare_url)
    commit_count = commit_req.json()['total_commits'] + 1
    print(commit_count)
    return commit_count


def get_first_commit(owner, repo):
    url = '{}/repos/{}/{}/commits'.format(base_url, owner, repo)
    req = requests.get(url)
    json_data = req.json()

    if req.headers.get('Link'):
        page_url = req.headers.get('Link').split(',')[1].split(';')[0].split('<')[1].split('>')[0]
        req_last_commit = requests.get(page_url)
        first_commit = req_last_commit.json()
        first_commit_hash = first_commit[-1]['sha']
    else:
        first_commit_hash = json_data[-1]['sha']
    return first_commit_hash


def main():
    owner = 'getredash'
    repo = 'redash'
    # Took the last commit, Can do it automatically also but keeping it open
    sha = '5ba15ef35074a88daa5032ec4bec34d3a22a607e'
    get_all_commits_count(owner, repo, sha)


if __name__ == '__main__':
    main()