from bs4 import BeautifulSoup
import re
import pandas as pd


def remove_emoji(string):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "🤗"
        "🦙"
        "🦅"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", string)


if __name__ == "__main__":
    perf_html_table_path = "data/llm/perf_html_table"

    with open(perf_html_table_path, "r") as f:
        html_table = f.read()
    soup = BeautifulSoup(html_table, "html.parser")

    # Find the header row
    header_row = soup.find_all("tr")[0]
    header_columns = header_row.find_all("th")
    header = [remove_emoji(col.text.strip()).strip() for col in header_columns]
    header = header[1:]
    header = header[:-1]

    # Find the data rows
    data_rows = soup.find_all("tr")[1:]  # Skip the first row because it's the header

    all_rows_content = []
    for row in data_rows:
        columns = row.find_all("td")
        column_content = [
            remove_emoji(col.text.strip()).strip().replace("**", "") for col in columns
        ]
        if column_content[4].startswith("<") or column_content[8] == "N/A":
            continue
        column_content[4] = column_content[4].replace("~", "").replace("+", "")
        column_content[4] = column_content[4][:-1]
        column_content[4] = int(column_content[4])
        column_content[6] = int(column_content[6])
        column_content[7] = float(column_content[7])
        column_content[8] = int(column_content[8])
        column_content[9] = float(column_content[9])
        column_content = column_content[1:]
        column_content = column_content[:-1]
        all_rows_content.append(column_content)

    print(header)

    print(all_rows_content)

    save_data = pd.DataFrame(data=all_rows_content, columns=header)
    save_data.to_csv("data/llm/llm_perf_a100_80g.csv", index=False)
