# Internet Crawler for Text and Images

## Usage

 ### Get text from a website (and store it in a database)

**Definition**

 `GET /read-text/<url-to-website>`

 **Response**

- `200 OK` on success

```json
    {
        "requested-url": "https://www.example.com",
        "text": "text content of the requested website without tags"
    }
```

### Get images from a website (and store it in a database)

**Definition**

 `GET /read-images/<url-to-website>`

 **Response**

- `200 OK` on success

```json
    {
        "requested-url": "https://www.example.com",
        "images": {
            "img_1.jpeg",
            "img_2.jpeg", 
            ..., 
            "img_n.jpeg"
        }
    }
```