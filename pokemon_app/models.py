from django.db import models

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name_jp = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)

    class Meta:
        db_table = "pokemon"  # ✅ ここで手動作成したテーブル名と一致させる

    def __str__(self):
        return self.name_jp

