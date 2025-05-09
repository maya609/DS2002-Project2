# Flask Chatbot: Netflix + TMDB Movie Info

## How it works
- Searches `cleaned_netflix.csv` for matching titles
- If not found, fetches info from the TMDB API

## API Endpoint
`POST /chat`

### Request Format
```json
{ "query": "The Office" }
```

## Response
Returns a JSON object containing the movie/show information, with a `"source"` field indicating whether the result came from the local dataset or the TMDB API.

### Example Response
```json
{
  "source": "local",
  "title": "Inception",
  "type": "Movie",
  "release_year": 2010
}
```

## Deployment
This chatbot is hosted on a Google Cloud Platform VM and is publicly accessible via the web.

**Live chatbot URL:**  
[http://34.57.146.240:5000/chat](http://34.57.146.240:5000/chat)

## How to Test It

You can test the chatbot using `curl` from your terminal:

```bash
curl -X POST http://34.57.146.240:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "Inception"}'
```

You should receive a JSON response with the movie info if the title is found in the dataset or via the TMDB API.



