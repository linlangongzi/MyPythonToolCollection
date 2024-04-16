from subprocess import Popen, PIPE


def get_commit_stats(commit):
    """
        Extracts insertions (+) and deletions (-) counts from a commit message.
    """
    command = ["git", "show", "--format=%b", "-n", "1", commit]
    with Popen(command, stdout=PIPE, stderr=PIPE) as process:
        output, err = process.communicate()
        if err:
            return None;
        stats = output.decode("utf-8").strip().split("\n")
        added = sum(int(line.split()[0]) for line in stats if line.startswith("+"))
        removed = sum(int(line.split()[0]) for line in stats if line.startswith("-"))
        return added, removed

def main():
    """
    Iterates through commits, sums code changes, and prints the results.
    """
    total_added = 0
    total_removed = 0
    for commit in (line.strip() for line in Popen(["git", "rev-list", "--all"], stdout=PIPE).communicate()[0].decode("utf-8").splitlines()):
        added, removed = get_commit_stats(commit)
        if added is not None:
            total_added += added
            total_removed += removed
    print("Total lines added:", total_added)
    print("Total lines removed:", total_removed)
    print("Total lines of Committed: ", total_added + total_removed)

if __name__ == "__main__":
    main()
