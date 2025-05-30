from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    series,  # noqa: F401
    inner_radius,  # noqa: F401
    inner_label,  # noqa: F401
    stack,  # noqa: F401
    pattern,  # noqa: F401
    custom_color,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdRose')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的风玫瑰图。',
        },
        {
            'path': 'series',
            'title': '多系列风玫瑰图',
            'description': '通过参数`seriesField`设置分组字段。',
        },
        {
            'path': 'inner_radius',
            'title': '设置内部半径',
            'description': '通过参数`innerRadius`设置内部半径。',
        },
        {
            'path': 'inner_label',
            'title': '使用内部标签',
            'description': '通过参数`label`控制文字标签在内部显示。',
        },
        {
            'path': 'stack',
            'title': '开启堆叠',
            'description': '基于参数`seriesField`、`isStack`实现分组堆叠效果。',
        },
        {
            'path': 'pattern',
            'title': '带贴图',
            'description': '通过参数`pattern`设置贴图。',
        },
        {
            'path': 'custom_color',
            'title': '自定义颜色',
            'description': '通过参数`color`设置自定义颜色，譬如对于排序后的数据，基于透明度变化定义漂亮的渐变色。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
