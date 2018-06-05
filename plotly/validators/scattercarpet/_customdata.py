import _plotly_utils.basevalidators


class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self, plotly_name='customdata', parent_name='scattercarpet', **kwargs
    ):
        super(CustomdataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='data',
            **kwargs
        )