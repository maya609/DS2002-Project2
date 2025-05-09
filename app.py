from flask import Flask, request, jsonify
import pandas as pd
from tmdb_api import search_tmdb_movie

app = Flask(__name__)

# Load local dataset with all columns cast to native Python types
df = pd.read_csv('cleaned_netflix.csv').astype(object)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query', '').lower()

    # Check local Netflix data
    local_result = df[df['title'].str.lower() == query]
    if not local_result.empty:
        row = local_result.iloc[0]
        return jsonify({
            'source': 'local',
            'title': str(row['title']),
            'type': str(row['type']),
            'release_year': row['release_year']  # Already a native Python int or None
        })

    # Fallback to TMDB API
    api_key = "496259302f8b26ddff3d8d9a35247d5c"
    tmdb_result = search_tmdb_movie(query, api_key)
    tmdb_result['source'] = 'tmdb'
    return jsonify(tmdb_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
