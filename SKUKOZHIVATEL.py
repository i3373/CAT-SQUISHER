import numpy as np
from scipy import integrate
from PIL import Image



# Input Data
image_name = "cat_0.png"
number_of_squeezed_cats = 60 # The higher the number the slower the squeezing


image = Image.open(image_name)
width, height = image.size
def f(t, r):
    x, y = r
    fx = -x
    fy = -y
    return fx, fy
# Taken from explanation of video, where solve_ivp explained



SKUKOZHIVATEL_RESULT = integrate.solve_ivp(f, (0, 10), (width, height), t_eval= np.linspace(0, 10, number_of_squeezed_cats))
for i in range (0, number_of_squeezed_cats):
    a, b = int(SKUKOZHIVATEL_RESULT.y[0][i]), int(SKUKOZHIVATEL_RESULT.y[1][i])
    if a <= 1 or b <= 1:
        continue
    # There were some negative numbers, so program crashed, so I added a check for that

    image.resize((a, b)).save(f"cat_{i+1}.png")
    i = i + 1


