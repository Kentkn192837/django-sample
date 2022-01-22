### build
How to build?

```
$ docker-compose up -d
```

プロジェクト作成コマンド
```
$ docker-compose run web django-admin.py startproject app .
```

アプリケーション新規作成コマンド
```
$ python manage.py startapp <作りたいアプリ名>
```

コンテナ内に入るコマンド
```
$ docker exec -it django-sample_web_1 /bin/sh
```
