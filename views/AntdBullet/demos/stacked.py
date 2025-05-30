import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBullet(
        data=[
            {
                'title': '满意度',
                'ranges': [40, 70, 100],
                'measures': [30, 50],
                'target': 85,
            },
        ],
        measureField='measures',
        rangeField='ranges',
        targetField='target',
        xField='title',
        color={
            'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
            'measure': ['#5B8FF9', '#61DDAA'],
            'target': '#39a3f4',
        },
        label={
            'measure': {
                'position': 'middle',
                'style': {
                    'fill': '#fff',
                },
            },
        },
        xAxis={
            'line': None,
        },
        yAxis=False,
        tooltip={
            'showMarkers': False,
            'shared': True,
        },
        legend={
            'custom': True,
            'position': 'bottom',
            'items': [
                {
                    'value': '差',
                    'name': '差',
                    'marker': {
                        'symbol': 'square',
                        'style': {
                            'fill': '#FFbcb8',
                            'r': 5,
                        },
                    },
                },
                {
                    'value': '良',
                    'name': '良',
                    'marker': {
                        'symbol': 'square',
                        'style': {
                            'fill': '#FFe0b0',
                            'r': 5,
                        },
                    },
                },
                {
                    'value': '优',
                    'name': '优',
                    'marker': {
                        'symbol': 'square',
                        'style': {
                            'fill': '#bfeec8',
                            'r': 5,
                        },
                    },
                },
                {
                    'value': '第一季度',
                    'name': '第一季度',
                    'marker': {
                        'symbol': 'square',
                        'style': {
                            'fill': '#5B8FF9',
                            'r': 5,
                        },
                    },
                },
                {
                    'value': '第二季度',
                    'name': '第二季度',
                    'marker': {
                        'symbol': 'square',
                        'style': {
                            'fill': ' #61DDAA',
                            'r': 5,
                        },
                    },
                },
                {
                    'value': '目标值',
                    'name': '目标值',
                    'marker': {
                        'symbol': 'line',
                        'style': {
                            'stroke': '#39a3f4',
                            'r': 5,
                        },
                    },
                },
            ],
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdBullet(
    data=[
        {
            'title': '满意度',
            'ranges': [40, 70, 100],
            'measures': [30, 50],
            'target': 85,
        },
    ],
    measureField='measures',
    rangeField='ranges',
    targetField='target',
    xField='title',
    color={
        'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
        'measure': ['#5B8FF9', '#61DDAA'],
        'target': '#39a3f4',
    },
    label={
        'measure': {
            'position': 'middle',
            'style': {
                'fill': '#fff',
            },
        },
    },
    xAxis={
        'line': None,
    },
    yAxis=False,
    tooltip={
        'showMarkers': False,
        'shared': True,
    },
    legend={
        'custom': True,
        'position': 'bottom',
        'items': [
            {
                'value': '差',
                'name': '差',
                'marker': {
                    'symbol': 'square',
                    'style': {
                        'fill': '#FFbcb8',
                        'r': 5,
                    },
                },
            },
            {
                'value': '良',
                'name': '良',
                'marker': {
                    'symbol': 'square',
                    'style': {
                        'fill': '#FFe0b0',
                        'r': 5,
                    },
                },
            },
            {
                'value': '优',
                'name': '优',
                'marker': {
                    'symbol': 'square',
                    'style': {
                        'fill': '#bfeec8',
                        'r': 5,
                    },
                },
            },
            {
                'value': '第一季度',
                'name': '第一季度',
                'marker': {
                    'symbol': 'square',
                    'style': {
                        'fill': '#5B8FF9',
                        'r': 5,
                    },
                },
            },
            {
                'value': '第二季度',
                'name': '第二季度',
                'marker': {
                    'symbol': 'square',
                    'style': {
                        'fill': ' #61DDAA',
                        'r': 5,
                    },
                },
            },
            {
                'value': '目标值',
                'name': '目标值',
                'marker': {
                    'symbol': 'line',
                    'style': {
                        'stroke': '#39a3f4',
                        'r': 5,
                    },
                },
            },
        ],
    },
)
"""
        }
    ]
