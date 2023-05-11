from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from api import models
from work.serializers import WorkDetailsSerializer
from django.contrib.auth import get_user_model

WORK_URL = reverse('work:work-list')


#help func for testing
def work_url(work_id):
    return reverse('work:work-detail', args=[work_id])

def create_task(**args):
    details = {
        'name': 'test',
        'description': 'test',
    }
    details.update(args)
    task = models.Task.objects.create(**args)
    return task

def create_work(**args):
    test_task = create_task()
    work = models.Work.objects.create(name='test')
    work.tasks.add(test_task)
    return work

class WorkModelApiTests(TestCase):
    def test_creating_work(self):
        task1 = create_task()
        work = models.Work.objects.create(name='test work')
        work.tasks.add(task1)
        saved_work = models.Work.objects.get(pk=work.pk)
        self.assertEqual(saved_work.tasks.count(), 1)

    def test_retriving_work_list(self):
        work = create_work()
        url = work_url(work.id)
        client = APIClient()
        user = get_user_model().objects.create_user(
            email='test@example.com', password='testpassword123', is_staff=True, user_type='admin'
        )
        client.force_authenticate(user=user)

        result = client.get(url)
        serializer = WorkDetailsSerializer(work)
        self.assertEqual(result.data, serializer.data)