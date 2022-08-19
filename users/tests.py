from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        superuser = db.objects.create_superuser('test@gmail.com', 'test-username', 'test-password')

        self.assertEqual(superuser.email, 'test@gmail.com')
        self.assertEqual(superuser.username, 'test-username')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertEqual(str(superuser), 'test-username')

        # with self.assertRaises(ValueError):
        #     db.objects.create_superuser(email='test@gmail.com', username='test-username', password='test-password', is_superuser=False)

        # with self.assertRaises(ValueError):
        #     db.objects.create_superuser(email='test@gmail.com', username='test-username', password='test-password', is_staff=False)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('test@gmail.com', 'test-username', 'test-password')

        self.assertEqual(user.email, 'test@gmail.com')
        self.assertEqual(user.username, 'test-username')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        # with self.assertRaises(ValueError):
        #     db.objects.create_user(email='', username='test-username', password='test-password')
