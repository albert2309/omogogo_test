from django.test import TestCase
from .models import Bucketlist, Tag
# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)
    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': bucketlist.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class TagTestCase(TestCase):
    def setUp(self):
        self.tag_name = "Tag Test"
        self.tag = Tag(tag=self.tag_name)

    def test_model_can_create_a_tag(self):
        old_count = Tag.objects.count()
        self.tag.save()
        new_count = Tag.objects.count()
        self.assertNotEqual(old_count, new_count)


from django.urls import reverse
class ViewTagTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.tag_data = {'tag': 'Go to Ibiza'}

        self.response = self.client.post(
            reverse('create'),
            {'tag': 'alb'})

    def test_api_can_create_a_tag(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_tag(self):
        taglist = Tag.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': taglist.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, taglist)
#
    def test_api_can_update_tag(self):
        """Test the api can delete a bucketlist."""
        taglist = Tag.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': taglist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)