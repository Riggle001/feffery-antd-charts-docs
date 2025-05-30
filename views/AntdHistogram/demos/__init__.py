from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    bin_number,  # noqa: F401
    stack,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdHistogram')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的直方图。',
        },
        {
            'path': 'bin_number',
            'title': '自定义分箱数',
            'description': '通过参数`binNumber`自定义分箱数。',
        },
        {
            'path': 'stack',
            'title': '堆叠直方图',
            'description': '堆叠形式的直方图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
