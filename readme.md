## The assignment: Web page analyser service
Implement a service that acts as a web analysing service. The service has a REST API that takes an url as input. The service scrapes the page behind that url and does textual analysis for the contents. The analysis done in this exercise consists of two outputs:
- the word frequencies of the textual content after required data normalisations and cleaning is done
- List of person names found in the page.

This result is provided for the user.
#### Example input:
```json
{"url": "https://en.wikipedia.org/wiki/Space_physics"}
```

#### Example result:
```json
{"word_counts": {"earth": 11,
"first": 5,
...
},
"names": ["William Gilbert", "George Graham", ...]
}"
```


The results don't need to be 100% correct.

The scraping doesn't need to work in more complex sites, no need to evaluate JS. It is enough that it works on static web pages.

The context for this service is that it would be put into a cloud environment for multiple users.


### Some Requirements:
- This service should be packaged inside a docker container.
- Return a Zip file with the solution (source codes + dockerfile) 1-2 days prior to the interview.
- Readme.md that explains how to compile and run the application.
- We would like you to demonstrate idiomatic styles of the chosen programming languages.
- Please avoid making your solution available to potential third parties by e.g. posting it to an open service like github


### Virtual environment
- Create the virtualenv
```bash 
virtualenv -p python3.8 venv
```
- Activate the virtualenv
```bash
source venv/bin/activate
```

### How to Run It

- Install requirements as usual:
    ```bash
       pip install -r requirements/requirements.txt
       pip install -r requirements/test-requirements.txt
    ```
  
- Run the FastAPI app using:
  ```bash
  uvicorn main:app --reload
  ```
  
- Open API Documentation after running to try out the API:
  http://127.0.0.1:8000/docs


- Run pytest with coverage:
  ```bash
  coverage run -m pytest
  ```

### TODO Improvement:

- `scrape_paragraph()` only scrape `<p>`, could this be `<body>` instead
- `count_word()` does not ignore special character, therefore have distinct count between `earth` and `earth's`
- `count_word()` does not return sorted frequency.
- Unit Tests
- Make more idiomatic
- Dockerize
