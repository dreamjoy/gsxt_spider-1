#!/usr/bin/env python
# -*- coding:utf-8 -*-
from task.search.cracker.gsxt_xizang_worker import GsxtXiZangWorker


class GsxtSearchListXiZangWorker(GsxtXiZangWorker):
    def __init__(self, **kwargs):
        GsxtXiZangWorker.__init__(self, **kwargs)

    def get_detail_html_list(self, seed, session, param_list):
        return len(param_list), []
