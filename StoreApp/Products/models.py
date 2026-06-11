from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Наименование категории", max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="Описание категории", blank=True)
    image = models.ImageField(verbose_name="Изображение категории", upload_to="categories/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория товара")
    name = models.CharField(verbose_name="Наименование товара", max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="Описание товара", blank=True)
    price = models.DecimalField(verbose_name="Цена товара", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name="Товара в наличии", default=0)
    image = models.ImageField(verbose_name="Изображение товара", upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    