from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Удаляет все данные и загружает тестовые категории и продукты'

    def handle(self, *args, **options):
        self.stdout.write('Удаляем все продукты...')
        Product.objects.all().delete()

        self.stdout.write('Удаляем все категории...')
        Category.objects.all().delete()

        self.stdout.write('Создаём категории...')
        categories = [
            {'name': 'Электроника', 'description': 'Техника и гаджеты'},
            {'name': 'Одежда', 'description': 'Модная одежда'},
            {'name': 'Книги', 'description': 'Различные книги'},
            {'name': 'Дом и интерьер', 'description': 'Товары для дома и декор'},
            {'name': 'Спорт', 'description': 'Спортивные товары и экипировка'},
        ]

        category_objs = []
        for cat in categories:
            category_obj = Category.objects.create(**cat)
            category_objs.append(category_obj)
            self.stdout.write(f'Создана категория: {category_obj.name}')

        # Получаем пользователя для владельца продуктов
        owner = User.objects.first()
        if not owner:
            self.stdout.write(self.style.ERROR('Нет пользователей для задания владельца продукта. Пожалуйста, создайте пользователя.'))
            return

        self.stdout.write('Создаём продукты...')
        products = [
            {'name': 'Смартфон', 'description': 'Современный смартфон с большим экраном', 'category': category_objs[0], 'price': 29999.99},
            {'name': 'Ноутбук', 'description': 'Мощный ноутбук для работы и игр', 'category': category_objs[0], 'price': 79999.00},
            {'name': 'Футболка', 'description': 'Хлопковая футболка с принтом', 'category': category_objs[1], 'price': 799.50},
            {'name': 'Джинсы', 'description': 'Удобные джинсы классического кроя', 'category': category_objs[1], 'price': 2499.00},
            {'name': 'Роман', 'description': 'Увлекательный художественный роман', 'category': category_objs[2], 'price': 450.00},
            {'name': 'Кулинарная книга', 'description': 'Рецепты для домашней кухни', 'category': category_objs[2], 'price': 600.00},
            {'name': 'Диванная подушка', 'description': 'Мягкая декоративная подушка для дивана', 'category': category_objs[3], 'price': 1200.00},
            {'name': 'Футбольный мяч', 'description': 'Качественный мяч для игры на улице', 'category': category_objs[4], 'price': 1500.00},
        ]

        for prod_data in products:
            product_obj = Product.objects.create(
                owner=owner,
                status='draft',  # статус по умолчанию
                **prod_data
            )
            self.stdout.write(f'Создан продукт: {product_obj.name} (Категория: {product_obj.category.name}, Владелец: {product_obj.owner.email})')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))
