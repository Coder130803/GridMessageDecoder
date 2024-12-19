import requests
from bs4 import BeautifulSoup

def display_secret_message(url):
    """
    Fetches HTML data from the Google Doc URL, parses the table, 
    generates the grid, and prints the secret message.
    """
    # Step 1: Fetch the HTML content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status Code: {response.status_code}")
    html_content = response.text

    # Step 2: Parse the HTML table using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')  # Find all table rows
    data = []

    # Step 3: Extract data from table rows
    for row in rows[1:]:  # Skip the header
        cols = row.find_all('td')  # Find all columns in a row
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            data.append((x, y, char))

    # Step 4: Determine grid dimensions
    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, y, _ in data)

    # Step 5: Create and fill the grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in data:
        grid[y][x] = char

    # Step 6: Print the grid
    for row in grid:
        print(''.join(row))
