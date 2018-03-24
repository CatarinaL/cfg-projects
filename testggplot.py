import matplotlib as mpl
#i need this matplotlib.use() at least on macOS
#because of backend issues...
#see: https://matplotlib.org/faq/usage_faq.html#what-is-a-backend
#it aplies to running this script, so not good for production
mpl.use('Agg')
#import matplotlib.pyplot as plt
from ggplot import *

#colors?
def get_color_swatch():
    class gg_stub:
        pass
    return (gg_stub() + scale_color_brewer()).manual_color_list

swatch = get_color_swatch()

#le data
diamonds.head()

#blank canvas
p = ggplot(aes(x='date', y='beef', color = 'clarity'), data=meat)
#add points to plot
p + geom_point()
p.save('img/testimage.png', width=12, height=8, dpi=144)
#p.show()
p + geom_point() + geom_line() + scale_color_brewer(type='seq')
p.save('img/testimage2.png', width=12, height=8, dpi=144)

c = ggplot(mtcars, aes(x='wt', y='mpg', label='name', color = 'clarity'))
c + geom_text(size=5) + geom_point() + scale_color_brewer(type='qual')
#angle attribute doesnt seem to be working
c.save('img/testimage3.png', width=12, height=8, dpi=144)
