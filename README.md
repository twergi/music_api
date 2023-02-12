# Music API

## Setting up
### Docker
- Clone repository
- In `Dockerfile`:
  - Set `DEBUG` to `True` or anything else for `False`
  - Set `SECRET_KEY` for Django secret key
- Build image with `docker-compose build`, while in repository folder
- Start container from created image with `docker-compose up`

### Manual
- Clone repository
- Create virtual environment
- In environment:
  - Set `DEBUG` to `True` or anything else for `False`
  - Set `SECRET_KEY` for Django secret key
- Run application with `python manage.py runserver`, while in working derictory

## Usage
### Swagger Web
- Open `127.0.0.1:8000/api/schema/docs/` in your browser

### Postman
- `.yaml` file can be obtained with accessing `127.0.0.1:8000/api/schema/`

### DRF
- Access `127.0.0.1:8000/api/` for routes
