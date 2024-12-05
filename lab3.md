# Лабораторная работа №3 - Метрики программного кода 
## Выбранные метрики
* Цикломатическая сложность (CC)
* Индекс поддерживаемости (MI)
* Метрики HAL 
* Соответствие кода стандартам языка (PEP 8)
* Обобщённая оценка кода (pep 8, refactor, warning, error, fatal)

## Цикломатическая сложность (CC)
```commandline
radon cc . -e "venv/*,hmtl/*,latex/*"
```
Результат до оптимизации:
```commandline
services/dataset.py
    M 30:4 DefaultDataset.__getitem__ - C
    C 14:0 DefaultDataset - B
    C 5:0 Dataset - A
    M 10:4 Dataset.__getitem__ - A
    M 20:4 DefaultDataset.__init__ - A
services/runner.py
    M 29:4 Runner.start - C
    C 5:0 Runner - B
    M 10:4 Runner.__init__ - A
    M 16:4 Runner.run - A
services/qa_model.py
    M 36:4 DefaultQAModel.predict - B
    C 21:0 DefaultQAModel - A
    C 8:0 BaseQAModel - A
    M 12:4 BaseQAModel.__init__ - A
    M 18:4 BaseQAModel.predict - A
    M 28:4 DefaultQAModel.__init__ - A
core/schemas/question.py
    C 5:0 AskReq - A
    C 10:0 AskRes - A
api/router.py
    F 9:0 ask - A
```
Результат после оптимизации:
```commandline
services/dataset.py
    C 5:0 Dataset - A
    C 14:0 DefaultDataset - A
    M 10:4 Dataset.__getitem__ - A
    M 20:4 DefaultDataset.__init__ - A
    M 30:4 DefaultDataset.__getitem__ - A
services/runner.py
    M 29:4 Runner.start - A
    C 5:0 Runner - A
    M 10:4 Runner.__init__ - A
    M 16:4 Runner.run - A
services/qa_model.py
    M 36:4 DefaultQAModel.predict - A
    C 21:0 DefaultQAModel - A
    C 8:0 BaseQAModel - A
    M 12:4 BaseQAModel.__init__ - A
    M 18:4 BaseQAModel.predict - A
    M 28:4 DefaultQAModel.__init__ - A
core/schemas/question.py
    C 4:0 AskReq - A
    C 9:0 AskRes - A
api/router.py
    F 9:0 ask - A
```

## Индекс поддерживаемости (MI)
```commandline
radon mi . -e "venv/*,hmtl/*,latex/*"
```
Результат до оптимизации:
```commandline
main.py - A
services/dataset.py - A
services/runner.py - A
services/qa_model.py - A
services/__init__.py - A
core/__init__.py - A
core/schemas/question.py - A
core/schemas/__init__.py - A
api/router.py - A
api/__init__.py - A
```
Оптимизация не требуется

## HAL 
```commandline
radon hal . -e "venv/*,hmtl/*,latex/*"
```
Результат до оптимизации:
```commandline
main.py:
    h1: 5
    h2: 22
    N1: 14
    N2: 28
    vocabulary: 27
    length: 42
    calculated_length: 109.71713608445735
    volume: 199.7052750908657
    difficulty: 3.1818181818181817
    effort: 635.4258752891182
    time: 35.30143751606212
    bugs: 0.06656842503028856
services/dataset.py:
    h1: 0
    h2: 0
    N1: 0
    N2: 0
    vocabulary: 0
    length: 0
    calculated_length: 0
    volume: 0
    difficulty: 0
    effort: 0
    time: 0.0
    bugs: 0.0
services/runner.py:
    h1: 7
    h2: 23
    N1: 16
    N2: 30
    vocabulary: 30
    length: 46
    calculated_length: 123.69340944371453
    volume: 225.71696739799185
    difficulty: 4.565217391304348
    effort: 1030.4470250777888
    time: 57.247056948766044
    bugs: 0.07523898913266396
services/qa_model.py:
    h1: 5
    h2: 31
    N1: 26
    N2: 52
    vocabulary: 36
    length: 78
    calculated_length: 165.18972609642998
    volume: 403.2541501125003
    difficulty: 4.193548387096774
    effort: 1691.0657907943562
    time: 93.94809948857534
    bugs: 0.1344180500375001
```
Результат после оптимизации:
```commandline
main.py:
    h1: 1
    h2: 2
    N1: 1
    N2: 2
    vocabulary: 3
    length: 3
    calculated_length: 2.0
    volume: 4.754887502163469
    difficulty: 0.5
    effort: 2.3774437510817346
    time: 0.1320802083934297
    bugs: 0.0015849625007211565
services/runner.py:
    h1: 2
    h2: 3
    N1: 3
    N2: 4
    vocabulary: 5
    length: 7
    calculated_length: 6.754887502163469
    volume: 16.253496664211536
    difficulty: 1.3333333333333333
    effort: 21.67132888561538
    time: 1.2039627158675212
    bugs: 0.005417832221403845
services/qa_model.py:
    h1: 5
    h2: 20
    N1: 13
    N2: 26
    vocabulary: 25
    length: 39
    calculated_length: 98.04820237218406
    volume: 181.11039140121426
    difficulty: 3.25
    effort: 588.6087720539464
    time: 32.700487336330355
    bugs: 0.06037013046707142
```

