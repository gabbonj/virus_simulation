from .. import imports

plt = imports.plt


def plot_data():
    for item in imports.settings.data.items():
        assert isinstance(item[1], list)
        plt.plot([x for x in range(len(item[1]))], item[1], label=item[0])

        plt.title(item[0])
        plt.grid(color='c', linestyle=':')
        plt.legend(shadow=True)
        plt.show()