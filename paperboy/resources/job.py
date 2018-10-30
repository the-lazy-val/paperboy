import json
from .base import BaseResource


class JobResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(JobResource, self).__init__(*args, **kwargs)

    def on_get(self, req, resp):
        resp.content_type = 'application/json'
        req.context['params'] = req.params
        resp.body = json.dumps(self.db.jobs.list(req.context, self.session))

    def on_post(self, req, resp):
        resp.content_type = 'application/json'
        req.context['params'] = req.params
        resp.body = json.dumps(self.db.jobs.store(req.context, self.session))
        # self.scheduler.store()


class JobDetailResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(JobDetailResource, self).__init__(*args, **kwargs)

    def on_get(self, req, resp):
        resp.content_type = 'application/json'
        req.context['params'] = req.params
        resp.body = json.dumps(self.db.jobs.detail(req.context, self.session))
