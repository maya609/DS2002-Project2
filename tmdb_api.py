import requests

def search_tmdb_movie(query, api_key):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': query,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get('results', [])

        if results:
            top_result = results[0]
            return {
                'title': top_result.get('title'),
                'overview': top_result.get('overview'),
                'release_date': top_result.get('release_date'),
                'vote_average': top_result.get('vote_average')
            }
        else:
            return {'message': 'No results found.'}
    except Exception as e:
        return {'error': str(e)}