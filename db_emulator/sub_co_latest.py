
import da
PatternExpr_177 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])
PatternExpr_197 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub'), da.pat.FreePattern('sub_id'), da.pat.ConstantPattern('Res'), da.pat.FreePattern('res_id'), da.pat.ConstantPattern('s'), da.pat.FreePattern('master')])
PatternExpr_212 = da.pat.FreePattern('p')
PatternExpr_256 = da.pat.ConstantPattern('Decision from Worker')
PatternExpr_260 = da.pat.FreePattern('p')
PatternExpr_290 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])
PatternExpr_308 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub'), da.pat.FreePattern('sub_id'), da.pat.ConstantPattern('Res'), da.pat.FreePattern('res_id'), da.pat.ConstantPattern('Master'), da.pat.FreePattern('master')])
PatternExpr_323 = da.pat.FreePattern('p')
PatternExpr_295 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])])
PatternExpr_359 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])
PatternExpr_377 = da.pat.TuplePattern([da.pat.ConstantPattern('Sub'), da.pat.FreePattern('sub_id'), da.pat.ConstantPattern('Res'), da.pat.FreePattern('res_id'), da.pat.ConstantPattern('Master'), da.pat.FreePattern('master')])
PatternExpr_392 = da.pat.FreePattern('p')
PatternExpr_364 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Sub')])])
PatternExpr_481 = da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision')])
PatternExpr_499 = da.pat.ConstantPattern('Policy Decision')
PatternExpr_503 = da.pat.FreePattern('p')
PatternExpr_486 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Policy Decision')])])
PatternExpr_637 = da.pat.ConstantPattern('Send me Subject Hash')
PatternExpr_641 = da.pat.FreePattern('p')
PatternExpr_655 = da.pat.ConstantPattern('Send me Resource Hash')
PatternExpr_659 = da.pat.FreePattern('p')
_config_object = {'channel': 'fifo', 'clock': 'Lamport'}
import sys
import random

class Sub_Co(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Sub_CoReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_0', PatternExpr_177, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_1', PatternExpr_197, sources=[PatternExpr_212], destinations=None, timestamps=None, record_history=None, handlers=[self._Sub_Co_handler_196]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Sub_CoReceivedEvent_2', PatternExpr_256, sources=[PatternExpr_260], destinations=None, timestamps=None, record_history=None, handlers=[self._Sub_Co_handler_255])])

    def setup(self):
        self._state.app_id = None

    def run(self):
        super()._label('_st_label_174', block=False)

        def ExistentialOpExpr_175():
            for (_, _, (_ConstantPattern190_,)) in self._Sub_CoReceivedEvent_0:
                if (_ConstantPattern190_ == 'Sub'):
                    if True:
                        return True
            return False
        _st_label_174 = 0
        while (_st_label_174 == 0):
            _st_label_174 += 1
            if ExistentialOpExpr_175():
                _st_label_174 += 1
            else:
                super()._label('_st_label_174', block=True)
                _st_label_174 -= 1

    def _Sub_Co_handler_196(self, sub_id, res_id, master, p):
        self._state.app_id = p
        self.output(((('Request from Application received with ' + sub_id) + ' and ') + res_id))
        res_hash = master.res_dict
        res_coord_id = res_hash[res_id]
        self.output(('Subject coord sending to Resource Coord ' + str(res_coord_id)))
        self._send(('Sub', sub_id, 'Res', res_id, 'Master', master), res_coord_id)
    _Sub_Co_handler_196._labels = None
    _Sub_Co_handler_196._notlabels = None

    def _Sub_Co_handler_255(self, p):
        self.output('!!')
        self._state.app_id = self._state.app_id
        self._send('Policy Decision', self._state.app_id)
    _Sub_Co_handler_255._labels = None
    _Sub_Co_handler_255._notlabels = None

class Worker(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._WorkerReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_WorkerReceivedEvent_0', PatternExpr_290, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_WorkerReceivedEvent_1', PatternExpr_308, sources=[PatternExpr_323], destinations=None, timestamps=None, record_history=None, handlers=[self._Worker_handler_307])])

    def setup(self):
        pass

    def run(self):
        a = False
        super()._label('_st_label_287', block=False)
        _st_label_287 = 0
        while (_st_label_287 == 0):
            _st_label_287 += 1
            if PatternExpr_295.match_iter(self._WorkerReceivedEvent_0):
                _st_label_287 += 1
            else:
                super()._label('_st_label_287', block=True)
                _st_label_287 -= 1

    def _Worker_handler_307(self, sub_id, res_id, master, p):
        self.output(((('Request from Resource_Coord received with ' + sub_id) + ' and ') + res_id))
        sub_hash = master.sub_dict
        self._send('Decision from Worker', sub_hash[sub_id])
    _Worker_handler_307._labels = None
    _Worker_handler_307._notlabels = None

