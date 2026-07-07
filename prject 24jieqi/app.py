from flask import Flask, render_template

app = Flask(__name__)

# 1. 生成 24 节气数据
solar_terms = []
term_names = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
              "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
              "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
              "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"]
for i, name in enumerate(term_names, 1):
    # 文件名采用 01.png ~ 24.png 形式以匹配 static/images 目录
    solar_terms.append({
        'id': i, 'name': name, 'image': f'{i:02d}.png',
        'desc': f'{name}是二十四节气之一，代表着季节的转换和自然的律动。',
        'season': 'spring' if i <= 6 else ('summer' if i <= 12 else ('autumn' if i <= 18 else 'winter'))
    })

# 2. 固定 4 个商品数据 (对应您的需求)
# 说明：static/images 目录中仅存在 toy.png，此处对所有商品统一指向 toy.png 以保证正常显示；
# 实际项目中应放置 figure.png / bag.png / candle.png 等真实素材。
shop_items = [
    {'id': 101, 'name': '怀中陪伴毛绒玩偶', 'image': 'toy.png', 'desc': '软萌节气限定，抱在怀里的温暖。', 'price': 129},
    {'id': 102, 'name': '指尖灵气树脂摆件', 'image': 'toy.png', 'desc': '桌面上的东方灵气，治愈系掌心好物。', 'price': 89},
    {'id': 103, 'name': '一起走！帆布包', 'image': 'toy.png', 'desc': '将四时之美背在身上，文艺出街必备。', 'price': 79},
    {'id': 104, 'name': '节气印象香薰套装', 'image': 'toy.png', 'desc': '用气味感知四季，东方草木调香氛。', 'price': 199},
]

@app.route('/')
def index(): return render_template('index.html')

@app.route('/display')
def display(): return render_template('display.html', terms=solar_terms)

@app.route('/culture/<int:id>')
def culture_detail(id):
    term = next((item for item in solar_terms if item["id"] == id), None)
    return render_template('culture.html', term=term)

@app.route('/interactive')
def interactive(): return render_template('interactive.html')

@app.route('/quiz')
def quiz(): return render_template('quiz.html')

@app.route('/shop')
def shop(): return render_template('shop.html', items=shop_items)

@app.route('/product/<int:id>')
def product_detail(id):
    item = next((item for item in shop_items if item["id"] == id), None)
    return render_template('product_detail.html', item=item)

if __name__ == '__main__':
    # 监听 0.0.0.0 使外部也可访问；提供可分享的访问链接
    app.run(host='0.0.0.0', debug=True, port=5000)