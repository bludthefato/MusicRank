from django.test import TestCase
from django.contrib.auth.models import User
from .models import Album

class AlbumTestCase(TestCase):
    def test_album_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        album = Album.objects.create(title='Test Album', artist='Test Artist', review='Great album!', user=user)
        self.assertEqual(album.title, 'Test Album')
        self.assertEqual(album.artist, 'Test Artist')
        self.assertEqual(album.review, 'Great album!')
        self.assertEqual(album.user, user)
