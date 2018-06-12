#!/usr/bin/env python
# -*- coding:utf-8 -*-

from task.search.cracker.gsxt_guangdong_worker import GsxtGuangDongWorker


class GsxtSearchListGuangDongWorker(GsxtGuangDongWorker):
    def __init__(self, **kwargs):
        GsxtGuangDongWorker.__init__(self, **kwargs)

    def get_detail_html_list(self, seed, session, param_list):
        return len(param_list), []
