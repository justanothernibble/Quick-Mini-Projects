"""
Movie API in Python
My key: NOPE.
"""

import requests as req
import json
import seaborn as sb
import requests

api_key = "NOPE."


def movie_insights(movie):
    for key, value in movie.items():
        if key=='Title' or key=='Year' or key=='Genre' or key=='imdbRating':
            print(f"{key}: {value}")

def search_multiple_titles(titles):
    results = []
    for title in titles:
        dTemp = {}
        current_response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={make_formatted(title)[0]}")
        data_of_current_title = current_response.json()
        i=0
        for key,value in data_of_current_title.items():
            if key=='Title' or key=='Year' or key=='Genre' or key=='imdbRating':
                dTemp[key] = value
        results.append(dTemp)
        i+=1
    return results
        
def make_formatted(title):
    splitted_title = title.split()
    if len(splitted_title) == 1:
        formatted_title = splitted_title[0]
        return [formatted_title, True]

    else:
        formatted_title = splitted_title[0]
        try:
            for i in range(len(splitted_title)-1):

                formatted_title = f"{formatted_title}+{splitted_title[i+1]}"
            return [formatted_title, True]
        except Exception as e:
            return [f"Error: {e}", False]

while True:
    choice = int(input("What do you want to do?\n1. Search 1 title\n2. Search multiple titles\n3. Exit\n> "))

    if choice == 1:
        title = input("Enter a title\n> ")
        processed_title = make_formatted(title)

        if processed_title[1] == True:
            j=0
            response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={processed_title[0]}")
            if response.status_code == 200:   # HTTP Status code (200 means success)
                print("HTTP Connection made: Success")
                movie = response.json()       # Display the JSON response
                for i, key in enumerate(movie):
                    if key == 'Response' or key == 'Error':
                        print(f"{key}: {movie[key]}")
                        j+=1
                        if j == 2:
                            break
                movie_insights(movie)

            elif response.status_code == 404:
                print("Movie not found") # error handling

            else:
                print(f"Unknown Error: {response.status_code}") # more error handling...
        else:
            print(f"There was an error: {processed_title[0]}\nSuccess: {processed_title[1]}") # even more error handling... guess what comes next?

    elif choice == 2:
        title_list = []
        i=0
        while True:
            new_title_or_exit = int(input("Would you like to... \n1. Enter a new title\n2. Exit\n> "))
            if new_title_or_exit == 1:
                i+=1
                title_temp = input(f"Enter title {i}:\n> ")
                title_list.append(title_temp)
            elif new_title_or_exit == 2 and len(title_list)>0:
                print("Fetching API data... Please wait")
                break
            elif new_title_or_exit == 2 and len(title_list)==0:
                print("Exiting")
                break
            else:
                print("Invalid input")
        if len(title_list)>0:
            multiple_titles_data = search_multiple_titles(title_list)
            for i in range(len(multiple_titles_data)):
                movie_insights(multiple_titles_data[i])
                print("")


    elif choice == 3:
        print("Goodbye")
        break