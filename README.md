# Сервис для конвертации температур 


## Пример Использования:

1.  F -> C and F -> K:

	`Введите число градусы Фаренгейта:`  
	`120 F`  
	`Conversion result: 120.0°F = 48.89°C`
	`Conversion result: 120.0°F = 322.04°K`  

2. K -> C and K -> F:

	`Введите число градусы Кельвина:`  
	`2 K`  
    `Conversion result: 2.0°K = -271.15°C`
    `Conversion result: 2.0°K = -456.07°F`

3. C -> F and C -> K:

	`Введите число градусы Цельсия:`  
	`12 C`  
	`Conversion result: 12.0°C = 53.6°F`
    `Conversion result: 12.0°C = 285.15°K`  

## Docker:

1. `docker build -t dc .`
2. `docker run dc`


## Test: 
dev:

[![.github/workflows/main.yaml](https://github.com/Search2know/Converter/actions/workflows/main.yaml/badge.svg?branch=dev)](https://github.com/Search2know/Converter/actions/workflows/main.yaml)

main:

[![.github/workflows/main.yaml](https://github.com/Search2know/Converter/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/Search2know/Converter/actions/workflows/main.yaml)