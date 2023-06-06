import requests


def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to download data")


def extract_data(data):
    show_info = {
        'id': data['id'],
        'url': data['url'],
        'name': data['name']
    }

    episodes = data['_embedded']['episodes']
    episode_list = []
    for episode in episodes:
        episode_info = {
            'season': episode['season'],
            'number': episode['number'],
            'type': episode['type'],
            'airdate': episode['airdate'],
            'airtime': episode['airtime'],
            'runtime': episode['runtime'],
            'average_rating': episode['rating']['average'],
            'summary': episode['summary'].strip('<p>').strip('</p>'),
            'medium_image': episode['image']['medium'],
            'original_image': episode['image']['original']
        }
        episode_list.append(episode_info)

    return show_info, episode_list


# Download the data from the API link
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
show_data = download_data(url)

# Extract the required data attributes
show_info, episode_list = extract_data(show_data)

# Print the show info
print("Show Info:")
print("ID:", show_info['id'])
print("URL:", show_info['url'])
print("Name:", show_info['name'])
print()

# Print the episode list
print("Episode List:")
for episode in episode_list:
    print("Season:", episode['season'])
    print("Episode Number:", episode['number'])
    print("Type:", episode['type'])
    print("Airdate:", episode['airdate'])
    print("Airtime:", episode['airtime'])
    print("Runtime:", episode['runtime'])
    print("Average Rating:", episode['average_rating'])
    print("Summary:", episode['summary'])
    print("Medium Image:", episode['medium_image'])
    print("Original Image:", episode['original_image'])
    print()
