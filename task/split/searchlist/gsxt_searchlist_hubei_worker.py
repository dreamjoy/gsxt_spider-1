#!/usr/bin/env python
# -*- coding:utf-8 -*-

from task.search.cracker.gsxt_hubei_worker import GsxtHuBeiWorker


class GsxtSearchListHuBeiWorker(GsxtHuBeiWorker):
    def __init__(self, **kwargs):
        GsxtHuBeiWorker.__init__(self, **kwargs)

    def get_detail_html_list(self, seed, session, param_list):
        return len(param_list), []
