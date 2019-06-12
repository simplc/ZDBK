import random

def pseudo_ZhiDao(i):
    question = {
        "text": "这是第%d个问题" % i,
        "ask_time": "2019-0%d-01" % (random.randint(1, 9))
    }

    answers = []
    n_answers = random.randint(1, 5)
    for j in range(n_answers):
        ans = {
            "user": "小明",
            "t": "2020-01-01",
            "likes": random.randint(50, 99),
            "dislikes": random.randint(0, 49),
            "accepted": True if random.randint(0, 1) else False,
            "text": "这是第%d个回答 " % (j) * random.randint(10, 20)
        }
        answers.append(ans)

    return {"type": "zd", "doc_id": "zd_%s" % i, "question": question, "answers": answers}

def pseudo_BaiKe(i):
    title = {
        "text": "第%d条百科" % i,
        "desc": "第%d条百科的描述" % (i) * 10
    }

    sections = []
    n_sections = random.randint(1, 5)
    for j in range(n_sections):
        sec = {
            "title": "第%d小节的标题" % j,
            "text": "第%d小节的内容 " % (j) * random.randint(10, 20)
        }
        sections.append(sec)

    return {"type": "bk", "doc_id": "bk_%s" % i, "title": title, "sections": sections}

def pseudo_all():
    n_results = 80
    n_zds = random.randint(20, 60)
    n_bks = n_results - n_zds

    results = []
    for i in range(n_zds):
        results.append(pseudo_ZhiDao(i + 1))
    for i in range(n_bks):
        results.append(pseudo_BaiKe(i + 1))

    random.shuffle(results)
    return results