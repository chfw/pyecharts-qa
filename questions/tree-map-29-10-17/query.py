from pyecharts import TreeMap

data = [
    {
        "value": 10,
        "name": "我是A",
    },
    {
        "value": 10,
        "name": "我是B",
        "children": [
            {

                'children': [
                    {
                        'value': 12,
                        "name": "我是B.children.a"
                    },
                    {
                        "value": 28,
                        "name": "我是B.children.b"
                    },
                    {
                        "value": 20,
                        "name": "我是B.children.c"
                    },
                    {
                        "value": 16,
                        "name": "我是B.children.d"
                    }],
                "value": 2,
                "name": "我是B.children",                
            }]},
            {'children': [{'value': -1.9, 'name': '浙大网新'}, 
              {'value': -1.8, 'name': '综艺股份'}, 
              {'value': -0.7, 'name': '佳都科技'}, 
              {'value': -1.3, 'name': '烽火通信'}, 
              {'value': 1.3, 'name': '信威集团'}, 
], 
'value': 10, 
'name': 'IPV6概念'}
]

def getLevelOption():
    return [{
        'itemStyle': {
            'normal': {
                'borderColor': '#777',
                'borderWidth': 0,
                'gapWidth': 1
            }
        },
        'upperLabel': {
            'normal': {
                'show': False
            }
        }
    }, {
        'itemStyle': {
            'normal': {
                'borderColor': '#555',
                'borderWidth': 5,
                'gapWidth': 1
            },
            'emphasis': {
                'borderColor': '#ddd'
            }
        }
    }, {
        'colorSaturation': [0.35, 0.5],
        'itemStyle': {
            'normal': {
                'borderWidth': 5,
                'gapWidth': 1,
                'borderColorSaturation': 0.6
            }
        }
    }]

treemap = TreeMap("树图-下钻示例", width=1200, height=600)
treemap.add("演示数据", data, is_label_show=True, label_pos='inside',
            treemap_left_depth=2)
for series in treemap._option['series']:
    series['upperLabel'] = dict(normal=dict(
                        show=True,
                        height=30))
    series['levels'] = getLevelOption()
treemap.render()
