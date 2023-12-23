import base64
import io
import matplotlib.pyplot as plt
import matplotlib as mpl


def create_graphics(payments, months):
    plt.style.use("fivethirtyeight")
    mpl.rcParams['font.size'] = 8
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['axes.facecolor'] = '#d9d9d9'
    mpl.rcParams['axes.edgecolor'] = '#d9d9d9'
    mpl.rcParams['grid.color'] = '#ffffff'
    mpl.rcParams['grid.linestyle'] = '-'
    mpl.rcParams['figure.facecolor'] = '#d9d9d9'
    mpl.rcParams['figure.edgecolor'] = '#d9d9d9'
    mpl.rcParams['savefig.facecolor'] = '#d9d9d9'
    mpl.rcParams['savefig.edgecolor'] = '#d9d9d9'

    fig, ax = plt.subplots()
    ax.plot(months, payments, marker='o', linestyle='-')
    ax.set_xticks(range(1, 13))
    ax.set(xlabel='Meses', ylabel='Valores', title='Balanço Financeiro')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    image_base64 = base64.b64encode(image_png).decode('utf-8')
    image_html = f'<img src="data:image/png;base64,{image_base64}">'
    return image_html
