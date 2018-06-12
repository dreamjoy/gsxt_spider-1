#!/usr/bin/env python
# -*- coding:utf-8 -*-

from task.search.cracker.gsxt_tianjin_worker import GsxtTianJinWorker


class GsxtSearchListTianJinWorker(GsxtTianJinWorker):
    def __init__(self, **kwargs):
        GsxtTianJinWorker.__init__(self, **kwargs)

    def get_detail_html_list(self, seed, session, param_list):
        return len(param_list), []
