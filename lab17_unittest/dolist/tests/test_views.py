from django.test import TestCase
from django.urls import reverse
from .models import Todolist
from .forms import Todolistform
from .views import addTodoitem, completedTodo, deletecompleted, deleteAll

class TodoviewsTestCase(TestCase):
    def setUp(self):
        # create inital data for testing
        self.task1 = Todolist.object.create(text = "Task 1", completed = False)
        self.task2 = Todolist.object.create(text = "Task 2", completed = False)
        self.task3 = Todolist.object.create(text = "Task 3", completed = True)

    def test_index_view(self):
        # test the index view render the correct context and template
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')