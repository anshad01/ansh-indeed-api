import indeed

# Replace with your actual API key
client = indeed.IndeedClient(api_key="YOUR_API_KEY")

params = {
    "q": "software engineer",
    "l": "San Francisco",
    "radius": 25,
    "jt": "fulltime",
}

search_response = client.search(**params)

# Process and display job results
for job in search_response.results:
    print(job.title, job.company, job.location, job.url)
