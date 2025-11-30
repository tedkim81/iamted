# IamTed

## What is this?
* I am Ted Kim. This is the code of my profile page.

## Project Status
* **⚠️ Django Framework: DEPRECATED**
* The Django project in this repository is no longer maintained.
* The profile page has been converted to a static HTML document and is now hosted on AWS S3.
* All current content is available in `static/html/` directory:
  - `index.html` - Main profile page (supports Korean/English via `?lang=ko` or `?lang=en`)
  - `blog_profile.jpg` - Profile image
  - `favicon.ico` - Favicon

## Deployment
* The static HTML files in `static/html/` are deployed to AWS S3 for web hosting.
* No server-side framework is required anymore.

## What can be helpful?
* ~~a reference of simple django project~~ (deprecated)
* A reference for converting Django templates to static HTML with multilingual support