QUERIES = [
    ('http://localhost:8000/1/queries/count/2015', {"count": 573697}),
    ('http://localhost:8000/1/queries/count/2015-08', {"count": 573697}),
    ('http://localhost:8000/1/queries/count/2015-08-03', {"count": 198117}),
    ('http://localhost:8000/1/queries/count/2015-08-01 00:04', {"count": 617}),
    ('http://localhost:8000/1/queries/popular/2015?size=3', {"queries": [
        {"query": "http%3A%2F%2Fwww.getsidekick.com%2Fblog%2Fbody-language-advice", "count": 6675},
        {"query": "http%3A%2F%2Fwebboard.yenta4.com%2Ftopic%2F568045", "count": 4652},
        {"query": "http%3A%2F%2Fwebboard.yenta4.com%2Ftopic%2F379035%3Fsort%3D1", "count": 3100}
    ]}),
    ('http://localhost:8000/1/queries/popular/2015-08-02?size=5', {"queries": [
        {"query": "http%3A%2F%2Fwww.getsidekick.com%2Fblog%2Fbody-language-advice", "count": 2283},
        {"query": "http%3A%2F%2Fwebboard.yenta4.com%2Ftopic%2F568045", "count": 1943},
        {"query": "http%3A%2F%2Fwebboard.yenta4.com%2Ftopic%2F379035%3Fsort%3D1", "count": 1358},
        {"query": "http%3A%2F%2Fjamonkey.com%2F50-organizing-ideas-for-every-room-in-your-house%2F", "count": 890},
        {"query": "http%3A%2F%2Fsharingis.cool%2F1000-musicians-played-foo-fighters-learn-to-fly-and-it-was-epic", "count": 701}
    ]}),
]

URLS = ["https://backmarket.fr", "https://www.ikea.com"]
