import _plotly_utils.basevalidators


class IdssrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='idssrc', parent_name='heatmap', **kwargs):
        super(IdssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )