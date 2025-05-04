# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import sys
from collections import defaultdict

def main(file_paths):
    book_user_map = defaultdict(set)

    for i, file in enumerate(file_paths):
        try:
            df = pd.read_csv(file, usecols=["Title", "Exclusive Shelf"])
            for index, row in df.iterrows():
                if book_user_map.__contains__(row["Title"]) and row["Exclusive Shelf"] == "read":
                    book_user_map[row["Title"]] = book_user_map[row["Title"]] + 1
                elif row["Exclusive Shelf"] == "read":
                    book_user_map[row["Title"]] = 1;
        except Exception as e:
            print(f"Error processing {file}: {e}")
    for key, value in book_user_map.items():
        if value > 1:
            print(f"{key} has been read by {value} readers")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shared_books.py user1.csv user2.csv [user3.csv ...]")
    else:
        main(sys.argv[1:])

