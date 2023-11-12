


## <div align="center">Стэк технологий📑</div>
<div align="center">
  <a href="https://www.python.org/doc/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
  <a href="https://pytorch.org/docs/stable/index.html"><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"></a>
  <a href="https://opencv.github.io/cvat/docs/"><img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/django-%23white.svg?style=for-the-badge&logo=django&logoColor=white"></a>
  <br>
  <a href="https://github.com/ultralytics/ultralytics/actions/workflows/ci.yaml"><img src="https://github.com/ultralytics/ultralytics/actions/workflows/ci.yaml/badge.svg"></a>
</div>

## <div align="center">О нашем решении📝</div>
<p>Мы представляем модель для автоматического детектирования различных категорий мусора на ленте мусороперерабатывающего завода, запечатленных на 11-канальном видео. Данное приложение является решением для автоматизации процесса сортировки мусора по категориям для дальнейшего перепроизводства переработанного мусора.
</p>


## <div align="center">Быстрый старт🎢</div>
<details open>
  
#### Установка зависимостей
<p>
Для работы необходим заранее установленный python 3.10+
</p>

<p>
Для запуска проекта необходимо установить зависимости. Необходимые для работы проекта библиотеки можно посмотреть в файле <a href="https://github.com/st43r/GarbageCounter/blob/main/requirements.txt">requirements.txt</a> и установить их вручную. Также можно воспользоваться командой:
</p>
  
```bash
$ pip install -r requirements.txt
```

</details>

## <div align="center">Концепт работы программы</div>
<p>
  Видеопоток с камер передается на обученную нейронную сеть, которая маркирует изображение мусора определенной категорией и передает на web-интерфейс оператора, позволяя как в режиме реально времени видеть расположение определенной категории на ленте, так и в формате csv для дальнейшего анализа

Уникальность нашего решения в том, что использовалась генерация стрима конвейера для лучшего обучения и переразметили мусор, поскольку некоторая разметка была некорректна
</p>


