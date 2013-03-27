#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
print "[PYTHON] render docs"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os.path
currentdir = os.curdir

docs_src = os.path.join(currentdir, 'docs_src')
docs_output_path = os.path.join(currentdir, 'docs')
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src,'index.html'), docs_output_path)

static_dir_src = os.path.join(currentdir, 'docs_src', 'html', 'static')
static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
shutil.copytree(static_dir_src, static_dir_dst)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(os.path.join(currentdir, 'docs_src'), format='text')

import global_constants as global_constants
import utils as utils

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()

metadata = {}
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?t=41607'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/firs/'

import firs
from cargos import registered_cargos
from industries import registered_industries
# default sort for docs is by id
registered_cargos = sorted(registered_cargos, key=lambda registered_cargos: registered_cargos.id)
registered_industries = sorted(registered_industries, key=lambda registered_industries: registered_industries.id)

class DocHelper(object):
    # dirty class to help do some doc formatting
    def get_industry_name(self, industry, economy=None):
        # industries don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = industry.get_property('name', economy)
        string_id = utils.unwrap_nml_string_declaration(name)
        return base_lang_strings.get(string_id, 'NO NAME ' + industry.id)

    def get_registered_industries_sorted_by_name(self):
        # industries don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict((self.get_industry_name(industry), industry) for industry in registered_industries)
        return sorted(result.items())

    def get_cargo_name(self, cargo):
        # cargos don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = cargo.type_name
        string_id = utils.unwrap_nml_string_declaration(name)
        return base_lang_strings.get(string_id, 'NO NAME ' + cargo.id)


def render_docs(doc_list, file_type):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(registered_cargos=registered_cargos, registered_industries=registered_industries,
                              economy_schemas=economy_schemas, global_constants=global_constants, repo_vars=repo_vars,
                              metadata=metadata, utils=utils, doc_helper=DocHelper())
        # save the results of templating
        if file_type == 'html':
            subdir = 'html'
        else:
            subdir = ''
        doc_file = codecs.open(os.path.join(docs_output_path, subdir, doc_name + '.' + file_type), 'w','utf8')
        doc_file.write(doc)
        doc_file.close()


economy_schemas = {}
for economy in global_constants.economies:
    enabled_cargos = [cargo for cargo in registered_cargos if not cargo.economy_variations[economy].get('disabled')]
    enabled_industries = [industry for industry in registered_industries if industry.economy_variations[economy].enabled]
    economy_schemas[economy] = {'enabled_cargos':enabled_cargos, 'enabled_industries':enabled_industries}

# render standard docs from a list
html_docs = ['set_overview', 'code_reference','economies']
txt_docs = ['changelog', 'license', 'readme', 'test_docs']

render_docs(html_docs, 'html')
render_docs(txt_docs, 'txt')