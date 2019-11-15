### Postmortem

## What Went Wrong

1. Project structure is not ideal due to occurring circular imports. Should have used:
    * cookiecutter template,
    * blueprints,
    * application factories.

2. No real database for persistent storage. Used shelve which has drawbacks like:
    * it is not secure,
    * lack of scalability,
    * will be slow/unmanageable once data gets big (if exceeds the size of RAM).

3. Should have started writing tests earlier. Refactoring wouldn't be necessary and it would lead to cleaner code in the first place.

4. App does not manage to scrape pages which are protected against scraping like amazon.com. Could be overcome on a per website basis.

5. Some websites load their content in chunks. The app does not download content which isn't loaded right away.

6. Websites load images in different ways. Hence, the value of src of the img tag can differ. Therefore, for some sites the url generated to download the img can be incorrect.

## What Went Right

1. Docker configuration.

2. Celery-Flask synchronization.

3. Async task queue architecture.
