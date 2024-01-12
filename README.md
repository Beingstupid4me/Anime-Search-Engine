# Anime Search with MyAnimeList API

This Python script uses the MyAnimeList API from RapidAPI to search for anime information.

## How it works

1. The script first establishes a connection with the MyAnimeList API.
2. It then asks the user to input the name of an anime they want to search for.
3. The script sends a GET request to the API with the anime name.
4. The API returns a list of anime that match the search query.
5. The script prints out the titles and descriptions of the search results.
6. The user is then asked to select one of the results by entering its serial number.
7. The script sends another GET request to the API to get more detailed information about the selected anime.
8. Finally, the script prints out the detailed information, including the synopsis of the anime.

## Usage

To run the script, you will need Python installed on your machine. You will also need your RapidAPI key. Please replace 'X-RapidAPI-Key' and 'X-RapidAPI-Host' in the script with your actual RapidAPI key and host.

Please note: Do not share your RapidAPI key publicly to prevent misuse.

## Limitations

This script won't run in environments that don't support user input or external API calls. Also, it won't run if the RapidAPI key or host is incorrect.

## Authors
- Amartya Singh
- Abhishek Bansal
- Adarsh jha
