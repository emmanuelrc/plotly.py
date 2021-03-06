import _plotly_utils.basevalidators


class FillcolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self, plotly_name='fillcolor', parent_name='contour', **kwargs
    ):
        super(FillcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            colorscale_path='contour.colorscale',
            **kwargs
        )
