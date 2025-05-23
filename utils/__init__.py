import os
import mistune
from typing import List
from flask import request
from itertools import groupby
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc
from mistune.renderers.markdown import MarkdownRenderer

# 国际化
from i18n import translator
from config import DocsConfig

markdown_parser = mistune.create_markdown(renderer='ast')
markdown_renderer = MarkdownRenderer()


def get_doc_anchor_link_dict(catalog: list):
    """将原始catalog数据结构转换为适用于AntdAnchor的多层linkDict"""
    result = []
    for key, group in groupby(
        [
            {**item, 'group': item.get('group', i)}
            for i, item in enumerate(catalog)
        ],
        key=lambda x: x['group'],
    ):
        items = list(group)
        if isinstance(key, str):
            result.append(
                {
                    'title': key,
                    'href': '#' + 'demo-container-' + items[0]['path'],
                    'children': [
                        {
                            'title': item['title'],
                            'href': '#' + 'demo-container-' + item['path'],
                        }
                        for item in items
                    ],
                }
            )
        else:
            result.append(
                {
                    'title': items[0]['title'],
                    'href': '#' + 'demo-container-' + items[0]['path'],
                }
            )
    return result


def get_extra_api_descriptions(component: Component) -> str:
    """尝试获取指定组件额外的API说明"""
    # 若当前组件存在额外API说明文件
    if f'{component.__name__}.md' in os.listdir(
        './public/extra_api_descriptions'
    ):
        # 获取当前国际化语种
        current_locale = request.cookies.get(translator.cookie_name, 'zh-cn')
        if current_locale == 'zh-cn':
            with open(
                './public/extra_api_descriptions/{}.md'.format(
                    component.__name__
                ),
                encoding='utf-8',
            ) as f:
                return f.read()
        elif current_locale == 'en-us':
            with open(
                './public/extra_api_descriptions/en_us/{}.md'.format(
                    component.__name__
                ),
                encoding='utf-8',
            ) as f:
                return f.read()


def generate_component_props(component_props: List[dict]) -> str:
    """解析转换指定组件的参数说明"""

    # TODO
    # 多语种国际化判断
    # # 获取当前国际化语种
    # current_locale = request.cookies.get(translator.cookie_name, 'zh-cn')

    items = []
    for item in component_props:
        if item['type'] == 'props':
            # 合成当前板块参数说明markdown
            raw_markdown = ''
            for prop in item['props']:
                # 若参数存在文档
                if DocsConfig.props_descriptions['zh-cn'].get(
                    prop.get('source') or prop.get('name')
                ):
                    raw_markdown += (
                        '- **{}** '.format(prop['name'])
                        + DocsConfig.props_descriptions['zh-cn'][
                            prop.get('source') or prop.get('name')
                        ]
                    )
                else:
                    print(prop['name'])
            items.append(
                {
                    'key': item['name'],
                    'title': item['name'],
                    'children': fmc.FefferyMarkdown(
                        className='side-props-markdown',
                        markdownStr=raw_markdown,
                    ),
                }
            )
        elif item['type'] == 'prop':
            raw_markdown = ''
            # 若参数存在文档
            if DocsConfig.props_descriptions['zh-cn'].get(
                item.get('source') or item.get('name')
            ):
                raw_markdown = DocsConfig.props_descriptions['zh-cn'][
                    item.get('source') or item.get('name')
                ]
                # 若当前项文档内容存在需要替换的内容
                if item.get('replacements'):
                    for origin, replacement in item['replacements'].items():
                        raw_markdown = raw_markdown.replace(origin, replacement)
            else:
                print(item['name'])
            items.append(
                {
                    'key': item['name'],
                    'title': fac.AntdSpace(
                        [
                            item['name'],
                            fac.AntdTag(
                                content=item['description'],
                                color='blue',
                            ),
                        ]
                    ),
                    'children': fmc.FefferyMarkdown(
                        className='side-props-markdown',
                        markdownStr=raw_markdown,
                    ),
                }
            )

    return fac.AntdAccordion(
        items=items,
        accordion=False,
        size='small',
        style={'background': 'transparent'},
    )


def generate_shortcut_panel_data(raw_menu_data: list) -> list:
    """基于侧边菜单栏生成快捷搜索面板所需数据结构"""

    data = []
    for level1 in raw_menu_data:
        if level1['component'] == 'ItemGroup':
            for level2 in level1['children']:
                if level2['component'] == 'Item':
                    data.append(
                        {
                            'id': level2['props']['key'],
                            'title': level2['props']['title'],
                            'section': level1['props']['title'],
                            'handler': '() => window.open("{}")'.format(
                                level2['props']['href']
                            ),
                        }
                    )

                elif level2['component'] == 'SubMenu':
                    for level3 in level2['children']:
                        if level3['component'] == 'Item':
                            data.append(
                                {
                                    'id': level3['props']['key'],
                                    'title': level3['props']['title'],
                                    'section': '{} / {}'.format(
                                        level1['props']['title'],
                                        level2['props']['title'],
                                    ),
                                    'handler': '() => window.open("{}")'.format(
                                        level3['props']['href']
                                    ),
                                }
                            )
                        elif level3['component'] == 'SubMenu':
                            for level4 in level3['children']:
                                if level3['props']['title'].startswith(
                                    'AntdTable'
                                ):
                                    data.append(
                                        {
                                            'id': level4['props']['key'],
                                            'title': translator.t(
                                                'AntdTable 表格：'
                                            )
                                            + level4['props']['title'],
                                            'section': '{} / {} / {}'.format(
                                                level1['props']['title'],
                                                level2['props']['title'],
                                                level3['props']['title'],
                                            ),
                                            'handler': '() => window.open("{}")'.format(
                                                level4['props']['href']
                                            ),
                                        }
                                    )
                                else:
                                    data.append(
                                        {
                                            'id': level4['props']['key'],
                                            'title': level4['props']['title'],
                                            'section': '{} / {} / {}'.format(
                                                level1['props']['title'],
                                                level2['props']['title'],
                                                level3['props']['title'],
                                            ),
                                            'handler': '() => window.open("{}")'.format(
                                                level4['props']['href']
                                            ),
                                        }
                                    )

    return data
