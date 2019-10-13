from pathlib import Path


def append_to_file(path, to_write):
    with open(path, "a") as file:
        file.write(to_write)


if __name__ == "__main__":
    filename = "JIRA_tasks.txt"
    delimiter = "-" * 80
    path = Path() / filename

    jira_task_name = input("JIRA task name: ")
    jira_task_desc = input("JIRA task description: ")

    _jira_task_desc_underscored = jira_task_desc.replace(" ", "_")
    jira_full_task = f"{jira_task_name} - {jira_task_desc}"
    first_commit = f"Close {jira_full_task}"
    another_commit = f"{jira_task_name} - <message>"
    git_branch_name = f"{jira_task_name}-{_jira_task_desc_underscored}"

    info = {
        "GIT": git_branch_name,
        "JIRA": jira_full_task,
        "First": first_commit,
        "Other": another_commit,
    }

    lines = "\n".join([f"{key}:\t{value}" for key, value in info.items()])
    result = f"{lines}\n{delimiter}\n"

    print(lines)
    append_to_file(path, result)
