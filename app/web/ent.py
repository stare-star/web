# from app.view_models.trade import TradeInfo
from app import cache
from app.forms.ent import SearchForm
from app.libs.helper import is_code_or_key
from app.models.ent import entResult
from app.view_models.ent import EntCollection
from flask import render_template, flash, request
from flask_login import login_required

from . import web


# from app.models.gift import Gift
# from app.models.wish import Wish


@web.route('/ent/search', methods=['Get', 'POST'])
@login_required
def entsearch():
    """
        企业代码检索
        不缓存，缓存的意义很小，反而会占用内存
    """
    form = SearchForm(request.args)

    q = form.q.data.strip()
    ents = EntCollection()
    code_or_key = is_code_or_key(q)

    if code_or_key == 'code':
        res = entResult.query.filter_by(entname=q).all()
        ents.fill(res, q)
        if not res:
            flash('该企业代码不存在，查询失败')

    else:
        res = entResult.query.filter_by(label=q).all()
        ents.fill(res, q)

        if not res:
            flash('该企业类别不存在，查询失败')

    # return str(res.label)
    return render_template('search_ent_result.html', ents=ents)


@web.route('/ent/pie', methods=['Get', 'POST'])
@login_required
@cache.cached(timeout=1800)
def entpie():
    values, names = entResult().get_pie()
    print("--------------")
    print("--------------")

    print(names)

    return render_template('pie.html',  values= values, names=names)

@web.route('/ent/bar', methods=['Get', 'POST'])
@login_required
def entbar():
    values, names = entResult().get_pie()
    print("--------------")
    print("--------------")

    print(names)

    return render_template('bar.html',  values= values, names=names)
