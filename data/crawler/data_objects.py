import json


class Api:
    # An API has a name(title), tags, url, versions
    # Note: Categories and Tags are the same
    def __init__(self, title, tags, description, url, versions):
        self.title = title
        self.tags = tags
        self.description = description
        self.url = url
        self.versions = versions

    def add_version(self, version):
        self.versions.append(version)

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


class ApiVersion:
    # An API's version has a name, style(REST or other), version(as number, e.g. 1.0), status, release_time
    def __init__(self, version_title, style, version, status, submit_date, version_link):
        self.version_title = version_title
        self.style = style
        self.version = version
        self.status = status
        self.submit_date = submit_date
        self.version_link = version_link

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


# Changelog of an API or Mashup
class Changelog:
    def __init__(self, content, date):
        self.content = content
        self.date = date


# A Deadpooled API has a deprecate date additionally
class DeadPoolApi(Api):
    def __init__(self, title, tags, description, url, versions, changelogs, deprecated_date_estimated):
        super(DeadPoolApi, self).__init__(title, tags, description, url, versions)
        self.changelogs = changelogs
        self.deprecated_date_estimated = deprecated_date_estimated

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


# 定义几个类来标记访问的情况
class SimplifiedApi:
    def __init__(self, api_title, url):
        self.api_title = api_title
        self.url = url

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


class VersionVisit:
    def __init__(self, version_title, version_url, from_api, visit_status, is_accessible, is_endpoint_accessbile,
                 is_homepage_accessible):
        self.version_title = version_title
        self.version_url = version_url
        self.from_api = from_api
        self.visit_status = visit_status
        self.is_accessible = is_accessible
        self.is_endpoint_accessbile = is_endpoint_accessbile
        self.is_homepage_accessible = is_homepage_accessible

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


class VisitStatus:
    def __init__(self, visit_url, visit_label, status_code):
        self.visit_url = visit_url
        self.visit_label = visit_label
        self.status_code = status_code

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


class Mashup:
    def __init__(self, title, tags, description, related_apis, categories, url, mashup_type, submit_date=''):
        self.title = title
        self.tags = tags
        self.description = description
        self.related_apis = related_apis
        self.categories = categories
        self.url = url
        self.mashup_type = mashup_type
        self.date = submit_date
        # time

    def add_related_api(self, api):
        self.related_apis.append(api)

    def add_category(self, category):
        self.categories.append(category)

    def has_api(self, api_name):
        return api_name in self.related_apis

    def set_date(self, date):
        self.date = date

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)


class DeadpoolMashup(Mashup):
    def __init__(self, title, tags, description, related_apis, categories, url, mashup_type, changelogs,
                 deprecated_date_estimated, submit_date=''):
        super(DeadpoolMashup, self).__init__(title, tags, description, related_apis, categories, url, mashup_type,
                                             submit_date='')
        self.changelogs = changelogs
        self.deprecated_date_estimated = deprecated_date_estimated

    def json(self):
        return json.dumps(obj=self, default=lambda x: x.__dict__, sort_keys=False, indent=2)
