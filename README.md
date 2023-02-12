# Music API

## Setting up
### Docker
- Clone repository `git clone https://github.com/twergi/music_api.git`
- In `Dockerfile`:
  - Set `DEBUG` to `True` or `False`
  - Set `SECRET_KEY` for Django secret key
- Build image with `docker-compose build`, while in working directory
- Start container from created image with `docker-compose up`

### Manual
- Clone repository `git clone https://github.com/twergi/music_api.git`
- Create virtual environment (e.g. `python -m virtualenv venv`)
- In environment:
  - Set `DEBUG` to `True` or `False`
  - Set `SECRET_KEY` for Django secret key
- Run application with `python manage.py runserver`, while in working directory

## Usage
### Swagger Web
- Open `localhost:8000/api/schema/docs/` in your browser

### Postman
- `.yaml` file can be obtained by accessing `localhost:8000/api/schema/`

### DRF
- Access `localhost:8000/api/` for routes
