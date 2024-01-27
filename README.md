# CAT-SQUEEZER
Squizing an image of a cat according to integral curve of system of ODE, using function "solve_ivp"

Итак, мы сделали это, господа, мы сжали бедного кота.
Как мы это сделали? Мы представили, что размеры нашей картинки — начальные точки на некоем фазовом пространстве системы уравнений:<br />
![image](https://github.com/i3373/CAT-SQUEEZER/assets/101145638/f3f4d0a5-2aad-4982-9e74-023b7b83c3aa) <br />
И, соответственно, просто изменяли их размеры в зависимости от изменения точек в зависимости от времени. Кстати, фазовое пространство данной системы выглядит примерно так: <br />
![image](https://github.com/i3373/CAT-SQUEEZER/assets/101145638/c35bc724-6eef-4df3-9478-ce63d095bb34)

Результат работы программы: <br />
![ezgif-5-27b2dd656e](https://github.com/i3373/CAT-SQUEEZER/assets/101145638/ab1d640d-081e-4d5c-ac7a-901dfd86f7f2)

Еще можно побаловаться меняя системы уравнений вот здесь, например, чтобы кота плющило, нужно заменить fx = x; fy = -y:
![image](https://github.com/i3373/CAT-SQUEEZER/assets/101145638/778cc67b-1e28-4885-b5ce-61f8c888a5d8)

Вот здесь мы меняем имя файла и количество итераций нашего скукоживания, чем больше число, тем "медленнее" будет скукоживаться кот:
![image](https://github.com/i3373/CAT-SQUEEZER/assets/101145638/8e3bcb7d-72dd-4e94-9a90-0b6126505bd0)
