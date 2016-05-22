from data_describe import concrete
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')


def violin_viz(df):
    ax = sns.violinplot(df)
    plt.xticks(rotation=60)
    plt.show()


violin_viz(concrete)
