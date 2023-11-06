---------------
#####  1  #####
---------------
Doctest для morse_encode.py находится в самом файле morse_encode.py. Поэтому применяем команду doctest к нему, находясь в том же каталоге

```
python -m doctest -o NORMALIZE_WHITESPACE -v morse_encode.py
```

---------------
#####  2  #####
---------------
В случае если не установлена библиотека pytest, то нужно ее установить через команду
```
pip install -U pytest
```
Тестируемая функция находится в файле morse_decode.py. Тесты же в файле Test_morse_decode.py. Его и запускаем (запускаем pytest)
```
python -m pytest -v Test_morse_decode.py 
```

---------------
#####  3  #####
---------------
Тестируемая функция находится в файле one_hot_encoder.py. Тесты же в файле Test_one_hot_encoder.py. Его и запускаем (запускаем unittest)
```
python -m unittest -v Test_one_hot_encoder.py
```

---------------
#####  4  #####
---------------
В случае если не установлена библиотека pytest, то нужно ее установить через команду
```
pip install -U pytest
```

Тестируемая функция находится в файле one_hot_encoder.py. Тесты же в файле Test_one_hot_encoder_pytest.py. Его и запускаем (запускаем pytest)
```
python -m pytest -v Test_morse_decode.py 
```

---------------
#####  5  #####
---------------
В случае если не установлена библиотека pytest, то нужно ее установить через команду
```
pip install -U pytest
```
Тестируемая функция находится в файле what_is_year_now.py. Тесты же в файле Mock_test_year.py. Его и запускаем (запускаем pytest с флагом для проверки coverage --cov=what_is_year_now)
```
python -m pytest -q Mock_test_year.py --cov=what_is_year_now 
```
И для создания html файла, который показывает coverage тестами исходного файла what_is_year_now.py нужно добавить еще один флаг --cov-report html
```
python -m pytest -q Mock_test_year.py --cov=what_is_year_now --cov-report html
```