class Res_Co(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Res_CoReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Res_CoReceivedEvent_0', PatternExpr_359, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_Res_CoReceivedEvent_1', PatternExpr_377, sources=[PatternExpr_392], destinations=None, timestamps=None, record_history=None, handlers=[self._Res_Co_handler_376])])

    def setup(self, workers):
        self._state.workers = workers
        pass

    def run(self):
        super()._label('_st_label_356', block=False)
        _st_label_356 = 0
        while (_st_label_356 == 0):
            _st_label_356 += 1
            if PatternExpr_364.match_iter(self._Res_CoReceivedEvent_0):
                _st_label_356 += 1
            else:
                super()._label('_st_label_356', block=True)
                _st_label_356 -= 1

    def _Res_Co_handler_376(self, sub_id, res_id, master, p):
        self.output(('Request from Subject_Coord received with ' + res_id))
        w_num = random.randint(0, len(self._state.workers))
        w_id = self._state.workers[w_num]
        self.output(('Sending request to Worker ' + w_id))
        self._send(('Sub', sub_id, 'Res', res_id, 'Master', master), w_id)
    _Res_Co_handler_376._labels = None
    _Res_Co_handler_376._notlabels = None

class Application(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ApplicationReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ApplicationReceivedEvent_0', PatternExpr_481, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ApplicationReceivedEvent_1', PatternExpr_499, sources=[PatternExpr_503], destinations=None, timestamps=None, record_history=None, handlers=[self._Application_handler_498])])

    def setup(self, sub_id, res_id, master):
        self._state.sub_id = sub_id
        self._state.res_id = res_id
        self._state.master = master
        self._state.sub_hash = dict()

    def run(self):
        self.output('Applocation BP 1')
        self._send('Send me Subject Hash', self._state.master)
        self.output('Application BP 2')
        sub_coord_id = self._state.sub_hash[self._state.sub_id]
        self.output(('Sending this request to ' + str(sub_coord_id)))
        self._send(('Sub', self._state.sub_id, 'Res', self._state.res_id, 'Master', self._state.master), sub_coord_id)
        super()._label('_st_label_478', block=False)
        _st_label_478 = 0
        while (_st_label_478 == 0):
            _st_label_478 += 1
            if PatternExpr_486.match_iter(self._ApplicationReceivedEvent_0):
                _st_label_478 += 1
            else:
                super()._label('_st_label_478', block=True)
                _st_label_478 -= 1

    def _Application_handler_498(self, p):
        self.output('Policy Evaluated. Done!!')
    _Application_handler_498._labels = None
    _Application_handler_498._notlabels = None

class Master(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_0', PatternExpr_637, sources=[PatternExpr_641], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_636]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_1', PatternExpr_655, sources=[PatternExpr_659], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_654])])

    def setup(self, num_sub_co, num_res_co, num_workers, num_sub_attrs, num_res_atts):
        self._state.num_sub_co = num_sub_co
        self._state.num_res_co = num_res_co
        self._state.num_workers = num_workers
        self._state.num_sub_attrs = num_sub_attrs
        self._state.num_res_atts = num_res_atts
        self._state.sub_dict = dict()
        self._state.res_dict = dict()

    def run(self):
        self.initialize()

    def initialize(self):
        sub_attrs = ['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5']
        res_attrs = ['Res1', 'Res2', 'Res3', 'Res4', 'Res5']
        worker = da.new(Worker, num=self._state.num_workers)
        workers = [w for w in worker]
        sub_co = da.new(Sub_Co, num=self._state.num_sub_co)
        res_co = da.new(Res_Co, [workers], num=self._state.num_res_co)
        (self._state.sub_dict, self._state.res_dict) = self.create_dicts(sub_co, res_co, sub_attrs, res_attrs)
        self.output('bp 2')
        sub_id = random.randint(0, len(sub_attrs))
        res_id = random.randint(0, len(res_attrs))
        da.start(sub_co)
        da.start(res_co)
        da.start(worker)
        self.output('bp 3')

    def create_dicts(self, sub_co, res_co, sub_attrs, res_attrs):
        list_sub_coords = [p for p in sub_co]
        list_res_coords = [p for p in res_co]
        self._state.sub_dict = {}
        self._state.res_dict = {}
        for i in range(len(sub_attrs)):
            self._state.sub_dict[sub_attrs[i]] = list_sub_coords[i]
        for i in range(len(res_attrs)):
            self._state.res_dict[res_attrs[i]] = list_res_coords[i]
        return (self._state.sub_dict, self._state.res_dict)

    def _Master_handler_636(self, p):
        self.output('baluchi')
        self._send(('Subject Hash', self._state.sub_dict), p)
    _Master_handler_636._labels = None
    _Master_handler_636._notlabels = None

    def _Master_handler_654(self, p):
        self._send(('Resource Hash', self._state.res_dict), p)
    _Master_handler_654._labels = None
    _Master_handler_654._notlabels = None

class _NodeMain(da.DistProcess):

    def run(self):
        num_sub_co = (int(sys.argv[1]) if (len(sys.argv) > 1) else 5)
        num_res_co = (int(sys.argv[1]) if (len(sys.argv) > 2) else 5)
        num_workers = (int(sys.argv[1]) if (len(sys.argv) > 3) else 5)
        sub_id = sys.argv[4]
        res_id = sys.argv[5]
        num_sub_attrs = 5
        num_res_attrs = 5
        master = da.new(Master, [num_sub_co, num_res_co, num_workers, num_sub_attrs, num_res_attrs])
        app = da.new(Application, [sub_id, res_id, master], num=1)
        da.start(master)
        self.output(' master started')
        da.start(app)
        self.output('application started')
