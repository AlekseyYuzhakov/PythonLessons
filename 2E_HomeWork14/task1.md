Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи. Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение NegativeValueError.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2). Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError с текстом Ширина должна быть положительной, а не {value}

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4. При необходимости выбрасывать исклчение NegativeValueError с текстом Высота должна быть положительной, а не {value}

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter() возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).

Запускать тесты не надо, автотест это сделает сам:

