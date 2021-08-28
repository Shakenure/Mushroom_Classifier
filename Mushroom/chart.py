from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import io
import matplotlib.pyplot as plt; plt.rcdefaults()

def draw(request):
    fig = Figure()

    x = np.arange(1, 10)
    y = np.arange(1, 5)
    plt.bar(x, y, align="center", alpha=0.5, label="Name")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response