## Соответствие кода стандартам языка (PEP 8)
```commandline
isort . --check
```
Результат до оптимизации:
```commandline
ERROR: /home/naivash/projects-study/hse-sdt-lab/services/dataset.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/naivash/projects-study/hse-sdt-lab/services/qa_model.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/naivash/projects-study/hse-sdt-lab/core/schemas/question.py Imports are incorrectly sorted and/or formatted.
ERROR: /home/naivash/projects-study/hse-sdt-lab/api/router.py Imports are incorrectly sorted and/or formatted.
```
Результат после оптимизации - отсутствие предупреждений

## Обобщённая оценка кода  
```commandline
pylint . --ignore=venv,html,latex
```
Результат до оптимизации:
```commandline
************* Module main
main.py:19:0: C0304: Final newline missing (missing-final-newline)
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:5:0: W0611: Unused Runner imported from services.runner (unused-import)
************* Module services.dataset
services/dataset.py:1:0: C0114: Missing module docstring (missing-module-docstring)
services/dataset.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)
services/dataset.py:45:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
services/dataset.py:45:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
services/dataset.py:14:0: R0903: Too few public methods (1/2) (too-few-public-methods)
services/dataset.py:2:0: W0611: Unused Any imported from typing (unused-import)
************* Module services.runner
services/runner.py:67:0: C0301: Line too long (101/100) (line-too-long)
services/runner.py:1:0: C0114: Missing module docstring (missing-module-docstring)
services/runner.py:37:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
services/runner.py:37:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
services/runner.py:29:4: R0912: Too many branches (15/12) (too-many-branches)
************* Module services.qa_model
services/qa_model.py:33:0: C0301: Line too long (118/100) (line-too-long)
services/qa_model.py:34:0: C0301: Line too long (111/100) (line-too-long)
services/qa_model.py:99:0: C0304: Final newline missing (missing-final-newline)
services/qa_model.py:1:0: C0114: Missing module docstring (missing-module-docstring)
services/qa_model.py:15:8: W0107: Unnecessary pass statement (unnecessary-pass)
services/qa_model.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
services/qa_model.py:8:0: R0903: Too few public methods (1/2) (too-few-public-methods)
services/qa_model.py:21:0: R0903: Too few public methods (1/2) (too-few-public-methods)
services/qa_model.py:3:0: C0411: standard import "typing.Tuple" should be placed before third party import "transformers.BertForQuestionAnswering" (wrong-import-order)
services/qa_model.py:3:0: W0611: Unused Tuple imported from typing (unused-import)
************* Module core.schemas.question
core/schemas/question.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/schemas/question.py:5:0: C0115: Missing class docstring (missing-class-docstring)
core/schemas/question.py:10:0: C0115: Missing class docstring (missing-class-docstring)
core/schemas/question.py:2:0: W0611: Unused ConfigDict imported from pydantic (unused-import)
************* Module api.router
api/router.py:12:0: C0304: Final newline missing (missing-final-newline)
api/router.py:1:0: C0114: Missing module docstring (missing-module-docstring)
api/router.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
-----------------------------------
Your code has been rated at 7.12/10
```
Результат после оптимизации 
```commandline
...
------------------------------------------------------------------
Your code has been rated at 8.33/10 
```

## Выводы
* Цикломатическая сложность кода показала, что в некоторых местах сложность соответствует уровню С - то есть
(moderate - slightly complex block) сложность, что не критично, но требовало улучшений. Были оптимизированы некоторые
циклы, чем улучшилась сложность кода 
* Индекс поддерживаемости изначально был на высшем уровне А, потому что код проекта написан согласно слоистой
архитектуре
* HAL метрики дают много информации о коде, замечено, что после улучшения параметры difficulty, time, bugs
резко снизились (где-то на порядок и выше), что говорит об улучшении качества кода 
* Соответствие кода стандартам языка - было обнаружено, что в некоторых местах импорты не соответствуют стандартам,
что было исправлено
* Обобщённая оценка кода - показала множество проблем, связанных с кодом. После улучшений общая оценка улучшилась
с 7.12 до 8.33