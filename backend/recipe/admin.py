from django.contrib import admin

from .models import (FavoriteRecipe, Ingredient, IngredientsInRecipe, Recipe,
                     ShoppingCart, Subscribe, Tag)


class IngredientsInRecipeInline(admin.TabularInline):
    model = IngredientsInRecipe
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'author',
        'count_favorite',
        'publication_date'
    )
    search_fields = (
        'author',
        'name',
        'tags',
        'publication_date'
    )
    list_filter = (
        'author',
        'name',
        'tags'
    )

    inlines = (IngredientsInRecipeInline, )

    def count_favorite(self, obj):
        return FavoriteRecipe.objects.filter(recipe=obj).count()

    count_favorite.short_description = 'В избранном'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'color',
        'slug',
    )
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'recipe',
    )
    search_fields = (
        'user',
        'recipe'
    )
    list_filter = (
        'user',
        'recipe'
    )


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'favorite_recipe',
    )
    search_fields = ('user',)
    list_filter = ('user',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'user',
        'follow_date'
    )
    search_fields = (
        'author',
        'follow_date')
    list_filter = (
        'author',
        'user',
        'follow_date')
