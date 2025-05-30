from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    draggable,  # noqa: F401
    custom_color,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdSankey')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的桑基图。',
        },
        {
            'path': 'draggable',
            'title': '节点可拖拽',
            'description': '设置参数`nodeDraggable=True`开启节点可拖拽调整功能。',
        },
        {
            'path': 'custom_color',
            'title': '自定义节点颜色',
            'description': '通过参数`color`自定义要素颜色。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
