import os
import json
import ast
from flask import Flask, render_template, request, \
    redirect, url_for, session, g
from flask_sqlalchemy import SQLAlchemy

from . import app, db
from .models import ZhiDaoDoc, ZhiDaoAnswer, ZhiDaoPicture, \
    BaiKeDoc, BaiKeItem, BaiKePicture, BaiKeSection
from .search import search, get_page


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/s', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        kw = request.args['keyword']
        cur_page_id = int(request.args['page'].strip('/'))
        results = search(kw)
        total_num = len(results)

        (litem, ritem), total_num_pages, (lpage, rpage) = naive_pagination(cur_page_id, len(results))

        results = [('zd' if isinstance(res, ZhiDaoDoc) else 'bk', res) for res in results[litem:ritem]]

        return render_template('search_result.html', kw=kw, results=results, num=total_num,
            cur=cur_page_id, total=total_num_pages, lp=lpage, rp=rpage)


@app.route('/zd_detail/<id>/')
def zd_detail(id):
    zd_doc = get_page(int(id))  # ZhiDaoDoc
    return render_template('zhidao_detail.html', zd_doc=zd_doc)

@app.route('/bk_detail/<id>/')
def bk_detail(id):
    bk_doc = get_page(int(id))  # BaiKeDoc
    return render_template('baike_detail.html', bk_doc=bk_doc)

def naive_pagination(cur_page_id, num_items):
    items_per_page = 10
    page_gap = 3
    visiable_num_pages = 6
    left_item_id = (cur_page_id - 1) * items_per_page
    right_item_id = cur_page_id * items_per_page

    total_num_pages = int((num_items - 1) / items_per_page) + 1
    left_page_id = max((cur_page_id - page_gap), 1)
    right_page_id = min(total_num_pages + 1, left_page_id + visiable_num_pages)

    return (left_item_id, right_item_id), total_num_pages, (left_page_id, right_page_id)


if __name__ == '__main__':
    app.debug = True
    app.run()
