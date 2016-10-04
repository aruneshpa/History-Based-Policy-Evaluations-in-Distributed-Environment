
import da
PatternExpr_178 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])
PatternExpr_196 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub'), da.pat.FreePattern('subid'), da.pat.ConstantPattern('Res'), da.pat.FreePattern('resid'), da.pat.FreePattern('res_hash')])
PatternExpr_209 = da.pat.FreePattern('p')
PatternExpr_244 = da.pat.ConstantPattern('Decision from Res_Co')
PatternExpr_248 = da.pat.FreePattern('p')
PatternExpr_183 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])])
PatternExpr_278 = da.pat.TuplePattern([da.pat.ConstantPattern('Res')])
PatternExpr_296 = da.pat.TuplePattern([da.pat.ConstantPattern('Res'), da.pat.FreePattern('resid')])
PatternExpr_303 = da.pat.FreePattern('p')
PatternExpr_283 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Res')])])
PatternExpr_372 = da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision')])
PatternExpr_390 = da.pat.ConstantPattern('Policy Decision')
PatternExpr_394 = da.pat.FreePattern('p')
PatternExpr_377 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision')])])
_config_object = {'channel': 'fifo', 'clock': 'Lamport'}
import sys

class Sub_Co(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Sub_CoReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_0', PatternExpr_178, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_1', PatternExpr_196, sources=[PatternExpr_209], destinations=None, timestamps=None, record_history=None, handlers=[self._Sub_Co_handler_195]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_2', PatternExpr_244, sources=[PatternExpr_248], destinations=None, timestamps=None, record_history=None, handlers=[self._Sub_Co_handler_243])])

    def setup(self):
        self._state.app_id = None

    def run(self):
        a = False
        super()._label('_st_label_175', block=False)
        _st_label_175 = 0
        while (_st_label_175 == 0):
            _st_label_175 += 1
            if PatternExpr_183.match_iter(self._Sub_CoReceivedEvent_0):
                _st_label_175 += 1
            else:
                super()._label('_st_label_175', block=True)
                _st_label_175 -= 1

    def _Sub_Co_handler_195(self, subid, resid, res_hash, p):
        self._state.app_id = p
        self.output(((('Request from Application received with ' + subid) + ' and ') + resid))
        res_coord_id = res_hash[resid]
        self.output(('Subject coord sending to Res Co with ' + str(res_coord_id)))
        self._send(('Res', resid), res_coord_id)
    _Sub_Co_handler_195._labels = None
    _Sub_Co_handler_195._notlabels = None

    def _Sub_Co_handler_243(self, p):
        self.output('Aa gaya bc!!')
        self._state.app_id = self._state.app_id
        self._send('Policy Decision', self._state.app_id)
    _Sub_Co_handler_243._labels = None
    _Sub_Co_handler_243._notlabels = None

class Res_Co(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Res_CoReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Res_CoReceivedEvent_0', PatternExpr_278, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Res_CoReceivedEvent_1', PatternExpr_296, sources=[PatternExpr_303], destinations=None, timestamps=None, record_history=None, handlers=[self._Res_Co_handler_295])])

    def setup(self):
        pass

    def run(self):
        a = False
        super()._label('_st_label_275', block=False)
        _st_label_275 = 0
        while (_st_label_275 == 0):
            _st_label_275 += 1
            if PatternExpr_283.match_iter(self._Res_CoReceivedEvent_0):
                _st_label_275 += 1
            else:
                super()._label('_st_label_275', block=True)
                _st_label_275 -= 1

    def _Res_Co_handler_295(self, resid, p):
        self.output(('Request from Subject_Coord received with ' + resid))
        self._send('Decision from Res_Co', p)
    _Res_Co_handler_295._labels = None
    _Res_Co_handler_295._notlabels = None

class Application(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ApplicationReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ApplicationReceivedEvent_0', PatternExpr_372, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ApplicationReceivedEvent_1', PatternExpr_390, sources=[PatternExpr_394], destinations=None, timestamps=None, record_history=None, handlers=[self._Application_handler_389])])

    def setup(self, sub_hash, sub_IDs, res_hash, res_IDs):
        self._state.sub_hash = sub_hash
        self._state.sub_IDs = sub_IDs
        self._state.res_hash = res_hash
        self._state.res_IDs = res_IDs
        pass

    def run(self):
        sub_id = self._state.sub_IDs[1]
        sub_coord_id = self._state.sub_hash[sub_id]
        res_id = self._state.res_IDs[2]
        res_coord_id = self._state.res_hash[res_id]
        self.output(('Sending this request to ' + str(sub_coord_id)))
        self._send(('Sub', sub_id, 'Res', res_id, self._state.res_hash), sub_coord_id)
        super()._label('_st_label_369', block=False)
        _st_label_369 = 0
        while (_st_label_369 == 0):
            _st_label_369 += 1
            if PatternExpr_377.match_iter(self._ApplicationReceivedEvent_0):
                _st_label_369 += 1
            else:
                super()._label('_st_label_369', block=True)
                _st_label_369 -= 1

    def _Application_handler_389(self, p):
        self.output('Policy Evaluated. Done!!')
    _Application_handler_389._labels = None
    _Application_handler_389._notlabels = None

class _NodeMain(da.DistProcess):

    def run(self):
        num_sub_co = (int(sys.argv[1]) if (len(sys.argv) > 1) else 3)
        num_res_co = (int(sys.argv[1]) if (len(sys.argv) > 1) else 3)
        sub_co = da.new(Sub_Co, num=num_sub_co)
        res_co = da.new(Res_Co, num=num_res_co)
        list_sub_coords = [p for p in sub_co]
        list_res_coords = [p for p in res_co]
        sub_IDs = ['sub1', 'sub2', 'sub3']
        res_IDs = ['res1', 'res2', 'res3']
        sub_dict = {}
        res_dict = {}
        for i in range(3):
            sub_dict[sub_IDs[i]] = list_sub_coords[i]
        for i in range(3):
            res_dict[res_IDs[i]] = list_res_coords[i]
        app = da.new(Application, [sub_dict, sub_IDs, res_dict, res_IDs], num=1)
        da.start(sub_co)
        da.start(res_co)
        da.start(app)
