import csv
from django.core.management.base import BaseCommand
from pokemon_app.models import Pokemon

class Command(BaseCommand):
    help = 'インポートするポケモンデータをCSVから読み込んでデータベースに挿入します'

    def handle(self, *args, **kwargs):
        with open('C:/Users/ryota/pokemon_project_v2/pokemon_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # CSVの内容を使用してポケモンをデータベースに挿入
                Pokemon.objects.create(
                    id=row['id'],
                    name=row['name'],
                    type=row['type']
                )
                self.stdout.write(self.style.SUCCESS(f"ポケモン {row['name']} をデータベースに追加しました。"))
