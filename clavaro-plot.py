
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image

my_dpi = 96
fig, ax = plt.subplots (
  1, 2, figsize=(951/my_dpi, 420/my_dpi), dpi=my_dpi,
  gridspec_kw={'width_ratios': [14, 18]})
cmap1 = sns.color_palette (palette="tab20c", n_colors=18)
ax[0].set (ylim=(0.0, 2.25))
ax[1].set (ylim=(0.0, 2.25))
df1 = pd.read_csv (
  "results-left.txt", header=None, 
  usecols=[0,1], names=["x","y"])
df2 = pd.read_csv (
  "results-right.txt",header=None, 
  usecols=[0,1], names=["x","y"])
sns.boxplot (data=df1,x='x',y='y',ax=ax[0], palette=cmap1)
sns.boxplot (data=df2,x='x',y='y',ax=ax[1], palette=cmap1)
ax[0].set_title('Left')
ax[0].set_ylabel ('')    
ax[0].set_xlabel ('')
ax[1].set_title('Right')
ax[1].set_ylabel ('')    
ax[1].set_xlabel ('')
fig.tight_layout ()
fig.savefig ("results-1.png")

image1 = 'results-1.png'
image2 = 'clavaro.png'
img1 = Image.open (image1)
img2 = Image.open (image2)
w1,h1 = img1.size
w2,h2 = img2.size
margin = 20
result = Image.new (
  mode='RGB', size=(w1, h1 + margin + h2),color='white')
result.paste (img1, (0, 0))
result.paste (img2, (0, h1 + margin))
result.save ('results.png')
result.show()

