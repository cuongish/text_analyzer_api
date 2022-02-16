## Web page analyzer service

`wiki_api` is a simple API which analyze the text of a given website URL, and returns a list of word frequencies 
and a list of person names found in the page.

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
#### Locally
- Install requirements as usual:
    ```bash
       pip install -r requirements/requirements.txt
       pip install -r requirements/test-requirements.txt
    ```
  - Install spacy en_core_web_sm after installing requirements:
    ```bash
    python -m spacy download en_core_web_sm
    ```

- Run unit tests with coverage:
  ```bash
  coverage run -m pytest
  ```
- Run the FastAPI app using:
  ```bash
  uvicorn app.main:app --reload
  ```
- Open API Documentation after running to try out the API: http://127.0.0.1:8000/docs


#### Or via Dockerfile
- Build docker image of `wiki_api`
  ```bash
  docker build -t wiki_api_image .
  ```
- Start the Docker Container based on the image of `wiki_api`
  ```bash
  docker run -d --name wiki_api_container -p 80:80 wiki_api_image
  ```
- Now you should be able to check it in your Docker container's URL, for example: http://0.0.0.0/, 
http://192.168.99.100/text_analyzer or http://127.0.0.1/docs (or equivalent, using your Docker host).

### Improvement TODO:

- `scrape_paragraph()` was designed to only scrape `<p>` part of html. Does this meet the requirement?

- `count_word()` using Counter only count the text splitting by space, therefore does not split special characters like
possessive`'s`, thus distinctly counts between `earth` and `earth's`. In next iterations, `spaCy` should be used to tokenize 
the passage first to filter out the special character via `tag_`

- `text_analyze()` does not  return the sorted frequency list. However, this is not in the requirement.

- Including and installing`spacy`.`en_core_web_sm` via requirements.txt instead of via the Dockerfile

- 100% coverage for Unit Tests

- Make more idiomatic