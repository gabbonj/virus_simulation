from .. import imports

plt = imports.plt


def plot_data():
    i = 0
    for item in imports.settings.data.items():
        assert isinstance(item[1], list)
        plt.figure(i)
        y = list(item[1])
        x = [x for x in range(len(item[1]))]
        if len(x) == len(y):
            plt.plot(x, y, label=item[0])
        else:
            print('\n\npisello\n\n')

        plt.title(item[0])
        plt.grid(color='c', linestyle=':')
        plt.legend(shadow=True)
        i += 1
    plt.show()