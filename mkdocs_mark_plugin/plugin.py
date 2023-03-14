import logging
import os
import pathlib
import re
from collections import defaultdict
from glob import glob
from urllib.parse import quote

import parse
from mkdocs.plugins import BasePlugin
from mkdocs.utils import warning_filter

LOG = logging.getLogger("mkdocs.plugins." + __name__)
LOG.addFilter(warning_filter)

LINK_RE = r"(\[([\w\s]+)\]\(ac:(\)|[\w\s]*)\))"


class Replacer:
    def __init__(self, link_map):
        self.link_map = link_map

    def __call__(self, match):
        # Group 1 is the whole link
        # Group 2 is the link text
        # Group 3 is the target title (or nothing)
        target_title = match.group(3).strip() or match.group(2).strip()
        target_doc = self.link_map[target_title.lower()]
        return match.group(0).split("(")[0] + f"({target_doc})"


class MarkLinksPlugin(BasePlugin):
    def __init__(self):
        self.title_map = None

    def _init_title_map(self, config):
        self.title_map = {}
        for md_file in glob(f"{config['docs_dir']}/**md"):
            with open(md_file) as inf:
                contents = inf.read()
                results = parse.search("# {title}\n", contents)
                if results is None:
                    raise ValueError(f"No H1 level title found in {md_file}")
                self.title_map[results["title"].lower().strip()] = pathlib.Path(
                    md_file
                ).relative_to(config["docs_dir"])

    def on_page_markdown(self, markdown, page, config, files, **kwargs):
        # Initializes the filename lookiup dict if it hasn't already been initialized
        if self.title_map is None:
            self._init_title_map(config)

        # Getting the root location of markdown source files
        base_docs_dir = config["docs_dir"]

        # Getting the page path that we are linking from
        abs_page_path = page.file.abs_src_path

        # Find and fix links
        markdown = re.sub(LINK_RE, Replacer(self.title_map), markdown)

        return markdown
