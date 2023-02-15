# Music API

## Setting up
### Docker
- Clone repository `git clone https://github.com/twergi/music_api.git`
- In `Dockerfile`:
  - Set `DEBUG` to `True` or `False`
  - Set `SECRET_KEY` for Django secret key
- Build image with `docker-compose build`, while in working directory
- Start container from created image with `docker-compose up`

### Manual (using Python's virtualenv)
- Clone repository `git clone https://github.com/twergi/music_api.git`
- Create virtual environment `python -m virtualenv venv`
- Set environment variables (add lines to the `activate` file in `./venv/bin/` or `.\venv\Scripts\`):
  - Set `DEBUG` to `True` or `False` (e.g. `export DEBUG=True`)
  - Set `SECRET_KEY` for Django secret key (e.g. `export SECRET_KEY=<DJANGO_SECRET_KEY>`)
- Activate environment:
  - Linux - `source ./venv/bin/activate`
  - Windows - `.\venv\Scripts\activate`
- Run application with `python manage.py runserver`, while in working directory

## Usage
### Swagger Web
- Open `localhost:8000/api/schema/docs/` in your browser

### Postman
- `.yaml` file can be obtained by accessing `localhost:8000/api/schema/`

### DRF
- Access `localhost:8000/api/` for routes
