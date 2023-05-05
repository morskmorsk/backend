from django.test import TestCase
from accounts.models import CustomUser
import pytest

pytestmark = pytest.mark.django_db


class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass123')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertIsNone(self.user.phone_number)
        self.assertIsNone(self.user.address)
        self.assertIsNone(self.user.service_provider)
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')
        self.assertIsNone(self.user.last_login)
        # self.assertIsNone(self.user.date_joined)
        self.assertEqual(self.user.groups.all().count(), 0)
        self.assertEqual(self.user.user_permissions.all().count(), 0)
        self.assertEqual(self.user.get_username(), 'testuser')
        self.assertEqual(self.user.get_full_name(), '')
        self.assertEqual(self.user.get_short_name(), '')
        self.assertEqual(self.user.get_group_permissions(), set())
        self.assertEqual(self.user.get_all_permissions(), set())
        self.assertFalse(self.user.has_perm(''))
        self.assertTrue(self.user.has_perms([]))
        self.assertFalse(self.user.has_module_perms(''))
        self.assertFalse(self.user.is_anonymous)
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(self.user.get_user_permissions(), set())

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')
