"""Создание пользовательских методов

Также мы можем создавать пользовательские методы и свойства для моделей,
чтобы расширить их функциональность. Например, мы можем создать метод
"get_summary" для модели "Post", который будет возвращать краткое
описание поста.

Внесём изменения в класс Post в файле models.py:

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
    return f'Title is {self.title}'
    def get_summary(self):
    words = self.content.split()
    return f'{" ".join(words[:12])}...'


Здесь мы создаем метод "get_summary", который возвращает первые 12 слов
контента поста и добавляет многоточие в конце.

...
text = '\n'.join(post.get_summary() for post in posts)
...

Вместо полного текста теперь можем получать первые несколько слов.
Django не ограничивает разработчика не методы внутри моделей. Подобный
подход, когда данные и расчёты производятся в моделях более
предпочтителен, чем расчёты внутри представлений по выгруженным из
модели данным. Тем более не стоит переносить расчёты в представления, о
которых мы будем подробно говорить на следующей лекции."""