# MusicRank Django Project - AI Agent Instructions

## Architecture Overview
- **Framework**: Django 5.2.8 with MTV pattern (Models-Templates-Views)
- **Apps**: Single main app `MusicRank` handling album reviews; project root `trabalho`
- **Database**: SQLite3 (`db.sqlite3`) with migrations in `MusicRank/migrations/`
- **Media Handling**: Images stored in `media/albums/` for album covers, `media/avatars/` for user profiles
- **Authentication**: Django's built-in auth with custom `UserProfile` model for avatars
- **Language**: Portuguese (pt-br) with timezone America/Sao_Paulo

## Key Models
- `Album`: title, artist, image (optional), review, user (FK to User)
- `UserProfile`: OneToOne to User, avatar (optional)

## URL Patterns & Views
- Root `/`: `inicio` view - shows landing if not logged in, else all albums
- `/albums/`: List all albums (recent first)
- `/album/<id>/`: Detail view for specific album
- `/postar/`: Create album (login required)
- `/editar/<id>/`: Edit album (owner only)
- `/deletar/<id>/`: Delete album (owner only)
- `/profile/`: User profile with their albums
- Auth: `/login/`, `/logout/`, `/register/`

## Developer Workflows
- **Run server**: `python manage.py runserver`
- **Migrations**: `python manage.py makemigrations` then `python manage.py migrate`
- **Testing**: `pytest` (configured in `pytest.ini` with `DJANGO_SETTINGS_MODULE=trabalho.settings`)
- **Static files**: Served via Django in debug; collect with `python manage.py collectstatic` for production
- **Media files**: Served only in DEBUG mode via URL patterns in `trabalho/urls.py`

## Conventions & Patterns
- **View naming**: Portuguese verbs (e.g., `postar` for create, `editar` for edit, `deletar` for delete)
- **Template structure**: Base `mestre.html`, includes like `cabecalho.html`, `controle.html`
- **Forms**: ModelForms excluding user field (set in view); custom `CustomUserCreationForm` removing help text
- **Messages**: Use Django messages for success/error feedback (e.g., `messages.success(req, 'Album added successfully!')`)
- **Image uploads**: `upload_to` paths like `"albums/"`, `"avatars/"`
- **Profile creation**: Auto-create `UserProfile` on user registration in `register` view
- **Ordering**: Albums ordered by `-id` (most recent first) in `albums` view

## Dependencies
- Core: Django 5.2.8, Pillow 12.0.0 (for image handling)
- Testing: pytest with Django settings

## File Organization
- **Settings**: `trabalho/settings.py` - DEBUG=True, SQLite, media/static config
- **Models**: `MusicRank/models.py` - Album and UserProfile
- **Views**: `MusicRank/views.py` - CRUD operations with login_required decorators
- **Forms**: `MusicRank/forms.py` - AlbumForm, CustomUserCreationForm
- **Templates**: `MusicRank/templates/` - HTML files with Django template syntax
- **Static**: `MusicRank/static/estilo.css` - Custom CSS for styling
- **Tests**: `MusicRank/tests.py` - Basic model tests; run with pytest

## Common Patterns
- **Get or create profile**: `user_profile, created = models.UserProfile.objects.get_or_create(user=req.user)`
- **Owner checks**: Use `get_object_or_404(models.Album, id=album_id, user=req.user)` for permission
- **Form handling**: `if form.is_valid(): album = form.save(commit=False); album.user = req.user; album.save()`
- **Redirect after action**: Always redirect to 'inicio' after CRUD operations

## Notes
- No API endpoints; purely web-based with server-side rendering
- Images are optional; handle gracefully in templates (e.g., placeholder if no image)
- User avatars shown in nav with dropdown menu for profile/logout</content>
<parameter name="filePath">c:\Users\vinicius\Downloads\MusicRank\.github\copilot-instructions.md