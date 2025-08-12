from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" с необходимыми правами'

    def handle(self, *args, **options):
        group_name = 'Модератор продуктов'
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(f'Группа "{group_name}" создана')
        else:
            self.stdout.write(f'Группа "{group_name}" уже существует')

        content_type = ContentType.objects.get_for_model(Product)

        can_unpublish_perm, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            defaults={
                'name': 'Может отменять публикацию продукта',
                'content_type': content_type,
            }
        )
        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=content_type
        )

        group.permissions.add(can_unpublish_perm, delete_perm)
        group.save()

        self.stdout.write('Права can_unpublish_product и delete_product назначены группе.')
        self.stdout.write(f'Группа "{group_name}" настроена.')
