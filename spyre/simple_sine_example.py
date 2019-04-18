try:
    from . import server
except Exception:
    import server

import matplotlib.pyplot as plt
import numpy as np


class SimpleSineApp(server.App):
    title = "Simple Sine App"
    inputs = [
        {
            "type": "text",
            "key": "text",
            "value": "hello world",
            "label": "Teste",
            "action_id": "sine_wave_plot"
        }, {
            "type": "text",
            "key": "freq",
            "value": "0",
            "label": "Frequência",
            "action_id": "sine_wave_plot"
        }, {
            "type": 'checkboxgroup',
            "label": 'Axis Labels',
            "options": [
                {"label": "x-axis", "value": "x", "checked": True},
                {"label": "y-axis", "value": "y"}
            ],
            "key": 'axis_label',
            "action_id": "refresh",
        }
    ]

    outputs = [{
        "type": "plot",
        "id": "sine_wave_plot"
    }]

    def getPlot(self, params):
        f = float(params['freq'])
        t = params['text']
        x = np.arange(0, 2 * np.pi, np.pi / 150)
        y = np.sin(f * x)

        fig = plt.figure()
        splt1 = fig.add_subplot(1, 1, 1)
        splt1.plot(x, y)

        splt1.set_title(t)
        axis_label = params['axis_label']
        for axis in axis_label:
            if axis == "x":
                splt1.set_xlabel('x axis')
            if axis == "y":
                splt1.set_ylabel('y axis')

        return fig


if __name__ == '__main__':
    app = SimpleSineApp()
    app.launch()
