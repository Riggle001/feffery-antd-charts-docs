from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdRingProgress')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的进度环图。',
        },
        {
            'path': 'custom',
            'title': '外观调整',
            'description': '自定义进度环的更多外观配置。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
