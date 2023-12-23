import base64
import io
import matplotlib.pyplot as plt


def create_graphics(payments, months):
    fig, ax = plt.subplots()
    ax.plot(months, payments, marker='o', linestyle='-')
    ax.set_xticks(range(1, 13))
    ax.set(xlabel='Meses', ylabel='Valores', title='Gráfico Mensal')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    image_base64 = base64.b64encode(image_png).decode('utf-8')
    image_html = f'<img src="data:image/png;base64,{image_base64}">'
    return image_html
