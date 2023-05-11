from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api import models
from task.serializers import TaskDetailsSerializer, TaskSerializer

TASK_URL = reverse('task:task-list')


#help func for testing
def task_url(task_id):
    return reverse('task:task-detail', args=[task_id])

def create_task(**args):
    details = {
        'name': 'test',
        'description': 'test',
    }
    details.update(args)
    task = models.Task.objects.create(**args)
    return task


class TaskModelApiTests(TestCase):
    def test_creating_task(self):
        details = {
            'name': 'test',
            'description': 'test',
        }
        result = self.client.post(TASK_URL, details)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_retriving_task_list(self):
        create_task()

        result = self.client.get(TASK_URL)
        tasks = models.Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)

    def test_retriving_task_details(self):
        task = create_task()
        url = task_url(task.id)
        result = self.client.get(url)
        serializer = TaskDetailsSerializer(task)
        self.assertEqual(result.data, serializer.data)