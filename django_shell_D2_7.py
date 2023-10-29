from news.models import *

# 1. Создать двух пользователей (с помощью метода User.objects.create_user).
user1 = User.objects.create(username='Vasya_1', first_name='Вася')
user2 = User.objects.create(username='Petya_2', first_name='Петя')

# 2. Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(authorUser=user1)
author2 = Author.objects.create(authorUser=user2)

# 3. Добавить 4 категории в модель Category.
cat1 = Category.objects.create(name='Python')
cat2 = Category.objects.create(name='JS')
cat3 = Category.objects.create(name='Django')
cat4 = Category.objects.create(name='Docker')

# 4. Добавить 2 статьи и 1 новость.
post1_art = Post.objects.create(author=author1, categoryType=Post.ARTICLE, title="Article_1", text="Первая статья - текст")
post2_art = Post.objects.create(author=author2, categoryType=Post.ARTICLE, title="Article_2", text="Вторая статья - текст")
post3_news = Post.objects.create(author=author2, categoryType=Post.NEWS, title="News_3", text="Первая новость - текст")

# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

post1_art.postCategory.add(cat2)
post2_art.postCategory.add(cat3, cat4)
post3_news.postCategory.add(cat1, cat3, cat4)

# 6. Создать как минимум 4 комментария к разным объектам модели Post
# (в каждом объекте должен быть как минимум один комментарий).

comm1 = Comment.objects.create(commentPost=post1_art, commentUser=user1, text=f"Комментарий на '{post1_art.title}' от {user1.username}")
comm2 = Comment.objects.create(commentPost=post2_art, commentUser=user1, text=f"Комментарий на '{post2_art.title}' от {user1.username}")
comm3 = Comment.objects.create(commentPost=post3_news, commentUser=user1, text=f"Комментарий на '{post3_news.title}' от {user1.username}")
comm4 = Comment.objects.create(commentPost=post3_news, commentUser=user2, text=f"Комментарий на '{post3_news.title}' от {user2.username}")


# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям,
# скорректировать рейтинги этих объектов.

post1_art.like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).dislike()

Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=3).dislike()

comm1.like()
comm2.like()
comm3.like()
comm4.like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=3).like()

# 8. Обновить рейтинги пользователей.

author1.update_rating()
Author.objects.get(authorUser=User.objects.get(username="Petya_2")).update_rating()

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

best_author = Author.objects.all().order_by('-ratingAuthor').first()
print(f"Лучший автор: {best_author.authorUser.username}, рейтинг: {best_author.ratingAuthor}")

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
# основываясь на лайках/дислайках к этой статье.

best_post = Post.objects.all().order_by('-rating').first()
print(f"Лучшая статья:\n Дата: {best_post.dateCreation.strftime('%d-%m-%Y %H:%M:%S')}\n Автор: {best_post.author.authorUser.username}\n"
      f" Рейтинг: {best_post.rating}\n Заголовок: {best_post.title}\n Превью: {best_post.preview()}")

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

best_post_comments = Comment.objects.filter(commentPost=best_post)
best_post_comments.values('dateCreation', 'commentUser__username', 'rating', 'text')
