from django.conf import settings
from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator

from users.models import User


class Ingredient(models.Model):

    name = models.CharField(
        max_length=settings.LENGTH_NAME_ING,
        verbose_name='Название ингредиента'
    )
    measurement_unit = models.CharField(
        max_length=settings.LENGTH_UNIT,
        verbose_name='Единица измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):

    name = models.CharField(
        max_length=settings.LENGTH_NAME_TAG,
        verbose_name='Название тега',
        unique=True
    )
    color = models.CharField(
        max_length=settings.LENGTH_COLOR,
        verbose_name='Цвет в НЕХ',
    )
    slug = models.SlugField(
        max_length=settings.LENGTH_SLUG_TAG,
        verbose_name='Уникальный слаг',
        validators=[validators.RegexValidator(regex=r'^[-a-zA-Z0-9_]+$')],
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):

    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег рецепта',
        related_name='recipes'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipe'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Список ингредиентов',
        through='IngredientsInRecipe',
    )
    name = models.CharField(
        max_length=settings.LENGTH_NAME_RECIPE,
        verbose_name='Название рецепта'
    )
    image = models.ImageField(
        upload_to=settings.IMAGE_DIR,
        verbose_name='Фото'
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    cooking_time = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления в минутах'
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации рецепта'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-publication_date',)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='recipe_shopping_cart'
    )

    class Meta:
        verbose_name = 'Список покупок'

    def __str__(self):
        return f'{self.user.username}, {self.recipe.name}'


class IngredientsInRecipe(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='recipe'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
        related_name='ingredient'
    )
    amount = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return f'{self.ingredient} в {self.recipe} в кол-ве {self.amount}'


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite'
    )
    favorite_recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Избранный рецепт',
        related_name='favorite_recipe'
    )

    class Meta:
        verbose_name = 'Избранный рецепт'

    def __str__(self):
        return f'{self.user} {self.favorite_recipe}'


class Subscribe(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор рецепта',
        on_delete=models.CASCADE,
        related_name='following'
    )
    follow_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подписки на автора'
    )

    class Meta:
        verbose_name = 'Подписка на автора'
        verbose_name_plural = 'Подписка на авторов'

    def __str__(self):
        return f'{self.user.username , self.author.username}'
