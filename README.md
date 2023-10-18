[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/iHpKfUUO)

## Структура репозитория
1) Файл hw2+project.ipynb, в котором написаны комментарии к коду пошагово и показано, как получаются индексы (в программе они только загружаются)
2) Файл запуска консольной программы main.py
3) Файл страниц веб-приложения app.py
4) Модуль main_web.py, обрабатывающий запрос с сайта
5) Модули search.py и load_indeces.py, к которым обращаются файлы запуска
6) Вспомогательные модули preprocess_text.py и delete_OOVs.py, к которым обращается модуль search.py
7) Четыре индекса и корпус в виде .pickle файлов
8) Корпус я здесь не дублирую, он доступен по адресу: http://www.labinform.ru/pub/named_entities/collection5.zip

## Метрики
| Index type    | Average time, ms  | Memory, bytes |
|:-------------:|:----------------- |:------------- |
| BM-25         | 10.4              | 608164        |
| Word2Vec      | 22.7              | 2400128       |
| Navec         | 23.3              | 2400128       |
| BERT          | 327               | 8192128       |

## Использование
Для работы консольной программы необходимо иметь используемые ей модели Word2Vec и Navec, они доступны для скачивания по адресу http://vectors.nlpl.eu/repository/20/220.zip и https://storage.yandexcloud.net/natasha-navec/packs/navec_news_v1_1B_250K_300d_100q.tar соответственно. 
Пользователь располагает в пути модули main, preprocess_text, delete_OOVs, create_index и search. Затем ему достаточно обратиться к файлу main.py и ввести аргументы запроса через пробел, чтобы программа вывела список ранжированных по релевантности запросу документов и время выполнения запроса.

### Аргументы
query (str) - текст запроса

index_type (str) - нужный тип индекса: 'bm25', 'w2v', 'navec' или 'bert'

n (int) - количество документов, которое нужно отобразить, по умлочанию 2

### Пример
```
python main.py телефон bm25 2
```
