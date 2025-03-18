import csv
from django.core.management.base import BaseCommand
from pokemon_app.models import Pokemon

class Command(BaseCommand):
    help = "Load Pokémon data from CSV into the database"

    def handle(self, *args, **kwargs):
        csv_file = "pokemon_data.csv"  # CSVのパスを適宜変更

        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # データを作成または更新
                    pokemon, created = Pokemon.objects.update_or_create(
                        id=row['id'],
                        defaults={
                            'name': row['name'],
                            'type': row['types'],  # CSVの列名に合わせる
                            'image_url': row['image_url']
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Added {pokemon.name}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"Updated {pokemon.name}"))
        
            self.stdout.write(self.style.SUCCESS("Successfully loaded Pokémon data!"))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR("File not found: Ensure 'pokemon_data.csv' exists"))

