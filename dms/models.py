from django.db import models


class Tree(models.Model):
    parend_id = models.IntegerField(verbose_name="親ID")
    name = models.CharField(verbose_name="名称", max_length=255)
    owner_id = models.IntegerField(verbose_name="所有者ID")
    history = models.TextField(verbose_name="作業履歴")
    is_directory = models.BooleanField(verbose_name="ディレクトリフラグ")

    # Only when is_directory is 1
    child_ids = models.CharField(verbose_name="カンマ区切りの子要素ID", blank=True)

    # Only when is_directory is 0
    mimetype = models.CharField(verbose_name="ファイルのMIMEタイプ", max_length=255)
    is_checkout = models.BooleanField(verbose_name="チェックアウトフラグ")
    version = models.FloatField(verbose_name="バージョン情報")
