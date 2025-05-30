from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    nested,  # noqa: F401
    drilldown,  # noqa: F401
    add_interactions,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdTreemap')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的矩形树图。',
        },
        {
            'path': 'nested',
            'title': '嵌套矩形树图',
            'description': '嵌套形式展示矩形树图。',
        },
        {
            'path': 'drilldown',
            'title': '矩形树图下钻功能',
            'description': '基于`drilldown`参数，为矩形树图开启下钻功能。',
        },
        {
            'path': 'add_interactions',
            'title': '添加更多交互功能',
            'description': '基于`interactions`参数，为矩形树图开启鼠标平移、滚轮缩放等交互功能。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
