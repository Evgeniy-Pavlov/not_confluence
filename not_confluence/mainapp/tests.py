from django.test import TestCase
from .models import User, Project, Article
from .views import ArticleListView, ProjectListView
import datetime
from http import HTTPStatus
from bs4 import BeautifulSoup
from django.test import TestCase
from .models import User, Project, Article



# Create your tests here.

class TestUser(TestCase):
    def setUp(self) -> None:
        self.user_1 = User.objects.create(login='semenovse',
                        last_name='Семенов', first_name='Семен', patronymic='Евгеньевич')
        self.user_2 = User.objects.create(login='petrovvv',
                        last_name='Петров', first_name='Виктор', patronymic='Викторович')


    def test_create_user(self):
        self.assertEqual(self.user_1.login, 'semenovse')
        self.assertEqual(self.user_1.last_name, 'Семенов')
        self.assertEqual(self.user_1.first_name, 'Семен')
        self.assertEqual(self.user_1.patronymic, 'Евгеньевич')


    def test_update_user(self):
        result_update = User.objects.filter(login='petrovvv').update(first_name='Виталий',
                            last_name='Петренко', patronymic='Витальевич', login='petrenkovv')
        self.assertEqual(result_update, 1)
        user_update = User.objects.get(login='petrenkovv')
        self.assertEqual(user_update.first_name, 'Виталий')
        self.assertEqual(user_update.last_name, 'Петренко')
        self.assertEqual(user_update.patronymic, 'Витальевич')


class TestProject(TestCase):
    def setUp(self) -> None:
        self.user_1 = User.objects.create(login='test_user',
                        last_name='Тестовый', first_name='Тест', patronymic='Тестович')
        self.user_2 = User.objects.create(login='test_user_2',
                        last_name='Тестовый', first_name='Тест', patronymic='Тестович')
        self.project_1 = Project.objects.create(name='TestProject_1', user_create=self.user_2)
    

    def test_create_project(self):
        project = Project.objects.create(name='TestProject', user_create=self.user_1)
        self.assertEqual(project.name, 'TestProject')


    def test_update_project(self):
        result_update = Project.objects.filter(name='TestProject_1').update(name='TestProjectUp')
        self.assertEqual(result_update, 1)
        project_update = Project.objects.get(user_create=self.user_2)
        self.assertEqual(project_update.name, 'TestProjectUp')


class TestArticle(TestCase):
    def setUp(self) -> None:
        self.user_1 = User.objects.create(login='author_1',
                        last_name='Автор', first_name='Первый', patronymic='Тестович')
        self.user_2 = User.objects.create(login='author_2',
                        last_name='Автор', first_name='Второй', patronymic='Тестович')
        self.project_1 = Project.objects.create(name='ProjectArticle_1', user_create=self.user_1)
        self.project_2 = Project.objects.create(name='ProjectArticle_2', user_create=self.user_2)
        self.article_1 = Article.objects.create(title='Testing title',
                            body='Test body article', author=self.user_2, project=self.project_2)


    def test_create_article(self):
        article = Article.objects.create(title='Testing title test test_create_article',\
                    body='Test body test_create_article',
                    author=self.user_1, project=self.project_1)
        self.assertEqual(article.title, 'Testing title test test_create_article')
        self.assertEqual(article.body, 'Test body test_create_article')
        self.assertEqual(article.author, self.user_1)
        self.assertEqual(article.project, self.project_1)


    def test_update_article(self):
        result_update = Article.objects.filter(author=self.user_2,
                        project=self.project_2, title='Testing title').update(title='Update title',
                        body='Update body', user_update=self.user_1,
                        date_update=datetime.datetime.now())
        self.assertEqual(result_update, 1)
        article_update = Article.objects.get(body='Update body')
        self.assertEqual(article_update.title, 'Update title')
        self.assertEqual(article_update.body, 'Update body')
        self.assertEqual(article_update.author, self.user_2)
        self.assertEqual(article_update.project, self.project_2)
        self.assertEqual(article_update.user_update, self.user_1)


class TestProjectView(TestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(login='user_project_1',
                        last_name='Куликов', first_name='Петр', patronymic='Петрович')
        self.project_1 = Project.objects.create(name='Project_view', user_create=self.user_1)


    def test_status_code_projectview(self):
        response= self.client.get('/project-list/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


    def test_card_projectlist(self):
        response= self.client.get('/project-list/')
        self.assertTrue(response.context['project_list'].first().id, self.project_1.id)


    def test_card_project_attribute(self):
        response= self.client.get('/project-list/')
        cards_project = BeautifulSoup(response.content, 'lxml')
        data = cards_project.find_all('div', class_='card-body')
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].find('h5', class_='card-title').text, self.project_1.name)
        self.assertEqual(data[0].find('a', id='form-detail').get('href'), '/project-detail/1/')
        delete_link = data[0].find('a', id='delete-form')
        self.assertEqual(delete_link.get('href'), '/project-delete/1/')
        user_create_info = data[0].find('p', class_='card-text', id='user-create')
        self.assertTrue(self.user_1.login in user_create_info.text)
