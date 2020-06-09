# exam_decorator

### Overview
Реализация парметрического декоратора-логгера с использованием `unittest.mock` + `pytest` + `pytest.mark.parametrize`

Настройка окружения
```shell script
python3.7 -m venv ~/Projects/envs/exam_decorator
pip install --upgrade pip
source ~/Projects/envs/exam_decorator/bin/activate
```

Устанавливаем зависимости
```shell script
pip install -r requirements/dev.txt
```

Запуск тестов
```shell script
python -m pytest exam_decorator.py
```

Результаты логирования записаны в файл function_logger.log
