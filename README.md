# Internet Crawler for Text and Images

&nbsp;

## Usage

&nbsp;

### Get text from a website (and store it in shelve file)

**Definition**

 `POST /read-text`

 **Arguments**
 - `"url":string` url to the requested website

 **Response**

- `200 OK` on success

```json
    {
        "task-id": <id>,
        "requested-url": "https://www.example.com"
    }
```

**Usage**

`curl localhost:5000/read-text -d "url=https://www.example.com" -X POST`


&nbsp;

### Get images from a website (and store it in shelve file)

**Definition**

 `POST /read-images`

 **Arguments**
 - `"url":string` url to the requested website

 **Response**

- `200 OK`on success

```json
    {
        "task-id": <id>,
        "requested-url": "https://www.example.com"
    }
```

**Usage**

`curl localhost:5000/read-images -d "url=https://www.allegro.pl" -X POST`

&nbsp;

### Get status of the requested task

**Definition**

 `POST /status`

 **Arguments**
 - `task-id:str` the id of the requested task

 **Response**

- `200 OK` on success

```json
    {
        "task-id": <id>,
        "status": "SUCCESS|RUNNING|PENDING|FAILURE"
    }
```

**Usage**

`curl localhost:5000/status -d "task-id=<id>" -X POST`

&nbsp;

### Save downloaded text/image data

**Definition**

`POST /save`

**Arguments**
 - `content:str` type of content to download, supports `"text"|"images"`

 **Response**

- `200 OK` on success

```json
    {
        "task-id": <id>,
        "requested-content": "text|images"
    }
```

**Usage**

`curl localhost:5000/save -d "content=text" -X POST`
