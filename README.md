# Internet Crawler for Text and Images

## Usage

 ### Get text from a website (and store it in a database)

**Definition**

 `GET /read-text`

 **Arguments**
 - `"url-to-website":string` url to the requested website

 **Response**

- `200 OK` on success

```json
    {
        "task-id": 1,
        "requested-url": "https://www.example.com",
        "text": "text content of the requested website without tags"
    }
```

### Get images from a website (and store it in a database)

**Definition**

 `GET /read-images`

 **Arguments**
 - `"url-to-website":string` url to the requested website

 **Response**

- `200 OK` on success

```json
    {
        "task-id": 1,
        "requested-url": "https://www.example.com",
        "images": {
            "img_1.jpeg",
            "img_2.jpeg", 
            ..., 
            "img_n.jpeg"
        }
    }
```

**Definition**

 `GET /status`

 **Arguments**
 - `task-id:int` the id of the requested task

 **Response**

- `200 OK` on success

```json
    {
        "task-id": 1,
        "status": "RUNNING|PENDING|ERROR|CANCELLED"
    }
```