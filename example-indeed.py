import indeed

# Replace with your actual client_id and client_secret
client = indeed.IndeedClient(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")

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
