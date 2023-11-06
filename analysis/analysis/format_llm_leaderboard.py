import pandas as pd
from data.llm.open_llm_leaderboard import header, content
from bs4 import BeautifulSoup


if __name__ == "__main__":
    header = header[1:-1]
    header[1] = "Average"
    for i in range(len(content)):
        soup = BeautifulSoup(content[i][1], "html.parser")
        model = soup.find_all("a")[0].text.strip()
        content[i][1] = model
        content[i] = content[i][1:-1]
        content[i][0] = (
            content[i][0].split("/")[1] if "/" in content[i][0] else content[i][0]
        )

    print(header)
    print(content)

    save_data = pd.DataFrame(data=content, columns=header)
    save_data.to_csv("data/llm/llm_leaderboard.csv", index=False)
