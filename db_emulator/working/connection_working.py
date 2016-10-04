
import da
PatternExpr_173 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])
PatternExpr_191 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub'), da.pat.FreePattern('subid'), da.pat.ConstantPattern('Res'), da.pat.FreePattern('resid')])
PatternExpr_202 = da.pat.FreePattern('p')
PatternExpr_178 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])])
PatternExpr_241 = da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision')])
PatternExpr_259 = da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision'), da.pat.FreePattern('subid'), da.pat.FreePattern('resid')])
PatternExpr_268 = da.pat.FreePattern('p')
PatternExpr_246 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision')])])
_config_object = {'channel': 'fifo', 'clock': 'Lamport'}
import sys

class Sub_Co(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Sub_CoReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_0', PatternExpr_173, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_1', PatternExpr_191, sources=[PatternExpr_202], destinations=None, timestamps=None, record_history=None, handlers=[self._Sub_Co_handler_190])])

    def setup(self):
        pass

    def run(self):
        a = False
        super()._label('_st_label_170', block=False)
        _st_label_170 = 0
        while (_st_label_170 == 0):
            _st_label_170 += 1
            if PatternExpr_178.match_iter(self._Sub_CoReceivedEvent_0):
                _st_label_170 += 1
            else:
                super()._label('_st_label_170', block=True)
                _st_label_170 -= 1

    def _Sub_Co_handler_190(self, subid, resid, p):
        self.output(((('Request from Application received with ' + subid) + ' and ') + resid))
        self._send(('Policy Decision', subid, resid), p)
    _Sub_Co_handler_190._labels = None
    _Sub_Co_handler_190._notlabels = None

class Application(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ApplicationReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ApplicationReceivedEvent_0', PatternExpr_241, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ApplicationReceivedEvent_1', PatternExpr_259, sources=[PatternExpr_268], destinations=None, timestamps=None, record_history=None, handlers=[self._Application_handler_258])])

    def setup(self, p):
        self._state.p = p
        pass

    def run(self):
        self._send(('Sub', 'Sub1', 'Res', 'Res1'), self._state.p)
        super()._label('_st_label_238', block=False)
        _st_label_238 = 0
        while (_st_label_238 == 0):
            _st_label_238 += 1
            if PatternExpr_246.match_iter(self._ApplicationReceivedEvent_0):
                _st_label_238 += 1
            else:
                super()._label('_st_label_238', block=True)
                _st_label_238 -= 1

    def _Application_handler_258(self, subid, resid, p):
        self.output(((('Policy Evaluated. Done!! for ' + subid) + ' and ') + resid))
    _Application_handler_258._labels = None
    _Application_handler_258._notlabels = None

class _NodeMain(da.DistProcess):

    def run(self):
        sub_co = da.new(Sub_Co, num=1)
        app = da.new(Application, num=3)
        da.setup(app, sub_co)
        da.start(sub_co)
        da.start(app)
