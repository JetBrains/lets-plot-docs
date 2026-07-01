import os
import re
from collections import namedtuple
from xml.dom import minidom
from argparse import ArgumentParser


DEF_SITEMAP_FILENAME = "sitemap.xml"
DEF_WEB_ROOT = "https://lets-plot.org"


Transformation = namedtuple('Transformation', ['regex', 'function'])


class SitemapURL:

    to_remove = False
    changefreq = None
    priority = None

    def __init__(self, path: str, web_root: str):
        self._path = path[1:] if path.startswith("/") else path
        self.url = "{0}/{1}".format(web_root, self._path)

    def apply(self, transformation):
        if self._check(transformation):
            return transformation.function(self)
        else:
            return self

    def append_to_xml(self, xml_doc, urlset):
        if self.to_remove:
            return

        url_node = xml_doc.createElement('url')

        loc_node = xml_doc.createElement('loc')
        loc_node.appendChild(xml_doc.createTextNode(self.url))
        url_node.appendChild(loc_node)

        if self.changefreq is not None:
            changefreq_node = xml_doc.createElement('changefreq')
            changefreq_node.appendChild(xml_doc.createTextNode(self.changefreq))
            url_node.appendChild(changefreq_node)

        if self.priority is not None:
            priority_node = xml_doc.createElement('priority')
            priority_node.appendChild(xml_doc.createTextNode(str(self.priority)))
            url_node.appendChild(priority_node)

        urlset.appendChild(url_node)

    def _check(self, transformation):
        return transformation.regex.match(self._path) is not None

    def __str__(self):
        return '<SitemapURL url="{0}"{1}{2}{3}/>'.format(
            self.url,
            '' if self.changefreq is None else ' changefreq="{0}"'.format(self.changefreq),
            '' if self.priority is None else ' priority="{0}"'.format(self.priority),
            '' if not self.to_remove else ' remove="true"',
        )


def _set_to_remove(to_remove: bool = True):
    def update(sitemap_url: SitemapURL) -> SitemapURL:
        sitemap_url.to_remove = to_remove
        return sitemap_url
    return update


def _set_changefreq(changefreq: str):
    valid_changefreq = ['always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never']
    assert changefreq in valid_changefreq, "Unknown value of changefreq: '{0}'".format(changefreq)
    def update(sitemap_url: SitemapURL) -> SitemapURL:
        sitemap_url.changefreq = changefreq
        return sitemap_url
    return update


def _set_priority(priority: float):
    assert priority >= 0.0, "Bad value of priority: {0} < 0.0".format(priority)
    assert priority <= 1.0, "Bad value of priority: {0} > 1.0".format(priority)
    def update(sitemap_url: SitemapURL) -> SitemapURL:
        sitemap_url.priority = float(priority)
        return sitemap_url
    return update


transformations = [
    Transformation(re.compile(r"^404\.html$"), _set_to_remove()),
    Transformation(re.compile(r"^_static\/.*"), _set_to_remove()),
    Transformation(re.compile(r"^genindex\.html$"), _set_to_remove()),
    Transformation(re.compile(r"^search\.html$"), _set_to_remove()),
    Transformation(re.compile(r"^pages\/"), _set_to_remove()),
    Transformation(re.compile(r"^python\/shared"), _set_to_remove()),
    Transformation(re.compile(r"^python\/pages\/include"), _set_to_remove()),
    Transformation(re.compile(r"^kotlin\/api-reference\/navigation\.html$"), _set_to_remove()),
    Transformation(re.compile(r"^kotlin\/-lets--plot--kotlin\/.*"), _set_to_remove()),
    Transformation(re.compile(r"^(?!.*index\.html$)kotlin\/api-reference\/-lets--plot--kotlin.*$"), _set_to_remove()),
    Transformation(re.compile(r"^python\/pages\/api\/.*"), _set_changefreq('monthly')),
    Transformation(re.compile(r"^examples\/.*"), _set_changefreq('monthly')),
    Transformation(re.compile(r"^kotlin\/api-reference\/.*"), _set_changefreq('monthly')),
]


def _get_all_html_filenames(html_dir: str):
    for root, dirs, files in os.walk(html_dir):
        for filename in files:
            if filename.endswith(".html"):
                yield os.path.join(root.replace(html_dir, ""), filename).replace("\\", "/")


def generate_sitemap(html_dir: str, sitemap_filename: str = DEF_SITEMAP_FILENAME, *, web_root: str = DEF_WEB_ROOT):
    xml_doc = minidom.Document()
    urlset = xml_doc.createElement("urlset")
    urlset.setAttribute('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")
    xml_doc.appendChild(urlset)

    for html_filename in sorted(_get_all_html_filenames(html_dir)):
        sitemap_url = SitemapURL(html_filename, web_root)
        for transformation in transformations:
            sitemap_url = sitemap_url.apply(transformation)
        sitemap_url.append_to_xml(xml_doc, urlset)

    with open(sitemap_filename, "wb") as f:
        f.write(xml_doc.toprettyxml(indent="    ", encoding='utf-8'))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', required=True, metavar='INPUT', help="Path to the directory with html pages.")
    parser.add_argument('-f', '--filename', required=True, metavar='FILE_NAME', help="Path to the sitemap xml file.")
    parser.add_argument('-w', '--web_root', default=DEF_WEB_ROOT, metavar='WEB_ROOT', help="Site address.")
    args = parser.parse_args()

    generate_sitemap(html_dir=args.input, sitemap_filename=args.filename, web_root=args.web_root)
